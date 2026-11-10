"""Evaluate exact entity type and span matches on a labeled JSONL corpus."""

import argparse
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path

from backend.dlp import pii


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", type=Path, default=Path("benchmarks/synthetic_pii_r3.jsonl"))
    args = parser.parse_args()
    data = args.dataset.read_bytes()
    cases = [json.loads(line) for line in data.decode("utf-8").splitlines() if line.strip()]
    counts = defaultdict(Counter)
    counts["total"] = Counter()
    for case in cases:
        expected = {(e["type"], e["start"], e["end"]) for e in case["entities"]}
        detected = set(pii.detect(case["text"]))
        country = case["country"]
        counts[f"country/{country}"]
        for metric, entities in (
            ("tp", expected & detected),
            ("fp", detected - expected),
            ("fn", expected - detected),
        ):
            for kind, _, _ in entities:
                for group in ("total", f"country/{country}", f"entity/{kind}", f"country_entity/{country}/{kind}"):
                    counts[group][metric] += 1

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
    print(json.dumps({
        "dataset": str(args.dataset),
        "dataset_sha256": hashlib.sha256(data).hexdigest(),
        "detector_sha256": hashlib.sha256(Path(pii.__file__).read_bytes()).hexdigest(),
        "cases": len(cases),
        "matching": "exact_type_and_span",
        "comparators": dict.fromkeys(("Presidio", "Cloudflare DLP", "Google Model Armor"), "NO EJECUTADO"),
        "results": results,
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
