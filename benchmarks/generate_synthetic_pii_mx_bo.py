"""Emit the labeled MX/BO corpus as JSONL from annotated synthetic scenarios."""

import json
import re
from collections import Counter


ANNOTATION = re.compile(r"\[\[([A-Z_]+)\|([^\[\]]+)\]\]")
TARGETS = {"CURP": "MX", "RFC": "MX", "CI_BO": "BO", "NIT_BO": "BO"}
ENTITY_TYPES = TARGETS.keys() | {"CEDULA", "EMAIL", "NIT", "TARJETA"}

# Mark only the text expected to be replaced. A negative can still contain
# an existing category, such as EMAIL covering a CURP-shaped local part.
SCENARIOS = {
    "CURP": (
        ("positivo", "CURP: [[CURP|AEXZ000229XQOBCDZ7]].", "Fecha bisiesta, marcador X y código QO."),
        ("positivo", "Clave ([[CURP|BIQX840229HQTNRL08]]).", "Año bisiesto con diferenciador numérico y código QT."),
        ("positivo", "Identificación: [[CURP|COXB951231MDFMPR14]].", "Último día del año y código DF."),
        ("positivo", "Dato [[CURP|duez030915xnezrsa1]], recibido.", "Minúsculas, marcador X y código NE."),
        ("positivo", "Valor: [[CURP|EXQA010101HASTLCA2]].", "X en segunda posición y año 2001."),
        ("positivo", '{"curp":"[[CURP|FAXQ781106MBCVRL25]]"}', "Valor citado dentro de JSON."),
        ("ambiguo", "Inventario [[CURP|GEZB920315HCLDRS04]].", "Forma completa aunque el contexto sea inventario."),
        ("positivo", "Dígito final distinto: [[CURP|AEXZ000229XQOBCDZ8]].", "El dígito cumple el formato y su cálculo queda fuera del alcance."),
        ("positivo", "Límite inferior de la ventana: [[CURP|HIQX000101MCMNRS09]].", "Diferenciador numérico y fecha posible en 1900."),
        ("positivo", "Límite superior de la ventana: [[CURP|JEZQ991231HNLDTRK5]].", "Diferenciador alfabético y fecha posible en 2099."),
        ("ambiguo", "Contacto [[EMAIL|AEXZ000229XQOBCDZ7@correo.invalid]].", "El correo cubre la clave completa."),
        ("positivo", "Titulares [[CURP|KAXQ640229MPLBRC19]] y [[CURP|LOXZ041031HQRGRDA4]].", "Dos claves distintas en el mismo texto."),
        ("negativo", "CURP: AEXZ000229XQOBCD07.", "El 29 de febrero de 1900 es imposible."),
        ("negativo", "CURP: BIQX841331HQTNRL08.", "Mes 13."),
        ("negativo", "CURP: COXB950431MDFMPR14.", "Abril no tiene día 31."),
        ("negativo", "CURP: DUEZ030915XZZZRSA1.", "Código de lugar fuera del catálogo."),
        ("negativo", "CURP: DUEZ030915FNEZRSA1.", "Marcador no admitido."),
        ("negativo", "CURP: AEXZ000229XQOBCDZX.", "El último carácter debe ser numérico."),
        ("negativo", "CURP: ABXZ000229XQOBCDZ7.", "Segunda letra fuera del conjunto de vocales y X."),
        ("negativo", "CURP: AEXZ000229XQOBADZ7.", "Vocal en el bloque de consonantes."),
        ("negativo", "SKU ref_AEXZ000229XQOBCDZ7.", "La clave aparente está dentro de un token."),
        ("negativo", "SKU AEXZ000229XQOBCDZ77.", "Prohibido detectar un prefijo de un token largo."),
        ("negativo", "CURP: AEXZ000229XQOBCDZ.", "Falta el último dígito."),
        ("negativo", "CURP: AEXZ００0229XQOBCDZ7.", "Dígitos de ancho completo."),
    ),
    "RFC": (
        ("positivo", "RFC: [[RFC|A&Z0002291A2]].", "Persona moral, ampersand y fecha posible en 2000."),
        ("positivo", "RFC de contacto [[RFC|BUÑQ920229M17]].", "Persona física con Ñ y fecha bisiesta."),
        ("positivo", "Registro [[RFC|ñ&k791201z9m]].", "Persona moral en minúsculas con Ñ y ampersand."),
        ("positivo", "RFC: [[RFC|&AZ050131C00]].", "Ampersand al inicio del valor."),
        ("positivo", "Código fiscal ([[RFC|TEQZ991231X38]]).", "Persona física y puntuación exterior."),
        ("positivo", '{"rfc":"[[RFC|NQZ0402293D1]]"}', "Persona moral en JSON."),
        ("positivo", "Datos de febrero [[RFC|PEXZ9602299A8]].", "Persona física sin rótulo inmediato."),
        ("ambiguo", "Inventario [[RFC|VQZ971028MZ9]].", "La forma completa se detecta sin etiqueta."),
        ("positivo", "Operación [[RFC|ROQZ001231A7B]].", "Último carácter alfabético en el bloque final."),
        ("positivo", "RFC nacional [[RFC|RAQZ010101000]].", "La terminación 000 no es una excepción general."),
        ("ambiguo", "Contacto [[EMAIL|BUÑQ920229M17@correo.invalid]].", "El correo cubre el RFC aparente."),
        ("positivo", "Claves [[RFC|SEÑQ6902153Z1]] y [[CURP|AEXZ000229XQOBCDZ7]].", "Dos tipos nuevos en el mismo texto."),
        ("negativo", "RFC: XAXX010101000.", "Clave genérica nacional del SAT."),
        ("negativo", "RFC: xexx010101000.", "Clave genérica extranjera con minúsculas."),
        ("negativo", "RFC: NQZ0102293D1.", "El 29 de febrero es imposible para ambos siglos."),
        ("negativo", "RFC: TEQZ991332X38.", "Mes y día fuera de rango."),
        ("negativo", "RFC: TÉQZ991231X38.", "Letra con tilde fuera del bloque admitido."),
        ("negativo", "RFC: ROQZ001231A-B.", "Guion dentro del bloque alfanumérico final."),
        ("negativo", "RFC: ROQZ００1231A7B.", "Dígitos de ancho completo."),
        ("negativo", "Lote XTEQZ991231X38.", "Valor aparente embebido en un token más largo."),
        ("negativo", "Lote &TEQZ991231X38.", "Ampersand contiguo a un bloque de cuatro caracteres."),
        ("negativo", "Lote BUÑQ920229M17&.", "Ampersand unido al extremo derecho."),
        ("negativo", "RFC: QZ971028MZ9.", "Solo dos caracteres iniciales."),
        ("negativo", "RFC: VQZ971028MZ.", "Bloque final incompleto."),
    ),
    "CI_BO": (
        ("positivo", "CI: [[CI_BO|01234]].", "Límite inferior y cero inicial."),
        ("positivo", "C.I. #[[CI_BO|1098765432]].", "Límite superior y separador numeral."),
        ("positivo", "CI Bolivia = [[CI_BO|12345001-2B SC]].", "Complemento y extensión separados por espacio."),
        ("positivo", "CI BO: [[CI_BO|12345002-3C-LP]].", "Complemento y extensión unidos con guiones."),
        ("positivo", "Cédula boliviana [[CI_BO|12345003-4d]].", "Complemento en minúscula."),
        ("positivo", "CI [[CI_BO|12345004-SC]].", "Sufijo único que también es código departamental."),
        ("positivo", "ci\t[[CI_BO|12345005 or]].", "Tabulador y extensión departamental en minúscula."),
        ("positivo", '{"ci":"[[CI_BO|12345006-5E OU]]"}', "Clave y valor JSON con extensión OU."),
        ("positivo", "CI: [[CI_BO|12345007 PD]].", "Extensión Pando separada por espacio."),
        ("positivo", 'Registro CI "[[CI_BO|12345008-6F]]".', "Comillas exteriores al valor."),
        ("ambiguo", "CI: [[CI_BO|12345009]] gracias.", "Preserva la palabra siguiente."),
        ("positivo", "CI: [[CI_BO|12345010]] y CI: [[CI_BO|12345010]].", "Mismo valor en dos posiciones independientes."),
        ("negativo", "Pedido 12345001-2B SC.", "Falta una etiqueta de identidad."),
        ("negativo", "Inventario 12345004-SC.", "Extensión aparente sin etiqueta."),
        ("negativo", "CI: 1234.", "Raíz de cuatro dígitos."),
        ("negativo", "CI: 10987654321.", "Raíz de once dígitos."),
        ("negativo", "CI: 12345001-2BX.", "Complemento de tres caracteres unido al valor."),
        ("negativo", "CI: 12345002-3C-XYZ.", "Extensión unida fuera de la lista operativa."),
        ("negativo", "CI: 12345003XYZ.", "Sufijo pegado a la raíz."),
        ("negativo", "SKU_CI: 12345004.", "Rótulo dentro de una palabra."),
        ("negativo", "CI12345005.", "Falta separador entre etiqueta y valor."),
        ("negativo", "CI:\n12345006.", "El contexto no atraviesa líneas."),
        ("negativo", "CI: １２345007.", "Raíz con dígitos de ancho completo."),
        ("regresion", "Cédula [[CEDULA|52123456]].", "La etiqueta genérica conserva el tipo colombiano."),
    ),
    "NIT_BO": (
        ("positivo", "NIT: [[NIT_BO|12345018]].", "Ocho dígitos y terminación de persona natural."),
        ("positivo", "NIT Bolivia: [[NIT_BO|123450026]].", "Nueve dígitos y terminación de persona jurídica."),
        ("positivo", "NIT boliviano [[NIT_BO|1234500045]].", "Diez dígitos y terminación documentada para extranjero."),
        ("positivo", "NIT BO = [[NIT_BO|12345000019]].", "Once dígitos y terminación personal."),
        ("positivo", "nit #[[NIT_BO|123450000027]].", "Doce dígitos, rótulo en minúscula y separador numeral."),
        ("ambiguo", "NIT BO: [[NIT_BO|1234567890128]].", "Trece dígitos que también pasan Luhn."),
        ("positivo", '{"nit":"[[NIT_BO|01234567890]]"}', "Cero inicial y formato JSON."),
        ("positivo", "NIT\t[[NIT_BO|1234500299]].", "Etiqueta seguida de tabulador."),
        ("positivo", 'NIT "[[NIT_BO|1234500381]]".', "Comillas exteriores al valor."),
        ("ambiguo", "NIT: [[NIT_BO|1234500382]].", "Terminación fuera de los ejemplos de emisión, con etiqueta."),
        ("positivo", "C.I.: [[CI_BO|12345042]] y NIT BO: [[NIT_BO|12345042018]].", "CI y NIT en la misma línea."),
        ("regresion", "NIT: [[NIT|800197268-4]].", "NIT colombiano con guion y verificador."),
        ("regresion", "NIT: [[NIT|800.197.268-4]].", "NIT colombiano con separadores de miles."),
        ("regresion", "Tarjeta [[TARJETA|1234567890128]].", "La misma secuencia Luhn mantiene su tipo con rótulo de tarjeta."),
        ("negativo", "Serie 12345018.", "Número continuo sin contexto tributario."),
        ("negativo", "NIT: 1234501.", "Siete dígitos."),
        ("negativo", "NIT: 12345678901234.", "Catorce dígitos, sin recorte."),
        ("negativo", "NIT: 12345018XYZ.", "Valor aparente dentro de un token más largo."),
        ("negativo", "NIT: 12345018-XYZ.", "Sufijo unido fuera del formato continuo."),
        ("negativo", "SKU_NIT: 12345018.", "Rótulo incrustado dentro de otra palabra."),
        ("negativo", "NIT12345018.", "Falta separador."),
        ("negativo", "NIT:\n12345018.", "Rótulo en la línea anterior."),
        ("negativo", "NIT: １２345018.", "Dígitos de ancho completo."),
        ("negativo", "NIT: 1234 5018.", "Número fragmentado por espacio."),
    ),
}


def make_case(target, index, difficulty, template, note):
    parts = []
    entities = []
    cursor = 0
    offset = 0
    for match in ANNOTATION.finditer(template):
        prefix = template[cursor:match.start()]
        kind, value = match.groups()
        if kind not in ENTITY_TYPES:
            raise ValueError(f"Unknown entity type {kind!r}")
        start = offset + len(prefix)
        offset = start + len(value)
        parts.extend((prefix, value))
        entities.append({"type": kind, "start": start, "end": offset})
        cursor = match.end()
    parts.append(template[cursor:])
    text = "".join(parts)
    if "[[" in text or "]]" in text:
        raise ValueError(f"Unparsed annotation in {target} case {index}")
    return {
        "id": f"MXBO-{target}-{index:02d}",
        "country": TARGETS[target],
        "target": target,
        "text": text,
        "entities": entities,
        "difficulty": difficulty,
        "note": note,
    }


def main():
    cases = [
        make_case(target, index, *scenario)
        for target, scenarios in SCENARIOS.items()
        for index, scenario in enumerate(scenarios, 1)
    ]
    texts = Counter(case["text"] for case in cases)
    if any(count > 1 for count in texts.values()):
        raise ValueError("Duplicate case text")
    for case in cases:
        print(json.dumps(case, ensure_ascii=False, separators=(",", ":")))


if __name__ == "__main__":
    main()
