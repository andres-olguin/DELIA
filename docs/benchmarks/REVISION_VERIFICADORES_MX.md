# Revisión de verificadores y contexto de CURP/RFC

Ejecución local del 9 de noviembre de 2026 con Python 3.14.4. La referencia
anterior del PR #20 es `f2e3f5a7c7fea090a5d1e68fc194403675fc4d4b`.
El [reporte JSON](../../benchmarks/resultados_revision_politica_mx.json)
identifica el código revisado por su SHA-256, registra los hashes de cada
corpus y del evaluador y contiene las diferencias por caso.

## Comportamiento implementado

CURP y RFC requieren formato, límites y fecha aceptados por las reglas actuales.
Cuando el verificador coincide, se protege el valor incluso sin etiqueta.
Cuando falla, se exige una etiqueta inmediata del mismo tipo, en la misma
línea. Esto protege datos con un posible error de captura.

El cálculo normaliza minúsculas y escapes JSON de Ñ sobre una copia del valor.
La detección y el enmascaramiento conservan los índices del texto original.
Las excepciones de RFC genéricos, la precedencia de correos y los contratos
de los tipos anteriores continúan bajo sus pruebas.

Los detalles de contexto, límites, calendario y excepciones están en la
[política de detección](ISSUE_16_COMPORTAMIENTO_DETECCION.md).

## Resultados con etiquetas históricas originales

| Detector | Casos | TP | FP | FN | Precisión | Recall |
|---|---:|---:|---:|---:|---:|---:|
| Línea base inicial | 172 | 71 | 3 | 79 | 95,95 % | 47,33 % |
| PR antes del ajuste | 172 | 99 | 5 | 51 | 95,19 % | 66,00 % |
| PR con verificador y contexto | 172 | 95 | 4 | 55 | 95,96 % | 63,33 % |

Hay cinco casos con cambios respecto al PR anterior. T0163 deja de producir
el falso positivo CURP. T0162 conserva el falso positivo RFC frente a su
etiqueta histórica negativa, porque se protege su contexto explícito.
Los casos T0061, T0064, T0067 y T0070 pierden un acierto cada uno. Reutilizan
una CURP con verificador incorrecto y palabras intermedias entre la etiqueta
y el valor. Se contabilizan como omisiones bajo esta política.

Los otros 167 casos conservan exactamente sus detecciones anteriores. Se
mantienen las 71 detecciones correctas de la línea base original. Los resultados
de Chile, Colombia y Global conservan sus valores anteriores.

El ajuste reduce un falso positivo y cuatro aciertos del PR anterior en este
corpus. La aceptación de este intercambio y de T0162 requiere revisión humana
antes de decidir la fusión.

## Corpus de desarrollo y ejemplos adicionales

| Corpus y versión | Detector anterior TP / FP / FN | Detector ajustado TP / FP / FN |
|---|---:|---:|
| MX/BO original de 96 casos | 55 / 0 / 0 | 36 / 0 / 19 |
| MX/BO actualizado de 96 casos | 55 / 0 / 0 | 55 / 0 / 0 |
| Política nueva de 60 casos | 29 / 26 / 0 | 29 / 0 / 0 |

La versión original de MX/BO contiene valores que se construyeron para comprobar
formato y fecha. El ajuste deja de aceptar 19 entidades de esa versión cuyos
verificadores fallan y carecen de etiqueta inmediata. Se conserva esta medición
en el JSON y la versión original del corpus en Git.

En el generador del corpus actualizado se corrigieron los verificadores de
los positivos de CURP/RFC. Dos escenarios mantienen deliberadamente un error
de verificador y ahora llevan etiqueta inmediata, con sus notas actualizadas.
Los 96 IDs y las 55 entidades esperadas se conservan. Se regeneraron los
índices a partir de las anotaciones del generador. Los negativos y los casos
bolivianos conservan sus entradas.

Los 60 ejemplos adicionales cruzan verificadores y contextos, además de cubrir
Ñ, ampersand, RFC físico y moral, casos especiales de verificador A/0, JSON,
límites, fechas y solapes con correo. Codex preparó los casos y sus etiquetas
antes de implementar el ajuste. Su revisión independiente por otra persona
sigue pendiente.

Los dos resultados de 100 % describen estos corpus de desarrollo y la política
acordada. Las etiquetas históricas originales producen las cifras de la tabla
de 172 casos.

## Verificación y reproducción

Se ejecutó `.venv/bin/python -m pytest -q --tb=short tests/` con resultado
de 390 pruebas aprobadas y 22 advertencias de obsolescencia. Los 78 casos
adicionales de pytest comprueban los 60 ejemplos nuevos, seis grupos de
mutaciones del verificador y doce variantes de contexto. Cada ejemplo del
corpus comprueba tipo, intervalos y texto enmascarado.

La regeneración del corpus MX/BO se contrastó byte por byte con el generador.
GitHub Actions ejecutará la suite y los tres benchmarks. El resultado remoto
debe consultarse en el commit publicado.

```bash
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_bo.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_policy.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_r3.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_r3.jsonl --detector-ref f2e3f5a7c7fea090a5d1e68fc194403675fc4d4b
```

Para repetir la medición de desarrollo con sus entradas originales:

```bash
report_dir=$(mktemp -d)
git show f2e3f5a:benchmarks/synthetic_pii_mx_bo.jsonl > "$report_dir/mx_bo_original.jsonl"
.venv/bin/python -m benchmarks.evaluate --dataset "$report_dir/mx_bo_original.jsonl"
.venv/bin/python -m benchmarks.evaluate --dataset "$report_dir/mx_bo_original.jsonl" --detector-ref f2e3f5a
```

La política de errores cubre fallos del verificador con formato y fecha
aceptados. Las variantes con longitud o fecha incorrectas quedan fuera de ese
reconocimiento. El cálculo local de consistencia requiere una verificación
distinta para demostrar inscripción o titularidad. La protección del proveedor
mediante `/proxy/v1/chat` tiene su seguimiento separado del detector.
