# DELIA — Hitos adicionales de Outcome Assurance (fechas y criterios)

**Fecha de propuesta: 09/11/2026.** Se integra con [roadmap empresarial existente](roadmap-con-fechas-y-gates.md), sin sustituirlo. Son metas **condicionales** y ninguna autoriza saltarse seguridad P0.

## Del 09/11/2026 al 15/01/2027

| Fecha límite | Entregable | Estado 09/11 | Gate |
|---|---|---|---|
| **13/11/2026** | Matriz global de competencia, claims revisados, diferencia explícita frente a Helio/AgentTrustOps/Temporal | Investigación documental creada | Revisor confirma que no se inventan características ni exclusividad |
| **16/11/2026** | Contrato ecommerce de laboratorio, tests negativos y reporte con modo sintético | Primer código de laboratorio publicado | CI dos versiones Python, sin efectos externos |
| **20/11/2026** | Especificación de contrato de resultados v0.1 (intención, precondición, autorización, ejecución, reconciliación, evidencia) | Documento inicial | Amenazas y límites auditados |
| **27/11/2026** | Egress DLP y auth/tenant del DELIA base según #6–#9 | P0 existente sin cerrar | No-Go si bypass o secretos |
| **04/12/2026** | Adapter tool-call con enforcement comprobado; contrato de negocio no sustituye control de permisos | Por implementar | Test E2E: acción denegada no se ejecuta |
| **11/12/2026** | Estado durable de operaciones, idempotencia y ejecución atómica de un caso ficticio | Por implementar | Tests de carrera, replay y caída |
| **18/12/2026** | Reconciliación con fuente de prueba autoritativa + caso unknown que no se marca exitoso | Por implementar | Verified/Hold/Mismatch trazables |
| **25/12/2026** | Control de procesos en API y exportación de evidencia mínima | Por implementar | Seguridad y contract tests |
| **08/01/2027** | Demo con 2 flujos: reembolso ecommerce y cambio CRM BPO, ambos sintéticos | Por implementar | E2E y métricas p95/costo |
| **15/01/2027** | Revisión beta avanzada y decisión Go/No-Go | Objetivo futuro | Todos los P0, equipo, docs, evidencia |

Se recomienda priorizar **un** flujo E2E completo sobre cuatro soluciones semiintegradas. La integración con una fuente real y el aislamiento multiempresa pueden extender el calendario.

## Validación de mercado

- **20/11/2026:** iniciar entrevistas sobre reembolsos y cambios de CRM, no sobre «¿te gustaría una plataforma de IA?».
- **18/12/2026:** objetivo de 5 conversaciones cualitativas con compradores que ya ejecuten esas operaciones; registrar alternativa usada y costo.
- **08/01/2027:** dos integradores externos intentan instalar demo y registran tiempo/errores.
- **31/01/2027:** decidir piloto de diseño con datos sintéticos o consentimiento/controles contractuales.
- **31/03/2027:** decidir negocio principal: SDK/contratos, Partner SaaS o servicios de integración; descartar lo que no tenga ROI demostrable.
- **30/06/2027:** canal Partner con primeros compradores solo si seguridad y costos.
- **31/12/2027:** revisar margen y retención de contratos, no cantidad de nombres de funcionalidades.

## Criterios S0–S4

S0: laboratorio local, sin identidades reales ni efecto, pruebas negativas.
S1: auth/tenant real y DLP de egreso, adapter único.
S2: durabilidad, recibos, reconciliación con proveedor auténtico bajo sandbox, revisión independiente y API.
S3: piloto empresarial con tratamiento de datos definido, contrato, runbook y aprobadores.
S4: producción con seguridad operativa, revisión externa y SLO basados en medición.

## Umbrales propuestos, NO hechos

- 0 operaciones duplicadas dentro de fixtures de test.
- 0 «VERIFIED» cuando la fuente está `unknown/pending`.
- 0 acciones ejecutadas sin autorización en batería E2E.
- 100 % de flujos instrumentados en el conjunto de prueba presentan cobertura y métricas.
- Tiempo de primera integración inferior a 2 h como hipótesis a validar, no promesa.
- Al menos una comparación de costo total con herramienta ya usada por comprador.
- 0 claims de certificación o cliente no verificadas en marketing.

## Plan B si excede capacidad

Mantener exclusivamente: seguridad P0, contrato ecommerce, motor determinista, demo y comparación de competidor. Posponer console SaaS, multi-cloud y verticales extras. No forzar integración a main de código de seguridad sin revisión y pruebas.

## Control de cambios

Dueño de cada tarea y reviewer solo después de aceptar disponibilidad. No se asigna trabajo automáticamente a Benjamín, Iván, Isaac, Nilson o Emmanuel. La estrategia de marca y capacitación es responsabilidad de dirección solo tras definir acuerdos.
