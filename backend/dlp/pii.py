import re
from datetime import date
from typing import NamedTuple
from unicodedata import category

class Finding(NamedTuple):
    type: str
    start: int
    end: int

_NIT_PRIMES = (3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67, 71)
_CURP_CHECKSUM_ALPHABET = "0123456789ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
_RFC_CHECKSUM_ALPHABET = "0123456789ABCDEFGHIJKLMN&OPQRSTUVWXYZ Ñ"

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
        body, dv = re.sub(r"[. \t]", "", raw).upper().split("-")
        return dv_fn(body) == dv
    return check


def _valid_rut_without_hyphen(raw: str) -> bool:
    body, digit = raw.split()
    return rut_dv(body) == digit.upper()


def _valid_date(value: str, century: int) -> bool:
    try:
        date(century + int(value[:2]), int(value[2:4]), int(value[4:6]))
    except ValueError:
        return False
    return True


def _valid_curp(raw: str) -> bool:
    # La regex comprueba estructura. El diferenciador determina la ventana del año.
    century = 1900 if raw[16].isdigit() else 2000
    return _valid_date(raw[4:10], century)


def _valid_rfc(raw: str) -> bool:
    if raw.upper() in {"XAXX010101000", "XEXX010101000"}:
        return False
    value = raw[-9:-3]
    return _valid_date(value, 1900) or _valid_date(value, 2000)


def _valid_mx_checksum(kind: str, raw: str) -> bool:
    # Normalizar solo para el cálculo, preservando los índices del cuerpo original.
    value = re.sub(r"\\u00[df]1", "Ñ", raw, flags=re.IGNORECASE).upper()
    if kind == "CURP":
        total = sum(
            _CURP_CHECKSUM_ALPHABET.index(char) * (18 - index)
            for index, char in enumerate(value[:-1])
        )
        return value[-1] == str((-total) % 10)
    body = value[:-1].rjust(12)
    total = sum(
        _RFC_CHECKSUM_ALPHABET.index(char) * (13 - index)
        for index, char in enumerate(body)
    )
    return value[-1] == "0123456789A"[(-total) % 11]


# Los límites conservan semántica Unicode, mientras los bloques de identificador
# usan letras y dígitos explícitos. Así se evita aceptar letras Unicode similares.
_CURP_PATTERN = (
    r"(?<![\w&-])(?ai:[A-Z][AEIOUX][A-Z]{2}[0-9]{6}[HMX]"
    r"(?:AS|BC|BS|CC|CH|CL|CM|CS|DF|DG|GR|GT|HG|JC|MC|MN|MS|NE|NL|NT|"
    r"OC|PL|QO|QR|QT|SL|SP|SR|TC|TL|TS|VZ|YN|ZS)"
    r"[B-DF-HJ-NP-TV-Z]{3}[A-Z0-9][0-9])(?![\w&-])"
)
# requests serializa Ñ/ñ como \u00d1/\u00f1 en JSON. Capturar el escape
# completo mantiene los índices sobre el cuerpo original y permite reemplazarlo.
_RFC_PATTERN = (
    r"(?<![\w&-])(?ai:(?:[A-ZÑñ&]|\\u00[DF]1){3,4}"
    r"[0-9]{6}[A-Z0-9]{3})(?![\w&-])"
)

# Etiqueta y valor en la misma línea, incluyendo claves y valores JSON citados.
_ID_SEPARATOR = r'"?(?:[ \t]*[:=#][ \t]*|[ \t]+)"?'
_MX_CONTEXT_PATTERNS = {
    kind: re.compile(r"(?<![\w&-])(?ai:" + kind + ")" + _ID_SEPARATOR + r"\Z")
    for kind in ("CURP", "RFC")
}
_NUMERIC_END = r"(?![\w-]|[.,/][0-9])(?![ \t]*-)"
_RUT_PATTERN = (
    r"(?<![\w.-])(?:[0-9]{1,2}(?:\.[0-9]{3}){2}|[0-9]{7,8})"
    r"[ \t]*-[ \t]*[0-9kK]" + _NUMERIC_END
)
_RUT_FIELD_PATTERN = (
    r"(?<!\w)(?ai:rut)(?:[ \t]+[^\W\d_]{1,24}){0,3}"
    + _ID_SEPARATOR
    + r"([0-9]{7,8}[ \t]+[0-9kK])"
    + _NUMERIC_END
)
_NIT_CO_PATTERN = (
    r"(?<![\w.-])(?:[0-9]{3}(?:\.[0-9]{3}){2}|"
    r"[0-9]{3}(?:[ \t]+[0-9]{3}){2}|[0-9]{9})"
    r"[ \t]*-[ \t]*[0-9]" + _NUMERIC_END
)
_CI_BO_PATTERN = (
    r"(?<!\w)(?ai:ci(?:[ \t]+(?:bolivia|bo))?|c\.i\.|c[eéÉ]dula[ \t]+boliviana)"
    + _ID_SEPARATOR
    + r"((?ai:[0-9]{5,10}(?:[ \t]*-[ \t]*[A-Z0-9]{2})?"
    r"(?:(?:[ \t]*-[ \t]*|[ \t]+)(?:BE|CB|CH|LP|OR|OU|PD|PT|SC|TJ))?))"
    + _NUMERIC_END
)
_NIT_BO_PATTERN = (
    r"(?<!\w)(?ai:nit(?:[ \t]+(?:bolivia|boliviano|bo))?)"
    + _ID_SEPARATOR
    + r"([0-9]{8,13})"
    + _NUMERIC_END
)
_REGIONAL_TYPES = {"CURP", "RFC", "CI_BO", "NIT_BO", "RUT", "NIT"}


def _has_combining_boundary(text: str, start: int, end: int) -> bool:
    # Una marca combinante pertenece al token vecino aunque no coincida con \w.
    for position in (start - 1, end):
        if 0 <= position < len(text) and category(text[position]).startswith("M"):
            return True
    return False

# (tipo, regex, validador opcional sobre el grupo a enmascarar, grupo)
# shortcut: NIT colombiano de 9 dígitos y RUT de 7-8, ampliar si aparecen falsos negativos.
_RULES = (
    # El orden resuelve empates de intervalo a favor del contexto boliviano.
    ("CI_BO", _CI_BO_PATTERN, None, 1),
    ("NIT_BO", _NIT_BO_PATTERN, None, 1),
    ("EMAIL", r"(?:[\w.+&-]|\\u00[dDfF]1)+@[\w-]+(?:\.[\w-]+)+", None, 0),
    ("RUT", _RUT_PATTERN, _check_id(rut_dv), 0),
    ("RUT", _RUT_FIELD_PATTERN, _valid_rut_without_hyphen, 1),
    ("NIT", _NIT_CO_PATTERN, _check_id(nit_dv), 0),
    ("TARJETA", r"\b\d(?:[ -]?\d){12,18}\b", lambda s: luhn(re.sub(r"\D", "", s)), 0),
    ("TELEFONO", r"\+(?:57|56)[\s-]?\d(?:[\s-]?\d){7,9}\b", None, 0),
    # La cédula no tiene dígito verificador: solo se detecta con una palabra de contexto.
    ("CEDULA",
     r"(?i)\b(?:c\.\s?c\.?|cc|c(?:[eé]|\\u00[ce]9)dula"
     r"(?:\s+de\s+ciudadan(?:[ií]|\\u00[ce]d)a)?)\s*"
     r"(?:no\.?|n[oº°]\.?|n[uú]mero|#)?\s*:?\s*"
     r"(\d(?:\.\d{3}){3}|\d{1,3}(?:\.\d{3}){1,2}|\d{6,10})"
     r"(?![\w-]|[.,/][0-9])", None, 1),
    # El verificador o el contexto inmediato se comprueban en detect().
    ("CURP", _CURP_PATTERN, _valid_curp, 0),
    ("RFC", _RFC_PATTERN, _valid_rfc, 0),
)

def detect(text: str) -> list[Finding]:
    found = []
    for kind, pattern, validate, group in _RULES:
        for m in re.finditer(pattern, text):
            if kind in _REGIONAL_TYPES and _has_combining_boundary(text, m.start(group), m.end(group)):
                continue
            if kind in _MX_CONTEXT_PATTERNS and not _valid_mx_checksum(kind, m.group(0)):
                # La homonimia se obtiene de 000–999 dividido entre 34.
                # Su cociente máximo es 29 (V en el Anexo II del SAT).
                # W/X/Y/Z no justifican aceptar un verificador fallido por contexto.
                if kind == "RFC" and m.group(0)[-3].upper() in "WXYZ":
                    continue
                context = _MX_CONTEXT_PATTERNS[kind].search(text, 0, m.start(group))
                if context is None or _has_combining_boundary(text, context.start(), m.start(group)):
                    continue
            if validate is None or validate(m.group(group)):
                found.append(Finding(kind, m.start(group), m.end(group)))
    # Ante solapes gana el hallazgo que empieza antes y, a igual inicio, el más largo.
    # A igualdad de intervalo prevalece el orden de _RULES.
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
