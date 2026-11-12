# Issue #11 — Referencia de CI en `main`

Fase 1, paso 2 del [issue #11](https://github.com/andres-olguin/DELIA/issues/11). La referencia es [Pruebas de DELIA #22](https://github.com/andres-olguin/DELIA/actions/runs/42949757043), ejecutada por un `push` a `main` tras el [merge del PR #20](https://github.com/andres-olguin/DELIA/pull/20). Commit `8bee51e627c0e9844f49f688d686de873857f19f`. Inicio: 10 de noviembre de 2026, 23:59 (hora de Santiago). Resultado: 3 de 3 jobs exitosos en 27 segundos.

| Job | Pruebas aprobadas | Advertencias de pytest | Comprobaciones generadas sin fallos |
|---|---:|---:|---:|
| [Suite completa, Python 3.14.4](https://github.com/andres-olguin/DELIA/actions/runs/42949757043/job/130291047772) | 611 | 12 | 4.440 (semillas `20261111` y `20261112`) |
| [Pruebas regionales, Python 3.13](https://github.com/andres-olguin/DELIA/actions/runs/42949757043/job/130291047950) | 455 | 0 reportadas | 2.220 (semilla `20261112`) |
| [Pruebas regionales, Python 3.11](https://github.com/andres-olguin/DELIA/actions/runs/42949757043/job/130291048100) | 455 | 0 reportadas | 2.220 (semilla `20261112`) |

Las 12 advertencias de la suite completa corresponden a dos avisos de deprecación: uso de `httpx` con `starlette.testclient` y uso de `datetime.utcnow()` en SQLAlchemy. Las 22 mencionadas en el issue pertenecen a una ejecución anterior. Los jobs regionales ejecutan un subconjunto de la suite completa.

## Benchmarks sintéticos del job principal

| Corpus | Casos | Aciertos | Falsos positivos | Omisiones |
|---|---:|---:|---:|---:|
| `synthetic_pii_mx_bo.jsonl` | 96 | 55 | 0 | 0 |
| `synthetic_pii_mx_policy.jsonl` | 60 | 29 | 0 | 0 |
| `synthetic_pii_r3.jsonl` (histórico) | 172 | 130 | 0 | 20 |
| `synthetic_pii_coverage.jsonl` | 60 | 35 | 0 | 0 |
| `synthetic_pii_contexts.jsonl` | 96 | 48 | 0 | 0 |

En el histórico, el detector encontró 130 de 150 entidades anotadas. La precisión observada fue 100 % y el recall, 86,67 %. Estas métricas se limitan a los corpus sintéticos. El workflow aún no genera un reporte de cobertura de líneas.

## Matriz de pruebas del issue #11

| Python | Dependencias fijadas | Qué ejecuta CI |
|---|---|---|
| 3.11 y 3.13 | `requirements-test-compat.txt` | Suite completa y escenarios generados con semilla `20261112` |
| 3.14.4 | `requirements-test.txt` | Suite completa, escenarios generados con ambas semillas y cinco benchmarks sintéticos |

Cada job ejecuta `pip check` tras instalar sus dependencias. Para reproducir la suite en un entorno virtual limpio con el intérprete elegido, instala el manifiesto correspondiente con `python -m pip install -r ARCHIVO`, ejecuta `python -m pip check` y luego `python -m pytest -q --tb=short tests/`.

La validación local previa al cambio del workflow obtuvo 611 pruebas aprobadas tanto en Python 3.11.18 como en 3.13.18. Las dependencias instaladas en esas dos ejecuciones se fijaron en `requirements-test-compat.txt`. La tabla inicial conserva los resultados históricos de GitHub Actions anteriores a la ampliación.

## Secuencia de trabajo del issue #11

1. **Referencia:** verificar la ejecución de `main` ✓, registrar los resultados ✓ y crear la rama de trabajo desde `main` actualizado (pendiente).
2. **CI reproducible:** revisar disparadores, matriz de Python, dependencias, caché y permisos.
3. **Cobertura y regresiones P0:** medir líneas y módulos, cubrir las regresiones críticas que falten y publicar reportes como artefactos de Actions.
4. **Advertencias:** comparar con la referencia, identificar el origen y documentar el plan de migración.
5. **Entrega:** abrir un PR separado, obtener revisión técnica, registrar la evidencia en Trello y verificar `main` tras la integración.
