# Contratos, dependencias y compatibilidad con DELIA existente

## No romper el repositorio actual
- No sobrescribir `app/main.py`, `app/api/proxy.py`, `backend/dlp/pii.py` ni `services/proxy.py` en este PR: pertenecen al plano actual con issues P0 abiertos y PR #20 pendiente.
- Nuevo prototipo en `trust_fabric/` sin rutas públicas ni efectos en sistemas externos.
- Antes de integrar, revisar el PR #19 (benchmark #12) y PR #20 (detectores #16). Rebase con cuidado, ejecutar corpus histórico y nuevo; no reapropiar trabajo de colaborador ni forzar cambios en su rama.
- Interacción futura con DLP mediante adaptador que reciba texto/estructura, y produzca `sanitized`, `findings`, `policy_version`, `rejected`, no datos sensibles en logs.

## Contrato de tool-call
Campos mínimos: `tenant_authenticated`, `agent_principal`, `tool_id`, `validated_arguments`, `policy_revision`, `correlation_id`. En el simulador, los tres primeros son texto declarado y por ello **NO equivalen a identidad confiable**. El adapter de producción crea un objeto con tenant y agente del token del servidor, nunca del cuerpo.

## Contrato de aprobación
Ticket asociado a fingerprint canónico de herramienta+parámetros+tenancy+versión+solicitante, TTL, aprobador distinto, scopes autorizados, consumo atómico, ventana antifraude, idempotencia. El simulador almacena los tickets en RAM; para producción usar transacciones con bloqueo optimista/serializable y rediseñar manejo de caídas.

## Contrato de recibos
Mínimo: id, tenant seudonimizado, agente seudonimizado, herramienta, versión de política, decisión, hash de argumentos, timestamp y firma. Nunca texto original. Retención, verificabilidad externa, canal de exportación y cadena de integridad por demostrar.

## Contrato de marketplace
Instalar solo bundles verificados con firma de publicador, compatibilidad de runtime y contrato de permisos; rollback y prueba de revocación. Nunca autoejecutar plugins descargados del catálogo.

## Mapa integraciones a explorar, no implementadas
- OpenAI/Anthropic: adaptadores via backend existente con allowed upstreams, timeouts y soporte de streaming (condicional).
- MCP: inventario, permisos por nombre y parámetros de tool; validar esquema de recursos y trusted server.
- CRM/ERP: fuentes de eventos bajo consentimiento y scopes; no almacenar secretos de cliente en repo.
- Slack/Teams/WhatsApp: aprobaciones con autenticación real y antifraude, no aceptar «OK» de cualquier mensaje.
- OIDC: proveedor empresarial, validación de issuer/audience y key rotation.
- Storage: Postgres/Redis cifrado y RLS según arquitectura; no asumir que un hash sustituye cifrado.

## Estrategia de compatibilidad TALIA→DELIA
Conservar compatibilidad mientras existan clientes e integraciones que usen nombres `talia_*`; versionar API, documentar deprecación, pruebas de dual-reading/migración y revisión de datos existentes. No eliminar nombres de tablas «por estética».
