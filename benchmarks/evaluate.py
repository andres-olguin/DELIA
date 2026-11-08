"""Measure exact entity type and span matches on a labeled JSONL corpus.

Adapted from the evaluator in repository commit 70c878e. The optional detector
revision executes trusted repository code to reproduce an earlier baseline.
"""

import argparse
import hashlib
import json
import platform
import subprocess
from collections import Counter, defaultdict
from pathlib import Path

from backend.dlp import pii


def load_cases(data):
    cases = [json.loads(line) for line in data.decode("utf-8").splitlines() if line.strip()]
    seen = set()
    for case in cases:
        if case["id"] in seen:
            raise ValueError(f"Duplicate case ID {case['id']}")
        seen.add(case["id"])
        previous_end = 0
        for entity in case["entities"]:
            start, end = entity["start"], entity["end"]
            if (
                type(start) is not int
                or type(end) is not int
                or not previous_end <= start < end <= len(case["text"])
            ):
                raise ValueError(f"Invalid or overlapping span in {case['id']}")
            previous_end = end
    return cases


def evaluate(cases, detect):
    counts = defaultdict(Counter)
    counts["total"] = Counter()
    errors = []
    for case in cases:
        expected = {(e["type"], e["start"], e["end"]) for e in case["entities"]}
        detected = {tuple(finding) for finding in detect(case["text"])}
        country_group = f"country/{case['country']}"
        counts[country_group]
        for kind, _, _ in expected | detected:
            counts[f"entity/{kind}"]
            counts[f"{country_group}/entity/{kind}"]
        for metric, entities in (
            ("tp", expected & detected),
            ("fp", detected - expected),
            ("fn", expected - detected),
        ):
            for kind, _, _ in entities:
                for group in (
                    "total", country_group, f"entity/{kind}", f"{country_group}/entity/{kind}"
                ):
                    counts[group][metric] += 1
        if expected != detected:
            errors.append({
                "id": case["id"],
                "fp": sorted(detected - expected),
                "fn": sorted(expected - detected),
            })

    results = {}
    for group, count in sorted(counts.items()):
        tp, fp, fn = (count[key] for key in ("tp", "fp", "fn"))
        denominator = 2 * tp + fp + fn
        results[group] = {
            "tp": tp,
            "fp": fp,
            "fn": fn,
            "precision": tp / (tp + fp) if tp + fp else None,
            "recall": tp / (tp + fn) if tp + fn else None,
            "f1": 2 * tp / denominator if denominator else None,
        }
    return results, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=Path("benchmarks/synthetic_pii_r3.jsonl"))
    parser.add_argument("--detector-ref", help="Trusted Git revision of backend/dlp/pii.py")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    dataset = args.dataset.read_bytes()
    revision = subprocess.check_output(
        ["git", "rev-parse", "--verify", f"{args.detector_ref or 'HEAD'}^{{commit}}"], text=True
    ).strip()
    if args.detector_ref:
        detector_source = subprocess.check_output(["git", "show", f"{revision}:backend/dlp/pii.py"])
        namespace = {"__name__": "benchmark_detector"}
        exec(compile(detector_source, f"{revision}:backend/dlp/pii.py", "exec"), namespace)
        detect = namespace["detect"]
    else:
        detector_source = Path(pii.__file__).read_bytes()
        detect = pii.detect
    cases = load_cases(dataset)
    results, errors = evaluate(cases, detect)
    report = {
        "dataset": str(args.dataset),
        "dataset_sha256": hashlib.sha256(dataset).hexdigest(),
        "detector_revision": revision,
        "detector_source": "git_revision" if args.detector_ref else "working_tree",
        "detector_sha256": hashlib.sha256(detector_source).hexdigest(),
        "evaluator_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "python": platform.python_version(),
        "cases": len(cases),
        "entities": sum(len(case["entities"]) for case in cases),
        "negative_cases": sum(not case["entities"] for case in cases),
        "matching": "exact_type_and_span",
        "comparators": dict.fromkeys(
            ("Presidio", "Cloudflare DLP", "Google Model Armor"), "NO EJECUTADO"
        ),
        "results": results,
        "case_errors": errors,
    }
    output = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(output, encoding="utf-8")
    else:
        print(output, end="")


if __name__ == "__main__":
    main()
