# Plan TALIA → DELIA — migración compatible (propuesto)

**Corte:** 2026-10-31. Plan documental; no declara migración ejecutada ni soporte de versiones que no existen. 

## Inventario actual de dependencias

| Ubicación | Dependencia visible | Riesgo si se renombra sin migración |
|---|---|---|
| `app/main.py` | título y `system` «TALIA» | consumidores de salud e indicadores pueden comparar texto |
| `app/api/proxy.py` | `talia_request_id`, errores TALIA | clientes parsean propiedad o mensajes |
| `app/database.py`, `.env.example` | `talia_logs` | cambiar nombre DB no migra datos automáticamente |
| `docker-compose.yml` | contenedor `talia_postgres`, nombre DB | datos persistentes y scripts de operación dependen de nombre |
| `backend/logger.py` | `TALIA APP` | filtros de observabilidad y alertas |
| `research/`, `docs/roadmap.md` | identidad antigua, siglas inconsistentes | ambigüedad en documentación histórica |

## Propuesta por etapas

1. **Inventariar contratos reales:** APIs consumidas, bases existentes, rutas, volúmenes, clientes integrados y scripts, sin suponer que existen usuarios productivos.
2. **No renombrar la base de datos en el parche P0:** conservar nombres internos heredados con advertencia; eliminar contraseñas codificadas primero.
3. **Versionar respuesta:** publicar `delia_request_id` de manera aditiva y, si hubiera consumidores de `talia_request_id` confirmados, conservar alias durante una ventana de deprecación acordada. No eliminar un campo sin test de compatibilidad.
4. **Documentar período de transición:** anuncio, versiones, fecha propuesta, pruebas de lectura/escritura, rollback y aprobación humana; actualmente **sin fecha acordada**.
5. **Migración DB por revisión:** script idempotente, backup/restauración, migraciones Alembic/SQL firmadas, no `create_all` ciego en datos existentes.
6. **Actualizar títulos, logs, Compose y referencias:** después de pruebas, preservando documentos históricos TALIA como antecedentes marcados.
7. **Retirar alias antiguos:** solo después de confirmar ausencia de consumidores y aprobar los cambios por PR.

## Criterios de aceptación

- Pruebas de contrato de `/proxy/v1/chat`, endpoints auditables y documentación.
- Aprobación de cambios de campos/estructuras y rollback reproducible.
- No se pierden datos ni se exponen secretos; sólo se prueba con datos sintéticos hasta revisión de seguridad.
- Actualizaciones por PR y **nunca mediante cambios de código directos a main**.

**Seguimiento:** [Issue de identidad heredada](https://github.com/andres-olguin/DELIA/issues/5) y [baseline P0](https://github.com/andres-olguin/DELIA/issues/6).
