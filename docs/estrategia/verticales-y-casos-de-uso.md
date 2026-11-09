# DELIA — Sectores, paquetes verticales, comprador y problema verificable

**Fecha:** 2026-11-09. Son oportunidades de descubrimiento, **no clientes confirmados ni pilotos existentes**. «Control» significa objetivo futuro de ejecución segura; no atribuirlo al motor local sin adapter.

## Método de puntuación
Criterios cualitativos 1 (bajo)–5 (alto), definidos por juicio exploratorio y pendientes de entrevistas: **dolor probable**, **integrabilidad**, **presupuesto accesible**, **fricción regulatoria** (5=muy alta). Priorizar donde dolor, integración y presupuesto sean altos y fricción manejable. No convertir puntaje en probabilidad de compra.

| Sector | Comprador inicial | Problema operativo concreto | Pack / flujo de demostración | Modelo posible | Fase |
|---|---|---|---|---|---|
| 01. Integradoras de agentes/consultoras TI | CTO/CEO técnico | Repetición de políticas y permisos entre múltiples clientes | Partner Hub: políticas tenant y autorización de herramienta CRM | B2B2B licencias + uso + servicios | **A — prioridad 1** |
| 02. SaaS B2B / plataformas con agentes | CTO/Head of Engineering | Tool-calls no auditables, datos externos, fuga de permisos | API Guard + Evidence: lectura permitida, modificación denegada | SaaS API / licencia | **A — prioridad 2** |
| 03. Comercio electrónico y retail | Head of CX/Operaciones | Bots con reembolsos, descuentos, pedidos y datos de clientes | Commerce Pack: refund approval con límites, protección de identificadores | SaaS/managed integration | **A — prioridad 3** |
| 04. Contact centers/BPO | Director Operaciones/CISO | Agentes con CRM y transcripciones, muchas interacciones sensibles | Contact Center Pack: redactado previo y aprobación de acciones CRM | Pago por agente/solicitud + soporte | **A — prioridad 4** |
| 05. Logística y transporte | COO/CTO | IA altera rutas, pedidos, información de conductores y facturación | Logistics Pack: cambios en despacho que requieren autorización | SaaS por volumen/tenant | **B** |
| 06. RR. HH. / HRTech | CTO/Legal/People Ops | CV y nómina con PII, agentes con permisos excesivos | HR Pack: lectura anonimizada y bloqueo de cambios de nómina | Enterprise / API / despliegue privado | **B — regulado** |
| 07. LegalTech y estudios jurídicos | Socio/CTO/Compliance | Contratos confidenciales y resúmenes con IA | Legal Pack: minimización de identificadores, permisos por materia | Self-hosted / servicio | **B — sensible** |
| 08. Fintech y pagos | CISO/Arquitecto | Agentes con información financiera y acciones de pago | Finance Pack: preautorización y registro de operaciones sintéticas | Enterprise / integración | **B/C — alta exigencia** |
| 09. Seguros / InsurTech | CTO/Riesgos | Expedientes, siniestros, datos personales y cambios de estado | Claims Pack: revisión humana de cambio de siniestro | SaaS enterprise / dedicated | **B/C** |
| 10. Servicios contables y tributarios | CTO/gerente de producto | RUT/NIT/RFC y documentos fiscales enviados a IA | Tax Pack: clasificación, redacción, evidencia y retención | SaaS/región/sector | **B** |
| 11. Salud / HealthTech | CISO/Director clínico | Información sanitaria y agentes que consultan expedientes | Clinical Data Pack: datos sintéticos, minimización y control de acceso | Dedicated / contrato | **C — riesgo alto** |
| 12. Educación / EdTech | TI/Seguridad | Expedientes de estudiantes, sistemas académicos y tutores | Campus Pack: identificación y control de acceso académico | SaaS institucional | **B** |
| 13. Manufactura / industria / IoT | CIO/OT security | IA conectada a inventario u órdenes de mantenimiento | Industrial Pack: solo recomendaciones; autorización de cambios | Enterprise/edge | **C — OT** |
| 14. Energía / utilities | CIO/CISO | Agentes con lectura de cuentas y cambios de servicio | Utilities Pack: verificación de acciones, permisos y reportes | Enterprise/on-prem | **C** |
| 15. Bienes raíces/administración de edificios | Operaciones/proptech | Asistentes con contratos, residentes, cobros y tickets | Property Pack: acceso por edificio y aprobación de ajustes | SaaS partner | **B** |
| 16. Sector público / govtech | TI/Legal/Compras | Documentos personales, servicios ciudadanos y trazabilidad | Public Sector Pack: clasificación y evidencia bajo pliegos | Licencia/on-prem/tender | **C — procurement** |
| 17. Gaming / agentes de soporte | Director plataforma/seguridad | IA modifica cuentas, inventarios digitales o sanciones | Gaming Pack: control de permisos en moderación y economía virtual | API/volumen | **B** |
| 18. Medios y marketing automatizado | Agencia/Brand safety | Agentes publican contenido o gastan en campañas sin revisión | Marketing Pack: aprobación de publicación/presupuesto | SaaS Partner | **B** |

## Cuatro paquetes concretos para construir antes que otros

### A1. DELIA Partner for Integrators
**Buyer:** CTO o director de tecnología de empresa que ya desarrolla agentes. **User:** arquitecto, equipo de soporte/seguridad. **Job-to-be-done:** reutilizar reglas de seguridad al agregar un segundo cliente, sin mezclar información. **Flujo demo:** cliente A permite leer CRM y prohíbe borrar; cliente B aplica otra política; un intento de usar datos de B desde A debe fallar de manera demostrable. **KPIs:** tiempo de incorporación de cliente, errores de aislamiento, horas de mantenimiento, margen por proyecto. **Requisito P0:** identidad/tenant real, adapters seguros y auditoría.

### A2. DELIA Commerce Control
**Buyer:** operaciones ecommerce/CX. **Job:** permitir asistencia con reembolsos y promociones sin ejecuciones no autorizadas. **Demo:** agente solicita reembolso ficticio, política exige aprobación humana sobre umbral y evita reutilizar ticket. **KPIs:** acciones bloqueadas indebidamente, tiempo de aprobación, errores de reembolso, soporte. **No prometer integraciones Shopify/WooCommerce hasta hacerlas y probarlas**.

### A3. DELIA Contact Center Privacy
**Buyer:** director BPO/seguridad. **Job:** minimizar PII en prompts/transcripciones y controlar cambios en CRM. **Demo:** números sintéticos regionales y operaciones «ver consulta» vs «modificar cuenta». **KPIs:** falsos negativos, falsos positivos, latencia p95, tiempos de gestión, volumen de solicitudes. **Bloqueantes:** DLP antes de egress y políticas de tratamiento.

### A4. DELIA SaaS Agent API
**Buyer:** CTO del software con LLM conectado a sistemas. **Job:** aplicar una misma política a herramientas de varios frameworks. **Demo:** deny/approve en adaptadores de prueba, con evidencia de SHA y regresión. **KPIs:** tiempo de integración y coste por 1.000 decisiones, número de integraciones y fallos P0. **Bloqueantes:** SDK API, contratos estables y autenticación.

## Criterios de prioridad comercial
- **Fase A (noviembre–marzo):** 01, 02, 03 y 04. Experimentos con datos sintéticos; avanzar solo con comprador real y necesidad acreditada.
- **Fase B (abril–septiembre):** logística, HRTech, LegalTech, contabilidad, EdTech, PropTech, gaming y marketing, según pilotos y capacidades.
- **Fase C (octubre en adelante):** fintech altamente regulado, salud, industria OT, energía y sector público, con control de riesgo, revisiones externas y contratos específicos.

## Requisitos de investigación por sector
Para cada uno: 10 conversaciones de descubrimiento como meta de muestreo, un comprador responsable identificado, stack actual, política de datos, 3 tareas críticas, alternativa más cercana, evidencia de presupuesto y coste de implementación. No afirmar «hay demanda» porque el mercado use IA.

## Riesgos que cambian la prioridad
- Salud: no entregar recomendaciones clínicas autónomas ni tratar expedientes reales en laboratorios.
- Finanzas: ningún pago real sin controles internos, acuerdos y pruebas externas.
- RR. HH.: decisiones automatizadas sobre personas pueden estar sujetas a restricciones fuertes y riesgos de discriminación.
- OT/energía: un agente no debe ejecutar cambios sobre infraestructura crítica solo por un modelo.
- Gobierno: contratación, requisitos públicos y seguridad de datos pueden extender los plazos considerablemente.
