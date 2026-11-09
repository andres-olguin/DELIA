# DELIA — tesis económica, escenarios y disciplina de unidad económica

**Advertencia:** cifras ilustrativas en USD, **no precios validados, clientes, proyecciones ni valoración de MasterTech**. Objetivo: crear un negocio de software recurrente B2B2B con capacidad de expansión regional sin prometer ingresos desproporcionados.

## Segmentos compradores
1. Integradores de agentes de IA para empresas: usan una instancia de políticas por cliente; valor de distribución B2B2B.
2. SaaS B2B que conecta IA a CRM, pagos, RR.HH. o documentos: compra control operacional y evidencia; necesita APIs y SSO.
3. Seguridad corporativa/fintech regulada: altos requisitos de revisión, mayor presupuesto potencial y ciclo de venta largo; no mercado inicial sin seguridad auditada.
4. Equipo de desarrollo con gateway ya instalado: posible plugin/adapter DELIA como «control plane» especializado.

## Ofertas hipotéticas (requieren entrevistas antes de publicar precios)
| Paquete | Precio de exploración | Alcance esperado | Restricciones |
|---|---:|---|---|
| Sandbox Developer | gratis con límites | demo local, docs, fixtures y benchmarking | no SLA/uso productivo |
| Team | US$149/mes | una organización, políticas esenciales y métricas básicas | consumo y soporte definidos |
| Business | US$499/mes | varios agentes, aprobaciones, evidencia y tenant audit | límites explícitos y soporte pactado |
| Integrator | US$1.499/mes + uso | varios clientes aislados, API, marca de canal | acuerdo de procesamiento de datos y QA |
| Enterprise | cotización + setup | requisitos de residencia/SSO y seguridad contractual | solo tras gates productivos |

No vender código de fuente abierta que no tenga licencia comercial compatible sin revisión; separar costes de proveedor LLM pagados por el cliente. Un porcentaje de comisión del canal debe salir del margen real.

## Tres escenarios de facturación mensual (aritmética ilustrativa)
- Bajo: 10 cuentas Team × US$149 = **US$1.490 MRR**, US$17.880 ARR antes de costos.
- Intermedio: 30 cuentas Business × US$499 = **US$14.970 MRR**, US$179.640 ARR antes de costos.
- Expansión: 100 cuentas Integrator × US$1.499 = **US$149.900 MRR**, US$1.798.800 ARR antes de costos.
El último escenario es **muy exigente y especulativo**: requiere ventas, equipo, seguridad, financiamiento, partnerships, soporte y retención probados. NO es objetivo financiero comprometido.

## Variables para fórmula de contribución
- `MRR = Σ(clientes_por_plan × precio_neto_plan)`.
- `ARR = MRR × 12` como run-rate anualizado, no ingreso ya reconocido.
- `Margen bruto = (ingresos - COGS)/ingresos`.
- `Margen de contribución = (ingresos - infraestructura - soporte variable - comisiones variables)/ingresos`.
- `CAC = costos atribuibles a captación / clientes nuevos`.
- `Payback_CAC_meses = CAC / (ARPA × margen bruto)` si denominador positivo.
- `Net_Revenue_Retention = (MRR_inicio + expansiones - contracciones - churn)/MRR_inicio`.
- `LTV` solo con cohortes de churn y margen medidos; no multiplicar ARPA arbitrariamente.
- `Burn_multiple = net_burn / net_new_ARR` si denominador positivo y periodo comparable.
- `Gross_Margin_Integrator` debe considerar instancia/tenant, soporte, revisión de seguridad, facturación, impuestos, integración y consumo de terceros.

## Ejemplo de punto de equilibrio
Supongamos solo para practicar: costo fijo mensual US$8.000, margen de contribución 75 %, ticket neto medio US$499. Necesita **al menos 22 cuentas** para cubrir ese costo fijo (8000/(499×0,75)=21,38; redondeo hacia arriba). Excluye impuestos, capex, deuda, marketing y cualquier pasivo no incluido. Recalcular con gastos reales antes de usarlo en inversiones.

## Canales y secuencia
- Entrevistas problema (sin pitch) → demostración offline → prueba técnica restringida → piloto con metas objetivas → contrato anual/uso → expansión por integrador.
- Reforzar dependencias del canal: marca blanca opcional, playbooks y documentación; descuentos basados en margen.
- Diferenciar marketing del producto de una garantía de cumplimiento legal.
- No prospectar organizaciones por perfil público suponiendo que utilizan LLM o necesitan DELIA; corroborar uso, comprador y capacidad.

## Potencial económico no es valuación
El mercado puede crecer por volumen de agentes y necesidades de control, pero no existe evidencia de participación DELIA, pricing, retención o ingresos. Para una valuación seria harían falta ARR reconocido, net retention, margen, crecimiento, churn, concentración, seguridad auditada, acuerdos de propiedad intelectual y cohortes. **Nunca llamar al ARR hipotético “facturación conseguida”.**

## Riesgos financieros
Falsos positivos bloquean operaciones y elevan soporte; falsos negativos destruyen confianza; uso irregular produce costos variables; dependencia de APIs incrementa riesgo de margen; ventas enterprise largas consumen caja; licencias y jurisdicciones generan gastos legales. Presupuesto de seguridad y seguros a considerar antes de clientes sensibles.

## Experimentos de monetización
A/B de propuestas con compradores (sin confundir interés con compra), piloto pagado solo tras gates, medir trabajo ahorrado comparado con flujo actual, voluntad de pagar sin descuentos artificiales y costo real por tenant/agente/mes. Documentar cada no-venta, no solo éxitos.
