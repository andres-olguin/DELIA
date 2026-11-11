# Revisión de verificadores y contexto de CURP/RFC

## Ampliación de cobertura, 10 de noviembre de 2026

La referencia anterior es `658dbad5b4112b44d3658922ee2bc7f5dfacb14e`.
El [reporte de cobertura](../../benchmarks/resultados_cobertura.json)
conserva los hashes de código, evaluador y datos y las diferencias por caso.
Los tres corpus anteriores se evaluaron con sus entradas y etiquetas originales.
La ampliación cubre RUT y NIT colombiano tras clasificar las 52 omisiones.

| Corpus | Antes TP / FP / FN | Después TP / FP / FN |
|---|---:|---:|
| Histórico, 172 casos | 98 / 0 / 52 | 114 / 0 / 36 |
| Desarrollo MX/BO, 96 casos | 55 / 0 / 0 | 55 / 0 / 0 |
| Política MX, 60 casos | 29 / 0 / 0 | 29 / 0 / 0 |
| Cobertura adicional, 60 casos | 6 / 2 / 29 | 35 / 0 / 0 |

Las 16 diferencias históricas son detecciones correctas nuevas en T0013–T0020
y T0033–T0040. La comparación exacta conserva los otros 156 casos y todos los
98 aciertos anteriores. El recall aumenta de 65,33 % a 76 %. La precisión
observada permanece en 100 % y el F1 pasa de 79,03 % a 86,36 %.

Se incorporaron espacios alrededor del guion de RUT/NIT y agrupaciones con
espacios en NIT colombiano, manteniendo sus verificadores. RUT sin guion
requiere campo etiquetado, descriptor limitado y DV correcto. Los límites se
reforzaron para evitar capturas parciales en números más largos o dentro de
tokens y agrupaciones mixtas.

Antes de modificar el detector se prepararon 60 casos de cobertura, con 35
entidades y 28 negativos. En la primera ejecución de pytest, 32 casos pasaron
y 28 fallaron. Tras el ajuste pasaron los 60. Se agregaron cinco grupos de
mutaciones del verificador y una prueba de JSON preparado por el consumidor
HTTP, incluyendo el verificador K de RUT. La suite completa obtuvo 484 pruebas
aprobadas y 12 advertencias.
El workflow ejecuta ahora los cuatro benchmarks.

Los ejemplos nuevos y sus etiquetas fueron preparados por Codex. Su revisión
independiente por otra persona queda pendiente. La comparación demuestra
conservación de las detecciones correctas en los corpus evaluados y describe
el comportamiento sobre esos datos de laboratorio.

Las 36 omisiones restantes se distribuyen así:

| Tipo | Omisiones | Motivo observado |
|---|---:|---|
| DIRECCION | 12 | Tipo pendiente de implementación. |
| CURP | 8 | Cuatro con estructura incompatible y cuatro con verificador incorrecto sin contexto inmediato admitido. |
| RFC | 4 | Clave genérica pública excluida por la política. |
| CI_BO | 4 | Palabras intermedias fuera del contexto admitido. |
| NIT_BO | 8 | Palabras intermedias fuera del contexto admitido. |

Las discrepancias entre etiquetas históricas y política deben revisarse con una
persona independiente antes de ampliar tolerancias de contexto o estructuras.
Las direcciones requieren especificación y pruebas propias. El corpus histórico
conserva tanto esas etiquetas como sus repeticiones.

```bash
.venv/bin/python -m pytest -q --tb=short tests/
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_r3.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_bo.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_policy.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_coverage.jsonl
```

## Corrección de los cuatro falsos positivos, 10 de noviembre de 2026

La referencia anterior es `b7d0294bf95a2d9c89257d2ab42de8ba3b45efa3`.
El [reporte de corrección](../../benchmarks/resultados_correccion_fp.json)
registra hashes de los detectores, los corpus y el evaluador, así como las
diferencias y los errores restantes por caso. Los tres corpus se evaluaron
con las mismas entradas y etiquetas que en esa referencia.

| Corpus | Antes TP / FP / FN | Después TP / FP / FN |
|---|---:|---:|
| Histórico, 172 casos | 95 / 4 / 55 | 98 / 0 / 52 |
| Desarrollo MX/BO, 96 casos | 55 / 0 / 0 | 55 / 0 / 0 |
| Política MX, 60 casos | 29 / 0 / 0 | 29 / 0 / 0 |

En el histórico se modifican exactamente cuatro casos. T0041, T0045 y T0049
repiten una cédula de diez dígitos con puntos. Se captura ahora el intervalo
completo en lugar de recortarlo. Cada corrección elimina un FP y un FN y agrega
un TP. Se bloquean también las capturas parciales de números más largos o con
agrupaciones incorrectas. El consumidor `LoggedSession` queda cubierto con un
JSON preparado que usa la palabra cédula con su tilde escapada.

T0162 deja de clasificarse como RFC. Se refinó la protección por contexto cuando
falla el verificador. En ese caso una homonimia iniciada en W/X/Y/Z se descarta,
incluso con etiqueta inmediata. El cálculo publicado toma las tres últimas
cifras de una suma, las divide por 34 y usa el cociente y el residuo para
construir la homonimia. El cociente máximo es 29, que corresponde a V. Esta
restricción se aplica a la clase de candidatos, con pruebas adicionales de las
cuatro letras, minúsculas y JSON.
[Documento técnico SAT, copia consultada, procedimiento y Anexo II](https://www.mariovaldez.net/files/IFAI%200610100135506%20065%20Algoritmo%20para%20generar%20el%20RFC%20con%20homoclave%20para%20personas%20fisicas%20y%20morales.pdf).

Se mantiene la protección conservadora de candidatos con verificador coherente
y la tolerancia previa a otros errores del verificador con etiqueta inmediata.
La cota adicional de homonimia endurece solamente esta última vía. La regla
local sigue teniendo un objetivo de enmascaramiento y requiere una comprobación
distinta para demostrar inscripción o titularidad.

Los otros 168 casos históricos conservan exactamente sus detecciones. Los
95 aciertos de la revisión anterior se mantienen y se agregan tres. Los
resultados son precisión 100 %, recall 65,33 % y F1 79,03 % en este corpus.
Las 52 omisiones restantes se conservan en el reporte. Las cifras describen
el laboratorio sintético y requieren revisión independiente de las etiquetas.

Se ejecutó la suite completa con 418 pruebas aprobadas y 12 advertencias de
obsolescencia. Las 25 pruebas añadidas cubren los cuatro casos históricos,
dieciséis variantes de cédula, cuatro grupos de RFC y un cuerpo JSON preparado
por el consumidor HTTP. Los comandos de los tres benchmarks figuran más abajo.
Los resultados del 9 de noviembre que siguen se conservan como antecedentes.

## Medición del ajuste inicial, 9 de noviembre de 2026

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
inicial de 390 pruebas aprobadas y 22 advertencias de obsolescencia. Tras
incorporar `main` en `a3db7ff` y resolver sus conflictos, la suite completa
obtuvo 393 pruebas aprobadas y 12 advertencias. Los 78 casos
adicionales de pytest comprueban los 60 ejemplos nuevos, seis grupos de
mutaciones del verificador y doce variantes de contexto. Cada ejemplo del
corpus comprueba tipo, intervalos y texto enmascarado.

La regeneración del corpus MX/BO se contrastó byte por byte con el generador.
GitHub Actions ejecutará la suite y los tres benchmarks. El resultado remoto
debe consultarse en el commit publicado.

La sincronización conservó íntegros los cambios de `main` en
`app/api/proxy.py`, `services/audit.py` y `services/proxy.py`, que deshabilitan
el envío antiguo al proveedor. Se conservaron también las pruebas nuevas de
Foundation de `main` y el caso aislado de importación rota del PR #20.

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
