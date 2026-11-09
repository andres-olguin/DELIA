# Las 20 capacidades DELIA Trust Fabric — catálogo auditable

Versión: 2026-11-09. **No confundir visión, prototipo y control productivo.** Marcas: `LAB` = demostrable en simulación, `PR` = existe en PR separado, `PLAN` = diseño, sin implementación completa. Prioridades P0 bloqueante, P1 beta avanzada, P2 versión posterior, P3 investigación.

| ID | Capacidad | Estado 09-11 | Prioridad | Criterio de aceptación y evidencia mínima |
|---|---|---|---|---|
| TF-01 | Privacy Vault: pseudónimos reversibles | PLAN | P2 | Cifrado autenticado con claves por tenant, rotación, retención/borrado, recuperación autorizada y prueba de aislamiento |
| TF-02 | Context Engine: PII contextual | PLAN; regex históricas existentes | P1 | Aciertos, omisiones y falsos positivos por país en corpus independiente; explicación por regla |
| TF-03 | LATAM Intelligence | PR #20 MX/BO; CL/CO parcial en main | P1 | RUT/NIT/CURP/RFC/CI por país, fuentes verificadas y versión de reglas, idiomas español/portugués |
| TF-04 | Multimodal Shield | PLAN | P2 | PDF/imágenes/tablas sintéticos, análisis de escapes y oclusión; no prometer detección universal |
| TF-05 | Sovereign Router | **LAB**: planificación sin red | P2 | Tabla explícita de destinos autorizados por país, región, proveedor y sensibilidad; rutas egress testeadas |
| TF-06 | Agent Firewall | **LAB**: decisión antes de ejecutar, sin adapter | P0/P1 | Deny-by-default, allowlist, políticas tenant, tests sobre adapter que no ejecuta operaciones denegadas |
| TF-07 | Human Approval | **LAB**: aprobación ligada y de único uso | P1 | Separación real de identidad, TTL, aprobador independiente, antifraude TOCTOU y persistencia transaccional |
| TF-08 | Agent Identity | LAB: roles declarados; NO autenticación | P0 | Credenciales temporales, autenticación mTLS/OIDC, scopes por herramienta, rotación y pruebas cross-tenant |
| TF-09 | Chain Guardian | PLAN | P2 | Propagación de restricciones en delegaciones y pruebas de rechazo de ampliación de privilegios |
| TF-10 | Agent Sandbox | **LAB**: herramientas ficticias en memoria | P1 | Adaptadores mock sin recursos reales, dry-run comparable con llamada real |
| TF-11 | Proof of Protection | **LAB**: recibos HMAC minimizados sin persistencia | P1 | Cadena auditada durable, timestamps confiables, rotación y verificación externa, retención y prueba de integridad |
| TF-12 | Policy Studio | LAB: modelo declarativo Python; UI PLAN | P1 | Versionado, conflictos, aprobación de políticas, simulación y rollback seguro |
| TF-13 | Compliance Navigator | PLAN | P2 | Trazabilidad control→obligación con fuente/fecha/jurisdicción; validación jurídica; sin certificación automática |
| TF-14 | Risk Observatory | **LAB**: agregación de decisiones en memoria | P1 | Dashboard protegido, agregados sin PII, p95, incidentes, alertas y acceso por tenant |
| TF-15 | Continuous Red Team | **LAB**: escenarios negativos sintéticos; servicio PLAN | P1 | Corpus versionado, ataques autorizados, gates CI, trend de regresiones y revisión humana |
| TF-16 | AI Security Twin | PLAN | P3 | Replica sintética de políticas, simulación reproducible de impactos sin sistemas productivos |
| TF-17 | Data Passport | **LAB**: etiquetas/finalidades locales, sin enforcement | P2 | Etiquetas de finalidad, origen, retención, consentimiento y control de propagación por adapter |
| TF-18 | Autonomous Response | PLAN | P3 | Contención reversible, permisos de activación y controles contra falsos positivos |
| TF-19 | Trust Score | PLAN | P2 | Explicación de cada submétrica, incertidumbre y fuentes; jamás calificación inventada |
| TF-20 | Security Marketplace | PLAN | P3 | Paquetes firmados, SBOM, pruebas, aislamiento, compatibilidad y revisión de terceros |

## Lectura de estados
- TF-06/07/10/11 tienen **solo núcleo de simulación** en `trust_fabric/`; es incorrecto decir «firewall enterprise listo», «aprobación segura por web», «log inmutable» o «sandbox de ejecución».
- TF-08 no tiene identidad verificada: `tenant_id`, `role` y `agent_id` son datos introducidos por el llamante. La política separa dominios lógicos, no garantiza aislamiento en red.
- TF-02/03 no deben mezclar la medición histórica de 172 casos con el corpus nuevo de 96.
- TF-12 solo define reglas como objetos; faltan DSL revisada, consola UI, esquema persistente y flujo de cuatro ojos.
- TF-15 no implica pentesting ni ataques sobre servicios ajenos: hoy son tests unitarios con datos sintéticos.

## Orden de ejecución por dependencia
1. P0 base `#6` arranque, `#7` auth/tenant, `#8` secretos/logs, `#9` sanitización egress, `#11` CI.
2. Identidad verificada y políticas sin bypass (TF-08, TF-06), reglas regionales medibles (TF-02/03) y evaluación E2E.
3. Aprobaciones con almacenamiento y concurrencia (TF-07), Policy Studio (TF-12), evidencia mínima (TF-11) y tablero (TF-14).
4. Red team sintético e integración con adapters (TF-15/10), demo multitenant con límites documentados.
5. TF-01/04/09/13/19 al alcanzar capacidad y pilotos; TF-16/18/20 como R&D posterior.

## Backlog épico sugerido para GitHub (sin asignaciones impuestas)
Para cada TF crear tickets separados de **diseño, implementación, pruebas y revisión de seguridad**. Campos mínimos: DRI aceptado, reviewer, dependencias, threat model, criterios negativos, evidencias SHA/run/benchmark y fecha acordada. No abrir 80 issues duplicados sin revisión del tablero previo. Etiquetas sugeridas `TF/P0` etc. Toda función se identifica por ID para conservar trazabilidad.

## Definición de más que MVP: beta avanzada
Una beta avanzada tiene interfaz operativa, API autenticada, controles de egreso probados, política versionada, aprobaciones durables, evidencias minimizadas, observabilidad por tenant, documentación y una demo E2E con datos sintéticos. **No necesita tener completas las veinte iniciativas para recibir el nombre beta avanzada**, ni puede llamarse producción por ello. Se prohíbe cambiar el estado de una capacidad por publicar un archivo o stub.

## Anexo de empaquetado sectorial (09/11/2026)

Se añadieron **4 manifests verticales de laboratorio**, sin identidad de usuario real ni tools externos, en `trust_fabric/packs/`: integradoras, SaaS B2B, ecommerce y contact centers. Se cargan mediante `trust_fabric/sector_packs.py` y pueden inspeccionarse con `python -m trust_fabric.packs_demo`. Es una prueba de empaquetado de políticas, **no cuatro soluciones desplegadas**. Su estado es `LAB`; ver [sector-packs.md](sector-packs.md).
