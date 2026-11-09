# DELIA — Investigación competitiva internacional y decisiones de producto

**Corte:** 09-11-2026. **Autoría:** investigación asistida y contraste de documentación pública. **Método:** búsqueda en inglés, español, portugués, francés, alemán, japonés y chino; mayor profundidad en inglés y español por cobertura de fuentes. No se afirma haber investigado «toda la web» ni todas las empresas/idiomas. Las fichas pueden cambiar. **NO hubo despliegue, benchmark instrumental, análisis de vulnerabilidades ni ensayo de precios de competidores**. Las funciones son *autodeclaraciones en repositorios o páginas oficiales* salvo que se señale lo contrario.

## 1. Descubrimiento que invalida claims anteriores

Tres propuestas que DELIA consideró altamente diferenciadoras **ya están expuestas por actores existentes**:

1. **Agent firewall, aprobaciones, dependencias y presupuestos acumulados:** Helio (https://github.com/gethelio/helio) describe reglas `ALLOW/APPROVE/DENY`, prerequisitos por herramienta, presupuestos entre servidores, auditoría de llamadas y simulación de políticas. Su README es una descripción del proyecto, no una auditoría independiente.
2. **Efectos empresariales con idempotencia y reconciliación:** AgentTrustOps (https://github.com/teresaliu90/AgentTrustOps) se presenta como control de efectos y reintentos con reconocimiento de estado desconocido. Su propio README distingue capacidades que aún no se han publicado.
3. **Durabilidad de procesos y aprobaciones:** Temporal (https://docs.temporal.io/ai) documenta workflows reanudables, aprobaciones, patrones saga y recuperación tras fallos. No debemos desarrollar nuestro propio scheduler sin demostrar necesidad.

**Decisión:** retirar de la narrativa cualquier claim «primero en aprobación de agentes», «único con reconcilicación» o «único con presupuestos autónomos». Ganar por implementación y empaquetado, no por inventar un componente ya conocido.

## 2. Comparación de referencias internacionales (26 opciones, no ranking)

| Solución / origen | Categoría | Capacidades publicadas que importan | Qué **no** asumir sobre ellos / DELIA | Fuente |
|---|---|---|---|---|
| Helio / repositorio inglés | Proxy MCP | Approval, presupuestos, prerequisitos, auditoría, múltiples upstreams | No decir que DELIA es pionero en estas funciones | https://github.com/gethelio/helio |
| AgentTrustOps / repositorio inglés | Side-effects | Bound approval, idempotencia, reconciliación, registros portables | Proyecto temprano; ciertas integraciones no publicadas | https://github.com/teresaliu90/AgentTrustOps |
| Agentgateway / Linux Foundation | Gateway abierto | LLM/MCP/A2A, auth, observabilidad, rutas, múltiples protocolos | No tiene sentido competir solo por conectividad | https://github.com/agentgateway/agentgateway |
| Cerbos + Agentgateway / UE | Autorización | Políticas por identidad, rol, herramienta, contexto vía ext_authz | No decir que «políticas contextuales» son nuevas | https://www.cerbos.dev/ecosystem/agent-gateway |
| Open Policy Agent / OSS | Policy-as-code | Motor declarativo de permisos reutilizable, Rego, decisión separada | Integrar o interoperar en vez de reescribir RBAC sin motivo | https://github.com/open-policy-agent/opa |
| Pomerium / gateway | IAM/MCP | OAuth, TLS, permisos por herramienta y proxy para servidores MCP | No afirmar que la gestión de tokens es exclusiva | https://www.pomerium.com/docs/capabilities/mcp |
| Temporal / durabilidad | Workflows | Esperas humanas, reanudación, workflow por entidad, sagas | No construir otro motor durable prematuramente | https://docs.temporal.io/ai |
| LangChain Deep Agents / agentes | Orquestación | Herramientas, subagentes, permisos y aprobaciones con framework | Diferenciar control externo vs. dentro del framework | https://docs.langchain.com/oss/javascript/deepagents/overview |
| Palo Alto Prisma AIRS / EE. UU. | Seguridad empresarial | Identidad, gobernanza de agentes y seguridad runtime declaradas | Competidor con escala, soporte e integraciones; no igualar claims | https://www.paloaltonetworks.com/ai-security/agent-security |
| Microsoft Foundry AI Gateway / EE. UU. | Gateway gestionado | Gobierno de herramientas MCP, autenticación, rate limiting y auditoría | Documentación en preview y limitaciones que pueden cambiar | https://learn.microsoft.com/azure/ai-foundry/agents/how-to/tools/governance |
| Google Agent Gateway / EE. UU. | Gateway y política | Control de herramientas, modelos, agentes, OAuth y observabilidad | No prometer interoperabilidad hasta pruebas | https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview |
| Tencent Cloud AI Agent Security Gateway / China | Gateway corporativo | Acceso de agente a MCP/API, control por recurso, identidad, credenciales y auditoría | China tiene ofertas reales; no presumir vacío global | https://cloud.tencent.com/document/product/1627/131323 |
| Tencent Cloud AI Gateway MCP / China | Gateway corporativo | ACL por tool/server, API Key/JWT/OAuth/OIDC, políticas | No presentar tool ACL como novedad | https://cloud.tencent.com/document/product/1826/134890 |
| IBM Agent Identity / Brasil (idioma PT) | Identidad y gobierno | Identidad de agente, responsabilidad, permisos, trazabilidad | Página localizada no significa producto creado en Brasil | https://www.ibm.com/br-pt/products/agent-identity |
| GitLab agent governance / Francia (idioma FR) | Gobernanza DevOps | Atribución, trazabilidad de intención de código, control de MCP y permisos | Versión localizada, no necesariamente empresa francesa | https://about.gitlab.com/fr-fr/blog/govern-agentic-ai-mcps-code-assistants/ |
| Google Agent Gateway / Alemania (DE) | Gateway | IAM/SPIFFE, acceso por herramienta, política por organización/proyecto | Página localizada de proveedor internacional | https://docs.cloud.google.com/gemini-enterprise-agent-platform/govern/gateways/agent-gateway-overview?hl=de |
| Obot / distribuidor japonés | Control de MCP | Distribución japonesa, identidad, credenciales centralizadas y tools aprobadas | El distribuidor no equivale a innovación exclusiva japonesa | https://www.pentio.com/news/2026_11_obot/ |
| human-mcp / chino simplificado | Human in the loop | Solicitudes a humanos a través de MCP, tareas, tiempos, UI y scopes | No vender sola la aprobación como ventaja única | https://github.com/LIghtJUNction/human-mcp/blob/main/README.zh-CN.md |
| SOIT / francés | Runtime gobernado | Agentes empresariales con permisos, secretos, auditoría, costos y traces | Requiere validar versión/funcionalidad, no comparar sin instalación | https://soit.ai/fr/ |
| Presidio / privacidad | Detección PII | Análisis, anonimización y uso como librería en otras plataformas | **Repositorio actual ahora es Data Privacy Stack**, no atribuir propiedad vigente sin verificación | https://github.com/data-privacy-stack/presidio |
| Dativo Talon / runtime | Controles de acciones | Decisiones en tool calls, rutas HTTP, seguridad y costos | No declarar «verificación de acciones» inédita | https://dativo.io/ |
| Tenuo / identidad por tarea | Auth por tarea | Warrants con permisos exactos en cada llamada | No decir que «scope por tarea» es nuevo | https://tenuo.ai/ |
| AuthSec / seguridad de agentes | Identidad agente | OAuth/PKCE, registros y permisos de agentes | No crear un IdP propio sin ventaja técnica | https://authsec.ai/ |
| TrustCircleAI / OSS | Inventario y evidencia | Human authority, inventario y evidencia firmada | No confundir «recibo HMAC» con plataforma GRC | https://github.com/mairp/trustcircle |
| AgentID / OPA proyecto | Manifiesto autorización | Declaración de autoridad, policy generation y refund demo | Manifiestos de agente con límites ya estudiados | https://github.com/orgs/open-policy-agent/discussions/754 |
| mcp-brasil / portugués | Conectores regionales | Muchas fuentes públicas brasileñas accesibles por MCP | Los datos regionales y conectores no constituyen por sí solos una plataforma de control | https://github.com/Mcp-Brasil/mcp-brasil |

**Advertencia:** esta matriz compara capacidades **declaradas**, no cumplimiento, calidad, rendimiento ni madurez verificados por el equipo DELIA. No se infieren ausencias: no aparecer en una página no significa que un proveedor carezca de la función. Los productos comerciales pueden tener tarifas/ediciones y estados beta diversos.

## 3. Evidencia multilingüe y límites

| Idioma de fuente | Ejemplos | Lo que enseña a DELIA |
|---|---|---|
| Inglés | Helio, AgentTrustOps, Temporal, agentgateway, Cerbos, OPA | Las capacidades técnicas y de recuperación que creíamos diferenciadoras están cubiertas por múltiples actores |
| Español | Documentación de DELIA y oferta Check Point de agent security | Hay comunicación comercial regional, pero **el idioma no acredita originalidad** |
| Portugués | IBM Agent Identity BR; mcp-brasil | Brasil necesita documentación y conectores contextuales, no solo traducción |
| Francés | GitLab (FR), SOIT | Gobernanza y runtime operan con vocabularios muy similares a nuestros conceptos |
| Alemán | Google Agent Gateway (DE), marco de administración alemana | La autonomía se define por riesgo/impacto y responsable, no una mera opción del usuario |
| Japonés | Obot distribuido por Pentio en Japón | Hay canal de distribución y partner local: distribución puede importar tanto como ingeniería |
| Chino | Tencent Cloud, human-mcp | Gateways con auth/ACL y flujos humanos son comunes también fuera de Occidente |

Fuentes relevantes: Alemania https://agentische-verwaltung.gov.de/framework-volltext/target-operating-model/faehigkeiten/governance/steuerung-und-verantwortung/ ; Francia https://about.gitlab.com/fr-fr/blog/govern-agentic-ai-mcps-code-assistants/ ; Japón https://www.pentio.com/news/2026_11_obot/ ; China https://cloud.tencent.com/document/product/1627/131323 ; Brasil https://www.ibm.com/br-pt/think/perspectives/how-to-effectively-govern-third-party-ai-agents-across-the-enterprise .

**Limitaciones:** no todos los idiomas tienen igual profundidad de búsqueda; no se realizó revisión de productos en todos los mercados, auditoría de código o benchmark de proveedores. La tabla sirve para planificación, no due diligence de inversión ni claims de ventas.

## 4. Diferenciación defendible a INVESTIGAR, no probada

La propuesta más específica de DELIA es **«contratos operacionales verificables para agentes de IA, adaptados a flujos empresariales y datos latinoamericanos, entregados a través de integradores»**.

Un *contrato operacional* especifica: identidad/verificación requerida, precondiciones de negocio, límites cuantitativos, herramienta, estados permitidos, aprobación, idempotencia, resultado esperado, verificación externa, tratamiento de resultados desconocidos, evidencia mínima, rollback/compensación y política de datos.

**Una aprobación no es un resultado**. Una acción permitida no significa que se ejecutó. Una respuesta exitosa de la herramienta no garantiza que el sistema de registro esté actualizado. Sin lectura independiente del sistema autoritativo, DELIA solo puede declarar «resultado reportado». Estas distinciones aumentan valor empresarial potencial, pero no son inéditas: AgentTrustOps y Temporal ya abordan partes importantes.

## 5. Evaluación frente a tres alternativas concretas

**Opción A — Helio como proxy:**
Si basta bloquear tool calls y poner aprobaciones/presupuestos, DELIA probablemente no aporta suficiente valor. Probar si un pack sectorial con invariantes de negocio y evidencia de resultado reduce trabajo significativo; si no, usar Helio o integrarlo.

**Opción B — AgentTrustOps + Temporal:**
Si el sistema necesita ejecución duradera y reconciliación, la alternativa existente puede ser mejor que reinventarlo. Probar DELIA como contrato sectorial/analizador de reglas y observabilidad de resultados por cliente, interoperando con orquestador subyacente.

**Opción C — Agentgateway + Cerbos/OPA:**
Si la empresa ya tiene gateway y políticas, DELIA podría ser un complemento de contrato de proceso y benchmark regional, no un reemplazo de infraestructura. Priorizar adapters con límites verificables y costo de integración menor.

## 6. Experimentos comparativos falsables

1. **Ejecución sin permiso:** conjunto sintético de acciones denegadas, el adapter real jamás ejecuta. Medir condiciones de excepción y fallas.
2. **Invariantes de negocio:** rechazo de reembolso duplicado, importe superior al saldo, tenant incorrecto, estado vencido, moneda incorrecta, usuario no verificado.
3. **Reconciliación:** casos de éxito confirmado, rechazo, timeout, resultado desconocido y divergencia; medir resolución sin duplicar efecto.
4. **Integración:** horas reales y costo operativo para añadir primer y segundo cliente en DELIA vs. Helio y alternativa actual del comprador.
5. **Regional:** pruebas independientes de PII CL/MX/CO/BO y posteriormente BR, separadas de corpus de desarrollo.
6. **Modelo comercial:** comprador asigna presupuesto a control de proceso, seguridad o automatización; medir WTP sin sesgo.
7. **TCO:** licencia, hosting, soporte, compliance, tiempo de integración y costo de incidentes medido; no simular ahorro seguro.

## 7. Decisión estratégica

**No competir por ser el gateway más grande.** Entregar primero un pack comercial de procesos empresariales, documentar mejor caso y comparar con la alternativa del comprador. Si no hay ventaja de adopción o utilidad demostrada, DELIA debe pivotar a SDK, conector, capa de contratos o servicio de integración.

La referencia de seguridad es OWASP: https://owasp.github.io/DevSecOpsGuideline/2-Process/2-2-Develop/2-2-5-AI-Agent-and-MCP-Security/ y CoSAI 2026: https://github.com/cosai-oasis/ws4-secure-design-agentic-systems/blob/main/whitepapers/model-context-protocol-security.md . **No equivalen a certificación.**
