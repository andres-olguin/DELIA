# Evaluación de identificadores de México y Bolivia

La [revisión posterior de verificadores](REVISION_VERIFICADORES_MX.md) documenta
el ajuste de contexto, la versión actualizada del corpus de desarrollo y las
mediciones con las etiquetas históricas originales.

Fecha de ejecución, 7 de noviembre de 2026. Python 3.14.4.

Se compararon el detector inicial y el detector implementado sobre el mismo
corpus de 96 textos. Hay 55 entidades esperadas y 45 casos sin entidades. De las
55 entidades, 49 pertenecen a CURP, RFC, CI_BO o NIT_BO y 6 a categorías existentes.

| Referencia | Commit del detector | Reporte completo |
|---|---|---|
| Inicial | `0c3ea173624c2c6565f4822848310bc1629c6f1f` | [JSON inicial](../../benchmarks/resultados_mx_bo_inicial.json) |
| Implementado | `0e2bfb5bddd3a3bec4c4d5aa916f03fc4db45a0d` | [JSON actual](../../benchmarks/resultados_mx_bo_actual.json) |

Cada acierto exige coincidencia exacta de tipo, inicio y fin. Un tipo o intervalo
incorrecto cuenta como falso positivo y también deja un falso negativo por la
entidad esperada. Las métricas se agregan por entidad, país y combinación de
ambos, sumando los conteos antes de calcular las proporciones.

| Métrica | Inicial | Implementado |
|---|---:|---:|
| Aciertos, TP | 6 | 55 |
| Falsos positivos, FP | 1 | 0 |
| Entidades sin detectar, FN | 49 | 0 |
| Precisión, TP / (TP + FP) | 85,71 % | 100 % |
| Recall, TP / (TP + FN) | 10,91 % | 100 % |
| F1, 2 TP / (2 TP + FP + FN) | 19,35 % | 100 % |

| País | Detector | TP | FP | FN | Precisión | Recall | F1 |
|---|---|---:|---:|---:|---:|---:|---:|
| México | Inicial | 2 | 0 | 24 | 100 % | 7,69 % | 14,29 % |
| México | Implementado | 26 | 0 | 0 | 100 % | 100 % | 100 % |
| Bolivia | Inicial | 4 | 1 | 25 | 80 % | 13,79 % | 23,53 % |
| Bolivia | Implementado | 29 | 0 | 0 | 100 % | 100 % | 100 % |

| Tipo nuevo | Entidades esperadas | TP inicial | FN inicial | TP implementado | FP implementado | FN implementado |
|---|---:|---:|---:|---:|---:|---:|
| CURP | 13 | 0 | 13 | 13 | 0 | 0 |
| RFC | 11 | 0 | 11 | 11 | 0 | 0 |
| CI_BO | 14 | 0 | 14 | 14 | 0 | 0 |
| NIT_BO | 11 | 0 | 11 | 11 | 0 | 0 |

El reporte inicial señala errores en 45 casos. Los 49 falsos negativos son las
entidades de las categorías nuevas. El falso positivo aparece en
`MXBO-NIT_BO-06`, donde la secuencia sintética etiquetada como NIT_BO también
pasa Luhn y el detector inicial devuelve TARJETA. La prioridad del contexto
tributario resuelve esa colisión en el detector implementado. El reporte actual
contiene una lista `case_errors` vacía.

Para reproducir la comparación desde la raíz del repositorio se ejecutaron
estos comandos sobre referencias de Git fijas.

```bash
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_bo.jsonl --detector-ref 0c3ea173624c2c6565f4822848310bc1629c6f1f --out benchmarks/resultados_mx_bo_inicial.json
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_bo.jsonl --detector-ref 0e2bfb5bddd3a3bec4c4d5aa916f03fc4db45a0d --out benchmarks/resultados_mx_bo_actual.json
```

`benchmarks/evaluate.py` adapta el evaluador del commit `70c878e` de la rama de
benchmark. Añade selección del detector por revisión, salida a archivo, errores
por ID de caso y comprobaciones de IDs y posiciones. Las referencias históricas
ejecutan el código del repositorio seleccionado. Sin `--detector-ref`, se evalúa
el detector del árbol de trabajo y se identifica de ese modo en el reporte.

Ambos reportes registran el mismo SHA-256 del corpus y del evaluador, junto con
el hash del detector y su revisión. El SHA-256 del corpus es
`ae057daaf0f22b29ce3665a494c2bb90e834463c299f5230a64afdcb178b6b20`.
Los JSON permiten revisar por separado las posiciones de cada error inicial.

Las pruebas de la herramienta verifican el requisito de tipo e intervalo exactos,
las fórmulas con aciertos y errores mezclados, la separación por país, los
denominadores cero y el rechazo de etiquetas inválidas o IDs duplicados.
Las nueve pruebas del evaluador están incluidas en la ejecución completa de
`tests/`, que obtuvo **170 pruebas aprobadas y 22 advertencias de obsolescencia**.
La ejecución completa necesitó salir del aislamiento que bloquea TestClient.
Se regeneraron ambos JSON y se comprobó igualdad byte por byte, además de
contrastar los resultados con el detector del árbol de trabajo.

El 100 % observado caracteriza este corpus de desarrollo, cuyos casos y
etiquetas se diseñaron junto con las reglas. La validación con ejemplos nuevos
y una revisión independiente de las etiquetas sigue pendiente. Los resultados
dependen del contexto definido para Bolivia, de los rangos de captura y de la
validación estructural mexicana acordada. El cálculo matemático de los
verificadores de CURP/RFC sigue pendiente. Los porcentajes tampoco miden tipos
ajenos al alcance, como direcciones, ni reemplazan los resultados del corpus
histórico de 172 casos. La [comparación histórica con el PR #20](REGRESION_HISTORICA_R3.md)
documenta los resultados y las diferencias por caso. Presidio, Cloudflare DLP
y Google Model Armor figuran como NO EJECUTADOS en los reportes.

La [guía de pruebas](../../CONTRIBUTING.md#pruebas) explica cómo reproducir el
entorno con dependencias fijadas. El
[workflow de GitHub Actions](../../.github/workflows/python-tests.yml) ejecuta
la suite completa y el benchmark actual con ese entorno. Su salida permite
revisar el resultado del detector para cada cambio.

El alcance operativo de la medición es `detect()` y el corpus sintético. Las
pruebas de enmascaramiento cubren `redact()` y el cuerpo enviado mediante
`LoggedSession`. La ruta `/proxy/v1/chat` reenvía por un servicio distinto
con HTTPX y queda fuera de esa verificación de enmascaramiento. Para el
seguimiento de su integración, consulta
[sanitización antes del proveedor](https://github.com/andres-olguin/DELIA/issues/9).

El contrato de `detect()` y `redact()` conserva las etiquetas existentes y
los índices sobre el texto original. Los nuevos tipos son `CURP`, `RFC`,
`CI_BO` y `NIT_BO`. La migración de nombres de API, campos heredados y base de
datos se documenta en el
[plan TALIA → DELIA](../PLAN_MIGRACION_TALIA_DELIA_2026-10-31.md).
