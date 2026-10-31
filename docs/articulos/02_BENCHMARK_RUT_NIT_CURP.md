# RUT, NIT y CURP en agentes de IA: cómo medir un detector sin engañarse

**Artículo técnico, 31/10/2026.** Ejemplos ficticios, sin datos personales de personas reales. No usar resultados como garantía de cumplimiento.

## Por qué una demo acertada no es una evaluación

Si un detector subraya correctamente un RUT, eso demuestra algo muy específico: ese patrón, con ese formato, en ese texto. No mide cuántos RUT detectaría entre cientos de combinaciones, cuántos identificadores inventaría en facturas ni cómo se comportaría ante formatos de OCR o errores tipográficos. Un equipo de integración debe medir **precision, recall y F1**, separando entidades, países y variantes.

**Definiciones:** 
- True positive (TP): la categoría y el tramo exacto de texto coincidieron con la etiqueta.
- False positive (FP): el detector devolvió un tramo o tipo no etiquetado.
- False negative (FN): se omitió una etiqueta de referencia.
- `precision=TP/(TP+FP)`, `recall=TP/(TP+FN)`, `F1=2PR/(P+R)`; si no hay denominador, informar *no definido*, no fabricar 100 %.

## Un corpus reproducible

La [base sintética DELIA Ronda 3](../../benchmarks/synthetic_pii_r3.jsonl) tiene **172 casos y 150 entidades etiquetadas**: identificadores CL, CO, MX y BO, tarjetas de test, teléfonos, correos `.invalid`, direcciones ficticias, variaciones y negativos. En cada registro se almacenan `country`, `target`, `text` y `entities[{type,start,end}]`. Un investigador independiente puede editar el corpus y agregar casos extremos.

Los documentos de identidad inventados se generan matemáticamente o con marcadores de prueba; incluso así, una secuencia inventada podría coincidir casualmente con un número emitido. No debe buscarse en servicios de terceros ni asociarse a una identidad real.

## Qué existe en DELIA hoy

`backend/dlp/pii.py` incluye validación de dígito RUT chileno, NIT colombiano, contexto para cédula, Luhn para tarjetas, emails y teléfonos CL/CO. No implementa RFC/CURP mexicanos, CI/NIT bolivianos ni direcciones. Además, el detector no está integrado en la salida HTTPX del proxy en `main`.

En un ensayo local del **archivo exacto de main** (Git blob `9cdc531fc7dfb38eb05e0c53bdb2cec795a4ae82`), con coincidencia estricta de tipo y span:

| Motor | TP | FP | FN | Precisión | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| DELIA actual | 71 | 3 | 79 | 95,95 % | 47,33 % | 63,39 % |
| Regex didáctica sin validadores | 60 | 6 | 90 | 90,91 % | 40,00 % | 55,56 % |

DELIA supera **solo** la regex didáctica en este conjunto, no a herramientas comerciales. La métrica por país de México y Bolivia arroja apenas 10 % de recall debido principalmente a emails, no a su capacidad de detectar identificadores fiscales nacionales. El ensayo no fue revisado de forma ciega ni ejecutado con muestras representativas de clientes.

## Lo que una evaluación robusta todavía requiere

1. Separar datos de desarrollo/test, revisar etiquetas por un tercero y normalizar formatos sin filtrar resultados.
2. Estratificar por tipo, país, largo de texto, OCR, unicode, campos ambiguos y densidad de entidades.
3. Medir intervalos de incertidumbre y variación entre versiones, no un único promedio agregado.
4. Comparar configuración equivalente de [Presidio](https://microsoft.github.io/presidio/supported_entities/), [Cloudflare DLP](https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/) y [Model Armor](https://cloud.google.com/security/products/model-armor).
5. Medir coste por solicitud, p95 latency, controles de retención y tratamiento de errores en **red real autorizada**.

**Estado actual de esas tres comparaciones:** NO EJECUTADAS, sin resultados publicados. No afirmar que el producto local sea superior por soporte de idioma o país.

## Lecciones operativas

El desafío de cédulas sin dígito verificador no se resuelve con una regex cada vez más amplia: puede producir falsos positivos en inventarios y órdenes. Los check digits tampoco validan que una persona exista o tenga derecho a usar un número.

Un filtro útil debe tener política configurada, minimizar datos y probar rechazo/aislamiento antes del egress. Por ello **un benchmark de la biblioteca no constituye benchmark del gateway entero**.

**Fuentes:** código `main` al 31-10-2026, [método documentado](../../benchmarks/README.md), [Presidio](https://microsoft.github.io/presidio/supported_entities/), [DIAN Colombia](https://www.dian.gov.co/), [Servicio Impuestos Internos Chile](https://www.sii.cl/), [SAT México](https://www.sat.gob.mx/). No se extrapola a datos productivos.
