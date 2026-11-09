# 01 — Beachhead: un comprador estrecho antes de conquistar el mercado

## Tesis comercial 2026

No vender «ciberseguridad para cualquier IA». Vender **puesta en marcha y control verificable de un flujo limitado** a empresas que **ya** despliegan agentes con CRM/ticketing y sufren integración de políticas, clientes o revisión humana.

### ICP primario durante 60 días

**Empresa:** integradora/MSP/consultora técnica B2B en Chile o México; preferentemente 5–40 personas y al menos dos clientes de automatización/IA con acceso a sistemas empresariales. Estos rangos son filtros experimentales, no tamaño de mercado comprobado. **Comprador económico:** founder/CTO o director de delivery con capacidad de contratar proyectos. **Champion:** arquitecto de agentes o líder de integración. **Usuario:** developer/operations que configura permisos y prueba errores.

**Disparador verificable:** segundo cliente empresarial pide reglas de seguridad, auditoría o revisión de tool-calls, mientras el equipo reescribe controles para cada proyecto. **Dolor económico a medir:** horas de integración, regresiones, fallos de permisos, soporte, proyectos retrasados y esfuerzo de demo/compliance.

**Herramientas existentes aceptadas:** LangChain/LangGraph, n8n, Make, CRM, help desk, MCP y gateway que ya usan; DELIA debe ofrecer interoperabilidad. No afirmar soporte para todas hasta probarlo.

**No-fit inmediato:** empresa que no usa agentes conectados a sistemas, empresa sin responsable de compra, compañía cuyo stack resuelve plenamente el problema, solicitud de datos sensibles o producción insegura antes de cerrar P0, proveedor que requiere SLA/auditoría externa ya disponible.

### Subproblema inicial a resolver

**BPO/CRM low-risk:** un agente solo consulta, etiqueta y propone cambios en tickets **ficticios**. Con política, no debe exportar contactos, borrar clientes ni modificar montos. Una persona puede confirmar una operación de bajo riesgo bajo futura autenticación real. La primera demostración usa CRM simulado sin operaciones externas.

¿Por qué no reembolsos primero? El laboratorio de reembolsos enseña bien contratos empresariales, pero ejecutar dinero crea mayores obligaciones y posibles pérdidas. Mantenerlo como caso sintético hasta S3/S4, no como primer piloto.

## ICP secundario, no comercializar en paralelo sin recursos

**SaaS B2B con 2+ herramientas de agente** y comprador CTO; ideal si puede usar código de muestra y reportar fricción. **Operaciones ecommerce:** probar en entorno ficticio de pedidos, luego cambios reversibles. **BPO directo:** considerar solo si la integradora como canal no demuestra tracción.

## Mensajes para elegir entre enfoque seguridad y operaciones

**Frente al CISO:** «Permisos y evidencias de herramientas por proceso y tenant».
**Frente al COO:** «Reducir revisiones, errores de operación y tiempos de incorporación».
**Frente al CTO:** «Contratos por herramienta y resultado, con tests de bypass, compatibles con tu stack».
**Frente a finanzas:** «Un costo total por flujo validado y criterios de abandono si no mejora la solución actual».

Todos son claims **propuestos**. No decir que DELIA ya entrega ese resultado.

## Diferenciación frente a sustituir por herramienta existente

- **Helio:** ya ofrece aprobaciones, reglas y presupuestos MCP; si ese flujo basta, no vender DELIA.
- **Temporal:** ya aporta workflows durables, idempotencia y recuperación; usarlo si conviene.
- **Agentgateway/Cerbos/OPA:** ya resuelven transporte y autorización; DELIA como capa de contratos sectoriales interoperable.
- **Grandes cloud/security:** tienen seguridad y escala; DELIA debe demostrar menor tiempo de adaptación a un flujo específico de integradora regional.

**Hipótesis de beneficio incremental:** un paquete de política + invariantes de negocio + pruebas de resultado + guion de integración puede reducir tiempo de delivery por segundo cliente comparado con ensamblar componentes. No es ventaja demostrada; comparar horas y errores de verdad.

## El segmento debe ganarse el derecho a expandirse

Antes de abordar otra industria, exigir:
- Al menos 5 entrevistas profundas en el mismo ICP, hechas con permiso.
- Dos responsables que confirmen el mismo costo concreto con datos o artefactos.
- Un comprador que acepte analizar una propuesta técnica/económica específica.
- Dos instalaciones independientes del laboratorio con tiempo y errores registrados.
- Un caso de no-fit explícito donde se concluye que DELIA no agrega valor.
- Seguridad P0 cerrada antes de recomendar despliegue empresarial.

## Ranking heurístico, no probabilidad

`commercial_ops.decision_support` puntúa nueve dimensiones 0–4 (problema, frecuencia, costo documentado, acceso al comprador, presupuesto, urgencia, integración, brecha frente al competidor, capacidad de entrega). Un índice 75/100 solo significa que **vale la pena evaluar**; no equivale a 75 % de probabilidad de venta. La herramienta siempre deja `real_world_pilot_authorized=false`.

## Investigación y límites del mercado

Gartner (septiembre 2026) plantea especialización de agentes para ROI; McKinsey (agosto 2026) reporta que parte de las empresas construyen herramientas internamente; CORFO/CCS (septiembre 2026) observa en Chile brechas de ejecución/gobierno. Eso respalda **probar el ICP**, no demuestra TAM, demanda pagada, volumen de empresas ni cuota de mercado DELIA. Véase [fuentes](14-fuentes-y-supuestos.md).
