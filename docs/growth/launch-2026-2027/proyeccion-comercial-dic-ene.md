# DELIA — Proyección de ventas dic 2026–ene 2027 (CLP, escenario y no forecast)

**Corte:** 09/11/2026. **Estado:** escenarios hipotéticos del programa de captación. No hay ventas, contratos, reuniones, cobros, MRR, campañas de pago activas ni conversión histórica comprobadas mediante este documento.

## Precio exploratorio de dos entregables

**A. DELIA Workflow Readiness Lab (diagnóstico): CLP $290.000 netos de IVA.** Diagnóstico profesional de un proceso sin acceso a producción: mapa de flujo, amenazas, contrato sintético, alternativas (incluida la recomendación de no usar DELIA) e informe. Precio de **experimento comercial**, no tarifa oficial ni obligación de entrega sin contrato.

**B. DELIA Sandbox Assurance Lab: CLP $790.000 netos de IVA.** Proyecto técnico de mayor alcance en laboratorio ficticio, si existe capacidad y condiciones contractuales. Debe cotizarse horas de ingeniería, QA, soporte y permisos. **No** garantiza seguridad, no opera pagos/CRM reales ni entrega certificación.

Los valores se eligieron para probar sensibilidad de compra y costos, **no porque el mercado haya confirmado disposición a pago**. Como orientación, una consultora chilena publica diagnóstico desde CLP $400k–800k, pero su alcance no es directamente equiparable: https://cercai.cl/precios-implementacion-ia-chile-2026/ . El costo de MasterTech debe revisarse independientemente.

## Embudo y proyección

| Escenario | Mes | Cuentas investigadas/contactos pertinentes (meta) | Reuniones (meta) | Propuestas (meta) | Diagnósticos vendidos (hipótesis) | Labs vendidos (hipótesis) | Ingreso (CLP) |
|---|---|---:|---:|---:|---:|---:|---:|
| Conservador | Dic 2026 | 20 | 3 | 1 | 0 | 0 | **$0** |
| Conservador | Ene 2027 | 35 | 6 | 2 | 1 | 0 | **$290.000** |
| Base | Dic 2026 | 45 | 8 | 3 | 1 | 0 | **$290.000** |
| Base | Ene 2027 | 70 | 14 | 6 | 2 | 1 | **$1.370.000** |
| Expansión | Dic 2026 | 70 | 15 | 7 | 2 | 0 | **$580.000** |
| Expansión | Ene 2027 | 110 | 24 | 11 | 4 | 2 | **$2.740.000** |

**En todos los escenarios:** enero incluye solo laboratorios derivados de diagnósticos anteriores si se realiza una contratación separada, nunca sobre la base de una promesa de software. Los contratos y cobros deben comprobarse.

## Escenario acumulado (dic–ene)

| Escenario | Ingresos netos de IVA | Costos directos hipotéticos | Marketing y contenidos | Contribución después de esos costos |
|---|---:|---:|---:|---:|
| Conservador | **$290.000** | $101.500 | $60.000 | **$128.500** |
| Base | **$1.660.000** | $699.500 | $100.000 | **$860.500** |
| Expansión | **$3.320.000** | $1.399.000 | $200.000 | **$1.721.000** |

**Cálculos:** 
- Ingreso mes = diagnósticos × 290.000 + labs × 790.000.
- Costos directos (NO auditados) = 35% ingresos diagnóstico + 50% ingresos lab.
- Contribución = ingresos – costos directos – gasto de marketing.
- **No es utilidad neta ni flujo de caja:** excluye salarios fijos, overhead, desarrollo de software, infraestructura general, impuestos, IVA, créditos, gastos financieros y cobros pendientes.
- Gasto de marketing NO es presupuesto de campañas pagadas ya ejecutadas. En noviembre se recomienda $0 pauta; diciembre y enero pueden ser contenido/herramientas.

## Qué significa cada escenario

**Conservador:** noviembre no produce interés suficiente para cierres en diciembre; una sola venta de diagnóstico posible en enero. Si el presupuesto real no llega, ingresos cero es perfectamente posible.

**Base:** al 31/12 se habría contratado un diagnóstico, y durante enero otros dos y un laboratorio con un cliente que aceptó evaluar bajo datos ficticios. Aún no hay facturación recurrente.

**Expansión:** exige capacidad comercial y técnica alta, múltiples aprobaciones presupuestarias, y dos laboratorios posteriores a diagnósticos de diciembre. No financiar nómina, deuda ni infraestructura sobre esta cifra.

## Metas de verificación de negocio

- **20/11:** al menos una conversación con comprador y problema identificados, o registrar que no se consiguió; sin inventar.
- **30/11:** revisar pipeline real: reunión, responsable de presupuesto, siguiente paso y costo de entrega.
- **15/12:** primera propuesta cotizada por escrito, si hay necesidad demostrada.
- **31/12:** reportar ofertas reales, ventas cobradas, servicios entregados y margen medido; no sustituir por proyección.
- **15/01:** si P0 crítico abierto, mantener solo diagnóstico/servicios de alcance seguro.
- **31/01:** comparar escenario vs cobros reales, razones de rechazo, enero de vacaciones y planes para febrero.

## Triggers de ajuste

- 0 reuniones en 15 contactos pertinentes → revisar ICP/mensaje antes de aumentar volumen.
- 3 reuniones sin dolor frecuente → cambiar problema/cliente, no fabricar software.
- Comprador interesado pero sin capacidad de pagar → buscar segmento con presupuesto, no ofrecer alcance indefinido gratis.
- Contrato supera capacidad de delivery → limitar trabajos o reprogramar; no cobrar servicio imposible.
- Costos directos observados superiores a porcentajes supuestos → ajustar precios o abandonar oferta.
- Si el contrato/piloto exige datos reales, PII o efectos externos con P0 abierto → no proceder.

## Fuentes y archivo de cálculo

[Modelo JSON editable](forecast-scenarios.json) y su [validador Python](../../../tools/forecast_delia_launch.py) reproducen cantidades y bloquean afirmar MRR sin respaldo. La hoja de cálculo Excel entregada en la conversación incorpora fórmulas y permite ajustar supuestos.

**No atribuir estos números a un estudio sectorial ni tratar escenario Base como probabilidad.** 
