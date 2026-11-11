# Revisión técnica adicional del PR #20

La [validación ampliada de contextos](VALIDACION_CONTEXTOS.md) registra la
revisión posterior con 611 pruebas y cinco benchmarks. Este documento conserva
los resultados del paso previo.

Fecha, 10 de noviembre de 2026. Revisión del diff desde `a3db7ff` hasta
`ed8c24047f9075136cbd98919f1bbf99254dd2b7` y corrección de los hallazgos.
El [reporte JSON](../../benchmarks/resultados_revision_final.json) registra el
hash del detector corregido, los datos evaluados y los resultados.

Benjamín (`benjadiaz112`) realizó la revisión técnica junto a Codex en la misma
sesión de implementación. Se usaron comprobaciones adicionales y escenarios
generados por Codex después de la implementación. La procedencia corresponde
a una revisión técnica propia. La independencia entre autores requiere una
revisión distinta y estos resultados deben conservar esa distinción.

## Hallazgos y correcciones

1. Una etiqueta como «cédula boliviana» funcionaba en texto directo y se omitía
   cuando JSON escapaba la tilde. Se agregó reconocimiento del escape del rótulo,
   conservando los límites y el intervalo original del identificador.
2. La regla de cédula colombiana omitía valores cuando la etiqueta y el número
   aparecían entre comillas como clave y valor JSON. Se admitieron esas comillas
   y se mantuvo la captura completa del número.
3. La descripción del PR conservaba métricas de la primera revisión y declaraba
   pendientes los verificadores ya implementados. Debe actualizarse al publicar
   la corrección para describir el comportamiento y la evidencia actuales.

Se agregaron dieciséis pruebas de regresión que verifican rótulos en mayúsculas,
escapes Unicode, límites del rótulo, comillas y el cuerpo preparado por
`LoggedSession`, tanto escapado como en UTF-8 literal.

## Comprobaciones realizadas

- Lectura del detector, evaluador, consumidor HTTP, pruebas, workflow,
  dependencias y cambios del PR respecto a `main`.
- Comparación exacta del proxy y los servicios con `main`. Se conservan sus
  bloqueos HTTP 503 y sus decisiones de integración.
- Suite completa con 500 pruebas aprobadas y 12 advertencias de obsolescencia.
- Reproducción de los cuatro benchmarks y comparación de los conjuntos de
  detecciones por caso, con datos y etiquetas intactos.
- Set de 700 comprobaciones generadas con semilla 20261111. Incluye 20 valores
  nuevos de cada uno de siete tipos, texto, JSON escapado/literal, repeticiones,
  prefijos Unicode y tokens negativos. El código calcula expectativas e
  intervalos a partir de las entradas, sin consultar la salida del detector ni
  sus funciones de validación.

El set generado señala 60 fallos al ejecutarse sobre `ed8c240`, todos por
rótulos JSON. Después de las correcciones se obtienen 700 comprobaciones sin
diferencias. Su construcción es sintética y dirigida por escenarios. El
procedimiento evalúa comportamiento de laboratorio.

| Corpus | Casos | TP | FP | FN |
|---|---:|---:|---:|---:|
| Histórico | 172 | 114 | 0 | 36 |
| Desarrollo MX/BO | 96 | 55 | 0 | 0 |
| Política MX | 60 | 29 | 0 | 0 |
| Cobertura RUT/NIT | 60 | 35 | 0 | 0 |

La revisión conserva las 36 omisiones históricas documentadas en el
[informe de cobertura](REVISION_VERIFICADORES_MX.md). El corpus de desarrollo
incluye repeticiones y casos preparados junto con las reglas. Las métricas se
limitan a los conjuntos evaluados.

## Reproducción

```bash
.venv/bin/python -m pytest -q --tb=short tests/
.venv/bin/python -m benchmarks.check_review_scenarios --seed 20261111
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_r3.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_bo.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_policy.jsonl
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_coverage.jsonl
```

El workflow ejecuta la suite, los escenarios generados y los cuatro benchmarks.
La ejecución final en GitHub debe identificarse por el SHA publicado.

El resultado permite revisar el aporte como mejora experimental del detector
y de su consumidor de texto/JSON. La autorización de producción, la sanitización
obligatoria de egreso y la migración comercial tienen sus seguimientos propios.
