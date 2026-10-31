# DELIA — Revisión de seguridad por archivo y líneas del parche P0 (Ronda 4)
**Fecha:** 2026-10-31. **Ámbito:** parche local `DELIA_fix_p0_baseline_2026-10-31.patch` de 12 archivos, SHA-256 `4274770fe70008f482d05fd284a31c37c1bcb151fb16db7824147d2e7be2c78b`. **Sin rama ni PR por ruleset #18:** este texto es el **comentario de revisión PREPARADO, NO PUBLICADO EN PR**. No afirma revisión formal aprobada. Revisar cada línea o intervalo listado contra diff real en rama antes de aprobar.

## Leyenda y puerta de salida
- **MEJORA PARCIAL**: cambia una exposición concreta; no certifica seguridad.
- **RIESGO ABIERTO**: falta control o prueba para entornos sensibles.
- **BLOQUEADOR**: mantener fuera de producción y de pilotos reales hasta cierre verificable.
- Fuentes: [auditoría Ronda 3](REGISTRO_INVESTIGACION_RONDA3_2026-10-31.md), [issues P0 #6–#11](https://github.com/andres-olguin/DELIA/issues), [TALIA→DELIA](PLAN_MIGRACION_TALIA_DELIA_2026-10-31.md), revisión manual del patch local 31/10/2026. Líneas refieren a archivos propuestos, no a `main`.

## Líneas y hallazgos
| Archivo y líneas propuestas | Revisión concreta de autenticación, aislamiento, logs, secretos, fallos, inyección, dependencias |
|---|---|
| `app/security.py:1–3` | **MEJORA PARCIAL**: `hmac`, `os` y excepciones FastAPI; no dependencia externa criptográfica. |
| `app/security.py:5–8` | Llave por entorno, ausencia →503. **RIESGO ABIERTO:** no rotación, KMS, identidad individual, múltiples claves ni comprobación de robustez de secreto. |
| `app/security.py:9–12` | 401 sin Bearer, 403 token incorrecto, comparación constante. **RIESGO ABIERTO:** ataques de fuerza bruta, rate limiting, longitud máxima del header no definidos; política de TLS y proxy TLS externo por evaluar. |
| `app/security.py:13–14` | **BLOQUEADOR**: retorna booleano sin identidad de tenant, scope, rol ni API key separada; una sola llave ve toda la auditoría. |
| `app/database.py:1–3` | Elimina import obsoleto de `declarative_base`, reduce warnings; no resuelve seguridad de conexión. |
| `app/database.py:5–10` | **MEJORA PARCIAL**: sin DSN con password hardcoded; producción exige `DATABASE_URL`. **RIESGO ABIERTO:** SQLite local por defecto y DSN no validada ni TLS de DB garantizado. No confundir esto con migración segura de PostgreSQL. |
| `app/database.py:11–19` | Sesión cerrada en `finally`, excepción de DB no filtrada. **RIESGO ABIERTO**: pool, timeouts, rollback y prueba de pérdida de DB faltantes. |
| `app/main.py:1–10` | Corrige imports y evita `Base.metadata.create_all` al inicio. **BLOQUEADOR**: migraciones Alembic verificadas todavía no existen, los esquemas históricos TALIA pueden diferir. |
| `app/main.py:12–14` | Endpoint salud indica explícitamente no productivo; evitar mostrar endpoint de salud con datos de infraestructura. |
| `app/main.py:16–23` | Protección de escritura audit, DTO filtrado. **BLOQUEADOR**: nadie verifica scopes/tenant; error de DB puede filtrar comportamiento de backend y dejar estado inconsistente. |
| `app/main.py:25–31` | Lectura audit autenticada y límite 1–100. **BLOQUEADOR**: lectura global para portador de llave; no consultas por tenant. |
| `app/schemas.py:1–5` | `extra='forbid'` impide pasar `prompt` o `response` arbitrarios en nuevo DTO. |
| `app/schemas.py:6–10` | Restricciones para campos, pero `agent_name`, `model_used`, `status` siguen libres: posible PII/inyección en metadatos o cardinalidad excesiva. Exigir enums y política de registros. |
| `app/schemas.py:12–15` | Respuesta sólo con metadatos. **BLOQUEADOR**: `app/models.py` histórico todavía contiene columnas `prompt` y `response`; requieren migración, retención/borrado sujeto a política y controles de acceso. |
| `app/api/proxy.py:1–12` | Imports consistentes y dependencia de llave en router. **RIESGO ABIERTO:** dependencia compartida de laboratorio, sin cuota, identidad ni tenant. |
| `app/api/proxy.py:14–23` | 422 para streaming/extra y allowlist de modelo por entorno. **RIESGO ABIERTO:** configuración y validación de modelos, tamaño en bytes y tokens totales, políticas por tenant no existen. |
| `app/api/proxy.py:25–29` | Ruta de bloqueo no registra raw text. **RIESGO ABIERTO:** `PROMPT_BLOCK_TEST` es una prueba de humo y NO una política empresarial. Fallos DB en ruta de bloqueo no están controlados. |
| `app/api/proxy.py:31–37` | Redacta TODOS los `message.content` antes del upstream y falla cerrado si detector produce excepción. **BLOQUEADOR**: detector deja sin detectar 79/150 positivos del corpus previo; no filtra URL, metadata, herramientas, archivos, imágenes, ni respuestas del proveedor. `extra` rechazado, lo cual reduce (no elimina) fuga. |
| `app/api/proxy.py:39–40` | **MEJORA PARCIAL**: no reenvía bearer del cliente; upstream toma secreto propio. No incluye prueba contra mitm/egress de red. |
| `app/api/proxy.py:41–45` | Registra sólo evento sin contenido; **BLOQUEADOR**: `db.commit()` ocurre DESPUÉS del envío, por lo que una falla de DB no impide que se haya enviado contenido; el resultado de proveedor puede incluir texto sensible sin control de salida. |
| `services/proxy.py:1–7` | URL única fija y HTTPS reduce SSRF por URL arbitraria. **RIESGO ABIERTO:** egress firewall, DNS pinning, dependencia de SDK y allowlist de modelos deben validarse. |
| `services/proxy.py:9–15` | Secreto upstream sólo por entorno; header cliente no se usa. **RIESGO ABIERTO:** protección de variables, rotación, vault, mínimo privilegio y almacenamiento de logs upstream no demostrado. |
| `services/proxy.py:16–20` | HTTPX timeout 30s, redirects deshabilitados, `raise_for_status`. **RIESGO ABIERTO:** proxy del entorno y variables de red, límites de tamaño de respuesta, cuotas y contenido de respuesta. |
| `services/proxy.py:21–26` | Traducción genérica 502/504 sin exponer cuerpos upstream: mejora control de errores; reintentos/circuit breaker y telemetría sin PII pendientes. |
| `services/audit.py:1–3` | Corrige import; no lógica nueva de seguridad. |
| `services/audit.py:11–26` | UUID sintético y bandera de prueba; no se accede a DB en función. **BLOQUEADOR:** no sustituye revisión de inyección de prompts, políticas de herramientas, autorización de acciones o DLP. |
| `models/chat.py:1–7` | Rechaza propiedades inesperadas por mensaje, role regex y longitud 12.000 caracteres. **RIESGO ABIERTO**: texto puede contener instrucciones maliciosas y PII no detectada. |
| `models/chat.py:9–16` | Modelo y número de mensajes acotados, control de temperatura y tokens; `extra` aún permitido en DTO pero se rechaza en router. **RIESGO ABIERTO:** límites de CPU, rate limits y payload total. |
| `tests/conftest.py:1–11` | Llaves sintéticas en fixtures, no credenciales reales. **RIESGO ABIERTO**: monkeypatch global de SQLAlchemy, pruebas compartidas pueden interferir; ver suites completas. |
| `tests/test_api.py:1–18` | Fixture SQLite, crea tablas sólo en tests. Al quitar create_all de app, migraciones siguen pendientes. |
| `tests/test_api.py:20–33` | Pruebas reales de 401/403 y rechazo de prompt crudo; faltan pruebas de acceso cruzado entre tenants y claves rotadas. |
| `tests/test_api.py:35–51` | Mock confirma sanitización email sintético y rechazo de streaming; faltan CURP, RFC, CI/NIT BO, falsos negativos, archivos, cabeceras, respuesta upstream, logs reales. |
| `.github/workflows/pytest.yml:1–8` | Evento pull_request hacia main y workflow_dispatch; permisos mínimos `contents:read`. **NO EJECUTADO EN GITHUB** por bloqueo rama/PR. |
| `.github/workflows/pytest.yml:10–25` | Python 3.11, timeout 12 min, pip y pytest. **RIESGO ABIERTO**: GitHub Action uses tags y no digest de commit, lock de hashes ausente, versiones/fuentes de dependencias deben verificarse, acción no ha corrido ni reportado cobertura. |
| `requirements.txt:1–7` | Pins exactos de paquetes. **RIESGO ABIERTO**: no lock/hash transitivo, SBOM ni `pip-audit`; vulnerabilidades y disponibilidad CI no comprobadas. |

## Pruebas realmente ejecutadas en laboratorio
```
Python 3.13.5 — copia reconstruida de código main + propuesta, no clon/CI:
python -m pytest -q tests/test_api.py
...... [100%]
6 passed, 2 warnings in 0.41s
```
Los warnings se originan en `datetime.utcnow()` de SQLAlchemy `app/models.py` no migrado. **No se ejecutó suite completa**, Python 3.11, Docker/Postgres, migración, pruebas e2e de red, estrés, pentest, ni GitHub Actions; no presentar esto como aprobación P0.

## Revisión humana obligatoria antes de aprobar el PR
1. **Crítico:** identidad y autorización por tenant; test A→B denegado sobre auditoría, agentes, presets y cuotas.
2. **Crítico:** cubrir 79 FN y aplicar sanitización real antes del egress, incluyendo variantes de payload y respuesta; prohibir uso real mientras recall sea deficiente.
3. **Crítico:** migración con backfill/retención/borrado controlado de las columnas antiguas `prompt`/`response`; compatibilidad histórica TALIA.
4. **Crítico:** auditar `backend/network_utils/replay_session.py` anterior porque todavía imprime URL completa con posible query token; no modificado en este parche.
5. **Alto:** manejo de fallos de DB antes/después del egress, transacciones, auditoría y errores que puedan contener secretos.
6. **Alto:** secreto upstream, allowlist de destinos/red, TLS, proxy corporativo, límites de tamaño, rate limiting, ataques por prompts y herramientas.
7. **Alto:** inspeccionar dependencia Python/CI y ejecutar suite completa sin secretos con reportes reales.
8. **Alto:** revisar control de salida, retención de datos y consentimiento antes de pilotos.

**Decisión propuesta:** abrir como PR **borrador** cuando el ruleset permita crear rama, comentar este análisis en PR y **solicitar cambios** hasta cerrar P0. Nunca fusionar automáticamente. Esta revisión no ha sido publicada en GitHub como comentario de PR porque el PR no existe.
