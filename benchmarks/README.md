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
