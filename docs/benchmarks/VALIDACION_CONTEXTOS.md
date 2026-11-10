# Ampliación de pruebas y validación de contextos

Fecha, 10 de noviembre de 2026. Benjamín (`benjadiaz112`) y Codex ampliaron
la validación del PR #20 desde `e554061977fd00867bf0bef265087714d36cdb28`.
El [reporte JSON](../../benchmarks/resultados_validacion_contextos.json)
registra los hashes de código, datos y evaluador, junto con las diferencias
por caso y los resultados de las comprobaciones.

## Decisión de detección

Se amplió el contexto de CI/NIT bolivianos y de los CURP/RFC con error de
verificador, usando un vocabulario acotado de descriptores de campo.
Incluye «número», «de identificación», «del titular», «de muestra»,
«de laboratorio», «de prueba», «de identidad», «del contribuyente»,
«Nro.», «No.» y «ficticio». Se admite uno por etiqueta, en la misma línea.
Los términos fuera de esa lista conservan el tratamiento anterior.

Esta política amplía etiquetas que expresan identidad. El resto de la
estructura, las fechas y las excepciones de verificador conservan sus
comprobaciones. Se mantiene la exclusión de RFC genéricos y la restricción
de homonimias fuera de rango con verificador incorrecto. Los detalles están
en la [especificación de detección](ISSUE_16_COMPORTAMIENTO_DETECCION.md).

También se reforzaron los límites del rótulo ante marcas combinantes y el
rechazo de bloques numéricos partidos después de CI/NIT bolivianos.
El enmascaramiento conserva los intervalos sobre el texto original.

## Pruebas preparadas antes del ajuste

El [corpus de contextos](../../benchmarks/synthetic_pii_contexts.jsonl)
contiene 96 casos, con 48 entidades esperadas y 48 negativos. Sus IDs y
posiciones se calcularon desde anotaciones explícitas. Los casos fueron
redactados por Codex antes de modificar las reglas. La procedencia corresponde
a validación sintética guiada por escenarios.

Los positivos cubren el contexto acotado. Los negativos incluyen palabras
ajenas al campo, rótulos de otro país, etiquetas dentro de otra palabra,
caracteres visualmente parecidos, saltos de línea, tokens incrustados,
exceso de longitud, separadores incorrectos y marcas combinantes.

Las diez pruebas adicionales de JSON comprueban claves acentuadas,
escapes y los intervalos del cuerpo original. Cinco pruebas del consumidor
HTTP verifican el cuerpo preparado y su longitud. Antes del ajuste, el
archivo de pruebas de contexto obtuvo 50 casos aprobados y 56 fallidos.
Después del ajuste pasan sus 106 casos.

Se amplió el comprobador generado con el modo `--contexts`. Las semillas
20261111 y 20261112 producen 2.220 comprobaciones cada una, con siete tipos,
variantes de contexto, negativos, texto, JSON literal y escapado y valores
repetidos. Se construyen valores y expectativas mediante cálculos y plantillas
del comprobador, sin usar la salida del detector para asignar las etiquetas.

La suite completa local en Python 3.14.4 obtuvo 611 pruebas aprobadas y
12 advertencias de obsolescencia. Las 4.440 comprobaciones generadas terminaron
sin diferencias. El workflow incluye pruebas regionales y comprobaciones
generadas también en Python 3.11 y 3.13, con dependencias de bootstrap fijadas
y requests 2.34.2. Esos jobs validan el subconjunto regional y su consumidor HTTP.

## Repetición de benchmarks

| Corpus | Casos | Antes TP / FP / FN | Después TP / FP / FN |
|---|---:|---:|---:|
| Histórico | 172 | 114 / 0 / 36 | 130 / 0 / 20 |
| Desarrollo MX/BO | 96 | 55 / 0 / 0 | 55 / 0 / 0 |
| Política MX | 60 | 29 / 0 / 0 | 29 / 0 / 0 |
| Cobertura RUT/NIT | 60 | 35 / 0 / 0 | 35 / 0 / 0 |
| Contextos adicionales | 96 | 4 / 2 / 44 | 48 / 0 / 0 |

Se compararon exactamente tipo e intervalo por caso. Los cuatro corpus previos
conservan sus entradas y etiquetas. Se mantuvieron todos los aciertos de la
revisión anterior. En el histórico se recuperaron cuatro CURP con etiqueta
extendida y error de verificador, cuatro CI bolivianos y ocho NIT bolivianos.
Los demás 156 casos históricos conservan sus detecciones.

El recall histórico aumenta del 76 % al 86,67 %, con precisión observada del
100 % y F1 del 92,86 %. Los dos falsos positivos del corpus nuevo estaban
asociados a rótulos con marca combinante. Se eliminan con la comprobación
del inicio completo de la coincidencia.

Las 20 omisiones restantes son doce direcciones de un tipo pendiente, cuatro
CURP con estructura incompatible y cuatro RFC genéricos excluidos por la
política. Sus etiquetas históricas se conservan.

Los ejemplos y el comprobador provienen de este trabajo de implementación y
validación. Las cifras describen los conjuntos sintéticos y las semillas
ejecutadas. Los formatos futuros, la validez de las etiquetas históricas
incompatibles y la evaluación poblacional requieren evidencia adicional.

## Reproducción

```bash
.venv/bin/python -m pytest -q --tb=short tests/
.venv/bin/python -m benchmarks.check_review_scenarios --contexts --seed 20261111
.venv/bin/python -m benchmarks.check_review_scenarios --contexts --seed 20261112
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_r3.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_bo.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_policy.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_coverage.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_contexts.jsonl
```
