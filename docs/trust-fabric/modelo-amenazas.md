# Modelo de amenazas DELIA Trust Fabric — STRIDE + riesgos de agentes

Versión 0.1, 2026-11-09. Sistema en desarrollo. Fuentes base: OWASP Top 10 for Agentic Applications 2026 (https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), OWASP Agent Control Standard (https://genai.owasp.org/initiatives/agentic-security-initiative/), NIST AI RMF. Utilizar como referencias, NO afirmar conformidad.

## Activos
Credenciales API; tokens y aprobaciones; datos personales; instrucciones de sistema; prompts; herramientas de pago/CRM; políticas por tenant; claves de cifrado; recibos y logs; modelos/archivos cargados. Actores: usuario humano, agente, integrador, proveedor LLM, aprobador, operador de plataforma, atacante externo, tercero de cadena de suministro.

## Matriz riesgo → control → evidencia
| Riesgo | Impacto | Control objetivo | Prueba negativa / evidencia |
|---|---|---|---|
| Suplantación de agente o aprobador | Crítico | Identidad verificable, session binding, MFA para aprobación | Tokens ausentes/expirados/reutilizados → 401/403 |
| Escalada entre tenants | Crítico | Tenant servidor derivado, query filters, row-level controls | A accede a B → denegado |
| Tool misuse / prompt injection | Crítico | Allowlist y política antes de adapter, argumentos validados | Prompt malicioso pide borrar datos → herramienta NO ejecutada |
| Bypass entre decisión y ejecución (TOCTOU) | Crítico | Hash de args+policy, consumo atómico y timeout | Argumentos cambiados o aprobación repetida → DENY |
| Fuga al proveedor | Crítico | DLP obligatorio pre-egress y rechazo por formato desconocido | Requests con PII sintética → upstream mock sin PII prevista |
| Exfiltración por logs | Alto | Minimización, truncamiento, no raw payload por defecto | Búsqueda de sentinel secreto en logs → 0 |
| Trazas falsas/incompletas | Alto | Recibos encadenados, HMAC en KMS y timestamps | Mutar campos/eventos → verificación falla |
| SSRF/DNS rebinding | Crítico | URL allowlist + resolución validada + TLS/timeout | Host local/metadata/redirect inesperado → bloqueado |
| Data poisoning / RAG injection | Alto | Proveniencia, separación instrucciones/datos y permisos | Documento exige cambio de política → denegado |
| Rogue agents y cascadas | Alto | Límites de iteraciones, presupuesto, kill switch | Bucle infinito ficticio → corte controlado |
| Aprobación coercitiva/humano confuso | Alto | Vista mínima de acción exacta, doble chequeo, separación de roles | Aprobador no ve importe/cambio → no aprobar |
| Marketplace supply chain | Alto | Firmas de paquetes, SBOM, permisos declarados y revisión | Paquete unsigned/comprometido → no instalar |
| Error de integración | Crítico | Test E2E con adapter que no permite bypass | Si policy engine cae, herramienta NO ejecutada |
| Reidentificación de tokens | Alto | Vault cifrado, acceso por finalidad, TTL, logs mínimos | Acceso cruzado a token → negado |
| Falsos positivos DLP | Medio | Benchmarks independientes, modo revisión con datos sintéticos | Caso no sensible bloqueado → tasa registrada |
| Falsos negativos DLP | Crítico | Corpus multi-jurisdicción + revisión humana | Variantes no reconocidas → registrar omisión, no prometer 100 % |

## Riesgo residual del prototipo actual
El motor del laboratorio no autentica el `tenant_id` ni el `approver_id`; por ello un llamante malicioso puede atribuirse roles. Solo se deben presentar sus resultados como **pruebas del algoritmo de política**, no como protección contra actores reales. Su almacenamiento en memoria no aporta consistencia multi-proceso ni preservación forense. Un recibo HMAC no garantiza implementación del bloqueo fuera del proceso.

## Gates de seguridad
S0 (laboratorio): datos sintéticos, no network, sin credenciales reales. S1 (alfa): auth+tenant real, tests cross tenant, policy enforcement en adaptadores; no PII externa. S2 (beta de piloto autorizado): prueba de egress, logs mínimos, cifrado, retención, restores, monitoreo, asesoría legal, consentimiento y aceptación de riesgos. S3 (producción): pruebas externas, SLAs negociados, seguridad operacional, backups, continuidad y plan de incidentes.

## Protocolo de vulnerabilidades
Seguir `SECURITY.md`; nunca publicar payloads de terceros ni logs sensibles en issues públicos. Hallazgos críticos bloquean releases y requieren revisión fuera de GitHub público cuando contengan datos sensibles.
