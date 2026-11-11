import json
from pathlib import Path

import pytest

from backend.dlp.pii import Finding, detect, redact


CORPUS = Path(__file__).resolve().parents[1] / "benchmarks/synthetic_pii_contexts.jsonl"
CASES = [json.loads(line) for line in CORPUS.read_text(encoding="utf-8").splitlines()]


@pytest.mark.parametrize("case", CASES, ids=lambda case: case["id"])
def test_controlled_contexts_preserve_exact_spans_and_masking(case):
    expected = [Finding(e["type"], e["start"], e["end"]) for e in case["entities"]]
    masked = case["text"]
    for finding in reversed(expected):
        masked = masked[:finding.start] + f"[[{finding.type}]]" + masked[finding.end:]
    assert detect(case["text"]) == expected, case["note"]
    assert redact(case["text"]) == (masked, expected)
    assert redact(masked) == (masked, [])


@pytest.mark.parametrize(("label", "value", "kind"), [
    ("CI número", "65432109-3C SC", "CI_BO"),
    ("NIT Bolivia de identificación", "38475916028", "NIT_BO"),
    ("CURP número", "PEQZ030415MNEBCDA0", "CURP"),
    ("RFC número", "FUÑQ990214M20", "RFC"),
    ("CÉDULA DE IDENTIDAD BOLIVIANA No.", "65432109-3C SC", "CI_BO"),
])
@pytest.mark.parametrize("escaped", [True, False])
def test_context_labels_survive_json_serialization(label, value, kind, escaped):
    text = json.dumps({label: value}, ensure_ascii=escaped)
    masked, findings = redact(text)
    assert json.loads(masked) == {label: f"[[{kind}]]"}
    encoded_value = json.dumps(value, ensure_ascii=escaped)[1:-1]
    assert [text[f.start:f.end] for f in findings] == [encoded_value]
    assert [f.type for f in findings] == [kind]
