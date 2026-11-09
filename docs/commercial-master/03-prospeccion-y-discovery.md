# 03 — Guía comercial reproducible: cuentas, entrevistas y seguimiento

## Principio

**No acumular 1.000 leads sin problema validado.** Investigar cuidadosamente cuentas existentes y preguntar por sus flujos. Usar información pública y contactos profesionales legítimos; no extraer ni publicar PII, ni automatizar mensajes masivos sin autorización. La información de relaciones se conserva en un CRM privado, no en GitHub.

## Sistema de investigación de cuenta (10 minutos)

1. Verificar que la empresa desarrolla agentes con acciones sobre sistemas, no solo produce contenido.
2. Identificar señales públicas de CRM, ERP, help desk o herramientas, con fuente y fecha.
3. Comprender cuál es su cliente tipo, país, sector y modelo de implementación.
4. Formular una hipótesis de **operación crítica concreta** que un agente podría intentar, marcada `NO VERIFICADA`.
5. Revisar cómo el stack actual podría resolverla (Helio, OPA, n8n o permisos del ERP).
6. Formular **una pregunta** consultiva para validar la hipótesis, sin afirmar que tienen un problema.
7. Descartar si hay incompatibilidad evidente, contacto no autorizado o daño/compromiso legal.

## Mensajes de primer contacto — estilo natural

**LinkedIn — integradora:** «Hola, vi que trabajan con agentes y automatizaciones empresariales. Estoy estudiando cómo gestionan los permisos cuando esos agentes consultan o modifican datos en CRM. Ustedes ya tienen algún control de aprobación o lo manejan directamente desde la integración? Estamos contrastando el enfoque de DELIA, todavía en desarrollo.»

**Email — CTO de SaaS:** «Estoy investigando cómo las plataformas B2B controlan operaciones de agentes cuando acceden a herramientas. En DELIA estamos construyendo un laboratorio de contratos operacionales con pruebas de resultados. Quería preguntarte qué parte de esos controles tienen resuelta hoy y qué les sigue costando mantener. No estamos ofreciendo un gateway de producción todavía.»

**Seguimiento 1 (separado y proporcional):** «Te escribo por la consulta sobre permisos y aprobaciones de agentes. Si no es algo que estén evaluando, todo bien y no insisto.»

**No enviar estos textos a contactos sin relación/contexto adecuados.** Adaptar al canal y su legislación; respetar solicitudes de no contacto.

## Guion de discovery de 25 minutos

0:00–2:00 → permiso y objetivo de aprender, no pitch.
2:00–7:00 → proceso que el equipo ya ejecuta, quién lo usa, software actual.
7:00–12:00 → última vez que falló o generó trabajo extra; evidencia de tiempo/costo.
12:00–17:00 → permisos, controles y solución existente; ¿qué no resuelven?
17:00–21:00 → consecuencia, urgencia y aprobación presupuestaria.
21:00–25:00 → resumir hechos y suposiciones, preguntar si un workshop de alcance tendría valor, acordar siguiente paso.

## Preguntas fuertes (elegir pocas)

- «Cuéntame el último caso en que un agente intentó hacer algo que requería aprobación».
- «¿Cuál fue la consecuencia y cuánto costó resolverla?».
- «¿Qué herramienta usaron para controlarlo? ¿Qué parte funcionó bien?».
- «Si duplican el número de clientes, ¿qué parte deben configurar desde cero?».
- «¿Cuánto tardaron en incorporar al último cliente con políticas distintas?».
- «¿Hay operaciones que hoy no automatizan aunque las tengan técnicamente listas?».
- «¿Quién decide que un sistema puede pasar de demo a producción?».
- «¿Qué paso necesitaría una autorización humana formal?».
- «Si lo construyeran ustedes, ¿cuántas horas y de quién requeriría?».
- «¿Qué compraron ya para resolver algo parecido? ¿Qué les hizo elegirlo?».
- «¿Qué presupuesto se asignó a esta clase de trabajo, si existe?».
- «¿Qué te haría concluir que DELIA no añade valor?».

No preguntar «¿comprarías DELIA?» como única evidencia. Buscar operaciones ya realizadas, presupuesto, decisiones y problemas anteriores.

## Registro seguro de evidencias (en sistema privado)

`opportunity_alias`, origen y fecha, consentimiento, segmento, proceso, dolor textual, alternativa, costo con fuente, actor económico, presupuesto indicado/no indicado, urgencia real, siguiente paso acordado, resultado/no-fit, requisitos de seguridad, fecha de próxima revisión, owner interno que acepta. El alias público o en demos debe empezar `SYN-`, sin persona/empresa identificable. **No registrar en archivos del repositorio emails, teléfonos, contratos ni nombres de clientes.**

## Clasificación posterior

- **No-fit:** problema bajo o controles existentes suficientes. No presionar.
- **Discovery:** dolor probable sin comprador o costo validado.
- **Validación:** problema real, alternativa y costo razonable conocidos.
- **Lab Evaluation:** comprador y equipo aceptan prueba sintética específica con criterio.
- **Seguridad:** cualquier dato real o acción de efecto externo requiere revisión independiente; no autorizar por score.
- **Oferta pagada:** solo servicio de alcance definido que MasterTech puede entregar con permiso/contrato; no vender el software incompleto.

## Cadencia sostenible (semanal)

Objetivo de planificación, ajustable a capacidad: 10 cuentas investigadas con fuente, 5 mensajes relevantes, 3 respuestas con contexto, 2 descubrimientos si hay aceptación, 1 revisión técnica de alternativa. Son **metas de actividad**, no conversiones previstas. Si ninguna respuesta, mejorar segmento/mensaje; no multiplicar spam.

## Reunión interna de pipeline de 25 minutos

- 5 min: avances de compradores, no commits.
- 5 min: tres razones de rechazo y lo que enseñaron.
- 5 min: evidencia de problema y oportunidad con presupuesto.
- 5 min: dificultades de entrega y exposición de riesgos.
- 5 min: experimentos próximos y tareas aceptadas.

Nunca reportar dinero como MRR sin contratos recurrentes activados y cobros pertinentes.

## Indicador comercial de verdad

Contar **problemas validados con dueño económico** y compradores que aceptaron evaluar un alcance pagado; no confundir número de mensajes enviados con probabilidad de éxito.
