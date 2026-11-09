# DELIA — Modelos de ingresos, precios, costos y economía unitaria

**Corte:** 2026-11-09. Todos los precios e ingresos son hipótesis exploratorias, **NO tarifas publicadas, ventas, clientes, previsiones ni valoraciones de MasterTech**.

## Diez vías de ingresos compatibles

| Código | Vía | Unidad económica | Condición de lanzamiento |
|---|---|---|---|
| R1 | DELIA Cloud SaaS | Organización/mes y volumen de decisiones | Auth, tenant, DLP, SRE, privacidad y soporte |
| R2 | DELIA Partner y OEM | Partner/mes, tenants activos, uso | Aislamiento real y acuerdos de canal |
| R3 | DELIA Enterprise privado | Licencia anual + mantenimiento y puesta en marcha | Despliegue reproducible, QA y revisión contractual |
| R4 | API de políticas | Por 1.000 decisiones o llamadas protegidas | Facturación medible, cuotas e idempotencia |
| R5 | Packs especializados | Complemento por vertical o conector | Pruebas por sector y mantenimiento |
| R6 | Ingeniería e integración | Alcance cotizado por proyecto | Equipo disponible, seguridad y handoff |
| R7 | Soporte gestionado | Retainer o SLA acordado | Capacidad real de respuesta |
| R8 | DELIA Academy | Cursos y talleres B2B | Contenido y evaluación; sin «certificación oficial» ficticia |
| R9 | DELIA Verify-as-a-Service | Evaluación recurrente con evidencias | Metodología reproducible, sin fingir auditoría acreditada |
| R10 | Ecosistema Marketplace | Comisión por paquete firmado | Base instalada, licencias y revisión supply-chain |

**Secuencia recomendada:** R6 + R1/R2 primero; R3/R4/R5 cuando existan pruebas e integraciones reales; R8 complementario; R9 condicionado a credibilidad; R10 como efecto de red, no en enero.

## Tarifas de laboratorio para entrevistas (USD)

| Edición | Precio mensual hipotético | Alcance que se investigaría | Estado |
|---|---:|---|---|
| Developer Lab | Gratis | CLI/documentación/demo offline | Diseño |
| Cloud Starter | US$199 | 1 organización, políticas básicas | No disponible |
| Cloud Growth | US$499 | Varios agentes, reportes y aprobaciones | No disponible |
| Partner | US$1.499 | Varias organizaciones, controles y SDK | No disponible |
| Enterprise Dedicated | US$3.999 equivalente mensual | Instalación dedicada, SSO y soporte pactado | No disponible |

Costos de proveedores LLM externos, impuestos, setup, almacenamiento y exceso de uso deben cotizarse por separado. Los precios podrían variar sustancialmente tras entrevistas.

## Modelo de unit economics

MRR neto = suma de cuentas pagadoras activas multiplicadas por su tarifa recurrente neta.
ARR anualizado = MRR neto × 12. No es ingreso reconocido anticipadamente.
Margen bruto = (Ingresos − costo de infraestructura y entrega atribuible) / Ingresos.
Contribución = Ingresos − COGS − comisiones variables − costos variables de soporte.
CAC = gasto de adquisición atribuible / nuevos clientes. Payback CAC = CAC / (ingreso mensual medio por cliente × margen bruto), cuando corresponda.
NRR = (MRR inicial + expansión − contracción − churn) / MRR inicial de cohorte.

## Escenarios aritméticos que NO son pronósticos

| Escenario de práctica | Starter ×199 | Growth ×499 | Partner ×1499 | Enterprise ×3999 | MRR USD |
|---|---:|---:|---:|---:|---:|
| Exploración | 8 | 2 | 0 | 0 | 2.590 |
| Base hipotética | 0 | 20 | 5 | 0 | 17.475 |
| Expansión extremadamente exigente | 0 | 40 | 20 | 5 | 69.935 |

El último equivale a US$839.220 de run-rate anualizado hipotético: **no es una previsión**, y supondría ventas internacionales, capital, operación y seguridad aún inexistentes.

### Sensibilidad de punto de equilibrio
Supuestos de ejercicio: costos fijos mensuales US$8.000; precio neto medio US$499; margen de contribución 75 %. Se necesitan al menos 22 cuentas equivalentes para cubrir **solo** esos costos fijos supuestos. Si el margen disminuye al 50 %, se necesitan al menos 33. Excluye impuestos, deuda, capital, costos no incluidos y adquisición incremental.

## Experimentos para validar precio

1. Veinte entrevistas enfocadas en costo del problema y solución actual.
2. Cinco comparaciones de costo total frente a tool stack existente.
3. Tres demos sintéticas por sector y medición de tiempo de integración.
4. Tres propuestas técnicas/económicas condicionadas, sin obligación de compra.
5. Primer piloto de pago únicamente tras gate de seguridad y contrato.
6. Revisar precio, uso y margen con datos reales; descartar producto sin beneficio incremental.

## Riesgos de escalamiento y caja

La venta enterprise puede demorar meses; la infraestructura cloud y el soporte 24/7 consumen recursos; las cuotas de modelos externos pueden erosionar margen; falsos positivos y fuga de datos crean costos reputacionales/jurídicos. Nunca suponer que los trabajos freelance del fundador son ingresos de MasterTech SpA. Evitar explorar 18 verticales a la vez antes de tener un segmento rentable.

## Medición mensual
MRR cobrado, ARR anualizado, churn, margen bruto/contribución, CAC y periodo de recuperación, concentración de clientes, consumo por tenant, p95, falsas alarmas, horas de soporte, tasa de integración exitosa, reservas de incidente y runway.

**Toda evaluación de financiación debe usar ingresos efectivamente observados, derechos de propiedad intelectual y contratos, no estas simulaciones.**
