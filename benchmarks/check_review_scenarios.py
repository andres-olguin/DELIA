"""Run deterministic synthetic review scenarios without external services."""

import argparse
import datetime
import json
import random
from pathlib import Path

from backend.dlp.pii import Finding, detect, redact


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", type=int, default=20261111)
    parser.add_argument("--out", type=Path)
    parser.add_argument("--contexts", action="store_true", help="Check controlled context variants")
    args = parser.parse_args()
    randomizer = random.Random(args.seed)
    checks = 0
    failures = []
    alphabet = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    rfc_alphabet = "0123456789ABCDEFGHIJKLMN&OPQRSTUVWXYZ Ñ"
    nit_weights = [3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71]

    def record(text, value, kind):
        nonlocal checks
        checks += 1
        expected = []
        cursor = 0
        while value and (start := text.find(value, cursor)) >= 0:
            expected.append(Finding(kind, start, start + len(value)))
            cursor = start + len(value)
        expected_text = text.replace(value, f"[[{kind}]]") if value else text
        masked, findings = redact(text)
        if detect(text) != expected or (masked, findings) != (expected_text, expected):
            failures.append({"check": checks, "type": kind, "text": text,
                             "expected": expected, "actual": findings})
        elif redact(masked) != (masked, []):
            failures.append({"check": checks, "type": kind, "reason": "not_idempotent"})

    for index in range(20):
        date = datetime.date(1991, 1, 1) + datetime.timedelta(days=randomizer.randrange(9000))
        stamp = date.strftime("%y%m%d")
        curp_body = "ZE" + "".join(randomizer.choices("BCDFGJKLMNPQRSTVZ", k=2))
        curp_body += stamp + randomizer.choice("HMX") + "NE"
        curp_body += "".join(randomizer.choices("BCDFGJKLMNPQRSTVZ", k=3))
        curp_body += "0" if date.year < 2000 else "A"
        curp_sum = sum(alphabet.index(char) * weight
                       for char, weight in zip(curp_body, range(18, 1, -1)))
        curp = curp_body + str((10 - curp_sum % 10) % 10)

        rfc_body = "".join(randomizer.choices("ABÑ&Z", k=3 + index % 2)) + stamp + "M2"
        padded = rfc_body.rjust(12)
        rfc_sum = sum(rfc_alphabet.index(char) * weight
                      for char, weight in zip(padded, range(13, 1, -1)))
        remainder = rfc_sum % 11
        rfc_digit = "0" if remainder == 0 else ("A" if remainder == 1 else str(11 - remainder))
        rfc = rfc_body + rfc_digit

        rut_body = str(randomizer.randrange(10000000, 99999999))
        rut_sum = sum(int(char) * (2 + offset % 6)
                      for offset, char in enumerate(rut_body[::-1]))
        rut_rest = 11 - rut_sum % 11
        rut_digit = "K" if rut_rest == 10 else ("0" if rut_rest == 11 else str(rut_rest))
        rut = rut_body + " " + rut_digit

        nit_body = str(randomizer.randrange(100000000, 999999999))
        nit_rest = sum(int(char) * weight
                       for char, weight in zip(nit_body[::-1], nit_weights)) % 11
        nit_digit = str(nit_rest if nit_rest < 2 else 11 - nit_rest)
        nit = " ".join(nit_body[offset:offset + 3] for offset in range(0, 9, 3)) + " - " + nit_digit

        ci = str(randomizer.randrange(1000000, 9999999)) + "-2B LP"
        nit_bo = str(randomizer.randrange(10000000000, 99999999999))
        cedula_body = str(randomizer.randrange(1000000000, 9999999999))
        cedula = cedula_body[0] + "." + ".".join(cedula_body[offset:offset + 3]
                                               for offset in range(1, 10, 3))

        for kind, label, value in [
            ("CURP", "CURP", curp), ("RFC", "RFC", rfc),
            ("CI_BO", "cédula boliviana", ci), ("NIT_BO", "NIT Bolivia", nit_bo),
            ("RUT", "RUT", rut), ("NIT", "NIT CO", nit), ("CEDULA", "cédula", cedula),
        ]:
            record(f"🧪 {label}: {value}.", value, kind)
            for escaped in (True, False):
                text = json.dumps({label: value}, ensure_ascii=escaped)
                encoded = json.dumps(value, ensure_ascii=escaped)[1:-1]
                record(text, encoded, kind)
            record(f"{label}: {value}; {label}: {value}.", value, kind)
            record(f"{label}: ref_{value}_tail", None, kind)
            if args.contexts and kind in {"CURP", "RFC", "CI_BO", "NIT_BO"}:
                contextual_value = value
                if kind in {"CURP", "RFC"}:
                    contextual_value = value[:-1] + ("0" if value[-1] != "0" else "1")
                for qualifier in ("de muestra", "del titular", "número", "de identificación", "No."):
                    field = f"{label} {qualifier}"
                    record(f"{field}: {contextual_value}.", contextual_value, kind)
                    for escaped in (True, False):
                        text = json.dumps({field: contextual_value}, ensure_ascii=escaped)
                        encoded = json.dumps(contextual_value, ensure_ascii=escaped)[1:-1]
                        record(text, encoded, kind)
                for invalid_label in (
                    f"{label} de contacto", f"{label} de compilación",
                    f"{label}\n", f"\u0301{label}",
                ):
                    record(f"{invalid_label}: {contextual_value}.", None, kind)

    result = {"seed": args.seed, "checks": checks, "failures": failures}
    if args.out:
        args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))
    assert not failures


if __name__ == "__main__":
    main()
