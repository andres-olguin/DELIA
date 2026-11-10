# Comparación del PR #20 con el benchmark histórico de 172 casos

Este documento registra la revisión `c2a1c9f` y conserva sus resultados.
El ajuste posterior de verificadores y contexto se evalúa en la
[revisión de verificadores](REVISION_VERIFICADORES_MX.md).

Ejecución local del 9 de noviembre de 2026 con Python 3.14.4. Se usó el mismo
[corpus sintético de Ronda 3](../../benchmarks/synthetic_pii_r3.jsonl) para ambos
detectores, con 150 entidades anotadas y 22 casos sin entidades. Cada acierto
exige coincidencia exacta de tipo y de posiciones de inicio y fin. Las etiquetas
históricas se conservaron como referencia, incluso cuando difieren de la
política del PR.

| Detector | TP | FP | FN | Precisión | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| Línea base histórica reproducida | 71 | 3 | 79 | 95,95 % | 47,33 % | 63,39 % |
| PR #20 | 99 | 5 | 51 | 95,19 % | 66,00 % | 77,95 % |

El PR conserva todas las detecciones previas, incluidos los 71 aciertos y los
3 falsos positivos de cédula en Colombia. Suma 28 aciertos y 2 falsos positivos
en los nuevos tipos. El recall sube 18,67 puntos porcentuales y la precisión
baja 0,75 puntos porcentuales, calculados antes de redondear.

| Grupo | Base TP / FP / FN | PR TP / FP / FN |
|---|---:|---:|
| Chile | 21 / 0 / 11 | 21 / 0 / 11 |
| Colombia | 32 / 3 / 14 | 32 / 3 / 14 |
| Global | 12 / 0 / 0 | 12 / 0 / 0 |
| México | 3 / 0 / 27 | 19 / 2 / 11 |
| Bolivia | 3 / 0 / 27 | 15 / 0 / 15 |

## Comparación por caso

Los conjuntos de detecciones fueron idénticos en 142 de los 172 casos. En los
30 casos que cambiaron se agregó exactamente una detección por caso. Todas las
detecciones de las categorías previas conservaron su tipo y sus posiciones.

| Cambio | Casos |
|---|---|
| 8 aciertos nuevos de CURP | T0061, T0063, T0064, T0066, T0067, T0069, T0070, T0072 |
| 8 aciertos nuevos de RFC | T0074, T0075, T0077, T0078, T0080, T0081, T0083, T0084 |
| 8 aciertos nuevos de CI_BO | T0086, T0087, T0089, T0090, T0092, T0093, T0095, T0096 |
| 4 aciertos nuevos de NIT_BO | T0098, T0101, T0104, T0107 |
| 1 falso positivo nuevo de RFC | T0162 |
| 1 falso positivo nuevo de CURP | T0163 |

T0162 contiene un valor parecido a un RFC que supera los chequeos de formato
y calendario. T0163 presenta como código de inventario un valor que cumple el
patrón y la fecha de una CURP. La regla mexicana reconoce ambos valores por
estructura y calendario sin exigir una etiqueta inmediata. El corpus marca
ambos casos como negativos.

De las 51 omisiones del PR, 31 pertenecen a categorías previas y ya estaban
presentes en la línea base. Las otras 20 corresponden a los cuatro tipos nuevos.

| Omisiones del PR | Casos | Motivo observado |
|---|---|---|
| 4 CURP | T0062, T0065, T0068, T0071 | Reutilizan un valor con una vocal en el bloque de tres consonantes. |
| 4 RFC | T0073, T0076, T0079, T0082 | Reutilizan un RFC genérico que el PR excluye por diseño. |
| 4 CI_BO | T0085, T0088, T0091, T0094 | El texto «de muestra» separa la etiqueta del valor. |
| 8 NIT_BO | T0097, T0099, T0100, T0102, T0103, T0105, T0106, T0108 | Las frases «Bolivia ficticio» y «de laboratorio» interrumpen el contexto inmediato admitido. |

La comparación confirma que las detecciones anteriores se preservan en este
corpus y muestra un aumento de falsos positivos al ampliar la cobertura.
Los resultados corresponden a las etiquetas históricas de laboratorio. El
[corpus de desarrollo MX/BO](RESULTADOS_MX_BO.md) y la evaluación con casos
independientes se reportan por separado.

## Reproducción

El detector de la línea base corresponde al blob histórico
`9cdc531fc7dfb38eb05e0c53bdb2cec795a4ae82`. GitHub identificó
`c2a1c9f298f33ddce79cadd28c3bb5f6e2fa1c67` como la revisión del PR #20 al
ejecutar la comparación. El SHA-256 del corpus fue
`191ae4de8598321402460e8367a2944a239f69a54d569a6065c287cef6bf4f3f`.

Desde la raíz del repositorio, con las dos revisiones disponibles en Git:

```bash
report_dir=$(mktemp -d)
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_r3.jsonl \
  --detector-ref 0c3ea173624c2c6565f4822848310bc1629c6f1f --out "$report_dir/base.json"
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_r3.jsonl \
  --detector-ref c2a1c9f298f33ddce79cadd28c3bb5f6e2fa1c67 --out "$report_dir/pr20.json"
.venv/bin/python - "$report_dir" <<'PY'
import json
from pathlib import Path
import sys

directory = Path(sys.argv[1])
base, pr = [json.loads((directory / file).read_text()) for file in ("base.json", "pr20.json")]
assert base["dataset_sha256"] == pr["dataset_sha256"]
for report in (base, pr):
    print(report["detector_revision"], report["results"]["total"])

# Con las mismas etiquetas, FP y FN determinan la salida completa de cada caso.
before, after = [{row["id"]: row for row in report["case_errors"]} for report in (base, pr)]
changed = [case for case in sorted(before.keys() | after.keys()) if before.get(case) != after.get(case)]
print(f"Casos con cambios: {len(changed)} de {base['cases']}")
for case in changed:
    print(case, before.get(case), "->", after.get(case))
PY
```
