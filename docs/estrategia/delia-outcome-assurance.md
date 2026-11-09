# DELIA Outcome Assurance — Propuesta de valor de próxima generación

> **Red team 09/11/2026:** Pruvz (https://pruvz.ai/), ACPT (https://www.acpt.cloud/), NIA (https://nia.sg/harness/) y AgentTrustOps ya describen verificación de efectos, políticas y evidencia, en niveles de madurez distintos. La combinación **no prueba exclusividad** de DELIA Outcome Assurance. Evaluar [ContractOps para integradoras](../competitive-assurance/README.md) como hipótesis de procesos portables/comparables, sin prometer integraciones o verificaciones productivas. Ver [22 competidores](red-team-competitivo-2026-11-09.md).


**Versión:** 09-11-2026. **Estado:** propuesta de producto + motor **local de laboratorio** en `experiments/contract_assurance/`; ni el gateway, ni el SDK ni la conciliación real con un proveedor están implementados. En `main` este módulo experimental NO puede interceptar aplicaciones reales ni realizar transacciones.

## Nombre y tesis

**DELIA** conserva su nombre histórico. La familia comercial propuesta se llama **DELIA Outcome Assurance** (evaluar marca/registro antes de comercializar).

**Propuesta:** «Antes de ejecutar, DELIA verifica si la operación es admisible; después, exige evidencia de lo que realmente ocurrió y detecta diferencias que requieren intervención».

Cliente de entrada: integradora B2B que despliega agentes de atención/ecommerce o SaaS con procesos de reembolso, cambios en cuentas y acciones sensibles.

El mayor beneficio económico potencial no es bloquear más prompts: es **reducir incertidumbre operacional y facilitar automatización gradual sin entregar autonomía sin límites**. La magnitud de ese beneficio debe medirse.

## Los seis pasos de un contrato operacional

1. **Intención:** propuesta `operation_id`, tenant, herramienta, argumentos validados y origen autenticado.
2. **Precondiciones:** factura/pedido existe, saldo, versión de datos, usuario validado, límites específicos, permisos y finalidad.
3. **Autorización:** autorización real que pueda imponerse al punto de ejecución, privilegios temporales y aprobaciones para alto impacto.
4. **Ejecución:** herramienta única con idempotencia, timeout, retry seguro y registro de estado `pending/committed/failed/unknown`.
5. **Reconciliación:** evidencia de fuente autoritativa (API/ERP/pagos, no texto inventado por LLM), comparación de importe/identificadores/estado, acción de compensación cuando corresponda.
6. **Evidencia y métricas:** informe mínimo sin PII cruda, versión de contrato/política, SHA, responsable, decisión, estado, latencia y costo total, con retención/configuración.

Una operación solo es **verificada** cuando se obtiene evidencia del sistema de registro con identidad y autenticidad apropiadas. El laboratorio actual únicamente compara objetos sintéticos y expresa `VERIFIED_SIMULATED`.

## Diferencia frente a productos ya existentes

**Helio** ofrece reglas, aprobaciones, prerequisitos, presupuesto y auditoría. **AgentTrustOps** aborda idempotencia y reconciliación. **Temporal** ofrece durabilidad y patrones saga. **Cerbos/OPA** ya resuelven políticas granulares. Por tanto, la innovación propuesta es una **experiencia de producto empaquetada**, no la propiedad exclusiva de esos algoritmos: configuración por proceso, contexto LATAM, control de resultados, pruebas incluidas, dashboard de valor y canal partner.

## Modelo de producto

- **DELIA Outcome Contracts:** catálogo JSON/schema de invariantes específicos y pruebas positivas/negativas.
- **DELIA Assurance SDK:** adaptador que valida contratos y exige un punto de enforcement real; no está disponible.
- **DELIA Outcome Ledger:** reconciliación con fuente verificada y evidencia duradera, con ciclo de errores/unknowns; no está disponible.
- **DELIA Proof Pack:** evidencia exportable con firma, versiones, test y retención; no está disponible.
- **DELIA Partner Assurance:** distintos clientes aislados, panel de salud de workflows y métricas económicas por contrato; no está disponible.
- **DELIA Regional Packs:** traducciones de reglas y normativa por país revisada por especialista; no está disponible.

## Demostrador en main

```bash
python -m unittest tests.test_outcome_contracts -v
python -m experiments.contract_assurance.demo
```
Ejemplo ficticio de reembolso MXN: revisar identidad declarada de tenant/pedido, monto pagado/saldo, verificación de cliente, versión de snapshot y duplicidad de `operation_id`. Devuelve `ELIGIBLE_FOR_AUTHORIZATION` **nunca `ALLOW`**, porque no se autentica al principal. Se compara un `SettlementObservation` ficticio para emitir `VERIFIED_SIMULATED/HOLD/REJECTED/MISMATCH`.

No hay banco, Stripe, transacción, PII, conexión externa, auditoría durable, identidad autenticada ni locks. **No probar con dinero ni datos de clientes**.

## Primer contrato sectorial: ecommerce

| Invariante | Caso negativo | Resultado esperado |
|---|---|---|
| Tenant y pedido coinciden | Tenant B sobre pedido A | DENY |
| Versión de snapshot igual | Lectura desactualizada | DENY |
| Moneda igual | Cambio MXN a CLP | DENY |
| Tope contractual | Monto excesivo | DENY |
| Pedido pagado | Pedido cancelado | DENY |
| Cliente verificado | Verificación ausente | DENY |
| Operación no repetida | operation_id ya registrado | DENY |
| Saldo suficiente | Reembolso excede saldo | DENY |
| Resultado desconocido | timeout/pending | HOLD, no asumir éxito |
| Importe confirmado igual | Confirmación divergente | MISMATCH |

**Cuidado:** pruebas de estado son snapshots ficticios. En producción la verificación requiere sistema transaccional con control de concurrencia e idempotencia permanente.

## Segundo contrato a investigar: BPO/CRM

Antes de modificar una cuenta: actor autenticado, finalidad, estado del ticket, aprobación del cliente según política, cambios permitidos, versión del registro y operación única. Luego releer el CRM autoritativo, comparar campos y generar evidencia/redacción. La ausencia de confirmación debe producir HOLD/REVIEW, no «finalizado».

## Métricas de impacto que permitirían precio premium

1. **Verified automation rate:** operaciones con resultados contrastados / operaciones elegibles, nunca confundir autorización con éxito.
2. **Unknown outcome rate:** operaciones con estado no confirmable / solicitudes de ejecución.
3. **Duplicate side-effect rate:** operaciones duplicadas observadas / acciones comprometidas (meta cero en el conjunto probado).
4. **Safe automation coverage:** % de flujos operativos instrumentados con contrato, identidad, enforcement y reconciliación; medir denominador auditado.
5. **Time-to-safe-deployment:** horas desde integración hasta 100 % de gates de ensayo; comparar con solución actual del comprador.
6. **Total cost per verified workflow:** costos Cloud, LLM, tools, revisión humana, fallos y soporte / operaciones verificadas.
7. **False blocks:** operaciones legítimas retenidas por DELIA / intentos legítimos del corpus.
8. **Unresolved reconciliation age:** tiempo de HOLD hasta resolución confirmada.
9. **Business net value:** gasto/incidentes observados con solución actual menos costo total de operar DELIA; no atribuir beneficios sin contrafactual.

## Propuesta comercial y pricing a INVESTIGAR

**Partner Platform:** tarifa base más tenants activos; **Verified Workflows:** volumen de operaciones verificadas e integración para packs sectoriales; **Assurance Services:** setup, pruebas y mantenimiento.

Si se cobra por operación confirmada, evitar incentivos a reportar falsos éxitos. Para flujos sensibles usar cobro mixto transparente por plataforma/uso y no volumen «exitoso» inventado. Precio condicionado a p95, tasa de reconciliación, margen y soporte reales.

## Por qué puede ganar, pero aún no gana

Valor potencial: un partner instala reglas de negocio y pruebas por cliente, gestiona evidencia de resultado y compara el costo de automatización protegida. Costos: adaptación de ERP/CRM, identidad, auditoría, reconciliación, soporte, leyes y cada país. Defensibilidad surge de contratos probados por sector, conectores confiables y distribución, no de un acrónimo nuevo.

**Condición de continuación:** 5 entrevistas con compradores de flujos de ecommerce/BPO, un benchmark pareado con al menos una alternativa existente, un ensayo E2E con fuente simulada que detecte resultados desconocidos y una oportunidad de piloto contractual. Si no existe valor incremental, pivotar a complemento de Helio, Temporal, Agentgateway u otra infraestructura.
