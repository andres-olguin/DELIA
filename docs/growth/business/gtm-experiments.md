# DELIA — Growth-to-Revenue Experiments (noviembre–febrero)

**Objetivo:** reducir incertidumbre en ventas y distribución de soluciones AI Control/Outcome, con énfasis en integradoras B2B CRM. **No** se han realizado los experimentos por publicar este documento.

## Embudo dual: ventas y developer advocacy

### Camino comercial

Cuenta investigada con fuente → conversación legítima → buyer problem documentado → comparación con herramienta actual → propuesta E1 Workflow Readiness Lab → contrato/cobro verificados → evaluación en sandbox → Partner Beta **solo tras gates**.

### Camino técnico

Contenido original con SHA → lectura de repo → ejecución demo → issue/pregunta técnica → colaboración/entrevista → integración experimental → comparación instalada con alternativa.

Al analizar conversión, separar ambos embudos. GitHub stars, views o número de publicaciones **no son ingresos**.

## Experimentos con decisión falsable

| ID | Fecha objetivo | Hipótesis | Evidencia mínima | Decisión si falla |
|---|---|---|---|---|
| G1 | 20/11 | Integradoras sufren costo por reescribir permisos de CRM para clientes | 3 entrevistas genuinas y un caso concreto | Ajustar segmento |
| G2 | 04/12 | Un test de tool denegada facilita comprensión técnica | 2 revisores ejecutan fixture sin ayuda | Simplificar kit |
| G3 | 18/12 | Un workshop de evaluación tiene comprador y precio | Propuesta de alcance aceptada o rechazada con razones | Cambiar oferta/alcance |
| G4 | 08/01 | Un segundo cliente sintético requiere menos configuración | Dos instalaciones y horas medidas con mismo entorno | Reusar gateway existente o pivotar |
| G5 | 15/01 | La beta avanzada pasa gates de seguridad | Acta Go/No-Go y tests E2E | No lanzamiento |
| G6 | 31/01 | Contenido con demo capta mejores conversaciones que noticias genéricas | Buyer meetings por contenido y fuente de atribución | Reducir canal |
| G7 | 15/02 | Modelo Partner tiene contribución razonable con soporte estimado/real | Unidad económica por tenant y 1–2 partners de diseño, si existen | Pricing/segmento revisado |

Objetivos de actividad y fechas; no forecasts. Equipo debe definir capacidad antes de comprometerlos públicamente.

## Tres paquetes comerciales, nunca prometer como ya disponibles

1. **E1 — Workflow Readiness Lab**: revisión de un proceso y su alternativa actual, con riesgos, contrato sintético, métricas y recomendación de comprar/no comprar DELIA. Servicio profesional potencialmente cobrable cuando hay capacidad y acuerdo.
2. **E2 — Agent Control Evaluation Pack**: batería de 10 escenarios sintéticos con un reporte verificable; hoy es un plan, no una evaluación acreditada.
3. **E3 — DELIA Partner Assurance**: eventual licencia recurrente por integradora/tenant/uso con políticas, permisos y evidencias seguras, pendiente de pruebas/producto.

Referencias: `docs/commercial-master/02-ofertas-y-precios.md`, `docs/research/agent-control/product-opportunity.md`.

## Distribución en dos países de entrada

**Chile:** probar compradores de consultoras, integradoras de CRM y automatizaciones empresariales; usar ITD-IA como contexto macro, no como TAM.  
**México:** investigar integradoras con agentes conectados a CRM; documentar horarios, soporte, cobro/contratos/impuestos pertinentes, formatos RFC/CURP cuando haya producto.  
**Brasil:** opción posterior con portugués revisado y soporte real. **EE. UU./Europa:** investigación y comunidad global, no prometer despliegue jurídico inmediato.

## Hipótesis de pricing e ingresos

- Workshop de alcance definido: rango exploratorio US$250–750, comparado con costo de horas e impuestos. **No tarifa publicada.**
- Partner: modelo hipotético base + tenants + volumen, simulado por `commercial_ops.demo`; no ingresos reales.
- Evaluación periódica: retainer solo si el comprador encuentra valor y existe capacidad de auditoría.

### Control de rentabilidad por cliente

`Margen de contribución = precio cobrado - nube - comisiones - horas variables de delivery/soporte - pasarela - costos directamente atribuibles.`

Registrar también CAC/costo fundador, ciclo de venta, tiempo al primer test, falsos bloqueos y costo por operación comprobada. No excluir horas humanas para aparentar margen SaaS.

## Medios como canal y no fin

Comparar LinkedIn/GitHub/video mediante **conversaciones calificadas originadas por canal** y tasa a diagnóstico comprado. Si después de ocho semanas no se identifica una fuente atribuible de conversaciones, ajustar formato/segmento; no asumir que el problema es «falta de alcance».

## Captación responsable

No comprar listas dudosas ni usar mensajes automáticos a gran escala. Para un comprador potencial se documenta relación profesional, motivo específico de contacto y salida fácil. Respetar preferencias/privacidad y legislación aplicable; CRM identificable privado. Los contenidos públicos no incluyen capturas de chats sin permiso.

## Filtro de embajadores/influencers

Solo colaboración con desarrolladores/seguridad que puedan reproducir la demo y revelar pago/patrocinio cuando corresponda. No pagar para afirmar seguridad inexistente ni ofrecer beneficio por reseña falsa. Audiencia masiva no necesariamente trae CTOs; preferir credibilidad técnica y comunidades.

## Partnership y academia

Dos rutas: comunidades dev/security (feedback y issues verificables) e integradoras (buyer discovery, eventualmente acuerdos). Ninguna es «alianza» por simple correo. Academy y webinar no implican acreditación o respaldo universitario. Reutilizar una misma batería de escenarios en documentación, demo, entrenamiento y workshop, con permisos apropiados.

## Reglas para una decisión de escala

Desbloquear segundo sector solo tras: problema pagado, instalación repetible, margen no negativo, dueño de mantenimiento, seguridad apropiada y retención. Desbloquear paid media solo tras demostrar mensajes orgánicos que generan conversaciones y una landing lista con disclaimers/captura consentida.
