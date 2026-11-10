import json
from pathlib import Path

import pytest

from backend.dlp.pii import Finding, detect, redact


HISTORICAL_CASES = [
    json.loads(line)
    for line in (
        Path(__file__).resolve().parents[1] / "benchmarks/synthetic_pii_r3.jsonl"
    ).read_text(encoding="utf-8").splitlines()
]


@pytest.mark.parametrize(
    "case",
    [case for case in HISTORICAL_CASES if case["id"] in {"T0041", "T0045", "T0049", "T0162"}],
    ids=lambda case: case["id"],
)
def test_historical_false_positives_match_original_labels(case):
    expected = [Finding(e["type"], e["start"], e["end"]) for e in case["entities"]]
    assert detect(case["text"]) == expected
    masked, findings = redact(case["text"])
    assert findings == expected
    if expected:
        assert masked == "cédula: [[CEDULA]]."
    else:
        assert masked == case["text"]


@pytest.mark.parametrize(("text", "value"), [
    ("cédula: 2.345.678.901.", "2.345.678.901"),
    ("C.C. 8.765.432.109", "8.765.432.109"),
    ("CC 1234567890", "1234567890"),
    ("Cédula 12.345.678.", "12.345.678"),
    ("cédula: 999.999.999", "999.999.999"),
    ("CC 12.345", "12.345"),
    (r"c\u00e9dula: 2.345.678.901", "2.345.678.901"),
    (r"C\u00c9DULA: 2.345.678.901", "2.345.678.901"),
    (r"c\u00e9dula de ciudadan\u00eda: 2.345.678.901", "2.345.678.901"),
    ("CC 12.345.678.901", None),
    ("CC 1.234.567.890.123", None),
    ("CC 12345678901", None),
    ("CC 12345678.9", None),
    ("CC 1.234.56.789", None),
    ("CC 12345678abc", None),
    ("Pedido 2.345.678.901", None),
])
def test_cedula_masks_complete_numbers_without_truncation(text, value):
    expected = []
    masked = text
    if value is not None:
        start = text.index(value)
        expected = [Finding("CEDULA", start, start + len(value))]
        masked = text[:start] + "[[CEDULA]]" + text[start + len(value):]
    assert detect(text) == expected
    assert redact(text) == (masked, expected)
    assert redact(masked) == (masked, [])


@pytest.mark.parametrize(("consistent", "inconsistent"), [
    ("QQZ850224W21", "QQZ850224W20"),
    ("QQZ850224X29", "QQZ850224X20"),
    ("QQZ850224Y26", "QQZ850224Y20"),
    ("QQZ850224Z23", "QQZ850224Z20"),
])
def test_rfc_context_cannot_rescue_out_of_range_homonym_with_wrong_checksum(
    consistent, inconsistent
):
    # Sin verificador coherente, el contexto no basta para estas homonimias.
    for text in (
        f"RFC: {inconsistent}",
        f'{{"rfc":"{inconsistent.lower()}"}}',
        f"Inventario {inconsistent}",
    ):
        assert redact(text) == (text, [])
    # Mantener la protección conservadora de candidatos matemáticamente coherentes.
    assert detect(consistent) == [Finding("RFC", 0, len(consistent))]
