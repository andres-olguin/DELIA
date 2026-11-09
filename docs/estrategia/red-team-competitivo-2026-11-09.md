# DELIA — Red team competitivo internacional: ¿por qué nos comprarían?

**Revisión:** 09/11/2026. **Método:** documentación y repositorios de **22 referencias** seleccionadas por similitud de producto, arquitectura, comprador o canal. No cubre todo el mercado; **no se instalaron los competidores ni se ejecutó benchmark pareado**. Es una evaluación crítica del **posicionamiento**, no un informe de penetración, certificación, prueba de precios ni predicción de ventas. Matriz de fuentes y conclusiones: [competidores-directos-2026-11-09.json](competidores-directos-2026-11-09.json).

## 1. Descartar explícitamente las afirmaciones que ya no se sostienen

| Claim anterior deseado | Por qué no sirve como exclusividad |
|---|---|
| «Primer firewall de agentes que permite/deniega tools» | Helio, Preloop, Gravitee, Runlayer, ServiceNow y gateways gestionados ya anuncian funciones comparables |
| «Primero con aprobaciones, presupuestos y herramientas MCP» | Helio, Preloop, NIA y otros declaran funciones en esas áreas |
| «Primero en verificar que una operación de negocio ocurrió realmente» | Pruvz y ACPT ya lo comercializan; AgentTrustOps declara reconciliación |
| «Primero con evidencia trazable/criptográfica» | AgentTrustOps, Pruvz, NIA, Helio y otros presentan registros y/o pruebas |
| «Primer B2B2B multi-tenant white label para integradoras» | Beyryl y CinderLabs AIRA ya anuncian portal multiempresa, white label o partners |
| «Único capaz de controlar desviación de reglas entre agentes» | Microsoft Agent 365 ya presenta plantillas de gobierno para evitar drift |
| «Primer estándar portátil de control de agentes» | OWASP Agent Control Standard (ACS) existe; NIST impulsa interoperabilidad |
| «Única seguridad PII sobre prompts y llamadas a tools» | PrivAiTe, Presidio, Lasso, Check Point y otros trabajan con DLP/PII |
| «Primera suite de pruebas de guardrails» | Promptfoo, ControlArena, garak, DeepTeam, PyRIT, Giskard y más ofrecen evaluación |

**No demostrar una ausencia en marketing NO significa que el competidor carece de una función.** La tabla se basa en funciones anunciadas; estado de producto y compatibilidad reales requieren instalación/revisión.

## 2. Amenazas más fuertes para la tesis de DELIA

### Pruvz — sustituto del resultado verificado
https://pruvz.ai/

Publica que su producto ya usa read-back independiente de Stripe y HubSpot test, evidencia criptográfica, verificación de estados empresariales y separación de tenants. **No se probó personalmente su implementación.** La idea «comparar esperado vs observado en un CRM» es insuficiente como ventaja.

**Qué debe demostrar DELIA:** entrega rápida de un contrato y tests de proceso en herramientas ya instaladas por una integradora, con estado de controles e informe exportable por cliente; comparar esfuerzo total con Pruvz.

### ACPT — competidor de contrato de resultado
https://www.acpt.cloud/

Describe contratos de resultado, reconstrucción de ejecución, ground truth, evaluación de reglas y evidencia. Su roadmap distingue NOW/NEXT/LATER; no confundir todas las ideas futuras con características presentes.

**Condición para ganar:** un nicho de integradoras/región/proceso donde la integración y el costo total sean demostrablemente mejores, no «inventamos Outcome Assurance».

### AgentTrustOps — competidor del commit point
https://github.com/teresaliu90/AgentTrustOps

Repo anuncia idempotencia duradera, autorizaciones verificadas, aprobación exacta, reconciliación de estados desconocidos, evidencia firmada y adaptadores (aunque reconoce límites de producción/estado de algunos ejemplos). DELIA no tiene actualmente una implementación equivalente productiva.

**Estrategia:** no reescribir su kernel sin razón; evaluar si se puede integrar como motor de efectos bajo un contrato de negocio DELIA. Comparar código, licencias y maintenance burden.

### Helio — competidor de proxy y servicios profesionales
https://github.com/gethelio/helio y https://helio.so/

No solo reglas MCP y aprobaciones: anuncia presupuestos acumulados, prerequisitos, protección de configuración, auditoría y servicios de política/revisión de despliegue. Incluso nuestra oferta temprana de workshop puede sustituirse por su consultoría.

**Estrategia:** vender comprensión de un proceso/varios sistemas con pruebas y costos, no una política MCP genérica. El primer comprador podría preferir Helio: aceptarlo y ofrecer integración complementaria solo si aporta valor.

### NIA AI Harness — competidor del resultado y el presupuesto
https://nia.sg/harness/

Plantea resultado independiente, límites y prueba a pedido. **No es exclusivo** hablar de costo por resultado verificado, guardrails y auditoría.

**Estrategia:** aportar una instalación más sencilla y menor trabajo para partners y casos regionales, con comparación pareada.

### Beyryl y CinderLabs AIRA — competidores del canal B2B2B
https://marketplace.microsoft.com/en-us/product/beyryl.beyryl_ms_2026?tab=overview ; https://cinderlabs.ai/aira/msp

Proponen entornos MSP multi-tenant, soporte de despliegue, white label, informes y monetización recurrente. El modelo comercial de DELIA Partner es replicable.

**Estrategia:** medir productividad de la segunda instalación por partner, demostrar un contrato específico y reducir carga humana de soporte. **No** afirmar 10× más rápido sin experimento.

### ServiceNow, Gravitee, Microsoft, Check Point — plataformas incumbentes
https://newsroom.servicenow.com/press-releases/details/2026/ServiceNow-advances-its-operational-harness-for-enterprise-AI-with-AI-Passport-and-expanded-governance-capabilities/default.aspx
https://www.gravitee.io/platform/ai-gateway
https://learn.microsoft.com/en-us/microsoft-agent-365/guidance/scale-governance
https://docs.lakera.ai/docs/agent-security

Identidad, gobierno de acciones, observabilidad, DLP, control de delegación, templates y métricas están en suites amplias. No es razonable competir contra sus recursos por **amplitud de features** durante la fase pre-venta.

**Estrategia:** interoperar y evitar sustituciones; crear kits que funcionen sobre stack existente.

## 3. El mercado comprador tiene cuatro alternativas más baratas que DELIA

1. **No automatizar** el proceso; mantener decisión humana donde el costo de falla supera el ahorro.
2. **Control nativo** del CRM, IAM, cloud/Agentforce, API gateway o plataforma de agentes.
3. **Ensamblar** OPA/Cerbos + Temporal + agentgateway + test runner + DLP.
4. **Adoptar una suite** Helio/Preloop/Pruvz/ACPT/ServiceNow y pagar por configuración.

**Criterio de compra:** solo recomendar DELIA si una combinación comprobada de horas ahorradas, cobertura de pruebas, reducción de errores observados y costo de soporte excede el costo de licenciar/configurar DELIA. Un cliente puede comprar únicamente el workshop de diagnóstico y decidir usar otra infraestructura.

## 4. Propuesta a INVESTIGAR que puede ser más defendible

### DELIA ContractOps for Integrators — hipótesis de posicionamiento

**«Una manera reproducible de adaptar, comprobar y mantener contratos de operaciones de agentes entre sistemas y clientes, sin imponer un nuevo gateway.»**

Un contrato portable de negocio declara `who`, `tenant`, `tool`, `allowed_effect`, `precondition`, `approval`, `expected_outcome`, `verification`, `evidence_scope`, `data_policy`, `retention` y `version`.

**Cinco partes del producto deseado:**
1. **Contract Builder:** plantilla de un flujo de CRM, no un estándar propietario universal. Definición legible para compradores.
2. **Cross-Stack Conformance:** pruebas y adaptadores hacia stack ya instalado (por ejemplo Helio/OPA/Cerbos); un fixture común detecta diferencias semánticas y políticas. **Actualmente solo se puede construir un laboratorio con respuestas ficticias**.
3. **Outcome Reconciliation:** fuente autoritativa y estado `VERIFIED/UNKNOWN/MISMATCH` con identidad, actor y transacciones reales. **Pendiente**.
4. **Tenant Delta & Partner Evidence:** diferencias de políticas entre clientes, documentación versionada, informes exportables minimizados; **pendiente**.
5. **Unit Economics & Buyer Proof:** tiempo para segunda instalación, falsos bloqueos, costo por resultado **independientemente verificado**, horas de soporte y control de margen. El simulador actual solo trabaja con supuestos.

**Diferenciación propuesta como combinación:** vertical estrecha BPO/CRM + interoperabilidad + packs por cliente + datos/riesgos regionales + evidencia de resultado + economía de delivery. Cada pieza tiene competidores; **solo un benchmark puede demostrar valor de la combinación**.

### Por qué no decir «totalmente único»

No existe método razonable para probar exclusividad sobre todos los productos/código y versiones del mundo, ni se puede impedir que un competidor copie una función. Un *moat* plausible puede surgir de integraciones comprobadas, plantillas mantenidas, tiempos de onboarding, relación con partners, calidad de datos permitidos y reputación, no de un nombre o lista de 30 capacidades.

## 5. Estrategia comercial que preserva caja

**Comprador ICP primario:** integradoras B2B que ya gestionan agents/CRM de 2+ clientes y pagan tiempo de configuración. **Oferta hoy propuesta:** diagnóstico de un workflow con presupuesto/alcance, riesgos, tests sintéticos y comparación honesta con gateway existente. Después: contrato y kit por proceso, luego SaaS Partner solo si P0 y benchmark.

**Contraoferta de confianza:** aceptar que Helio, Pruvz o código nativo sean mejores en un caso. Entregar al comprador un informe que incluya «no conviene usar DELIA aquí». La confianza puede aumentar la probabilidad de futuros contratos, pero no hay evidencia de esa tasa todavía.

## 6. Riesgo normativo: Chile

La BCN publica para Ley 21.719 una fecha diferida de entrada en vigor **01/12/2026** (versión revisada al corte). El Ejecutivo presentó un proyecto de prórroga (boletín 18.623-07), aprobado en Senado el **29/10/2026** y en **segundo trámite** ante la Cámara al 09/11. **La nueva fecha NO está promulgada en la documentación consultada.** No vender compliance automático ni afirmar certeza de calendario futuro.

Fuentes:
- https://www.bcn.cl/leychile/Navegar?idNorma=1209272&idVersion=2026-12-01
- https://camara.cl/legislacion/ProyectosDeLey/tramitacion.aspx?prmBOLETIN=18623-07&prmID=19307
- https://www.economia.gob.cl/2026/09/01/gobierno-propone-ampliar-plazo-para-implementar-nueva-ley-de-proteccion-de-datos-y-institucionalidad.htm

**Aplicación para DELIA:** una lista de controles y evidencia de flujos con PII, revisión por asesor legal chileno y pruebas regionales; no «certificado Ley 21.719».

## 7. Decisiones concretas

1. **No desarrollar** otro gateway generalista, kill-switch decorativo o motor de workflows desde cero solo para marketing.
2. **Diseñar** el contrato de proceso como formato portable y los tests que obligan a una implementación a cumplirlo; mapear OWASP ACS donde corresponda.
3. **Medir** segundo cliente/segundo sistema: tiempo real de integración, falsos bloqueos, fallos de deny y costo total.
4. **Probar** al menos dos stacks, uno en infraestructura ajena al equipo cuando haya permiso.
5. **Entrevistar** compradores sobre cuánto les cuesta mantener reglas por cliente y quién paga el gasto.
6. **Revisar** después de 15 entrevistas/no-fit; pivotar a SDK, evaluación por proyecto o pausa si no hay demanda.
7. **Mantener** PR #21 DRAFT y P0 de identidad/egreso/tools hasta pruebas independientes.

## 8. Referencias y límites

Matriz: [competidores-directos-2026-11-09.json](competidores-directos-2026-11-09.json); estudio internacional anterior [investigacion-global-2026-11-09.md](investigacion-global-2026-11-09.md); [roadmap de pruebas](../competitive-assurance/README.md).

Técnica: Microsoft Research (2026) https://www.microsoft.com/en-us/research/publication/where-does-exactly-once-live-model-harness-and-tool-contract-effects-on-duplicate-side-effects-in-llm-agents/ ; OWASP ACS https://genai.owasp.org/resource/agent-control-standard-acs/ ; NIST https://www.nist.gov/news-events/news/2026/02/announcing-ai-agent-standards-initiative-interoperable-and-secure .

**Auditoría documental, no benchmark comparativo ejecutado**. Ninguna cifra de ingresos, clientes, retención o superioridad técnica procede de este documento.
