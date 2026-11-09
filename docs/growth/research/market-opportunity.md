# Mercado, competencia y oportunidad de posicionamiento de DELIA — corte 09/11/2026

## 1. Las señales macro sí justifican exploración

- **Chile:** el ITD-IA 2026 de CORFO/CCS/PMG (740 empresas) sitúa la madurez media en 34/100 y gobernanza en 27/100. La encuesta informa amplias brechas en políticas y mecanismos de gobernanza. Esto sugiere trabajo de consultoría, capacitación, auditoría y producto, pero **no mide cuántas empresas comprarían DELIA**.
- **México:** Endeavor Mexico AI Pulse (163 empresas participantes) documenta adopción de IA y una brecha entre uso y captura de valor. Ese panel no representa automáticamente a todas las empresas mexicanas.
- **EE. UU. / global:** NIST AI Agent Standards Initiative y OWASP Agent Control Standard respaldan interoperabilidad, controles observables y seguridad como obstáculos de adopción.
- **B2B mediático:** Edelman/LinkedIn 2025 documenta la influencia de profesionales no visibles en las decisiones de compra; LinkedIn 2026 defiende video y voces humanas confiables en marketing B2B. Esto respalda **medir contenido técnico y reuniones**, no pagar influencers a ciegas.

Fuentes:
- https://www.ccs.cl/2026/09/04/chile-mide-primera-vez-madurez-ia-parte-34-100-puntos-oportunidad-escalamiento/
- https://mexico.endeavor.org/mexico-ai-pulse/
- https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure
- https://genai.owasp.org/resource/agent-control-standard-acs/
- https://www.edelman.com/index.php/expertise/Business-Marketing/2025-b2b-thought-leadership-report
- https://www.linkedin.com/business/marketing/blog/trends-tips/b2b-marketing-insights-creators-thought-leadership

## 2. Mapa de oportunidades por unidad de decisión

| Comprador | Problema a comprobar | Oferta para investigar | Descartar si |
|---|---|---|---|
| Integrador B2B | Tiempo de replicar controles para varios clientes | Workflow Readiness Lab → Partner | Tiene solución suficiente y barata |
| CTO SaaS | Agentes cambian registros sin autoridad | Contratos, control de tools, sandbox | No usa tools o ya tiene RBAC completo |
| Operaciones de atención | Supervisión de cambios de tickets/CRM | Control Evaluation Pack | No puede acceder a datos sintéticos ni comprar evaluación |
| CISO | Evidencia de permisos/revocación antes de producción | Evals de escenarios y reporte | Exige certificación hoy que DELIA no posee |
| Educación/desarrolladores | Aprender a probar agentes | Academy/community demo | Solo busca charla gratuita sin interés técnico |
| Finanzas | ROI de automatización con controles | Tiempo/costo por workflow verificable | No tiene baseline operativo |

**Prioridad hoy:** integradoras CRM/BPO low-risk; no aumentar campañas hacia seis compradores simultáneos. Proteger capacidad de ingeniería.

## 3. Competidores y alternativas

Helio (MCP approvals/budgets), AgentTrustOps (idempotencia/reconciliación), Temporal (durabilidad), Agentgateway (transporte/auth), Cerbos/OPA (policy-as-code) y proveedores cloud establecidos. Evaluar siempre **comprar, integrar, construir** y alternativa "no automatizar". La ventaja de DELIA sería una experiencia integrada por proceso y región, **solo si mediciones muestran menor costo de instalación y mejor control útil**.

Detalle: https://github.com/andres-olguin/DELIA/blob/main/docs/estrategia/investigacion-global-2026-11-09.md .

## 4. Efectos mediáticos medibles sin confundir viralidad y demanda

**Top-of-funnel:** alcance de publicaciones, clics verificados con UTM, visualizaciones completas.
**Mid-funnel:** visitas al README/demo, instalaciones reproducibles, correos B2B consentidos, reuniones con CTO.
**Bottom-funnel:** diagnósticos contratados, pilotos aprobados, evidencia de resultado, margen y renovación.

La hipótesis `LinkedIn + GitHub + video demostrativo` puede funcionar para integradoras, pero se debe ensayar frente a canales alternativos y capacidad del equipo. Un post con 100.000 vistas y cero compradores adecuados no es un éxito comercial.

## 5. Microexperimentos comparables

A. **Comparar contenido técnico vs noticias de riesgo:** dos publicaciones con CTA al mismo kit, medir visitas útiles y reuniones, sin engañar sobre seguridad.
B. **Comparar español vs inglés con piezas equivalentes:** tasa de conversación con compradores técnicos, no likes brutos. Portugués solo con revisión idiomática.
C. **Comparar workshop vs software aspiracional:** preguntarle al comprador qué pagaría hoy y por qué. Diferenciar propuesta de producto inexistente.
D. **Comparar dos tipos de demo:** revocación de tool y resultado desconocido en CRM simulado; medir comprensión técnica.
E. **Analizar cohortes de partner:** tiempo de implementación de cliente 1 vs 2 en entorno de prueba, soporte y costos de entrega.

## 6. Lo que aún NO sabemos

TAM/SAM/SOM contratables, frecuencia real de problemas en ICP, presupuesto, costos de seguridad por tenant, ratio de conversión, ROI de contenido, coste del canal partner, demanda de controles multi-turn y sensibilidad del mercado a precios. Estos datos requieren entrevistas, compras, instalaciones y análisis, no infografías o porcentajes extraídos de videos.

## 7. El diferenciador mediático

**DELIA publica la prueba y sus limitaciones.** Cada lanzamiento técnico relevante debería traer: commit SHA, test/fixture, entorno, qué se bloquea, qué sigue sin protegerse, costo de prueba y un CTA a discutir un proceso empresarial. Ser transparente puede construir confianza, pero requiere constancia y revisión. No es una certificación ni una ventaja automática.
