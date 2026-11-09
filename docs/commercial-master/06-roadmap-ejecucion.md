# 06 — Roadmap maestro y 120 días de reducción de riesgos

**Fecha base:** 09-11-2026. Fechas objetivo de gestión, no compromisos de entrega; sujetas a disponibilidad y veto técnico. **Objetivo 15/01/2027 = evaluación de beta avanzada, no lanzamiento productivo automático.**

## Fase 0 — preparar una venta realista, 09–15 noviembre 2026

- **10/11:** terminar scorecard y matriz de claims, revisar docs de competencia, no vender gateway productivo.
- **11/11:** ficha ICP primaria, 10 cuentas bajo investigación con permiso de contacto; 2 alternativas técnicas por cuenta.
- **12/11:** guion discovery de 25 min, demo del contrato sin operaciones reales, una ficha de oferta E1.
- **13/11:** documento de una página: problema, compradores, entrega, límites, beneficio a medir, precio de exploración.
- **15/11:** revisión independiente de seguridad y propiedad intelectual; asignar solo tareas aceptadas.

**Gate F0:** cualquier fundador puede explicar en 90 segundos quién compra y qué recibe **hoy**, distinguir servicio profesional de producto futuro, nombrar una alternativa ya disponible y señalar cuándo no se debe vender DELIA.

## Fase 1 — evidencia de problema, 16–29 noviembre 2026

- **20/11:** meta de 10 contactos legítimos personalizados, 3 conversaciones de descubrimiento confirmadas, propuesta de benchmark congelada.
- **24/11 13:00 Chile:** cierre de BIG13 Start-Up Chile; decidir **postular o descartar** después de leer bases/eligibilidad. Nunca afirmar fondos obtenidos.
- **27/11:** cierre planificado P0 de auth, egress, secretos, arranque y CI; la fecha no convierte faltantes en listos.
- **29/11:** resumen de cinco problemas encontrados, alternativas actuales y primera decisión de segmento.

**Gate F1:** al menos dos profesionales del ICP confirman un dolor comparable y coste/consecuencia; si no, reformular oferta antes de gastar más ingeniería.

## Fase 2 — demo con valor, 30 noviembre–13 diciembre 2026

- **04/12:** demostración en sandbox de una herramienta que no ejecuta al denegar; muestra de resultado desconocido.
- **07/12:** comparar contra solución actual de un integrador; registrar horas de configuración.
- **11/12:** diseño/implementación de idempotencia durable según capacidad y P0; test de replay y concurrencia.
- **13/12:** presentar un workshop E1 de alcance claro a compradores que pidieron evaluar.

**Gate F2:** no existe éxito sin test reproducible, SHA, requisitos negativos y costo de setup; si no hay demo segura, ofrecer exclusivamente consultoría/diagnóstico o aprendizaje.

## Fase 3 — de evidencia a oferta, 14–31 diciembre 2026

- **18/12:** objetivo de cinco entrevistas profundas y una comparación técnica basada en un proceso ficticio.
- **22/12:** validar disponibilidad de soporte, términos de piloto y presupuesto operativo.
- **27/12:** evaluación de consola/API y documentación de contratos; despriorizar UI si P0 no cerrado.
- **31/12:** reporte de tracción **real**: número de conversaciones, presupuestos explícitos, workshops contratados, intentos de instalación, costos y razones de rechazo.

**Gate F3:** un responsable económico acepta discutir un alcance pagado, o el equipo decide cambiar el ICP/posicionamiento; no simular LOIs o negocios en el informe.

## Fase 4 — 01–15 enero 2027

- **05/01:** primeros ensayos de onboarding por personas externas cuando exista producto de laboratorio instalable.
- **08/01:** demo completa CRM low-risk y comparativa documentada con herramienta existente; no producir pagos reales.
- **11–14/01:** tests de regresión, seguridad, rollback y desempeño medido; congelar funciones nuevas.
- **15/01:** **Go/No-Go** de beta avanzada según P0. La comercialización de software sigue condicionada a contratos, seguridad y costos; los servicios técnicos de alcance limitado son línea independiente.

## Fase 5 — 16 enero a 31 marzo 2027

- **31/01:** identificar hasta 2 design partners reales (deben aceptar), con entregables en sandbox y fechas.
- **28/02:** conocer tiempo de integración, costo de servicio por partner y primeras señales de disposición de pago; evaluar pricing.
- **15/03:** decidir si se incrementa alcance a ecommerce o se mantiene CRM/BPO.
- **31/03:** **decisión obligatoria** de producto, no solo reporte: seguir con Partner/Outcome, pivotar a SDK/pack sobre herramienta existente o suspender inversión si no hay dolor comprador.

## Metas de actividad, NO forecast

- 10–20 entrevistas acumuladas como objetivo hacia marzo, 2 pruebas de instalación independientes, 1–3 propuestas económicas, 1 contrato de piloto únicamente tras gates y capacidad.
- Objetivos MRR 2027 del roadmap anterior quedan expresamente **condicionados a evidencia de PMF**: no planificar contrataciones o deuda sobre números hipotéticos.
- Si pasan 3 semanas sin buyer evidence, dedicar menos horas a nuevas funciones y más a descubrimiento de mercado.

## Dependencias técnicas reales

#6 arranque → #7 auth → #8 secretos/logs → #9 pre-egress → #11 CI → PR #21 agente/approve → contratos de resultado en main → adapter seguro y fuente autoritativa → API/console. Ningún hito de ventas desbloquea seguridad por sí mismo.

## Restricciones de capacidad

Plan de ejemplo: dos personas 10–15 h/sem cada una pueden ejecutar algunas entrevistas, la demo y revisión; no pueden construir de forma creíble un gateway enterprise completo, SaaS multi-tenant, marketplace y 18 packs en 9 semanas. Exigir al responsable técnico una estimación detallada por historia antes de prometer fechas externas.

## Portafolio posmarzo

Solo si el ICP valida negocio: Partner SaaS y un segundo pack; después Enterprise dedicado e internacionalización. Mantener las 18 verticales y diez apuestas R&D como opciones, **no como backlog simultáneo comprometido**.
