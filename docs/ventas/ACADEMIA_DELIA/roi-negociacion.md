# Taller de valor económico, ROI y negociación

Material didáctico, no tarifa publicada de DELIA. Todas las cifras son hipótesis en USD (excepto donde se especifique moneda).

## Caso 1 — Integrador de cinco clientes (hipotético)
Supuestos: 5 clientes, 6 horas/cliente/mes de mantener políticas, coste laboral total US$30/h. Costo manual: 5×6×30 = **US$900/mes**. Suponga que una herramienta reduce esa tarea a 2 horas/cliente/mes: ahorro bruto potencial 5×4×30=US$600. Si la licencia costara US$499, ahorro neto atribuible antes de integración/soporte sería US$101/mes. **No es retorno demostrado**; hay que medir reducción real y agregar onboarding, errores y revisión humana.

Si la misma integradora ya posee una herramienta gratuita que resuelve el problema, el incremento de valor puede ser cero. No sumar hipotéticas multas evitadas como ingresos.

## Caso 2 — SaaS con control humano (hipotético)
30.000 tool calls/mes; 0,4 % requieren revisión = 120 casos; revisión previa 12 min/caso = 24 h/mes; nuevo flujo reduce a 5 min/caso = 10 h/mes; diferencia 14 h. A US$25/h = US$350/mes bruto. Si el plan fuese US$499/mes, ahorro de tiempo por sí solo no justifica el producto. El comprador podría valorar además auditoría y control de riesgos, pero habría que medirlos sin inventar cifras.

## Caso 3 — Empresa con integración costosa (hipotético)
Proceso manual inicial 160 h a US$45/h = US$7.200. Servicio de integración 80 h = US$3.600; diferencia posible de implementación US$3.600 **solo si se acredita comparabilidad**. Sumando suscripción, soporte y controles adicionales, calcular ROI con costos totales y horizonte de 12 meses.

## Taller de precios
Hipótesis comerciales del modelo económico: Developer gratis de laboratorio, Team US$149, Business US$499, Integrator US$1.499, enterprise cotización. **No se han validado ni aprobado estas tarifas**. Diseñar entrevista Van Westendorp, preguntas de precio y pruebas de valor sin sesgo.

## Fórmulas
`MRR = Σ cuentas reales activas × tarifa mensual neta`.
`Valor incremental = costo actual medido - costo total nuevo medido`.
`ROI simple = (beneficio neto atribuible - inversión)/inversión`, si hay inversión positiva y periodo consistente.
`Payback = costo de implementación / ahorro mensual neto`, solo cuando ahorro positivo demostrado.
`CAC payback = CAC/(ARPA × margen bruto)`, con datos reales de captación y COGS.
`Margen = (ingreso - costos atribuibles)/ingreso`, no omitir comisiones, nube o soporte.

## Reglas de una oferta piloto
- Una o dos integraciones concretas y una política.
- Todos los datos sintéticos o autorizados bajo gates.
- Métrica predefinida y valor de salida objetivo (incluido No-Go).
- Precio de piloto y costo de soporte explícitos, aprobación comercial/jurídica.
- Titularidad de integraciones, licencias, confidencialidad, borrado y acceso mínimos.
- Nada de SLA productivo mientras producto esté en investigación.
- Separar tarifa de uso del gateway del costo del modelo LLM externo.

## Objeciones de precio
«Es caro» → «¿Respecto de qué alternativa y costo total?».
«Necesito 70 % descuento» → «Podemos reducir alcance, soporte o número de tenants; no omitir seguridad».
«Me garantizan cumplimiento» → «No podemos ofrecer garantía legal; definamos obligaciones y revisión independiente».
«Sin referencia de cliente no compro» → «Es razonable. Podemos realizar una evaluación técnica limitada; quizá no sea momento de una compra».

## Negociación de canal B2B2B
Debe existir margen para integrador, MasterTech, hosting, seguridad y soporte. Hipótesis: venta neta US$1.499, comisión de 20 % = US$299,80, restantes US$1.199,20 antes de COGS/impuestos; no representa beneficio. Evitar revendedores sin acuerdos de responsabilidades y protección de datos.

## Taller de proyección con tres escenarios
- 10 Team: MRR US$1.490.
- 30 Business: MRR US$14.970.
- 100 Integrator: MRR US$149.900.
Son escenarios hipotéticos de escalado, **no metas validadas ni ingresos percibidos**. Para discutir el escenario mayor, el presentador debe identificar adquisición, churn, soporte, capital requerido, acreditación de seguridad y proveedores.

## Ejercicio de comité financiero
Un CFO objeta: «Con US$8.000 de costo fijo, US$499 de ARPA y margen 75 %, ¿cuántos clientes necesitan para cubrirlo?» Respuesta matemática: 22 cuentas, antes de otros costos/impuestos y con supuestos simplificados. Pedir la sensibilidad a precio, margen y volumen.

## Registro de experimentos
Hipótesis, número de entrevista, segmento, fecha, precio planteado, respuesta literal, objeciones, consentimiento y decisión. No almacenar el CRM con nombres y correos en repositorio público.
