# 20 — Gobierno del equipo, capacidad, incentivos y disciplina comercial

## Por qué es crítico para la venta

Aun con buen producto, una empresa en etapa inicial pierde clientes si nadie responde, se prometen fechas sin disponibilidad o el soporte no está cubierto. La confianza comercial requiere ownership: persona responsable, criterio de calidad, fecha y escalamiento.

## Gobierno propuesto (sin asignaciones personales automáticas)

**Product/Founder:** prioriza segmento, valida entrevistas y aprueba discurso y propuesta de precio. No cierra P0 técnico por necesidad comercial.
**Tech Lead:** arquitectura, repos, PR, seguridad de integraciones y revisión.
**QA/Security Reviewer:** revisa negativamente auth, replay, egress y trazas; separado del autor cuando sea posible.
**Delivery Lead:** limita alcance del workshop y estima horas reales; no acepta soporte ilimitado.
**Revenue Owner:** registro privado de pipeline, etapas, ofertas/cobros, márgenes y cadencias.
**Legal/Finance:** PI, licencias, condiciones de servicios, presupuesto y grants, con profesional cuando corresponda.

Un mismo colaborador puede cubrir más de un rol, pero no reemplaza revisiones independientes de seguridad. Asignar solo tras aceptación de tareas y condiciones.

## Roles y responsabilidades por etapa

| Proceso | Decisión de founder | Trabajo técnico | Evidencia |
|---|---|---|---|
| Contactar prospecto | Autorizar canal y mensaje | No aplica | Consentimiento/pertinencia |
| Discovery | Confirmar problema y buyer | Evaluar posibilidad de stack | Notas privadas |
| E1 Workshop | Cotizar margen y alcance | Entregar diagnóstico y alternatives | Informe firmado/revisado |
| E2 Sandbox | Aprobar contrato y riesgo | Simulación/CI/QA | Tests, SHA y permisos |
| Piloto productivo | Contrato, privacidad y aceptación | P0/S3/S4 verificados | Informe de seguridad y aceptación |
| Soporte | Presupuestar capacidad | Operación/SLAs realistas | Tickets y métricas |
| Comercialización | Validar pricing y canales | Medir costo y fiabilidad | Facturación/margen/churn |

## Regla de reuniones

- Weekly 25 min: ventas/mercado, P0, costos, decisión única de semana.
- Demo semanal opcional 15 min con casos reproducibles (no teatro).
- Quincenal 45 min: estrategia de producto, supuestos refutados, pívots.
- Mensual: caja, margen, aceptación de responsabilidades y riesgos.
- No convocar reuniones si no hay decisiones que tomar; usar registro escrito.

## Compensaciones e incentivos

No asumir remuneración fija ni participación de colaboradores. Antes de asignar trabajo con consecuencias comerciales, aclarar si es remunerado, a éxito, bajo contrato de servicios o voluntario permitido, con condiciones legales locales. Evitar promesas de equity sin documentación. Si hay comisiones por ventas, definir hecho generador (contrato/cobro), devoluciones, impuestos, plazo y márgenes. No pagar comisión sobre lead que solo respondió.

## Capacidad versus calendario

Pedir disponibilidad semanal en horas y fracción dedicada a P0 vs. nuevo producto. Una beta avanzada puede requerir cientos de horas de backend, seguridad, integración, QA y documentación; la existencia de 20 planes no crea capacidad humana. Reducir alcance primero, nunca QA ni gates críticos.

## Matriz de comunicación externa

- Solo responsables autorizados confirman precio, plazo, contrato y soporte.
- Equipo puede compartir estado LAB/documentación pública sin inventar madurez.
- Ramas y PRs de colaboradores conservan autoría y revisión.
- Un cliente potencial no controla unilateralmente el roadmap; priorizar por valor y capacidad.
- Los datos privados del cliente no se distribuyen por chats grupales si existe un canal seguro contractual.

## Decisiones Go/No-Go

Producto, seguridad, privacidad, capacidad de delivery, presupuesto y contrato deben ser aprobados **por separado**. Un éxito comercial no autoriza producción insegura; un CI verde no prueba fit de mercado. Ambos requieren evidencias distintas.
