# Issue #11 — Referencia de CI en `main`

Fase 1, paso 2 del [issue #11](https://github.com/andres-olguin/DELIA/issues/11). La referencia es [Pruebas de DELIA #22](https://github.com/andres-olguin/DELIA/actions/runs/42949757043), ejecutada por un `push` a `main` tras el [merge del PR #20](https://github.com/andres-olguin/DELIA/pull/20). Commit `8bee51e627c0e9844f49f688d686de873857f19f`. Inicio: 10 de noviembre de 2026, 23:59 (hora de Santiago). Resultado: 3 de 3 jobs exitosos en 27 segundos.

| Job | Pruebas aprobadas | Advertencias de pytest | Comprobaciones generadas sin fallos |
|---|---:|---:|---:|
| [Suite completa, Python 3.14.4](https://github.com/andres-olguin/DELIA/actions/runs/42949757043/job/130291047772) | 611 | 12 | 4.440 (semillas `20261111` y `20261112`) |
| [Pruebas regionales, Python 3.13](https://github.com/andres-olguin/DELIA/actions/runs/42949757043/job/130291047950) | 455 | 0 reportadas | 2.220 (semilla `20261112`) |
| [Pruebas regionales, Python 3.11](https://github.com/andres-olguin/DELIA/actions/runs/42949757043/job/130291048100) | 455 | 0 reportadas | 2.220 (semilla `20261112`) |

Las 12 advertencias de la suite completa corresponden a dos avisos de deprecación: uso de `httpx` con `starlette.testclient` y uso de `datetime.utcnow()` en SQLAlchemy. Las 22 mencionadas en el issue pertenecen a una ejecución anterior. En esa ejecución, los jobs regionales ejecutaron un subconjunto de la suite completa.

## Benchmarks sintéticos del job principal

| Corpus | Casos | Aciertos | Falsos positivos | Omisiones |
|---|---:|---:|---:|---:|
| `synthetic_pii_mx_bo.jsonl` | 96 | 55 | 0 | 0 |
| `synthetic_pii_mx_policy.jsonl` | 60 | 29 | 0 | 0 |
| `synthetic_pii_r3.jsonl` (histórico) | 172 | 130 | 0 | 20 |
| `synthetic_pii_coverage.jsonl` | 60 | 35 | 0 | 0 |
| `synthetic_pii_contexts.jsonl` | 96 | 48 | 0 | 0 |

En el histórico, el detector encontró 130 de 150 entidades anotadas. La precisión observada fue 100 % y el recall, 86,67 %. Estas métricas se limitan a los corpus sintéticos. La ejecución de referencia no generó un reporte de cobertura de líneas.

## Matriz de pruebas del issue #11

| Python | Dependencias fijadas | Qué ejecuta CI |
|---|---|---|
| 3.11 y 3.13 | `requirements-test-compat.txt` | Suite completa y escenarios generados con semilla `20261112` |
| 3.14.4 | `requirements-test.txt` | Suite completa, escenarios generados con ambas semillas y cinco benchmarks sintéticos |

Cada job ejecuta `pip check` tras instalar sus dependencias. Para reproducir la suite en un entorno virtual limpio con el intérprete elegido, instala el manifiesto correspondiente con `python -m pip install -r ARCHIVO`, ejecuta `python -m pip check` y luego `python -m pytest -q --tb=short tests/`.

La validación local previa al cambio del workflow obtuvo 611 pruebas aprobadas tanto en Python 3.11.18 como en 3.13.18. Las dependencias instaladas en esas dos ejecuciones se fijaron en `requirements-test-compat.txt`. La tabla inicial conserva los resultados históricos de GitHub Actions anteriores a la ampliación.

## Reportes de GitHub Actions

La sección **Artifacts** de cada ejecución guarda los reportes por 30 días. Cada versión de Python publica `pytest.xml` en formato JUnit. El artefacto de Python 3.14.4 también incluye `coverage.xml`, `coverage.json` y un JSON por cada corpus sintético. Coverage.py mide líneas y ramas en `app/` y `backend/`.

Si falla una prueba, el workflow conserva el resultado de fallo e intenta subir los reportes que alcanzó a generar. Los benchmarks se ejecutan tras una suite exitosa.

## Advertencias observadas y plan de migración

| Ejecución local | Pruebas aprobadas | Advertencias de pytest |
|---|---:|---|
| Python 3.11.18, validación previa a ampliar la matriz (`4f448ea`) | 611 | 1 de Starlette por `anyio.abc.BlockingPortal` |
| Python 3.13.18, validación previa a ampliar la matriz (`4f448ea`) | 611 | 1 de Starlette por `anyio.abc.BlockingPortal` y 11 de SQLAlchemy por `datetime.utcnow()` |
| Python 3.14.4, validación de reportes con las pruebas P0 | 615 | 1 de Starlette por `httpx` en `TestClient` y 11 de SQLAlchemy por `datetime.utcnow()` |

Los conteos corresponden a estas ejecuciones. Se actualizarán con los logs de los tres jobs del PR. Las 22 advertencias del registro inicial del issue son un dato histórico.

- **Starlette y AnyIO en 3.11/3.13.** La advertencia viene del cliente de pruebas de Starlette fijado en `requirements-test-compat.txt`, que usa un alias deprecado de AnyIO. Probar una combinación compatible de FastAPI, Starlette y AnyIO en un cambio separado. Actualizar las versiones fijadas después de que pasen `pip check` y la suite completa en ambos intérpretes.
- **Starlette y HTTPX en 3.14.4.** La advertencia se activa al importar `TestClient` en `tests/test_api.py`. Evaluar la migración del cliente de pruebas a `httpx2`, que sugiere la advertencia, y revisar por separado los demás usos de `httpx`. Validar con las pruebas de API y la suite completa antes de actualizar el manifiesto.
- **SQLAlchemy y fechas UTC.** Los modelos de `app/models.py` usan `datetime.utcnow` en valores por defecto. Revisar el contrato actual de fechas y su almacenamiento antes de cambiarlo. Probar una implementación que use UTC explícito y mantenga la compatibilidad con los valores existentes, con pruebas de persistencia y serialización.

La fase 4 deja identificado el origen y el plan de cada advertencia. Pytest conserva las advertencias visibles.

## Entrega pendiente

- [ ] Abrir el PR de `feat/11-ci-reproducible` hacia `main` y vincular el issue #11.
- [ ] Confirmar que pasan los tres jobs de Python. Revisar el conteo de pruebas y las advertencias de cada job.
- [ ] Descargar los tres artefactos y verificar los JUnit XML, la cobertura XML/JSON y los cinco reportes de benchmarks.
- [ ] Obtener revisión técnica y registrar el PR y la evidencia en Trello.
- [ ] Fusionar a `main` tras la revisión y comprobar la ejecución posterior al merge.

## Secuencia de trabajo del issue #11

1. **Referencia:** ejecución de `main` verificada, resultados registrados y rama de trabajo creada.
2. **CI reproducible:** disparadores, matriz, versiones fijadas, caché, permisos y `pip check` configurados.
3. **Cobertura y regresiones P0:** medición local y pruebas de base de datos completas. Reportes configurados, con publicación pendiente de verificar en el PR.
4. **Advertencias:** origen y plan de migración documentados.
5. **Entrega:** pendiente según la lista anterior.
