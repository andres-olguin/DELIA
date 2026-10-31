# Informe técnico de regalo — ¿Qué tan bien detecta DELIA identificadores de Latinoamérica?
**Material para entrevistas, sin venta ni garantía de producto.** MasterTech SpA · 31/10/2026 · Ronda 4 · Versión 1.0. Este archivo está dividido en **dos páginas editoriales** para exportación a PDF, sin testimonios ni comparaciones inventadas.

## PÁGINA 1/2 — Método y resultados verificados
**Problema de investigación:** equipos que integran LLM en aplicaciones podrían necesitar evitar la transmisión accidental de RUT (Chile), NIT/cédula (Colombia), CURP/RFC (México) o CI/NIT (Bolivia), sin introducir una herramienta innecesaria. Queremos entender cómo resuelven esto hoy.

**Diseño:** 172 textos sintéticos, 150 entidades etiquetadas y 22 casos sin etiquetas; categorías de CL, CO, MX, BO y globales. Comparación exacta de **tipo + posición del span**. No provienen de personas ni clientes. Una sola fuente de generación/etiquetado limita la validez externa. Código: [detector main](../../backend/dlp/pii.py) (blob `9cdc531fc7dfb38eb05e0c53bdb2cec795a4ae82`); [datos](../../benchmarks/synthetic_pii_r3.jsonl); [método](../../benchmarks/README.md).

| Evaluación histórica Ronda 3 | TP | FP | FN | Precisión | Recall | F1 |
|---|---:|---:|---:|---:|---:|---:|
| DELIA (ejecutado local, Python 3.13) | 71 | 3 | 79 | 95,95 % | 47,33 % | 63,39 % |
| Regex didácticas (ejecutado local) | 60 | 6 | 90 | 90,91 % | 40,00 % | 55,56 % |
| Microsoft Presidio | — | — | — | — | — | NO EJECUTADO |
| Cloudflare DLP | — | — | — | — | — | NO EJECUTADO |
| Google Model Armor | — | — | — | — | — | NO EJECUTADO |

**Por país, DELIA:** Chile F1 79,25 %; Colombia 79,01 %; México 18,18 %; Bolivia 18,18 %; global 100 % dentro de este corpus. **79 identificadores no detectados.** El resultado global positivo no mide todas las clases de PII. No hay certeza de sanitización integral ni despliegue seguro.

**Interpretación verificable:** DELIA superó sólo una baseline rudimentaria en ese corpus. **No existe evidencia de que gane a Presidio, Cloudflare ni Google**. El corpus NO permite prometer F1 real en producción, cumplimiento normativo, aislamiento entre clientes ni ausencia de fugas.

**Fuente y fecha:** [Registro Ronda 3](../REGISTRO_INVESTIGACION_RONDA3_2026-10-31.md) (31/10/2026).

---

## PÁGINA 2/2 — Alternativas, riesgo y colaboración
**Opciones externas a evaluar, no evaluadas experimentalmente:**

- **Microsoft Presidio:** software abierto extensible; la exactitud depende de reconocedores, configuración e idioma. [Instalación](https://microsoft.github.io/presidio/installation/) (consultado 31/10/2026).
- **Cloudflare AI Gateway DLP:** proveedor informa escaneo gratuito en todos los planes y sólo dos perfiles predeterminados sin suscripción Zero Trust. No se ha probado cobertura RUT/NIT/CURP. [Precios](https://developers.cloudflare.com/ai-gateway/reference/pricing/) (actualizado 15/10/2026).
- **Google Model Armor:** tarifa publicada de 2 millones de tokens mensuales gratuitos y sobreuso sujeto a cobro; cuenta, permisos y detector regional pendientes. [Página del producto](https://cloud.google.com/security/products/model-armor) (consultada 31/10/2026).

**Dónde DELIA podría aportar (hipótesis, NO demostrado):** cobertura medible de identificadores regionales en integraciones multiproveedor, política por cliente, trazabilidad reducida de metadatos y mecanismo de no envío. Pero todavía faltan CURP/RFC, CI/NIT bolivianos, direcciones y defensas robustas.

**Qué preguntar antes de construir:** (1) ¿Qué modelos y pasarelas usan actualmente? (2) ¿Qué información sensible envían realmente, bajo autorización? (3) ¿Qué herramientas filtran y quién revisa sus errores? (4) ¿Cuánto gastan en licencias, infraestructura y horas de ingeniería al mes? (5) ¿Quién tiene autoridad para aprobar cambio de tecnología? (6) ¿Cuál sería una razón para NO incorporar DELIA?

**Solicitud ética:** buscamos una conversación técnica voluntaria de 30 minutos, sin datos personales de clientes ni acceso a sistemas. A cambio compartimos este informe y el corpus sintético, incluso si la respuesta es que DELIA no aporta valor. No pedimos compra, piloto, cartas ni permisos de datos. Las respuestas sólo se usarán con consentimiento y se anonimizarán en resúmenes públicos.

**Límites de seguridad (P0 abiertos):** autenticación multitenant, minimización de logs, sanitización efectiva de salida y CI siguen pendientes en `main`; no aceptar datos reales ni crear cuentas productivas hasta revisión humana. [Issues](https://github.com/andres-olguin/DELIA/issues/6) · [Protocolo de competidores](../benchmarks/GUIA_COMPARADORES_DLP_RONDA4_2026-10-31.md).

**Contacto:** canal corporativo público de MasterTech SpA a través de [mastertechg.com](https://mastertechg.com). No se afirma que exista un estudio comercial científico ni compensación garantizada.
