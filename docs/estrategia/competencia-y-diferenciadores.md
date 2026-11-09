# DELIA — Competencia real y diferenciación comprobable

> **Actualización 09/11/2026:** Helio (https://github.com/gethelio/helio) ya documenta aprobación, prerequisitos y presupuestos acumulados; AgentTrustOps (https://github.com/teresaliu90/AgentTrustOps) aborda efectos, idempotencia y reconciliación; Temporal (https://docs.temporal.io/ai) cubre durabilidad. **No presentar DELIA Verified Workflows como categoría inédita.** Ver [matriz internacional](investigacion-global-2026-11-09.md) y [Outcome Assurance](delia-outcome-assurance.md).


**Investigación 09/11/2026.** No se han ejecutado pruebas comparativas estandarizadas de DELIA contra estos proveedores. Sus páginas pueden cambiar; toda comparación debe indicar versión, fecha, política, región y contexto.

## Competencia por categoría

| Categoría | Ejemplos revisados | Qué ofrecen/afirman | Implicación para DELIA |
|---|---|---|---|
| Multi-LLM gateways | LiteLLM, Cloudflare AI Gateway, Portkey | Enrutamiento, uso, límites, registro; Cloudflare incluye DLP para prompts y respuestas | No vender solo «gateway con PII» |
| Enterprise AI security | Palo Alto Prisma AIRS / Agent Security, Microsoft Defender/Purview | Identidad, gobernanza de agentes, controles runtime y visibilidad a escala | No afirmar que «agent firewall» es exclusivo |
| Agentes y plataforma cloud | Google Cloud Agent Gateway | Control programable user↔agent↔tool e integración de seguridad | DELIA debe interoperar, no competir por conectividad masiva |
| PII | Microsoft Presidio, PrivAiTe | Detectores, anonimizadores, reglas y protección de flujo según versión | Medir precisión local y costos de mantener recognizers |
| Open-source proxies | Grepture Proxy, LLM-Shield-Proxy | Filtros, inspección y funciones de seguridad parcialmente similares | Buscar casos de uso específicos, no copiar solo features |
| Seguridad MCP/agentes | Strathon, Soup Wall y otros | Políticas de herramientas, aprobaciones y controles | Importancia de la ejecución sin bypass y la calidad de evidencia |

## Verificaciones externas y referencias

1. OWASP, Agentic Security Initiative: https://genai.owasp.org/initiatives/agentic-security-initiative/
2. OWASP Top 10 for Agentic Applications (publicado 09/12/2025): https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
3. OWASP lanzamiento Agent Control Standard (02/09/2026): https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/
4. Cloudflare AI Gateway Features: https://developers.cloudflare.com/ai-gateway/features/
5. Palo Alto Prisma AIRS Agent Security: https://www.paloaltonetworks.com/ai-security/agent-security
6. Palo Alto AI Gateway (datasheet octubre 2026): https://www.paloaltonetworks.ca/resources/datasheets/prisma-airs-ai-gateway
7. Google Cloud Agent Gateway ISV ecosystem (mayo 2026): https://cloud.google.com/blog/products/identity-security/introducing-agent-gateway-isv-ecosystem-for-security-and-governance
8. Microsoft Cloud Adoption Framework AI agent governance: https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ai-agents/governance-security-across-organization
9. PrivAiTe: https://github.com/crp4222/PrivAiTe
10. Grepture: https://github.com/grepture/proxy
11. LLM-Shield-Proxy: https://github.com/ninadphalak/LLM-Shield-Proxy
12. Microsoft Presidio: https://github.com/microsoft/presidio

Enlaces de producto son **autodescripciones**, no benchmarks independientes. Evitar comparar precios de enterprise no públicos.

## Gran diferenciador aspiracional

**«Políticas verificables para acciones de agentes, con protección de datos regional y paquetes empresariales que una integradora puede replicar para múltiples clientes sin mezclar permisos».**

No se basa en afirmar exclusividad de tecnología. Combina cuatro hipótesis difíciles de ejecutar bien simultáneamente:

1. **Enforcement técnico real:** adapter sin bypass, autorización transaccional exacta y tests de mutación/replay/cross-tenant.
2. **Contexto regional auditable:** RUT, NIT, RFC, CURP, CI y textos de documentos, con conjuntos de evaluación independientes.
3. **Distribución B2B2B:** onboarding de una organización en minutos (meta), políticas aisladas por cliente y servicio de partner.
4. **Evidencia minimizada reproducible:** versiones, recibos, test de seguridad, runbooks, sin retener PII cruda por defecto.

## Defensibilidad económica (no patentabilidad)

Un patrón regex se copia rápidamente; una cadena completa de integraciones, soporte, datasets evaluados, confianza, contratos, API estable, partners activos y baja rotación de clientes es más difícil de replicar. Aun así no constituye una barrera garantizada: Microsoft, Google y Palo Alto tienen equipos y canales muy superiores.

**Medir la ventaja, no proclamarla:**
- Test «seguridad real»: herramienta denegada nunca ejecutada a través del punto de enforcement en escenarios auditados.
- Test «integración»: tiempo desde repositorio nuevo a primera política segura; fallos y esfuerzo de soporte.
- Test «regional»: TP/FP/FN, precisión y recall por idioma y entidad frente a baseline equivalente.
- Test «empresa»: aislamiento real entre tenants, RBAC/ABAC, revocación, retención y exportación.
- Test «valor»: ¿qué control faltaba? ¿Cuánto costaba antes? ¿Paga el integrador más que su alternativa?
- Test «finanzas»: margen real por cuenta y conversión por vertical.

## Decisión estratégica ante una ventaja insuficiente

Si un competidor resuelve el control de acciones y la única diferencia es el país del RUT, **no merece duplicar un gateway entero**. Pivotar a SDK, pack regional, plugin de políticas o servicio integrable. Si la plataforma existente tiene mejor seguridad, ofrecer interconexión en vez de reemplazo.

## Referencias regulatorias

- UE: el AI Act tiene fases de aplicación distintas por casos y anexos; verificar texto oficial actualizado, no usar el calendario como urgencia artificial. https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai
- Chile: Ley 21.719 y posibles ajustes legislativos requieren confirmación con fuente vigente al momento de contratar. https://www.bcn.cl/leychile/
- OWASP y NIST son marcos de referencia; aplicar controles inspirados en ellos **no** certifica a DELIA.

## Cómo responder a Emmanuel

«Los tres proyectos que compartiste resuelven partes similares de privacidad y proxy. Nuestra apuesta no es un filtro más: queremos que un integrador pueda gobernar acciones de agentes para varios clientes con controles específicos, prevención de uso indebido y evidencia verificable, apoyado por detección regional. Hoy tenemos un laboratorio de políticas; falta demostrarlo en un backend de producción. La comparación que importa será medir casos E2E y costo de integración contra otras herramientas, no decir que somos los primeros».
