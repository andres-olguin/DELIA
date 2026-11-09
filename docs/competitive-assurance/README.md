# DELIA — Competitive Assurance Lab / ContractOps Hypothesis

**Fecha:** 09/11/2026. **Estado:** investigación comercial y demostración de **contratos ficticios entre simulaciones de dos gateways**. No contiene adaptadores de Helio/OPA/Cerbos reales, ni autoriza una acción externa, ni verifica un CRM o resultado financiero. **NO se debe vender como control empresarial de producción.**

## Oportunidad

Los competidores directos Pruvz, ACPT, AgentTrustOps, Helio, NIA, Preloop, Beyryl y AIRA cubren buena parte de Outcome Assurance, gobierno, evidencia y canal integrador. DELIA debe comprobar una tesis más estrecha: **testear las reglas de un proceso de negocio igual en diferentes stacks y tenants, junto con la economía de instalación y operación**.

El comprador de hoy tiene sus propias políticas en CRM/gateway. La hipótesis de DELIA es dar un **contrato de proceso portátil, fixtures y evidencia de diferencias** que reduzcan la fricción de migración, evaluación y mantenimiento sin imponer otro ejecutor.

## Entregables de laboratorio (simulación)

- Archivo `contracts/ticketing_v1.json`: contrato de casos sintéticos con allow/deny/review y tenants.
- `compat_lab.py`: compara decisiones **declaradas por mocks** de dos adaptadores con el contrato; emite `MATCH`, `CONTRACT_VIOLATION`, `INDETERMINATE`; lo desconocido nunca cuenta como aprobado.
- `demo.py`: ejemplo local con un mock que incumple una regla de exportación y otro que no entrega evidencia suficiente.
- `tests/test_contract_compat_lab.py`: tests negativos de cross-tenant, falta de observación, conflicto, deriva de políticas y ausencia de falsos éxitos.

No se interceptan herramientas. No se prueba el comportamiento de un gateway real, ni existe evidencia de compatibilidad con los nombres de proveedores en el estudio. Si un proveedor no puede expresarlo/ejecutarlo, se debe reportar incompatibilidad, no simular soporte.

## Para que pueda diferenciar realmente a DELIA

1. **Implementar adaptadores con autorización y consentimiento** sobre dos herramientas reales —por ejemplo, Helio y Cerbos/OPA— y congelar versiones.
2. Probar que un `deny` produce **cero efectos de herramienta**, no solo una respuesta de bloqueo declarada.
3. Comprobar que actor/tenant se autentican fuera del payload del agente.
4. Comparar 10+ escenarios negativos y un conjunto de casos legítimos; reportar falsos bloques.
5. Medir tiempo de implementar cliente 1 y cliente 2 con y sin ContractOps, incluyendo soporte y costos.
6. Añadir verificación independiente de resultado contra sandbox CRM, sin estados falsamente `VERIFIED`.
7. Demostrar que el cliente pagará o que un integrador contrata el alcance.

## Demo

```bash
python -m unittest tests.test_contract_compat_lab -v
python -m competitive_assurance.demo
```

Solo librería estándar de Python 3.11+ y datos ficticios. Los resultados tienen etiqueta de modo `MOCK_ONLY_NO_ENFORCEMENT`.

## Agenda falsable

| Fecha | Meta | Condición |
|---|---|---|
| **13/11/2026** | Matriz de 22 competidores publicada y revisada | Fuentes, claims y limitaciones |
| **20/11/2026** | Contrato CRM v0.1 y 10 fixtures de prueba acordados | Análisis de amenazas P0 |
| **04/12/2026** | Primer adaptador real en sandbox, si hay capacidad | Prueba de no ejecución al DENY |
| **18/12/2026** | Segundo stack adaptado + evidencia de divergencia | Reproducible y revisor |
| **08/01/2027** | Instalación por tercero y tiempo de segundo tenant | Costos observados |
| **15/01/2027** | Gate de beta avanzada; P0 tiene veto | No-Go si bypass |
| **31/03/2027** | Decisión comercial continuar/pivotar/pausar | Buyer evidence, precio y margen |

No usar estrellas de GitHub ni resultados de tests ficticios como indicador de adopción pagada.

## Propuesta de valor que debe ganar derecho de existir

**DELIA ContractOps for Integrators:** «Evalúa y mantiene reglas empresariales de agentes entre herramientas, clientes y proveedores con contratos de proceso comprobables y costos transparentes». Se validará solo si **resuelve mejor o más barato** el trabajo que los compradores ya hacen con componentes nativos y gateways existentes.

## Base técnica

OWASP Agent Control Standard ofrece hooks portables; NIST promueve interoperabilidad. Por tanto, DELIA no debe inventar un protocolo incompatible. [Análisis de 22 competidores](../estrategia/red-team-competitivo-2026-11-09.md) y [matriz estructurada](../estrategia/competidores-directos-2026-11-09.json).

## Límites de mercado

No hay evidencia en este documento de pilotos, compradores, contratos, ingresos, ROI, ahorro, cumplimiento automático de Ley 21.719 ni unicidad mundial. Chile tiene proyecto pendiente sobre fecha de vigencia de la Ley 21.719 al corte.
