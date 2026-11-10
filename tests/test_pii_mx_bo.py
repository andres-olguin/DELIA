import json
from pathlib import Path

import pytest

from backend.dlp.pii import Finding, detect, redact


CORPUS = Path(__file__).resolve().parents[1] / "benchmarks" / "synthetic_pii_mx_bo.jsonl"
CASES = [json.loads(line) for line in CORPUS.read_text(encoding="utf-8").splitlines()]
POLICY_CORPUS = CORPUS.with_name("synthetic_pii_mx_policy.jsonl")
CASES += [json.loads(line) for line in POLICY_CORPUS.read_text(encoding="utf-8").splitlines()]


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


@pytest.mark.parametrize(("kind", "value"), [
    ("CURP", "NAQZ860412HJCPLR03"),
    ("CURP", "VEQX000229MNEBRCA7"),
    ("RFC", "ZAÑQ870614R22"),
    ("RFC", "&QZ030725L77"),
    ("RFC", "YQZ94061803A"),
    ("RFC", "YQZ940618080"),
])
def test_checksum_mutations_require_matching_context(kind, value):
    for digit in "0123456789A" if kind == "RFC" else "0123456789":
        candidate = value[:-1] + digit
        expected = [Finding(kind, 0, len(candidate))] if digit == value[-1] else []
        assert detect(candidate) == expected
        assert redact(f"{kind}: {candidate}")[0] == f"{kind}: [[{kind}]]"


@pytest.mark.parametrize(("prefix", "expected"), [
    ("curp = ", True),
    ("CURP # ", True),
    ("CURP\t", True),
    ('"CURP": "', True),
    ("miCURP: ", False),
    ("CURP:\n", False),
    ("CURP de contacto ", False),
    ("RFC: ", False),
    ("&CURP: ", False),
    ("-CURP: ", False),
    ("\u0301CURP: ", False),
    ("CÜRP: ", False),
])
def test_mx_context_boundaries(prefix, expected):
    value = "NAQZ860412HJCPLR04"
    findings = detect(prefix + value)
    assert findings == ([Finding("CURP", len(prefix), len(prefix) + len(value))] if expected else [])


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ('CI: 12345678 - 2B - SC', 'CI: [[CI_BO]]'),
        ('CI: 12345678-2B\t-\tSC', 'CI: [[CI_BO]]'),
        ('CI: 12345678 - SC', 'CI: [[CI_BO]]'),
        ('CI: 12345678\tSC', 'CI: [[CI_BO]]'),
        ('CÉDULA BOLIVIANA: 12345678', 'CÉDULA BOLIVIANA: [[CI_BO]]'),
        ('NIT BOLIVIANO: 12345018', 'NIT BOLIVIANO: [[NIT_BO]]'),
        ('NİT: 12345018', 'NİT: 12345018'),
        ('Cİ: 12345018', 'Cİ: 12345018'),
        ('CI: 12345678 - XYZ', 'CI: 12345678 - XYZ'),
        ('CI: 12345678-2B - XYZ', 'CI: 12345678-2B - XYZ'),
        ('CI: 12345.678', 'CI: 12345.678'),
        ('NIT: 12345018.99', 'NIT: 12345018.99'),
        ('NIT: 12345018,99', 'NIT: 12345018,99'),
        ('NIT: 12345018/99', 'NIT: 12345018/99'),
        ('CI: 12345678\r\nSC', 'CI: [[CI_BO]]\r\nSC'),
        ('NIT:\r\n12345018', 'NIT:\r\n12345018'),
        ('CI:\r12345678', 'CI:\r12345678'),
        ('CI: 12345678\u0301', 'CI: 12345678\u0301'),
        ('RFC: BUÑQ920229M17\u0301', 'RFC: BUÑQ920229M17\u0301'),
        ('CURP: AEXZ000229XQOBCDZ7\u0301', 'CURP: AEXZ000229XQOBCDZ7\u0301'),
        ('CІ: 12345678', 'CІ: 12345678'),
        ('RFC: BÜÑQ920229M17', 'RFC: BÜÑQ920229M17'),
        ('RFC: BUÑQ920229M17@correo.invalid', 'RFC: [[EMAIL]]'),
        ('RFC: &AZ050131C00@correo.invalid', 'RFC: [[EMAIL]]'),
        ('RFC: AZ&050131C00@correo.invalid', 'RFC: [[EMAIL]]'),
        ('NIT: 12345018@correo.invalid', 'NIT: [[EMAIL]]'),
        ('CI: 12345678-2B@correo.invalid', 'CI: [[EMAIL]]'),
        ('RFC: XEXX010101000, RFC: XAXX010101000', 'RFC: XEXX010101000, RFC: XAXX010101000'),
        ('RFC: A&Z0102291A2', 'RFC: A&Z0102291A2'),
        ('RFC: A&Z0002291A2', 'RFC: [[RFC]]'),
        (r'"rfc": "BU\u00d1Q920229M17"', '"rfc": "[[RFC]]"'),
        (r'"rfc": "bu\u00f1q920229m17"', '"rfc": "[[RFC]]"'),
        (r'Contacto BU\u00d1Q920229M17@correo.invalid', 'Contacto [[EMAIL]]'),
        ('CURP: AEXZ000229XQOBCD07', 'CURP: AEXZ000229XQOBCD07'),
        ('CURP: AEXZ000229XQOBCDA7', 'CURP: [[CURP]]'),
        ('CI: 12345678-5', 'CI: [[RUT]]'),
        ('NIT: 800197268-5', 'NIT: 800197268-5'),
        ('CI: 12345678-2B SC; CI: 87654321 LP', 'CI: [[CI_BO]]; CI: [[CI_BO]]'),
        ('CI: ' + ' ' * 4096 + 'pendiente', 'CI: ' + ' ' * 4096 + 'pendiente'),
    ],
)
def test_additional_context_and_boundaries(text, expected):
    assert redact(text)[0] == expected


def test_unicode_offsets_and_repeated_values():
    text = '👩🏽‍💻 México — CI: 12345678-2B SC; RFC: A&Z0002291A2; CI: 12345678-2B SC'
    findings = detect(text)
    assert [text[f.start:f.end] for f in findings] == [
        '12345678-2B SC', 'A&Z0002291A2', '12345678-2B SC'
    ]
    assert all(left.end <= right.start for left, right in zip(findings, findings[1:]))
    masked, _ = redact(text)
    assert masked == '👩🏽‍💻 México — CI: [[CI_BO]]; RFC: [[RFC]]; CI: [[CI_BO]]'
    assert redact(masked) == (masked, [])
