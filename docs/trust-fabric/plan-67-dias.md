# DELIA — plan acelerado de 67 días hacia beta avanzada

**Inicio:** lunes 9 de noviembre de 2026. **Fecha objetivo máxima:** viernes **15 de enero de 2027**. Duración: 67 días calendario. Meta: **beta avanzada condicionada**, no promesa de disponibilidad productiva, certificación o cobertura completa de veinte iniciativas. Este plan reemplaza la *prioridad de ejecución* del Gantt anterior, sin declarar completados sprints antiguos.

## Premisa de capacidad
Plazos sujetos a disponibilidad aceptada por cada colaborador, revisiones de seguridad y bloqueo de integraciones. No asignar tareas automáticamente por cargo ni usar sueldos ficticios. Si hay menos de 2 desarrolladores equivalentes a tiempo completo, recortar alcance de beta o reducir superficies. Mantener un único camino crítico: auth/tenant → DLP egress → policy enforcement → approval → audit → QA.

## Calendario por hitos
| Fase | Fechas | Entregables concretos | Gate de salida |
|---|---|---|---|
| 0. Línea base | 09–15 nov | Branch + PR, inventario amenazas, PR #19/#20 revisados, 3 demos sintéticas, CI Python | Sin bypass conocido de pruebas de laboratorio; P0 priorizados |
| 1. Núcleo protegido | 16–29 nov | Reparar importaciones/modelos, auth real, secreto externo, tenant isolation, sanitizer obligatorio antes de upstream, fixtures de contratos | 401/403, negativos, no PII prevista en egress mock, no credenciales en logs |
| 2. Agentes controlados | 30 nov–13 dic | Adapter de herramientas con deny-first, rol/scopes, approval durable, consumo atómico, políticas versionadas y revisión de reglas | Pruebas de replay, escalamiento, TOCTOU, cross-tenant y concurrencia |
| 3. Operación avanzada | 14–27 dic | Control plane y consola con Policy Studio mínimo, auditoría duradera sin PII, dashboard multitenant, API OpenAPI | Screenshots sintéticos, API contract tests, migraciones/backup/restauración |
| 4. Integraciones y aseguramiento | 28 dic–10 ene | 2 adapters priorizados, benchmark regional independiente, mocks de streaming y salida, sandbox, red-team sintético, observabilidad p95/costos | Regression gates, fail-closed, rendimiento medido, runbook y SBOM |
| 5. Beta avanzada | 11–15 ene | Ensayo de entrega, demo 12 min, demo 30 min, onboarding ficticio y 1–3 pilotos **solo si P0 y contrato habilitan**, propuesta comercial | Go/No-Go firmado: seguridad, exactitud, identidad, auditoría, soporte y costo medidos |

## Objetivos de estado por 15 de enero
**Beta avanzada P1**: TF-02/03 (PII regional con benchmark medible), TF-06/07/08 (agentes y aprobación real), TF-10/11/12/14/15 (sandbox, recibos, políticas, métricas y red-team), TF-05 **solo** ruta mínima de proveedor autorizada. TF-01/04/09/13/17/19: especificación y PoC si hay capacidad. TF-16/18/20: investigación y prototipo de laboratorio, **no** prometer funcionalidad operativa en enero. Las veinte ideas permanecen trazadas y financiables como portafolio, pero no todas pueden considerarse entregadas.

## Cronograma semanal de ingeniería
- **09 nov:** branch Trust Fabric, motor local, pruebas, documentación comercial; CI ejecutado. No integra main.
- **10–13 nov:** integrar no-regresión del corpus histórico y PR #20, revisar PR #19; diseñar P0 de tenant/auth/egress.
- **14–15 nov:** demo sintética y revisión arquitectónica formal; backlog con owners aceptados.
- **16–22 nov:** auth OIDC o API keys seguras con tenant derivado; Postgres migrado; logs minimizados; test cross-tenant.
- **23–29 nov:** DLP obligatoria en `/proxy/v1/chat`, upstream simulado, tamaños, timeouts y bloqueo de formatos desconocidos.
- **30 nov–06 dic:** ejecución de herramienta encapsulada, aprobaciones transaccionales e idempotencia.
- **07–13 dic:** policy versioning + tests de conflicto, caso demo reembolso con supervisor.
- **14–20 dic:** consola de política y aprobaciones, auditoría durable sin prompt crudo.
- **21–27 dic:** métricas y alertas, rollback, backup; revisión de accesibilidad.
- **28 dic–03 ene:** integración seleccionada con proveedor/MCP bajo permisos, streaming simulado, evaluación independiente.
- **04–10 ene:** pruebas adversariales, fuzzing sintético, carga 1/10/50 concurrentes, SLO exploratorios y hardening.
- **11–15 ene:** revisión de seguridad externa cuando sea viable, ensayos comerciales, capturas reproducibles, documentación de instalación y Go/No-Go.

## Gobernanza diaria
- Pull request pequeño y revisable; `main` protegida, sin commit directo.
- Daily asíncrono en tarjeta del proyecto solo si útil: «qué cambió», «prueba», «bloqueo», «siguiente acción».
- Revisión técnica de interfaces y seguridad dos veces por semana; demo de estado cada 7 días.
- No cerrar tarjetas por commits; gates con evidencia.
- Incorporar disponibilidad de Benjamín, Iván, Isaac, Andrés y Nilson solo tras aceptar tarea. Ninguna contribución gratuita se presupone obligatoria.

## Plan de contingencia (si falla un gate)
A. Falla autenticación: detener todo piloto real, seguir demo sintética offline. B. Falla PII: limitar producto a decisión de herramientas hasta corregir DLP. C. Falla aislamiento: desactivar multi-tenancy, solo entorno mono-organización aislado de laboratorio. D. No hay tiempo de UI: CLI verificable + demo API local, no fingir dashboard completo. E. Sin compradores entrevistados: no publicar precios definitivos ni proyección de ingresos como validada.

## Métricas de entrega — metas, NO hechos
- 0 operaciones prohibidas ejecutadas en fixtures de herramientas (no basta respuesta del motor).
- 0 bypass de DLP en conjunto sintético definido, con FN/FP visibles.
- Latencia p50/p95/p99 medida por ruta y carga, no estimada.
- 0 secretos ni textos sensibles completos en logs bajo pruebas; threat model revisado.
- 100 % de casos P0 automatizados en CI; sin regresión histórica de 172 casos sin explicar.
- 3 entrevistas de compra por país priorizado como mínimo exploratorio, 1 piloto por integración si existe capacidad y seguridad.

## Dependencias de terceros
Planificar API keys, infraestructura, proveedores, legal, hosting y presupuesto como **pendientes de aprobación**. No usar clientes reales ni cuentas productivas para evitar retrasos. Revisión de benchmarks comerciales por fuentes independientes; competencia evoluciona.

## Definición de No-Go
No publicar beta con datos reales si hay errores de auth, bypass egress, restauración sin permiso, secreto expuesto, pérdidas de auditoría o acciones no autorizadas. El 15 de enero es fecha de evaluación **no un permiso para saltar controles**.
