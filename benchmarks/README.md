# Corpus sintético de México y Bolivia

La [revisión técnica final](../docs/benchmarks/REVISION_FINAL_PR20.md) añadió
comprobaciones de serialización y corrigió dos omisiones en rótulos JSON. Los
cuatro benchmarks mantienen sus detecciones anteriores. La suite obtuvo 500
pruebas aprobadas y los escenarios de revisión añadieron 700 comprobaciones.
El [reporte de revisión](resultados_revision_final.json) registra el alcance,
la procedencia y los hashes de las mediciones.

La [ampliación de cobertura del 10 de noviembre](../docs/benchmarks/REVISION_VERIFICADORES_MX.md)
obtuvo 114 TP, 0 FP y 36 FN en los 172 casos históricos. Se conservaron los
98 aciertos anteriores y se agregaron 16 por formatos de RUT/NIT con espacios.
Los corpus de 96 y 60 casos de México/Bolivia conservan sus resultados. El
[reporte de cobertura](resultados_cobertura.json) registra las cuatro evaluaciones,
sus hashes y las diferencias por caso.

La [corrección del 10 de noviembre](../docs/benchmarks/REVISION_VERIFICADORES_MX.md)
obtuvo 98 TP, 0 FP y 52 FN en los 172 casos históricos, y mantuvo 55/0/0 y
29/0/0 en los corpus de 96 y 60 casos, respectivamente. Se conservaron las
entradas y etiquetas de los tres corpus para esa comparación. El
[reporte de corrección](resultados_correccion_fp.json) detalla los cuatro casos
modificados y los hashes de las mediciones.

La revisión de verificadores del 9 de noviembre ajustó los valores positivos
del corpus de desarrollo para incluir verificadores coherentes y dos errores de
captura con etiqueta inmediata. Los conteos de casos y entidades se mantienen.
La versión anterior está fijada en Git por `f2e3f5a`. Los reportes
`resultados_mx_bo_inicial.json` y `resultados_mx_bo_actual.json` corresponden a
esa versión anterior. La [revisión actual](../docs/benchmarks/REVISION_VERIFICADORES_MX.md)
separa las mediciones sobre cada versión del corpus.

[synthetic_pii_mx_bo.jsonl](synthetic_pii_mx_bo.jsonl) reúne 96 escenarios
seleccionados según la [especificación de detección](../docs/benchmarks/ISSUE_16_COMPORTAMIENTO_DETECCION.md).
Hay 48 casos por país, distribuidos en 40 positivos, 45 negativos, 7 ambiguos y
4 regresiones. Las 55 entidades anotadas incluyen 49 de los tipos nuevos y 6 de
categorías existentes. Los casos cubren fechas imposibles, límites, contexto,
claves genéricas, complementos y solapes.

Los textos se redactaron para el laboratorio. Las cadenas pueden coincidir
fortuitamente con identificadores emitidos y se usan sin consultar padrones ni
asociarlas con titulares. El corpus histórico de Ronda 3 se conserva para
reproducir sus resultados.

Desde la raíz, generar el archivo con Python estándar.

```bash
python3 benchmarks/generate_synthetic_pii_mx_bo.py > benchmarks/synthetic_pii_mx_bo.jsonl
```

El generador calcula los índices a partir de anotaciones en las plantillas.
Cada entidad señala el intervalo original con inicio inclusivo y fin exclusivo.
La regeneración produce el mismo archivo byte por byte. Para agregar un
escenario, se puede añadir al final del bloque de su tipo para preservar los
identificadores de los casos existentes.

El evaluador `benchmarks/evaluate.py` está incorporado a esta rama y compara
tipo e intervalo exactos. La medición sobre los mismos 96 casos pasó de 6
aciertos, 1 falso positivo y 49 falsos negativos a 55 aciertos, 0 falsos positivos
y 0 falsos negativos. Precisión, recall y F1 actuales alcanzan el 100 % en este
corpus de desarrollo. La evaluación independiente sigue pendiente.
[Resultados, límites y comandos reproducibles](../docs/benchmarks/RESULTADOS_MX_BO.md).

```bash
python3 -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_bo.jsonl
```

Los apartados de Ronda 3 y Ronda 4 que siguen conservan el estado histórico de
esas evaluaciones. El documento de resultados anterior describe las herramientas
y resultados de la rama de trabajo actual.

# Ejemplos para la política propuesta de CURP/RFC

[synthetic_pii_mx_policy.jsonl](synthetic_pii_mx_policy.jsonl) contiene 60 casos
nuevos preparados el 9 de noviembre de 2026 para la
[política de verificador y contexto](../docs/benchmarks/ISSUE_16_COMPORTAMIENTO_DETECCION.md#política-propuesta-tras-la-revisión-de-falsos-positivos).
Hay 27 escenarios centrados en CURP y 33 en RFC, 29 entidades esperadas y
32 casos sin entidades. La distribución es de 14 positivos, 4 ambiguos,
8 errores de captura protegidos por contexto, 2 regresiones de correo y
32 negativos.

Se cruzan verificadores correctos e incorrectos con etiquetas inmediatas,
inventarios, palabras intermedias, saltos de línea y etiquetas de otro tipo.
También se cubren RFC de personas físicas y morales, Ñ, ampersand, JSON,
escapes de Ñ, minúsculas, límites de token, fechas imposibles, claves genéricas,
precedencia de correo, repeticiones con distinto contexto y posiciones Unicode.
Los verificadores RFC incluyen los resultados especiales `A` y `0`.

| Entrada abreviada | Entidad esperada según la propuesta |
|---|---|
| `Dato NAQZ860412HJCPLR03` | CURP, verificador correcto. |
| `Dato NAQZ860412HJCPLR04` | Ninguna, verificador incorrecto sin etiqueta. |
| `CURP: NAQZ860412HJCPLR04` | CURP, protección del error de captura por contexto. |
| `Inventario NAQZ860412HJCPLR03` | CURP, verificador correcto incluso en inventario. |

Codex preparó estos ejemplos y sus etiquetas a partir de la política propuesta.
La revisión por otra persona sigue pendiente. Son un corpus adicional de
desarrollo y su procedencia debe acompañar cualquier informe de validación
independiente. Los seis valores base se construyeron localmente y se comprobó
que fueran distintos de los usados en los dos corpus anteriores. Se verificó
la congruencia matemática de sus últimos caracteres y de las cuatro mutaciones
del verificador. Los índices se obtuvieron de anotaciones explícitas mediante
`make_case()`, sin usar la salida del detector para asignar las etiquetas.
Se comprobaron IDs y textos únicos e intervalos válidos.

La comparación inicial con el detector de `f2e3f5a`, anterior al ajuste,
obtuvo TP=29, FP=26 y FN=0, con diferencias en 26 casos. Estos casos representan
el comportamiento pendiente de ajustar. Los resultados se reportan contra las
etiquetas de esta nueva política. El SHA-256 del archivo es
`75b1a97a50ab2610ed3544472905480b186abc1ccdd0b2f3b6c536b1eb49bf9e`.
Tras implementar la política se obtuvieron TP=29, FP=0 y FN=0. El informe
[JSON de la revisión](resultados_revision_politica_mx.json) conserva ambas
mediciones y los errores por caso.

```bash
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_mx_policy.jsonl
```

# Ejemplos adicionales de cobertura de RUT y NIT colombiano

[synthetic_pii_coverage.jsonl](synthetic_pii_coverage.jsonl) contiene 60 ejemplos
preparados antes de implementar la ampliación del 10 de noviembre. Hay 35
entidades esperadas y 28 casos sin entidades. Se cubren puntos, espacios,
tabuladores, guiones, RUT sin guion dentro de campos etiquetados, verificadores
incorrectos, límites de token, formatos mixtos, JSON, correos, repeticiones e
índices Unicode.

Los valores se construyeron localmente con dos bases RUT y dos bases NIT
distintas de las del corpus histórico. Las etiquetas se asignaron a partir de
los escenarios y sus intervalos se calcularon con anotaciones explícitas. Codex
preparó los ejemplos. Su revisión independiente por otra persona sigue pendiente.

La comparación pasó de TP=6, FP=2, FN=29 a TP=35, FP=0, FN=0. Las dos
detecciones incorrectas previas correspondían a candidatos truncados ante
sufijos decimales. Las pruebas también verifican las mutaciones de los
verificadores y el cuerpo JSON preparado por `LoggedSession`.

```bash
.venv/bin/python -m benchmarks.evaluate --dataset benchmarks/synthetic_pii_coverage.jsonl
```

# Ronda 3 — Corpus PII sintético y benchmarking reproducible

**Fecha:** 31/10/2026. [Dataset etiquetado JSONL](synthetic_pii_r3.jsonl): 172 casos de laboratorio, 150 entidades positivas, 22 registros sin entidades. Países CL/CO/MX/BO y categoría GLOBAL. Incluye RUT, NIT, cédula, CURP, RFC, CI/NIT boliviano, tarjetas de prueba, teléfonos, correos `.invalid`, direcciones inventadas y negativos difíciles.

El corpus se **generó programáticamente**, no se obtuvo de personas ni de clientes. **No se puede garantizar matemáticamente que una cadena numérica de prueba nunca coincida con un identificador emitido:** no intentar consultarla en servicios externos, ni publicar ejemplos con vinculación personal.

## Evaluación local ejecutada (no producción)

Se reconstruyó el archivo exacto `backend/dlp/pii.py` publicado en `main` con hash blob Git **`9cdc531fc7dfb38eb05e0c53bdb2cec795a4ae82`**, y se evaluó frente al corpus con métrica estricta de **tipo de entidad y span exacto**. Python 3.13 en laboratorio aislado. El código original del detector no fue modificado.

| Motor | TP | FP | FN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| DELIA actual | 71 | 3 | 79 | 95,95 % | 47,33 % | 63,39 % |
| Expresiones regulares básicas, comparación no productiva | 60 | 6 | 90 | 90,91 % | 40,00 % | 55,56 % |

Resultados por país DELIA, exactitud de spans y tipos:

| País | TP | FP | FN | Precision | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| Chile | 21 | 0 | 11 | 100 % | 65,63 % | 79,25 % |
| Colombia | 32 | 3 | 14 | 91,43 % | 69,57 % | 79,01 % |
| México | 3 | 0 | 27 | 100 % | 10 % | 18,18 % |
| Bolivia | 3 | 0 | 27 | 100 % | 10 % | 18,18 % |
| Global (tarjetas/negativos) | 12 | 0 | 0 | 100 % | 100 % | 100 % |

**Interpretación:** La alta precisión observada está condicionada a la detección de muy pocos tipos; **el recall total es bajo**. El 10 % en MX/BO corresponde esencialmente a correos sintéticos, no a cobertura de CURP/RFC/CI/NIT bolivianos, que no está implementada. Las direcciones no se detectan. No interpolar estos números a una población real ni a un SLA.

## Alternativas y estado

- **Microsoft Presidio:** **NO EJECUTADO** (paquete `presidio_analyzer` no instalado en entorno disponible). Documentación: https://microsoft.github.io/presidio/supported_entities/
- **Cloudflare AI Gateway DLP:** **NO EJECUTADO** (no se accedió a tenant, perfil DLP ni a una cuenta autenticada). Documentación: https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/
- **Google Model Armor:** **NO EJECUTADO** (no se accedió a proyecto, política ni credenciales autorizadas). Documentación: https://cloud.google.com/security/products/model-armor

**No existe ganador demostrado frente a esos tres proveedores.** El segundo baseline es deliberadamente rudimentario y no representa herramientas comerciales.

## Reproducción y limitación del repositorio

La herramienta Python `benchmarks/evaluate.py` quedó **preparada y ejecutada localmente**, pero **no publicada en GitHub** por el bloqueo del ruleset que impide crear ramas de código. Se entrega por separado como paquete descargable al responsable del repositorio. Una vez corregida [OPS-01](https://github.com/andres-olguin/DELIA/issues/18), subir a **rama nueva** y PR sin fusionar; no agregar script a `main`.

**Comando cuando se publique en rama:** `python benchmarks/evaluate.py --dataset benchmarks/synthetic_pii_r3.jsonl --out benchmarks/resultados_locales.json`. Su implementación usa Python estándar y el módulo `backend.dlp.pii`.

**Pruebas pendientes:** verificar versiones del motor, configuración exacta de competidores, métricas TP/FP/FN por span en ambientes homogéneos, generación de dataset estratificado con más variantes y revisión de las etiquetas por personas distintas de quien lo generó.


---

## Ronda 4 — verificación del baseline técnico y comparadores (31/10/2026)
**No reescribe los resultados de la Ronda 3.** La revisión original del detector (71 TP, 3 FP, 79 FN, F1 63,39 %) permanece como evidencia histórica sin validación independiente. **No se ejecutó Presidio, Cloudflare DLP ni Google Model Armor durante Ronda 4**; por tanto no hay nuevos valores TP/FP/FN/F1 por entidad/país ni ganador externo.

**Observación adicional ejecutada:** se reconstruyó un parche de API/auth/egress como diff local (no aplicado en `main`) y se ejecutó sólo `python -m pytest -q tests/test_api.py` con Python 3.13.5: **6 passed, 2 warnings** por `datetime.utcnow()`. Se hizo `git apply --check` del patch en snapshot de archivos base: **aplica correctamente**. NO se probó la suite completa `tests/` ni un servidor real, migraciones, aislamiento multitenant, Python 3.11/CI, respuesta LLM o cobertura PII ampliada. Las 6 pruebas NO son nuevas mediciones del detector.

**Microsoft Presidio:** `presidio_analyzer` no está instalado en el entorno de la ronda (`importlib.util.find_spec('presidio_analyzer')` → False). Sin paquetes/modelos/idiomas certificados ni resultado del runner, su benchmark sigue **NO EJECUTADO**. No se sustituyen sus resultados por predicciones sobre cobertura regional.

**Cloudflare DLP:** según [pricing oficial](https://developers.cloudflare.com/ai-gateway/reference/pricing/) (actualización 15/10/2026), AI Gateway ofrece escaneo DLP gratis con perfiles restringidos sin plan Zero Trust. **No ejecutado:** sin tenant autorizado ni instrumentación de spans; una respuesta `block/flag` a nivel solicitud sería **métrica por caso**, no estrictamente tipo+span.

**Google Model Armor:** [servicio oficial](https://cloud.google.com/security/products/model-armor) publica nivel gratuito de 2 millones de tokens/mes sujeto a condiciones de proyecto; **no ejecutado** por falta de cuenta/proyecto autorizado. No estimar cobertura de CURP/NIT sin API.

**Conclusión desfavorable:** el primer problema DELIA no es demostrar superioridad comercial sino la sanitización insuficiente de 79/150 entidades del set sintético; 10 % de recall de México y Bolivia es especialmente insuficiente. La comparación con regex didáctica sí favorecía DELIA en corpus anterior, pero no representa ventaja comercial. Priorizar tipos MX/BO, direcciones, negativos difíciles y asegurar que un falso negativo no llegue a terceros. Para credibilidad, evaluar mismos casos con anotador independiente y spans medibles en todos los sistemas.

[Guía de ejecución libre/gestionada y plantilla de resultados](../docs/benchmarks/GUIA_COMPARADORES_DLP_RONDA4_2026-10-31.md) · [Revisión de seguridad del patch](../docs/REVISION_SEGURIDAD_PARCHE_P0_RONDA4_2026-10-31.md). Estado de GitHub: [ruleset #18](https://github.com/andres-olguin/DELIA/issues/18) impide rama y PR; **CI de PR NO EJECUTADO**.
