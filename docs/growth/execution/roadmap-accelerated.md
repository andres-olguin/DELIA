# DELIA — Aceleración robusta hasta la beta avanzada de enero

**Programa de referencia:** 09/11/2026–15/02/2027. No prometer disponibilidad general ni forzar merge de código inseguro. Los hitos siguen siendo **metas**, sujetos a capacidad y seguridad. El objetivo comercial corre en paralelo, no sustituye QA.

## Dos velocidades: producto y crecimiento

**Track A — ingeniería/seguridad:** resolver P0, ejecutar un caso CRM E2E en sandbox, exportar evidencia mínima y poder repetirlo por segunda organización. No ampliar hacia pagos o datos clínicos.

**Track B — buyer/media/revenue:** entrevistas, estudio de alternativa, documentación original, demo pública reproducible, evaluar workshop de pago con entregables definidos, medición de canal. Nada requiere subir datos de terceros.

**Track C — investigación R&D:** casos del video convertidos en matriz de amenazas, corpus sintéticos, evidencia científica y publicaciones. 10–15 % de capacidad como máximo mientras P0 no esté resuelto, salvo equipo dedicado.

## Hitos con Definition of Done

| Fecha límite | Producto/seguridad | Comercial y medios | Gate |
|---|---|---|---|
| **13/11/2026** | Congelar top-10 de escenarios prioritarios; diagrama de rutas de ejecución y superficie de egress | Ficha pública con claims, 2 guiones revisados, 10 cuentas investigadas en CRM privado | Sin marketing de producción |
| **20/11/2026** | Priorización P0 con estimación y reviewer; versión de contrato CRM ficticio | Objetivo 3 discovery consentidos, 1 demo breve original publicada si es revisada; decidir postulación BIG13 | Buyer evidence y repos sin PII |
| **27/11/2026** | Tests de identidad/tenant, secretos y egress encaminados; no asumir P0 cerrados | Informe de primer test técnico y post de fallos reproducibles | Si bypass, solo LAB |
| **04/12/2026** | Adapter de tool que deniega en punto de ejecución con test E2E | Demo comparativa contra stack existente, explicación de costos | Tool deny no ejecutada |
| **11/12/2026** | Aprobación/versión y revocación sin reuso ni bypass, sujeto a capacidad | Primer workshop de alcance cotizado o constancia de no-fit | Claims revisados |
| **18/12/2026** | Idempotencia/persistencia y reconciliación con fuente ficticia separada | Informe mensual: problemas, entrevistas, costos, 1 publicación con datos negativos | UNKNOWN no es success |
| **08/01/2027** | Release candidate de beta de laboratorio con fixtures reproducibles y documentación | 2 instalaciones independientes objetivo, demo 12 min y 2 clips derivados originales | Sin P0 críticos al pasar S2 |
| **15/01/2027** | **Go/No-Go beta avanzada**, alcance que de verdad pasó pruebas | Kit comercial técnico v1, precio solo si comprador/entrega lo validan | Seguridad tiene veto |
| **31/01/2027** | Refinar API, soporte y diagnóstico de errores; no ampliar core sin evidencias | Hasta 2 design partners si aceptan y hay gates; entrevistas sistematizadas | Sin clientes ficticios |
| **15/02/2027** | Roadmap de primera integración repetible y plan de hardening | Informe de experimentos de demanda; decidir prioridad Partner/SDK/servicio | Decisión basada en datos |

Las fechas no acreditan hitos completados. Los riesgos P0 existentes son #6/#7/#8/#9/#11, y PR #21 permanece en revisión. No mezclar resultados sintéticos de PR #30 con ejecución empresarial real.

## Recursos y paralelismo realistas

**Escenario de planificación de ejemplo (NO disponibilidad del equipo):** si hay 45 horas semanales comprometidas entre colaboradores: 30 h ingeniería/QA, 9 h comercial y entrevistas, 4 h medios/comunidad, 2 h R&D. Los números son una partición para discutir. Si solo existen 15 h, reducir a 10 h P0, 3 h buyer, 2 h comunicación y posponer nuevos módulos.

**No convertir contenido mediático en una distracción de ingeniería.** El fundador u otra persona autorizada puede crear contenido desde demos ya terminadas; un developer no debe dedicar media semana a editar reels mientras un bypass P0 sigue abierto.

### Ingeniería: sprint 0–6

1. **Sprint 0:** inventario de ramas y PR, reproducir tests, registrar blockers/estándares.
2. **Sprint 1:** separar identidad del payload de LLM, recursos de tenant; egress y secretos.
3. **Sprint 2:** adapter único, permisos deny-by-default, logs minimizados, pruebas contra rutas alternativas.
4. **Sprint 3:** aprobación exacta, auditoría y persistencia de operaciones.
5. **Sprint 4:** reconcilición desde fuente de prueba, resultado desconocido, fallos y recuperación.
6. **Sprint 5:** SDK/docs, instalación ajena al equipo, comparación de costo y experiencia.

Cada sprint: 1–3 historias con dueño que acepte, revisor, criterios, tests de no regresión, SHA y posibilidad de rollback. Si un P0 bloquea, priorizarlo y reducir alcance de UI antes de mover fecha.

## SLO y objetivos numéricos SOLO para piloto sintético

- **0 ejecución de tool denegada** en la batería específica; registrar total de intentos, escenarios y cobertura.
- **0 éxito comunicado** para respuestas `unknown/pending`; registrar no ejecutados.
- **0 canaries sintéticos** de PII que alcancen upstream de ensayo cuando deberían enmascararse; publicar falsos positivos y negativos.
- **100 % de artefactos de benchmark** con versión/SHA, fixture y condiciones.
- **Meta exploratoria de onboarding:** menos de 2 horas en entorno definido, todavía no medida.
- **No prometer 99.9 % uptime** antes de tener producción y monitoreo.

## Puertas de release

- **R0:** documentación y demos ficticias, sin permiso de producción.
- **R1:** IAM, auth/tenant, egress, logs y secretos probados con tests reales.
- **R2:** adapter sin bypass, aprobación durable, revocación, persistencia y reconciliación de sandbox.
- **R3:** amenazas revisadas por tercero, incident response, backups/recovery, contrato y permisos de datos.
- **R4:** operación y soporte productivos medidos, con SLO y obligaciones jurídicas aplicables.

Una demo verde en R0 **no** equivale a R2. Si el 15/01 falta R2, entregar un demo de laboratorio con inventario de pendientes y redefinir beta, no disfrazar software.

## Robustez de ingeniería

CI Python 3.11 y 3.13, tests de contrato, seguridad de secretos, dependencia, fuzzing de parser y SDK donde corresponda, cross-tenant, idempotencia bajo concurrencia, inyección indirecta y cambio de herramienta. Evitar incorporar nuevas dependencias sin evaluar licencia, supply chain y mantenimiento. Separar benchmarks de desarrollo de holdouts independientes.

## Condiciones de aceleración

Se puede acelerar reduciendo trabajo innecesario: integrar OPA/Cerbos/Temporal/agentgateway donde convenga; reutilizar plantillas; trabajar con un proceso; posponer consola bonita; limitar idiomas a ES/EN de salida; preparar medios desde la misma demo verificable. **No se puede acelerar eliminando identidad, revisión, contratos o controles P0**.
