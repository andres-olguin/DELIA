import re
from typing import NamedTuple

class Finding(NamedTuple):
    type: str
    start: int
    end: int

_NIT_PRIMES = (3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71)

def rut_dv(body: str) -> str:
    total = sum(int(d) * (2 + i % 6) for i, d in enumerate(reversed(body)))
    r = 11 - total % 11
    return "K" if r == 10 else "0" if r == 11 else str(r)

def nit_dv(body: str) -> str:
    r = sum(int(d) * p for d, p in zip(reversed(body), _NIT_PRIMES)) % 11
    return str(r if r in (0, 1) else 11 - r)

def luhn(number: str) -> bool:
    digits = [int(d) for d in reversed(number)]
    total = sum(digits[0::2]) + sum(sum(divmod(2 * d, 10)) for d in digits[1::2])
    return total % 10 == 0

def _check_id(dv_fn):
    def check(raw: str) -> bool:
        body, dv = raw.replace(".", "").upper().split("-")
        return dv_fn(body) == dv
    return check

# (tipo, regex, validador opcional sobre el texto encontrado, grupo a enmascarar)
# shortcut: NIT solo de 9 dígitos y RUT de 7-8 (los comunes), ampliar si aparecen falsos negativos.
_RULES = (
    ("EMAIL", r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", None, 0),
    ("RUT", r"\b\d{1,2}\.?\d{3}\.?\d{3}-[\dkK]\b", _check_id(rut_dv), 0),
    ("NIT", r"\b\d{3}\.?\d{3}\.?\d{3}-\d\b", _check_id(nit_dv), 0),
    ("TARJETA", r"\b\d(?:[ -]?\d){12,18}\b", lambda s: luhn(re.sub(r"\D", "", s)), 0),
    ("TELEFONO", r"\+(?:57|56)[\s-]?\d(?:[\s-]?\d){7,9}\b", None, 0),
    # La cédula no tiene dígito verificador: solo se detecta con una palabra de contexto.
    ("CEDULA",
     r"(?i)\b(?:c\.\s?c\.?|cc|c[eé]dula(?:\s+de\s+ciudadan[ií]a)?)\s*(?:no\.?|n[oº°]\.?|n[uú]mero|#)?\s*:?\s*"
     r"(\d{1,3}(?:\.\d{3}){1,2}|\d{6,10})\b", None, 1),
)

def detect(text: str) -> list[Finding]:
    found = []
    for kind, pattern, validate, group in _RULES:
        for m in re.finditer(pattern, text):
            if validate is None or validate(m.group(0)):
                found.append(Finding(kind, m.start(group), m.end(group)))
    # Ante solapes gana el hallazgo que empieza antes y, a igual inicio, el más largo.
    found.sort(key=lambda f: (f.start, -(f.end - f.start)))
    result, last_end = [], 0
    for f in found:
        if f.start >= last_end:
            result.append(f)
            last_end = f.end
    return result

def redact(text: str) -> tuple[str, list[Finding]]:
    """Reemplaza cada hallazgo por [[TIPO]]. Sin token por valor aún: no es reversible."""
    findings = detect(text)
    out, pos = [], 0
    for f in findings:
        out += [text[pos:f.start], f"[[{f.type}]]"]
        pos = f.end
    out.append(text[pos:])
    return "".join(out), findings
