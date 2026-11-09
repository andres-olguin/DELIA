# Acta de transición Sprint 2 → Sprint 3 — DELIA / futura identidad DANREXO

**Corte comprobado:** lunes 09/11/2026 (Chile). **Base de inspección GitHub:** `main` en `296e13622870774dcee5527a540e856171d58d29`. **Situación:** Sprint 2 vencido en calendario, **NO aceptado técnicamente**. Sprint 3 iniciado en calendario, pero no autoriza extender funcionalidades de tráfico con P0 pendientes.

## 1. Fechas, alcance y semántica

- **Sprint 2:** 26/10–08/11/2026; fecha prevista ya vencida el 09/11 (**0 días restantes, 1 día de atraso temporal**).
- **Sprint 3:** 09/11–22/11/2026; su ventana de 14 días calendario comienza hoy, **13 días hasta el cierre previsto sin contar hoy**.
- **Definición de estado:** `implementado` ≠ `pruebas pasadas` ≠ `revisado y aceptado` ≠ `apto para producción`.
- **No usar un porcentaje de progreso para inferir seguridad.** De los cinco entregables/hitos originales del Sprint 2, al corte **0 están acreditados como aceptados formalmente**, dos tienen código parcial existente y tres carecen de evidencia de aceptación/cierre.

## 2. Auditoría de los cinco hitos originales del Sprint 2

| ID | Fecha original | Resultado buscado | Evidencia hallada | Estado de aceptación |
|---|---|---|---|---|
| S2-01 | 28/10 | Regex de cédula y NIT Colombia, borde y DV | `backend/dlp/pii.py` y `tests/test_pii.py` en main; detección estructural de algunas categorías; muestras sintéticas y limitaciones. No hay review/acta final específica del hito | **PARCIAL; validación y aceptación pendientes** |
| S2-02 | 31/10 | Módulo 11 y enmascaramiento RUT Chile | `rut_dv` y regla RUT presentes en main; pruebas de detector; no equivale a comprobar egreso upstream en API | **PARCIAL; sin aceptación integral** |
| S2-03 | 04/11 | Modelo PostgreSQL + Alembic migraciones auditables | `app/models.py` y `app/api/proxy.py` muestran discrepancia de campos de AuditLog; `app/main.py` llama `create_all`. [Foundation doctor](../../tools/foundation_doctor.py) identifica esto | **PENDIENTE / BLOQUEADO** |
| S2-04 | 07/11 | Middleware FastAPI de sanitización previo a proveedor + review | `services/proxy.py` aún envía `request.model_dump()` al upstream y `app/api/proxy.py` reenvía el request original. #9 abierto, sin egress garantizado | **PENDIENTE CRÍTICO** |
| S2-05 | 08/11 | Revisión ejecutiva de alcance y seguridad PII | No se encontró acta de aceptación ejecutiva y de seguridad formal, ni firma de reviewer; los controles del registro Foundation siguen abiertos | **PENDIENTE** |

### Avances reales adicionales (NO sustituyen los hitos)

- [PR #20](https://github.com/andres-olguin/DELIA/pull/20), **abierto**, aportado por Benjamín: detectores CURP/RFC México y CI/NIT Bolivia, corpus de desarrollo de 96 casos, automatización de tests, documentación. **HEAD al corte `f2e3f5a7`**, mergeable y 11 commits atribuidos a `benjadiaz112`.
- [CI del PR #20](https://github.com/andres-olguin/DELIA/actions/runs/42686868441) aprobó **312 tests, 22 warnings** en Python 3.14.4 sobre la rama del PR; **no equivale a merge a main ni a seguridad productiva**.
- [Regresión histórica](https://github.com/andres-olguin/DELIA/blob/feat/16-validadores-mx-bo/docs/benchmarks/REGRESION_HISTORICA_R3.md) *solo está en rama PR #20 al corte*: 172 casos; base 71 TP / 3 FP / 79 FN y nuevo 99 TP / 5 FP / 51 FN, 2 FP adicionales T0162/T0163. Corpus MX/BO de 96 casos: 55 TP / 0 FP / 0 FN **de desarrollo**; faltan casos independientes y decisión de tradeoff.
- [PR #19](https://github.com/andres-olguin/DELIA/pull/19) benchmark histórico sigue abierto. [PR #21](https://github.com/andres-olguin/DELIA/pull/21) Trust Fabric permanece **DRAFT**.
- [Foundation readiness](../foundation/readiness-controls.json) registra **13 controles, 0 formalmente verificados al corte**. Su verificador es estático, no un pentest ni certificación.

## 3. Decisión para el equipo

**Cerrar la VENTANA temporal Sprint 2, NO cerrar el issue #4 como `completed`.** Mantenerlo abierto como *aceptación pendiente / carryover*. Declarar Sprint 3 **ACTIVO EN CALENDARIO desde 09/11** y ejecutar dos líneas:

1. **Camino crítico seguridad y arquitectura heredado de S2:** #6 arranque/ORM → #7 auth/tenant → #8 logs/secretos → #9 sanitización obligatoria pre-egress → #10 threat model → #11 CI, con revisión E2E independiente. Sin esto: no producción, no datos reales, no claims de certificación.
2. **Nueva etapa S3 (09–22 noviembre):** capa de tráfico/rate limiting/cache Redis [solo si diseño no elude auth/DLP y no almacena PII sin protección], verificación de estrés con datos ficticios, y **workstream de identidad DANREXO** (#54), condicionado a búsqueda de marcas semejantes, propiedad intelectual, dominios, pruebas web y aprobación por dirección.

**Aclaración de marca:** DANREXO fue elegido como futuro nombre; no es marca registrada ni globalmente despejada. No renombrar repo, package o URLs por cuenta propia hasta autorización. Preservar trazabilidad TALIA → DELIA → DANREXO.

## 4. Orden de ejecución propuesto (fechas objetivo, no entregas comprometidas)

| Fecha | Entregable / responsable a confirmar | Evidencia requerida |
|---|---|---|
| **09/11** | Registrar acta y traspaso, revisar PR #20 | Documento + enlaces y comentarios; sin merge prematuro |
| **10–12/11** | Resolver inconsistencias de arranque, modelos y migraciones (#6); delinear auth/egress (#7–#9) | PR aislados y tests de import/DB no productivos |
| **11–15/11** | Benjamín: revisar T0162/T0163, holdout independiente y merge #20 **por su autor** tras revisión final; #11 después | SHA final, CI, política FP/FN y review; nunca cerrar #9 por ello |
| **13–18/11** | Implementar/revisar DLP pre-egress, auth/tenant, logs/secretos; en paralelo diseñar rate limiting Redis seguro | Test HTTP mock que comprueba **0 upstream requests** al bloquear; 401/403 y casos negativos |
| **16–20/11** | Redis/rate limit & cache con límites; QA de segundo tenant, timeouts y recuperación si P0 permite | CI, medición latencia/costo, no filtración cross-tenant, no caché de prompts sensibles sin política |
| **17–21/11** | Revisar BRAND-S3-01/02 con direccción; solo preparar inventario técnico de rebrand sin cambios irreversibles | Informes de marca, disponibilidad y decisión Go/No-Go; PR de inventario |
| **21–22/11** | Revisión técnica e instancia de cierre del sprint | Lista de cambios, QA, riesgos, evidencia y aprobación explícita; lo no hecho pasa al siguiente sprint |

**Responsables históricos en [roadmap](../roadmap.md):** Iván regex/DLP y ceremonias, Nilson modelos/Redis, dirección técnica Andrés, Isaac revisión ejecutiva. Son **asignaciones históricas planificadas, no confirmación de disponibilidad actual**. Benjamín aceptó seguir #11 después del PR #20; tareas #12/#55/#56 están asignadas en GitHub, pero deben secuenciarse según disponibilidad.

## 5. Gates para salir del carryover S2

- [ ] RUT CL y cédula/NIT CO: ejecutar suite reproducible, revisar casos negativos/falsos positivos y publicar límites.
- [ ] #6: arranque y ORM/migraciones auditables, sin import roto ni error de AuditLog; PR aceptado.
- [ ] #7/#8: auth y aislamiento aplicados al proxy/auditoría, secretos y logs minimizados, tests de rechazo.
- [ ] #9: upstream mock comprueba que el payload enviado está permitido/sanitizado o **no hay solicitud**; error/timeout/streaming no evaden controles.
- [ ] #10: modelo de amenazas + fail-safe aplicable al release.
- [ ] Revisión de ingeniería + aprobación ejecutiva sobre **solo el alcance probado**; acta con SHA, evaluadores y riesgos residuales.

**Importante:** cerrar el alcance de un detector aislado (#16) puede suceder antes que cerrar #4. La transición de calendario al S3 no depende de inventar un 100 % técnico del S2.

## 6. Fuente de verdad y seguimiento

- Sprint original: [docs/roadmap.md](../roadmap.md).
- [Issue #4](https://github.com/andres-olguin/DELIA/issues/4): aceptación del Sprint 2 (mantener abierto).
- [Issues #6–#11](https://github.com/andres-olguin/DELIA/issues): camino P0.
- [Issue #16 / PR #20](https://github.com/andres-olguin/DELIA/pull/20): MX/BO.
- [Issue #54](https://github.com/andres-olguin/DELIA/issues/54): branding S3 DANREXO.
- [Trello DELIA](https://trello.com/b/gZhMKd4R/delia): mover tarjetas solo al existir pruebas; evitar `Done` por haber pasado fecha.
- [Control de lanzamiento](../foundation/README.md): los tests sintéticos no certifican producción.

**Próxima revisión prevista:** 12/11/2026 y cierre del timebox S3: 22/11/2026.
