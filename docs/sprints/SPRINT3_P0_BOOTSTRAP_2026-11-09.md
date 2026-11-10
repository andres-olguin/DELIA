# Sprint 3 — Primer cambio ejecutable: P0 heredados (09/11/2026)

**Rama inicial:** `fix/s3-p0-bootstrap-failclosed-2026`. **Alcance:** seguridad preventiva del esqueleto de API e instalación de pruebas aisladas. El objetivo no es reclamar que el proxy funciona, sino **evitar que una ruta insegura heredada vuelva a reenviar datos** mientras se construye la política obligatoria. No se cambia el nombre del repositorio.

## Cambios de este primer PR

1. **Importaciones corregidas:** se deja de depender de módulos inexistentes `app.models.chat` y `app.services.*`. Se conservan `models/chat.py` y `services/` sin tocar PR #20.
2. **Cierre explícito de rutas expuestas:** `/proxy/v1/chat` y `/audit/` devuelven **HTTP 503**. Esto es un **corte deliberado de funcionalidad** para evitar egreso de datos sin auth/DLP; no es un gateway usable.
3. **No hay reenvío directo:** la función heredada `services.proxy.forward_request` también devuelve 503, sin crear cliente HTTP ni enviar Bearer del llamante.
4. **Sin auditoría insegura:** no se persisten prompts, respuestas o claves; `metadata.create_all` deja de ejecutarse al importar la aplicación.
5. **Base de datos:** ya no hay URL/contraseña implícita en el código: `DANREXO_DATABASE_URL` (o temporalmente `DATABASE_URL`) debe configurarse expresamente. La falta de URL produce 503 en dependencias de DB; modelos ORM existentes **no están migrados/alineados todavía**.
6. **Docker local:** contraseña de PostgreSQL obligatoria por variable y puerto vinculado solo a `127.0.0.1`. `.env.example` contiene placeholders, nunca secretos reales.
7. **Pruebas:** test de carga de aplicación, respuesta lab, no acceso /audit, no forward por ruta ni helper, test ORM con SQLite efímera y suite PII CL/CO; CI en 3.11/3.13 con dependencias explícitas.
8. **Guardrails Foundation:** escáner estático conserva detección de patrones heredados mediante fixture de regresión; que no aparezca una alarma estática **NO** significa que se haya probado la seguridad.

## Ejecución local aislada

```bash
python -m venv .venv
# activar venv según sistema operativo
python -m pip install -r requirements-bootstrap.txt
python -m pytest -q tests/test_api.py tests/test_models.py tests/test_pii.py
python -m unittest tests.test_foundation_doctor -v
python -m tools.foundation_doctor
python -m tools.foundation_doctor --require-production-ready  # falla intencionalmente
```

El `tests/conftest.py` define SQLite efímera para pytest. Nunca usar la base de datos de un cliente ni ejecutar la demostración con un token real. Iniciar `uvicorn app.main:app` solo para comprobar estado y rechazo, no para procesar solicitudes privadas.

## Lo que NO se ha terminado

- SEC-001: arranque **parcial**, faltan esquema de auditoría, Alembic y revisión de instalación externa.
- SEC-002: DLP pre-egress **sin implementar**; se ha bloqueado el egreso temporalmente.
- SEC-003: authn/authz, permisos y aislamiento tenant **no implementados**; no reemplazar 503 por 200 sin ellos.
- SEC-004: gestión de secretos/logs **parcial**; revisar infra y todas las rutas en futuro PR.
- SEC-005–008: migraciones, control de tools, idempotencia y verificación independiente aún **pendientes**.
- Redis/cache/rate limiting aún **sin activación**. Primero deben definirse identity, scopes, tenant boundaries y política de PII; cachear respuestas cruzadas sería un riesgo.
- DANREXO: marca elegida; inventario y clearance pendiente de #54/#56; no renombrar dominios, repo o endpoints por cuenta propia.
- PR #20: **Benjamín lo fusionará cuando cierre sus revisiones**, no se combina con este PR.
- No se concede licencia, compliance, piloto de datos reales, publicación de redes ni ingreso comercial.

## Próximo paso realmente útil

PR separado para **P0 #6** de modelos/auditoría/Alembic, seguido de **P0 #7/#9** con autenticación comprobada y pruebas de payload sintético sobre `httpx.MockTransport`. Reabrir el reenvío solo cuando controles denieguen por defecto, no haya ruta alternativa y se apruebe revisión independiente.

**Estado de salida de esta etapa:** `S3-P0-BOOTSTRAP_REVIEW` hasta pruebas y merge. `production_gateway: BLOCKED` hasta revisar SEC-001..SEC-008.
