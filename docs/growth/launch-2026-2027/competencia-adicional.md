# DELIA — Segunda expansión internacional: 18 referencias adicionales y evaluación de nombre

**Fecha:** 09/11/2026. Complementa [la auditoría anterior de 22](../../estrategia/red-team-competitivo-2026-11-09.md); **total documental acumulado: 40 referencias seleccionadas**. Esta selección NO equivale a revisar los 101 proveedores de un índice independiente, ni a una comparación funcional o de precios ejecutada.

## Los 18 casos adicionales

| Proyecto | Categoría | Qué declaran o documentan | Implicación para DELIA |
|---|---|---|---|
| [NVIDIA OpenShell](https://www.nvidia.com/en-us/ai/openshell/) | agent runtime isolation | Runtime sandbox policy, credential mediation, egress controls and auditing | DELIA no puede diferenciarse por sandbox/kill-switch o bloqueo de egress. |
| [NVIDIA Agent Policy Fabric](https://docs.nvidia.com/agent-policy-fabric/integrations/openshell) | policy federation | Separates enforcement/runtime boundary and policy decision service | La integración entre políticas y runtime también tiene un competidor; interoperar. |
| [APort](https://aport.io/) | agent authorization passport | AI Agent Passport, pre-action policies and signed decisions | No inventar nombre comercial Agent Passport ni decir que firma de decisiones es exclusivo. |
| [ContractOps by Kopilot](https://kopilot-ai.github.io/contractops/) | contract test reliability | CI contracts, scenarios, release gates, drift and reliability budgets | El nombre ContractOps ya se utiliza; no registrarlo ni reclamar exclusividad sin due diligence. |
| [EcoKure Assurance Fabric](https://jarvi3.com/showcase) | evidence-based decision gates | Deterministic checks, signed evidence, replayable contract checks | Gates + evidence + verifier no son un concepto exclusivo. |
| [Arcade](https://agents.arcade.dev/) | agent tool authorization | Auth, scopes, tool execution, governance, broad tool catalog | Un catálogo de conectores y permisos no basta como ventaja. |
| [Aembit](https://aembit.io/) | agent workload IAM | Blended user+agent identity, secretless short-lived credentials and policy | IAM de agentes especializado ya existe, conviene integrar. |
| [Astrix / Cisco](https://astrix.security/) | agent identity inventory | Discovery, NHI graph and agent access governance; no new standalone sales since June 30 2026 | Estado comercial importa: comparar con Cisco, no presentar Astrix como startup independiente. |
| [Noma Security](https://noma.security/platform) | runtime agent governance | Discovery, policy enforcement and runtime security using existing gateways | La superposición sin reemplazar gateway está ya comercializada. |
| [Zenity](https://zenity.io/) | agent runtime security | Agent discovery, identity, policy and runtime defense | La gobernanza transversal está disputada por empresas financiadas. |
| [Agent Control](https://agentcontrol.dev/) | open agent policy SDK | Policy control with allow/deny/steer/warn and SDK hooks | Delia debe competir con paquete de pruebas de proceso y costo, no por API de allow/deny. |
| [LangSmith](https://www.langchain.com/langsmith/evaluation) | agent eval and observability | Trajectory-level evaluations, online/offline tests, human review and tracing | Evals y regresión tampoco son exclusivos; concentrarse en efecto empresarial. |
| [Arize Phoenix](https://arize.com/phoenix/) | open-source agent eval | Open-source OpenTelemetry tracing and evaluator workflows | No recrear observabilidad genérica. |
| [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/guardrails/) | agent development runtime | Input/output and function-tool guardrails, approvals and traces; limits for hosted tools noted | Foco en cobertura entre frameworks, casos negativos y fallos específicos. |
| [Amazon Bedrock Automated Reasoning](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails-automated-reasoning-checks.html) | formal policy validation | Logic-backed policy checks; limited to defined variables, English US, detect mode | No decir que verificar políticas formales no existe; analizar tradeoffs regionales y alcance. |
| [F5 AI Guardrails](https://www.f5.com/company/news/press-releases/f5-accelerates-ai-security-with-integrated-runtime-protection-for-enterprise-ai-at-scale) | runtime AI protection | Runtime AI policies and red-team services for enterprises | No competir por plataforma de seguridad completa a corto plazo. |
| [NVIDIA NeMo Guardrails](https://docs.nvidia.com/nemo/guardrails/configure-guardrails/guardrail-catalog/agentic-security) | model and agent rails | Injection detection and agentic guardrails | Complementar con contratos de negocio y evidencia real. |
| [Braintrust](https://www.braintrust.dev/manifesto) | agent eval/observability | Evals, tracing and iterative agent quality measurement | Calidad de observabilidad/evals no es barrera competitiva suficiente. |

**Lectura de evidencia:** descripciones de proveedores/repositorios del 09/11/2026. No se han instalado sus productos, comprobado tasas de protección ni revisado contratos. Algunos tienen funcionalidades en preview o requieren planes específicos.

## Descubrimientos críticos que corrigen la estrategia

1. **«ContractOps» no es un nombre libre/exclusivo:** Kopilot presenta un producto así denominado para contratos y gates de agentes. Mantener `DELIA ContractOps` solo como **descriptor de investigación interno**, no como nueva marca prometida. Necesita análisis de disponibilidad de marca antes de registrar dominios, empresa, redes o comercialización.
2. **«AI Agent Passport» no es exclusivo:** APort lo utiliza expresamente para identidad y control de agentes. No crear un «pasaporte DELIA» alegando categoría inédita.
3. **«No reemplazar tu gateway» tampoco es exclusivo:** Noma y Arcade declaran integraciones con stack existente; NVIDIA OpenShell/Agent Policy Fabric separan runtime de decisión de políticas.
4. **Evals/trace-to-regression** ya son foco principal de LangSmith, Phoenix y Braintrust. No ofrecer observabilidad generalista como primera apuesta.
5. **Formal policy verification** tiene proveedores como AWS Bedrock Automated Reasoning. La ventaja eventual de DELIA sería el costo y la experiencia de pruebas de efectos de negocio en idiomas/procesos particulares, nunca «inventamos la verificación».
6. **Preacción y evidencia firmada** aparecen en APort, EcoKure y otras ofertas; no suponer patente, unicidad o inmunidad frente a competidores.
7. **Astrix pasó a Cisco** y terminó ventas independientes nuevas desde el 30/06/2026 según su propia web; registrar correctamente el estado comercial.

## Diferenciador mejorado: DELIA Operational Assurance Kits (nombre de trabajo)

No convertir la etiqueta en promesa exclusiva o marca registrada. Proponer **un servicio/producto de proceso reproducible para integradoras**:

- **Diagnóstico de proceso:** un mapa empresarial de riesgos, flujo, reglas y stack existente, incluyendo qué ya resuelve sin DELIA.
- **Contratos y fixtures interoperables:** un mismo caso CRM/ticketing expresado como tests para dos implementaciones reales cuando existan conectores; denegaciones y resultados inciertos se observan desde la herramienta de prueba, no desde un autoinforme del LLM.
- **Evidencia por cliente:** configuración, cambios semánticos, tasa de bloqueo/falso bloqueo, fuente autoritativa y limitaciones; sin filtrar datos entre tenants.
- **Modelo económico por entrega:** medir horas y costos del primer y segundo cliente, soporte y costo por operación efectivamente verificada.
- **Salida sin dependencia forzada:** informe y artifacts que el integrador pueda usar incluso si decide no instalar DELIA.

**Valor comercial hipotético:** reducir esfuerzo de QA/estandarización para integradoras multiproyecto que hoy reimplementan controles de agentes. La diferencia **debe ganarse mediante benchmarking y ventas reales**, no mediante una matriz de «checkmarks».

## Lo que hoy existe y lo que no

**Actual:** laboratorio de contrato CRM con dos adaptadores simulados (PR #44) y varios estudios/documentos.  
**Pendiente:** conectores auténticos, endpoint seguro de autorización, fuentes de resultado autoritativas, IAM/tenant isolation, herramientas productivas, auditoría independiente, compradores y MRR.

## Protocolo mínimo para comprobar ventaja en enero

- Dos integradores independientes deben instalar el kit en sistemas de prueba con versiones congeladas.
- Medir **minutos hasta un contrato evaluado**, **horas de segundo tenant**, **cobertura de casos DENY**, **falsos bloques**, **costos de equipo/infraestructura**, **tiempo de generar informe**.
- Comparar contra stack original de cada integrador + una alternativa real de la misma categoría.
- Un resultado `INDETERMINATE` o un test no ejecutado jamás contará como seguridad probada.
- Registrar también cuando DELIA hace la integración más cara. Pivotar a SDK/servicio o detener producto si el comprador no paga más por el diferencial.

## Fuente adicional de contexto

[Agent Security Index](https://agentsecurityindex.com/) reporta 101 herramientas en 6 categorías al 06/11/2026, 41 open source. Es un **directorio**, no evidencia de superioridad o tamaño de mercado. La política de marketing debe reflejar esa saturación, sin frases «la primera protección de agentes del mundo».

## Diferenciación que sí sería defendible si la ejecutamos

**DELIA no vende otra regla de bloqueo: ayuda a integradoras a entregar y comprobar con menos trabajo un flujo empresarial seguro para su segundo, tercer y décimo cliente.** La métrica económica de esa afirmación todavía está pendiente.