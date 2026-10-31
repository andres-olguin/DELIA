# ¿Cloudflare, LiteLLM, Presidio o un proxy propio? Cómo comparar controles de IA empresarial

**Artículo listo para revisión editorial, 31/10/2026.** Las funciones y precios públicos citados pertenecen a cada proveedor y pueden cambiar; no representan precio pagado en Latinoamérica.

## Primero, no mezclemos productos distintos

Un **gateway** normalmente concentra tráfico, credenciales, rate limits, routing y métricas. Una **biblioteca DLP/PII** detecta categorías de datos, pero no necesariamente gestiona usuarios o proveedores. Una **plataforma de observabilidad** registra trazas y evaluaciones, pero esos registros pueden ser otra fuente de exposición. Un **guardrail de contenido** evalúa instrucciones o contenido dañino; no sustituye clasificación de información personal.

En consecuencia, comparar «precio por millón de tokens» de una API de inspección con «precio mensual de gateway» puede ser engañoso. Hay que estimar costo total de instalación, uso, logs, soporte, seguridad y contratos.

## Cinco alternativas públicas

| Alternativa | Para qué suele usarse | Precio / condición pública | Pregunta decisiva |
|---|---|---|---|
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/reference/pricing/) | Gateway y control DLP, logs y políticas por plan | Funcionalidad central gratuita; límites, DLP y almacenamiento requieren revisión de plan | ¿El proveedor existente cubre el flujo? |
| [LiteLLM](https://www.litellm.ai/pricing) | Proxy multiproveedor y cuotas/fallback | Software libre sin licencia de compra; operar y mantener no es gratis | ¿El costo de operar OSS sería menor? |
| [Portkey](https://portkey.ai/pricing) | Gateway comercial, observabilidad y controles | Plan Production anunciado US$49/mes al corte, sujeto a cambios | ¿Qué control adicional necesitas realmente? |
| [Microsoft Presidio](https://microsoft.github.io/presidio/supported_entities/) | Reconocedores PII extensibles | Software abierto, infraestructura/ingeniería a cargo del cliente | ¿Qué identificadores deben agregar y cómo probarlos? |
| [Google Model Armor](https://cloud.google.com/security/products/model-armor) | Inspección de prompts/respuestas | Precio y tramo gratuito dependen de modalidad; consultar [tarifario](https://cloud.google.com/security-command-center/pricing) | ¿Qué precisión, política y costo total ofrece en tu nube? |

**No afirmamos que estas herramientas carezcan de RUT, NIT, CURP ni de capacidad de añadir reglas locales.** Una prueba controlada es la única forma de sostener una mejora.

## Preguntas que plantearía a cualquier proveedor

1. ¿Qué motor detecta PII y puede compartirse un corpus público sin exposición de datos reales?
2. ¿Cómo mide precision, recall y falsos negativos por país y categoría?
3. ¿Quién gestiona la clave del upstream y los datos de observabilidad?
4. ¿Se permite bloquear en modo fail-closed, con política distinta por cliente y proveedor?
5. ¿Qué contenido queda en logs, cuánto tiempo y con qué accesos?
6. ¿Quién paga tokens, inspecciones, egress y almacenamiento cuando hay reintentos?
7. ¿Qué ocurre si la herramienta falla, pierde conexión o recibe un formato no soportado?
8. ¿Existe rollback, migración y soporte contractual verificado?

## Un experimento desfavorable para DELIA

El detector de DELIA obtuvo **47,33 % de recall** sobre un corpus sintético de 150 entidades, mientras su proxy productivo actual no lo llama antes de transmitir solicitudes. Es un rendimiento insuficiente para vender protección completa. [Benchmark de laboratorio](../../benchmarks/README.md).

Concretamente, si ya utilizas una solución consolidada con controles suficientes, **no sería recomendable añadir DELIA hoy**. La oportunidad del proyecto sería descubrir un problema latinoamericano específico, superar una comparación reproducible y ofrecer integración con responsabilidad demostrable.

## Conclusión

La decisión empresarial no es «¿qué gateway tiene más funciones en una tabla?», sino «¿qué riesgo y costo concreto puede controlar, medido en nuestro entorno y sin introducir otro intermediario inseguro?». Presidio, Cloudflare y Google Model Armor **aún no fueron ejecutados** contra el dataset DELIA; cualquier ranking sería inventado.

**Fuentes:** documentación oficial de cada proveedor enlazada arriba y código DELIA `main`, fecha de corte 31-10-2026. No existe producto DELIA certificado ni una comparativa que declare vencedor.
