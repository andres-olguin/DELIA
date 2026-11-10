import json
from pathlib import Path

import pytest

from backend.dlp.pii import Finding, detect, redact


CORPUS = Path(__file__).resolve().parents[1] / "benchmarks/synthetic_pii_coverage.jsonl"
CASES = [json.loads(line) for line in CORPUS.read_text(encoding="utf-8").splitlines()]


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
def test_additional_formats_preserve_exact_detection_and_redaction(case):
    expected = [Finding(e["type"], e["start"], e["end"]) for e in case["entities"]]
    masked = case["text"]
    for finding in reversed(expected):
        masked = masked[:finding.start] + f"[[{finding.type}]]" + masked[finding.end:]
    assert detect(case["text"]) == expected, case["note"]
    assert redact(case["text"]) == (masked, expected), case["note"]
    assert redact(masked) == (masked, [])


@pytest.mark.parametrize(("kind", "body", "digit"), [
    ("RUT", "8234567", "1"),
    ("RUT", "94285716", "0"),
    ("RUT", "94285725", "K"),
    ("NIT", "812345678", "1"),
    ("NIT", "913572846", "1"),
])
def test_added_separators_preserve_checksum_validation(kind, body, digit):
    dotted = body[:-6] + "." + body[-6:-3] + "." + body[-3:]
    formats = [f"{dotted} - {{digit}}", f"{body}\t-\t{{digit}}"]
    if kind == "RUT":
        formats.append(f"{body} {{digit}}")
    else:
        formats.append(f'{dotted.replace(".", " ")} - {{digit}}')
    for template in formats:
        for candidate_digit in "0123456789K" if kind == "RUT" else "0123456789":
            value = template.format(digit=candidate_digit)
            text = f"{kind}: {value}"
            expected = (
                [Finding(kind, len(kind) + 2, len(text))]
                if candidate_digit == digit else []
            )
            assert detect(text) == expected
