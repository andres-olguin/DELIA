# Issue #16 — diagnóstico inicial

Fecha: 7 de noviembre de 2026 (America/Santiago).

## Alcance y estado

Este documento cierra el diagnóstico de la fase 1 del
[issue #16](https://github.com/andres-olguin/DELIA/issues/16): validadores de
CURP/RFC de México y CI/NIT de Bolivia. No implementa validadores ni resuelve
otros issues. Las fases siguientes deben confirmar formatos oficiales, revisar
las etiquetas, ampliar los casos sintéticos e implementar y evaluar las reglas.

- Rama de trabajo: `feat/16-validadores-mx-bo`, publicada con seguimiento remoto.
- Commit del código y corpus evaluados: `0c3ea173624c2c6565f4822848310bc1629c6f1f`.
- Al iniciar, el árbol estaba limpio y `main` coincidía con `origin/main` tras
  `git fetch origin`.
- Las reglas de GitHub consultadas protegen la rama predeterminada; la creación
  y publicación de esta rama se completaron correctamente.
- No se fusionaron cambios en `main`.

## Entorno observado

Python 3.14.4, entorno local `.venv`, pip 25.1.1. El README indica Python 3.11 o
superior, pero este diagnóstico no verifica otras versiones. `.venv` está
excluido de Git y no debe publicarse.

No se encontraron `requirements.txt`, `pyproject.toml` ni archivos de bloqueo de
dependencias en la revisión inicial. Se instalaron únicamente las dependencias
mínimas para ejecutar las pruebas PII actuales. El detector utiliza la biblioteca
estándar, pero `tests/conftest.py` importa SQLAlchemy al iniciar pytest.

Paquetes observados con `.venv/bin/python -m pip freeze`:

```text
iniconfig==2.3.1
packaging==26.3
pluggy==1.7.0
Pygments==2.21.0
pytest==9.2.0
SQLAlchemy==2.1.8
typing_extensions==4.16.0
```

Preparación realizada:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install --no-cache-dir pytest SQLAlchemy
.venv/bin/python -m pip check
```

`pip check` terminó con `No broken requirements found.` y se verificó la
importación de pytest y SQLAlchemy. El primer intento de descarga falló por
restricciones de red; el reintento autorizado completó la instalación.
La instalación sin versiones fijadas describe lo realizado; para recrear estas
versiones deben usarse las versiones exactas de la lista anterior. No representa
un entorno completo del backend ni una matriz de compatibilidad soportada.

## Pruebas PII iniciales

Ejecutadas por el usuario en su terminal, con salida compartida en el chat:

```bash
.venv/bin/python -m pytest -v tests/test_pii.py
```

Resultado reportado: **6 passed in 0.03s**, Python 3.14.4 y pytest 9.2.0.

```text
test_dv PASSED
test_rut PASSED
test_nit PASSED
test_cedula_requires_context PASSED
test_other PASSED
test_redact PASSED
```

Son las pruebas existentes de identificadores y enmascaramiento. No acreditan
cobertura de los nuevos identificadores del issue #16.

**NO EJECUTADOS en este diagnóstico:** suite completa `tests/`, pruebas de API y
modelos, CI, Docker/PostgreSQL, servicios externos y validaciones en otros Python.
No se afirma que esas comprobaciones pasen ni que el backend esté preparado.

## Revisión del corpus

Archivo: `benchmarks/synthetic_pii_r3.jsonl`.

- 172 casos, 150 entidades etiquetadas y 22 registros sin entidades.
- Países: CL 36, CO 55, MX 33, BO 32 y GLOBAL 16 casos.
- No se encontraron IDs duplicados ni posiciones fuera de los límites del texto.
  Esto no verifica la corrección semántica de cada posición o etiqueta.
- Hay 12 entidades positivas por tipo: `CURP`, `RFC`, `CI_BO` y `NIT_BO`.
- Los 12 positivos de CURP contienen solo 3 identificadores distintos; ocurre
  lo mismo con RFC. CI y NIT bolivianos tienen 12 valores distintos por tipo.
- Los negativos difíciles específicos son escasos: uno de CURP, uno de CI,
  uno de NIT boliviano y dos de RFC, uno de estos últimos sin identificador.
- La validez de los ejemplos según formatos oficiales sigue pendiente. No deben
  asumirse correctos por estar etiquetados como positivos.
- El corpus incluye categorías fuera del issue #16, como direcciones. Las
  métricas globales no deben interpretarse como métricas exclusivas de este issue.

## Evaluador disponible y ejecución inicial

`benchmarks/evaluate.py` no está en la rama actual. Se leyó desde la referencia
remota `origin/docs/issue-12-analisis-benchmark`, fijada al commit
`70c878e97dea1736c87d597d4d7d1cd9164fbab8`, y se ejecutó en memoria con el detector
de nuestra rama y el corpus local, sin cambiar de rama ni incorporar sus commits.

El evaluador usa coincidencia exacta de tipo y posiciones, cuenta TP/FP/FN y
calcula precisión, recall y F1 por entidad, país y combinación de ambos. Registra
hashes SHA-256 del dataset y detector. Si el denominador es cero, devuelve `null`.

Para repetir esta evaluación desde la raíz, con ese commit disponible en Git,
puede extraerse el script a una carpeta temporal y ejecutarlo sin integrarlo:

```bash
git show 70c878e97dea1736c87d597d4d7d1cd9164fbab8:benchmarks/evaluate.py > /tmp/delia-issue16-evaluate.py
PYTHONPATH="$PWD" .venv/bin/python /tmp/delia-issue16-evaluate.py --dataset benchmarks/synthetic_pii_r3.jsonl
```

Esos dos comandos son una alternativa de reproducción; la ejecución de este
diagnóstico leyó el script mediante `git show` y lo ejecutó en memoria capturando
su JSON. No se ejecutaron comparadores externos.

Hashes observados:

```text
dataset_sha256: 191ae4de8598321402460e8367a2944a239f69a54d569a6065c287cef6bf4f3f
detector_sha256: a1bd0c1af4e75547a9b9f4aa2414c352e5655ce45a5262ba67496496e780799f
```

Resultados obtenidos contra las etiquetas actuales:

| Grupo | TP | FP | FN | Precisión | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| Corpus completo | 71 | 3 | 79 | 95,95 % | 47,33 % | 63,39 % |
| México, todas sus categorías | 3 | 0 | 27 | 100 % | 10 % | 18,18 % |
| Bolivia, todas sus categorías | 3 | 0 | 27 | 100 % | 10 % | 18,18 % |
| CURP | 0 | 0 | 12 | No definida | 0 % | 0 % |
| RFC | 0 | 0 | 12 | No definida | 0 % | 0 % |
| CI_BO | 0 | 0 | 12 | No definida | 0 % | 0 % |
| NIT_BO | 0 | 0 | 12 | No definida | 0 % | 0 % |

Se reproducen los totales históricos publicados, sin que eso valide las etiquetas
de forma independiente. El recall del 10 % por país incluye correos; no demuestra
detección de los cuatro identificadores pendientes.

## Riesgos, compatibilidad y siguientes acciones

- Solo se trabajó con el corpus declarado sintético, sin consultas de identidad
  a autoridades, datos de clientes ni publicación de credenciales.
- Repeticiones, pocos negativos y etiquetas aún no verificadas limitan la
  representatividad. No extrapolar estas métricas a producción.
- La investigación de formatos oficiales y el diseño de contexto/solapes son
  necesarios antes de implementar. No se presupone un algoritmo verificador
  universal para las cuatro categorías.
- Debe revisarse y coordinarse la incorporación del evaluador necesario para
  el #16; no se considera implementado ni cerrado el issue #12.
- Se debe conservar el corpus histórico y versionar cualquier corpus revisado.
  Para una comparación antes/después, ejecutar ambos detectores sobre el mismo
  dataset revisado; cambiar etiquetas y código a la vez invalida una comparación
  directa sin una nueva medición inicial.
- Este paso solo añade documentación: no cambia APIs, campos heredados TALIA,
  nombres de base de datos ni contratos de detección/enmascaramiento.
- Las pruebas de regresión de los cambios futuros y la revisión humana del PR
  siguen pendientes; no se hará fusión automática.

Con la revisión, commit y publicación de este documento se cierra la fase 1.
La fase 2 empieza con la confirmación de formatos oficiales y la especificación
de comportamiento para el issue #16.
