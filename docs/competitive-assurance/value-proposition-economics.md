# DELIA ContractOps — Propuesta de valor y economía para el comprador

**Fecha:** 09/11/2026. **Estado comercial:** oferta de estudio / producto a validar, no servicio enterprise desplegado ni MRR demostrado.

## Propuesta que pondremos a prueba

**«Tu integradora ya tiene agentes y herramientas. DELIA busca reducir el trabajo de demostrar, cliente por cliente, que cada operación cumple reglas, se ejecuta dentro de permisos y produce el resultado esperado, sin obligarte a cambiar todo tu stack».**

**Comprador principal:** propietario/CTO de una integradora pequeña/mediana que implementa agentes en CRM/ticketing para múltiples empresas. **Usuario:** implementador de automatizaciones y auditor técnico. **Presupuesto:** horas de delivery, QA, soporte y go-live; se validará su origen en entrevistas.

## Tres dolores con evidencia requerida

1. **Control repetido:** cada segundo cliente obliga a rehacer reglas/policies y pruebas. Mostrar horas realmente trabajadas, no estimarlas por intuición.
2. **Resultado dudoso:** agentes marcan tarea «lista» aun cuando CRM/ERP responde con error o un estado no confirmado. Mostrar frecuencia y costo de revisión; no usar clientes reales sin permiso.
3. **Demostración comercial costosa:** un cliente nuevo pide revisar permisos, auditoría y retención. Mostrar tiempo de producir evidencia; no confundir logs con cumplimiento.

## Diferenciadores candidatos, ninguno exclusivo por sí solo

**A. Contrato de proceso antes de elegir gateway:** un archivo que define negocio y casos de prueba independientemente de Helio/Cerbos/agentgateway. **Diferencia esperada:** un mismo kit reutilizado por segundo tenant. OWASP ACS y estándares existentes deben respetarse; el formato no es «primero del mundo».

**B. Comparación de garantías entre stacks:** un runner que reporta diferencias y operaciones sin prueba. **Diferencia esperada:** decisiones `DENY/REVIEW/ALLOW` equivalentes, no «seguridad 100 %». Un green de mock no sirve como prueba real.

**C. Evidencia de resultado y no de intención:** proceso verificable de test, incluyendo acciones no ejecutadas y estados desconocidos. **Diferencia esperada:** menos incidentes sin resolver, comparado con procedimientos existentes. Pruvz/ACPT/AgentTrustOps ya implementan o investigan piezas similares.

**D. Productización para integradoras:** plantillas, onboarding, informes per-tenant, soporte definido, demostración transparente de costo total. **Diferencia esperada:** menos horas al segundo cliente, margen positivo para partner y para MasterTech. Beyryl/AIRA también ofrecen canal MSP; la diferencia depende de resultados.

**E. Contexto LATAM:** fixtures PII, particularidades de idioma y datos, políticas redactadas por país y revisión jurídica de vigencia. **Diferencia esperada:** cobertura útil, falso bloqueo medido y soporte local. No prometer conformidad normativa automática.

## Paquetes a presentar para descubrir voluntad de compra

| Paquete | Qué puede ofrecerse al principio | Unidades económicas | Precondición |
|---|---|---|---|
| **DELIA Workflow Readiness Lab** | Diagnóstico profesional de un proceso, alternativas, diagrama, reglas y pruebas ficticias | Proyecto con horas de equipo/costo total; precio solo por cotización | Capacidad real de consultoría, contrato, ninguna promesa de seguridad de software |
| **DELIA Contract Conformance Kit** | Futuro kit de política/test reproducible adaptado a dos stacks | Implantación por proceso + soporte de pruebas | Adaptadores reales probados y licencia/IP revisada |
| **DELIA Partner Assurance** | Futura suscripción per-tenant con gestión, evidencia y precio por uso/contrato | Base + tenants activos + medición clara | IAM, aislamiento, SLA, billing, seguridad P0, onboarding independiente |

**No vender los dos últimos como existentes.** Si el workshop revela que el cliente ya tiene todo solucionado, recomendar la alternativa y cerrar como no-fit.

## Simulación económica para conversación, NO forecast

Una integradora añade **tres clientes** y actualmente dedica **6 horas por cliente y mes** a QA/control manual, con costo interno imputado de **US$25/hora**: costo base **US$450/mes** (hipotético). Si tras implementar contratos/packs eso bajara a **3 horas por cliente**, trabajo evitado **US$225/mes** antes de costos DELIA.

Si suscripción, nube, revisión y soporte totaliza **US$250/mes**, el resultado de ese ejemplo es **-US$25/mes**. **No conviene comprar DELIA por ahorro de horas en ese caso** salvo que exista otro beneficio medido y suficiente.

Si el partner opera **diez clientes** con el mismo ahorro de 3 h × US$25 = **US$750/mes**, y el costo total de DELIA e implantación amortizada fueran US$300/mes, valor neto modelado sería **US$450/mes**, todavía antes de impuestos, adquisición e incidentes. La rentabilidad de DELIA para MasterTech se calcula por separado descontando COGS, soporte, comisiones y entrega. **Las dos cifras son puramente aritméticas**.

**Conclusión económica:** el canal puede ganar escala, pero no necesariamente margen. El valor depende del volumen de clientes, tamaño del problema y soporte. Nunca afirmar «ahorra X %» por este ejemplo.

## Modelo de precio a descubrir

- **Discovery:** pedir frecuencia de operación, incidentes, horas de QA, dueño del presupuesto y stack actual.
- **Van Westendorp adaptado / comparación de precios concretos:** presentar rangos exploratorios a personas con compra real y escuchar rechazos, sin afirmar precio oficial.
- **Prueba de oferta:** una cotización específica para un workshop; registrar si aprueban presupuesto, piden cambios o lo rechazan.
- **Expansión:** después de dos instalaciones y evidencia de retención, probar fee por tenant + contrato y service wrap.
- **Seguridad:** compradores con datos reales no desbloquean P0 por firmar contrato comercial.

## ¿En qué nos ganaría cada rival?

- **Pruvz:** verificación de resultado y pruebas criptográficas frente a nuestro laboratorio actual.
- **ACPT:** foco explícito en auditoría de resultados y procesos empresariales.
- **AgentTrustOps:** commit transaccional, idempotencia y reconcilación.
- **Helio:** setup rápido y proxy MCP con aprobaciones, presupuesto y servicios.
- **Beyryl/AIRA:** multiempresa y white label para MSP.
- **ServiceNow/Microsoft:** integración institucional con plataformas empresariales existentes.

**DELIA solo puede ganar mediante especialización y verificación.** Si el comprador ya dispone de una solución mejor y más barata, lo correcto es interoperar, integrarse o no vender.

## Diseño del primer estudio pareado

**Flujo:** ticket CRM sintético con lectura permitida, actualización bajo revisión, exportación denegada, tenant distinto y fallo `unknown`.

**Tratamientos:**
1. Stack actual del comprador sin DELIA.
2. Helio o Cerbos/OPA configurados según su documentación.
3. ContractOps real adaptado al stack correspondiente (cuando se construya).
4. Una alternativa de verificación de resultado Pruvz o AgentTrustOps si puede instalarse en condiciones comparables.

**Medir:** total horas de configuración para cliente 1 y 2, casos negativos que ejecutaron efecto (objetivo cero en el conjunto), falsos bloqueos, costo de mantener políticas, p95 de decisión bajo carga definida, calidad de evidencia y soporte humano. Datos ficticios y autorización expresa. Versiones/CI/entorno publicados con límites.

## Pruebas de falsación

- **20/11/2026:** definir contrato y registrar hipótesis con compradores reales.
- **18/12/2026:** comparar dos stacks instrumentados si alcanzamos un adapter y permisos; en caso contrario marcar `NOT_EXECUTED`.
- **08/01/2027:** dos integradores externos instalan y documentan tiempos.
- **31/03/2027:** si no hay comprador con presupuesto, ventaja probada o margen razonable, pivotar a SDK/consultoría o detener expansión.

## Respuesta sugerida al prospecto

«No te pediría que cambies el gateway. Primero queremos comprobar qué haces hoy para que un agente no ejecute operaciones indebidas, si tus políticas cambian entre clientes y cómo verificas los resultados. Estamos preparando contratos y pruebas reutilizables para ese trabajo. Si con tu stack actual ya es fácil, te lo diríamos; si encontramos una brecha, propondríamos una evaluación acotada con datos ficticios. DELIA todavía está en desarrollo y no lo estamos vendiendo como control de producción».

**Este texto no acredita una ventaja económica ni técnica hasta que las pruebas y compras se documenten.**