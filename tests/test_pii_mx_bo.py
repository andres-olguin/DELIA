import json
from pathlib import Path

import pytest

from backend.dlp.pii import Finding, detect, redact


CORPUS = Path(__file__).resolve().parents[1] / "benchmarks" / "synthetic_pii_mx_bo.jsonl"
CASES = [json.loads(line) for line in CORPUS.read_text(encoding="utf-8").splitlines()]


@pytest.mark.parametrize("case", CASES, ids=[case["id"] for case in CASES])
def test_detection_and_redaction(case):
    expected = [
        Finding(entity["type"], entity["start"], entity["end"])
        for entity in case["entities"]
    ]
    assert detect(case["text"]) == expected, case["note"]

    # Construir el texto esperado desde las etiquetas, independientemente del detector.
    expected_text = case["text"]
    for finding in reversed(expected):
        expected_text = (
            expected_text[:finding.start]
            + f"[[{finding.type}]]"
            + expected_text[finding.end:]
        )
    masked, findings = redact(case["text"])
    assert masked == expected_text, case["note"]
    assert findings == expected
