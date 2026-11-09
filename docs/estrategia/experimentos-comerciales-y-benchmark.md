# DELIA — Programa experimental para demostrar valor frente a competidores

**Versión:** 09-11-2026. **NO realizado aún:** benchmarking de competidores, pilotos empresariales, encuestas de precio y resultados económicos. Esta es una metodología, no un informe de resultados.

## Hipótesis central refutable

Una empresa que integra agentes en ecommerce o CRM puede reducir tiempo y riesgo de adopción mediante **contratos de operación versionados + verificación de resultado + evidencias reproducibles**, sin sustituir su gateway, mediante un paquete especializado para integradores.

Si esa combinación no reduce costo total o riesgo operativo medible frente al stack existente, **no existe razón suficiente para comprar DELIA** y se debe pivotar a un SDK/componente o usar alternativas.

## Tres ofertas a testear sin vender como disponibles

- **Evaluation Lab:** workshop técnico con datos sintéticos, inventario de acciones, prueba de contrato e informe; no intervención productiva.
- **Partner Pilot:** configuración de un flujo e integración bajo sandbox autorizado, un cliente de diseño y medición de costo/tiempo; solo tras S1/S2.
- **Outcome Assurance Subscription:** contrato anual/mes por organización/operación verificada y soporte, solo cuando exista S3/S4 y capacidad operativa.

No prometer certificaciones, seguridad cero fuga ni ROI garantizado.

## Matriz de compra por alternativa

| Alternativa instalada | ¿Qué ya resuelve? | Prueba de valor incremental DELIA |
|---|---|---|
| Helio | Llamadas MCP, aprobaciones, presupuestos y prerequisites según README | Contrato sectorial versionado y comparación de resultado del sistema autoritativo |
| AgentTrustOps | Side-effects, idempotencia y reconciliación según README | Configuración regional/multi-tenant/integrador, experiencia y coste medidos; si no mejora, integrar |
| Temporal | Durable workflows, aprobaciones y sagas | Crear política y pruebas de negocio sin mantener otra engine durable |
| Agentgateway + Cerbos/OPA | Gateway multi-protocolo y autorización fina | Mejor empaquetado de reglas y evidencia de resultados por sector, sin sustituir gateway |
| Microsoft/Google/Palo Alto | Gestión de identidad, seguridad y observabilidad extensa | Tiempo/costo de integración y especialización de proceso, no amplitud de funciones |
| Presidio/Cloudflare DLP | Detección/protección de datos | Comparar recall, false positives y operaciones protegidas en dataset independiente CL/MX/CO/BR |

## Protocolo técnico de comparación reproducible

1. Elegir mismo flujo (refund/CRM), mismas entradas sintéticas, amenazas y condiciones de salida.
2. Congelar versiones/commits de las herramientas y sus licencias.
3. Medir tiempo real de instalación, líneas de configuración (solo informativo), pasos manuales, costo infra y latencia.
4. Ejecutar al menos 10 casos negativos: cliente no autorizado, exceso de saldo, operación repetida, aprobación vencida, estado desconocido, retorno divergente, error HTTP, bypass de adapter, payload inesperado y caída del proceso.
5. Guardar logs redacted, artefacto de test, outputs y hashes. No inferir capacidad de producción a partir de una demo.
6. Medir cuántos escenarios cada solución **realmente cubre** y cuáles requieren un componente externo, sin penalizar por diseño si la integración es válida.
7. Proponer valor con base en tiempo/costo + requisitos; un resultado favorable sin revisor independiente queda preliminar.

## Metodología de precio

**Entrevista inicial:** problema, incidente o casi-incidente, solución actual, frecuencia, costo actual, usuario responsable, presupuesto, alternativa.
**Prueba de voluntad de pago:** cotización exploratoria de paquete concreto con alcance/exclusiones; documentar aceptación/rechazo y objeciones.
**Modelo de contribución:** suscripción fija + uso medido, menos nube, soporte, comisiones, revisión de seguridad y costo de conectores. Diferenciar facturación prometida, cobrada y recurrente real.

## Funnel y criterios de abandono

- 10 compradores entrevistados como meta inicial, de los cuales 5 ejecuten un flujo relevante.
- 3 compradores capaces de describir brecha no resuelta por stack actual.
- 2 integradores dispuestos a instalar demo offline y medir tiempos.
- 1 piloto contratado, **solo** tras aprobación S3.
- Si después de 15 entrevistas no hay un dolor repetido ni intención de presupuesto, pivotar a detector regional, pack de contratos sobre gateway existente o herramientas internas de MasterTech.

Los números son **criterios sugeridos de investigación**, no clientes entrevistados o ventas realizadas.

## Modelo ilustrativo de ROI, no forecast

Un partner integra 5 clientes; controles manuales requieren 6 h/cliente/mes a 30 USD/h = 900 USD/mes. Si un producto validado redujera a 2 h/cliente/mes, valor bruto de tiempo ~600 USD/mes antes de licencia, infra, revisión, falsos positivos y soporte. Si el costo DELIA excede el valor total y no hay reducción de incidentes demostrada, no existe ROI positivo de ese componente.

## Fechas propuestas

- **20/11/2026:** conjunto de casos y criterios de evaluación congelados.
- **04/12/2026:** 5 entrevistas técnicas registradas en CRM privado.
- **18/12/2026:** test funcional E2E en entorno sintético y evidencia de unknown result.
- **08/01/2027:** dos instalaciones ajenas al equipo y TCO comparativo.
- **15/01/2027:** gate de beta; no automatizar sistemas reales si hay P0.
- **31/03/2027:** decisión comercial seguir/pivotar con evidencias y pricing.

## Medidas de éxito

No solo tests verdes: **verified automation rate**, tasa unknown, operaciones duplicadas, porcentaje de cobertura de controles reales, costo por proceso confirmado, latencia p95 y errores de permisos; registrar baseline antes de cambios. Reportar confianza y tamaño de muestra. Beneficios de regulación o multas evitadas no son ingresos ni ahorros garantizados.

## Fuentes y confidencialidad

Fuentes técnicas en `investigacion-global-2026-11-09.md`. No subir entrevistas identificables, cuentas, contratos, capturas privadas ni documentos de clientes a GitHub público. Aprobación explícita antes de ejecutar tests en terceros.
