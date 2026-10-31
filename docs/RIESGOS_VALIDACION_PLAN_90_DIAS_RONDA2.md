# DELIA — Riesgos P0/P1, puertas de validación e hipótesis alternativas

**Corte:** 31/10/2026. Las horas son **estimación de ingeniería (EP)**, no tareas presupuestadas, compromisos de colaboradores ni cotización. El código en `main` no fue sometido a ejecución E2E/seguridad en este estudio. Consultar [auditoría previa](INTELIGENCIA_MERCADO_GO_TO_MARKET_CL_MX_CO_BO_2026-10-31.md) y [roadmap actual](roadmap.md), que contiene metas aún no demostradas.

## 1. Backlog técnico ordenado por riesgo

| Prioridad | Sistema | Evidencia del código | Esfuerzo EP | Puerta | Definición de terminado |
|---|---|---|---|---|---|
| P0 | **Trazabilidad código y arranque** | Imports app.models.chat y app.services no coinciden con árbol; AuditLog no coincide con kwargs de proxy | 10–22 horas | Bloqueante | Smoke test desde clon limpio; compilación e importación sin fallo; test POST bloqueado permitido con estructura consistente |
| P0 | **Autenticación, autorización y tenant isolation** | GET/POST /audit sin auth explícita; modelos multiempresa no garantizan aislamiento | 30–60 horas | Bloqueante | Tests negativos de token inválido, lectura otra empresa, enumeración, roles y claves |
| P0 | **Protección de logs y secretos** | AuditLog almacena prompt/response; DB URL con credencial literal; logs/errores a revisar | 20–40 horas | Bloqueante | Minimizar por defecto, secretos vía env/secret manager, retención definida, pruebas sin datos reales |
| P0 | **Sanitización antes de egress** | redact() solo en módulo de backend sin conexión al forward_request HTTPX | 24–48 horas | Bloqueante | Test de proveedor simulado rechaza/oculta PII según política; no se transmiten datos sin control en laboratorio |
| P0 | **Threat model y fail-safe** | Definir egress, fallas de motor, acceso y uso permitido de upstream | 16–32 horas | Bloqueante | Tabla amenazas; política fail-closed para datos marcados; handling y autorizaciones verificadas |
| P0 | **Pipeline tests, regresión y versiones** | Tests escritos sin ejecución verificada; sin evidencia de CI en este estudio | 16–32 horas | Bloqueante | pytest reproducible, suite CI, dependencias fijadas y casos negativos |
| P1 | **Benchmark sintético regional** | No hay resultados medidos de precision/recall vs Presidio/Cloudflare/Model Armor | 30–60 horas | Antes de claims comerciales | Dataset aprobado y etiquetado, versiones, resultados FP/FN por tipo y error bars |
| P1 | **Self-host reproducible** | Docker Compose/DB y configuración de despliegue sin runbook operable probado | 20–45 horas | Antes de piloto técnico | Instalación desde clon limpio, rollback, backup, monitoreo, gastos por request |
| P1 | **Rate limits y cuotas** | Objetivos Redis/cost del roadmap no aplicados por usuario/tenant | 24–45 horas | Antes de suscripción | Tests de cuota, key rotation, bypass, métricas por tenant |
| P1 | **Comparabilidad comercial y soporte** | No hay documentación cliente, seguridad contrato ni SLA medidos | 20–40 horas | Antes de SaaS pagado | DPA consultado, manual integración, límites soporte, factura y pricing model |
| P1 | **IDs México/Bolivia** | CURP/RFC y CI/NIT BO no existen en pii.py | 24–60 horas | Después de entrevistas país | Casos legales sintéticos, validación autoridad de formatos, benchmark positivo/negativo |
| P1 | **Fallback streaming y observabilidad** | Upstream estático; streaming/fallback del roadmap no está verificado | 40–80 horas | Segunda etapa del MVP | Tests E2E SSE, timeout, retry sin doble cobro, errores controlados |

**Rangos de esfuerzo:** no sumarlos como presupuesto sin asignación y estimación técnica en equipo. P0 estimados suman entre **116 y 234 horas** si son actividades independientes; integración/QA podría variar considerablemente. Revisar dependencias y pruebas de seguridad. P1 puede superponer esfuerzos. Estos números no se derivan de velocidad histórica de MasterTech; son heurísticas para ordenar el backlog.

**Secuencia recomendada frente al roadmap:** Sprint 2 (PII) debe limitarse a detector reproducible y autorización segura; Sprint 3 cuotas/costo solo después de corregir API/auth/secretos; Sprint 4 streaming y fallback tras egress verificado; Sprint 5 auditoría después de definir minimización y roles; Sprint 6 dashboard después de datos fiables; Sprint 7 piloto solo con criterios de seguridad, presupuesto y autorización. **No equiparar fechas Gantt originales con tareas completadas.**

## 2. Puertas exactas GO / PIVOT / STOP (propuesta)

**Puerta A — Antes de conversación comercial:** descripción honesta del estado, 160 cuentas en observación, 10 prioritarias verificadas por país, CRM sin datos sensibles y secuencia de consentimiento. **Solo investigación**, no oferta funcional.

**Puerta B — Problema repetido:** meta de al menos **20 entrevistas celebradas** (idealmente 5+ por país), **6 organizaciones** con problema específico reciente o costos comprobables; **3** con comprador/arquitecto identificados por rol y aceptación de benchmark. Estos umbrales son **HP**, no significancia estadística ni compromisos externos.

**Puerta C — Demostración técnica:** todos los P0 resueltos, tests en CI ejecutados sin fallas críticas, rastreo de salida HTTPX bajo política, autorización/tenant isolation, logs minimizados, dependencia y entorno verificados; corpus sintético por país y comparación frente a Presidio/Cloudflare/Model Armor. Sin esta puerta, **no usar datos reales**.

**Puerta D — Piloto de pago:** al menos **2 organizaciones con problema y sponsor** confirman por escrito alcance, datos sintéticos, criterios de aceptación, límites de responsabilidad y ruta presupuestaria; contrato y pagos aprobados. Un «me interesa» no es pedido ni intención vinculante.

**Puerta E — Validación comercial inicial:** al menos **1 piloto pagado realmente cobrado** + segunda cuenta independiente con necesidad similar; costos variables reales medidos. Un pago no es product-market fit definitivo.

**PIVOT:** 15+ entrevistas bien conducidas reportan necesidad de personalización pero el gateway propio no aumenta resultados; ofrecer módulo de recognizers LATAM para Presidio, servicios de evaluación o integraciones de seguridad bajo licencia y propiedad intelectual claras.

**STOP:** fuga o acceso inseguro no mitigable, necesidad cero con buena muestra, márgenes negativos en casos reales, rechazo universal de middleware adicional, obligaciones legales de riesgo fuera de capacidad.

## 3. Tres tesis alternativas que competimos entre sí

| Hipótesis | Cliente | Producto posible | Ventaja que necesita evidencia | Riesgo/competencia | Orden de prueba |
|---|---|---|---|---|---|
| **H1 — Integradores B2B2B** | Software factories con varias apps LLM | Módulo de políticas y recognizers como SDK/plugin OSS + servicio | Menos horas por cliente y tasas FP/FN mejores | Presidio/LiteLLM/extensión propia pueden bastar | **Primera** |
| **H2 — Fintech/seguro regulado** | Equipos con riesgo alto y presupuesto | Gateway privado y auditoría contractual | Reducción demostrable de exposición + aceptación compliance | Ciclo largo, certificaciones, SLA, responsabilidad | Segunda, tras P0 |
| **H3 — Detector de PII LATAM** | SaaS contable/HR y equipos de datos | Biblioteca local de PII con benchmark reproducible y asesoría | Precision/recall superior para RUT/NIT/RFC/CURP/CI con contexto | OSS fuerte, riesgo de commodity | **Prueba técnica paralela** |

**Selección:** H1 se prueba primero comercialmente porque permite descubrir necesidades sin pedir compromisos enterprise grandes; H3 es la ruta técnica de menor integración bajo el cumplimiento P0 mínimo, H2 solo cuando exista confianza y soporte. Una entrevista que no encuentra brecha valiosa cuenta como evidencia negativa.

## 4. Plan de 90 días por semana (propuesto, no comprometido)

| Semana | Fechas (Chile) | Responsable/país propuesto | Trabajo | Evidencia/medida |
|---|---|---|---|---|
| 1 | 02–08 nov 2026 | Chile: Andrés y Operaciones, revisión técnica; CO: apoyo técnico sujeto a acuerdo | Reproducir imports y fallos, crear issues P0 y threat model | Smoke test documentado y 10 fichas ola 1 revisadas |
| 2 | 09–15 nov 2026 | Chile: líder técnico y Operaciones; CO: revisión opcional | Corregir imports/modelos y ejecutar suite en entorno aislado; contactar cuentas con fuente | Tests iniciales, 8 invitaciones, consentimiento CRM |
| 3 | 16–22 nov 2026 | Chile: técnica y operaciones; MX enlace por definir | Auth/audit y segregación por tenant; 4 entrevistas meta | Pruebas negativas de acceso, registro dolor no inventado |
| 4 | 23–29 nov 2026 | Chile/CO: técnica según disponibilidad; MX/BO: ningún responsable asignado | Eliminar prompts de logs, secretos fijos y comprobar egress | Revisión de seguridad P0 y 4–6 entrevistas acumuladas |
| 5 | 30 nov–06 dic 2026 | Chile: ingeniería; Colombia rol ciberseguridad propuesto | Conectar redaction->proxy laboratorio, mock proveedor; casos sintéticos | Salida HTTPX inspeccionada, PII no enviada en positivos de prueba |
| 6 | 07–13 dic 2026 | Chile: QA y Operaciones; Bolivia prospectores locales solo si aceptan | Definir dataset sintético CL/CO/MX/BO, etiquetar negativos | 12 entrevistas meta y corpus aprobado |
| 7 | 14–20 dic 2026 | Chile/CO: ingeniería, entrevistas en los cuatro mercados sin responsables impuestos | Benchmark contra alternativa OSS/managed y costo total | Precision/recall por categoría, no claims de 100 % |
| 8 | 21–27 dic 2026 | Chile: dirección/operaciones; MX enlace voluntario si formalizado | Entrevistas comerciales, analizar objeciones y propuesta técnica | 20 entrevistas acumuladas objetivo, presupuesto y roles identificados |
| 9 | 28 dic 2026–03 ene 2027 | Chile: coordinación, Colombia/México/Bolivia contactos por confirmar | Go/no-go P0, revisión DPA, integrador piloto voluntario | Evidencia de seguridad mínima o detener pilotos |
| 10 | 04–10 ene 2027 | Chile/CO/MX/BO: equipo técnico solo tras aceptación explícita | Preparar pruebas sintéticas bajo alcance y acuerdo de piloto | 1–2 propuestas de piloto consentidas |
| 11 | 11–17 ene 2027 | Chile: dirección/operaciones; responsable técnico cliente por acordar | Piloto de laboratorio 30 días podría iniciar si P0 completos | Métricas y costos verificados, no contratos imaginarios |
| 12 | 18–24 ene 2027 | Chile: dirección/finanzas; aliados externos sin compromisos | Probar pricing, contrato, impuestos, soporte y continuidad | Márgenes reales y 2–3 decisiones de piloto, si existen |
| 13 | 25–31 ene 2027 | Chile: dirección, operaciones, técnico; ventas por país según disponibilidad | Evaluación pipeline, resultados de benchmarks, go/pivot/stop | Decisión escrita; primer ingreso como meta aspiracional sin garantía |

### Asignación de responsabilidades: situación humana

- **Chile:** Dirección MasterTech (Andrés) y Operaciones (Isaac) como coordinadores naturales, sujetos a disponibilidad real. Roles ingeniería/seguridad no necesariamente disponibles por jornada laboral.
- **Colombia:** Iván está vinculado al desarrollo y puede ser consultado para coordinación técnica; **función Scrum Master aún propuesta, no aprobada**. Nicole, Brayan y Vall no reciben tareas por este documento ni se los considera empleados.
- **México:** existen profesionales interesados/entrevistados (Alan Jareth, Jesús, José David), pero **su incorporación y NDA no están verificados como firmados**; no deben tener responsabilidad ni acceso a información privada por defecto. Contacto técnico/ventas México **por definir**.
- **Bolivia:** Roberto Carlos Olguín Ledezma entregó datos para acuerdo de confidencialidad, pero **firma y rol técnico no confirmados**; no asignar tareas ni prometer contratación. Coordinador Bolivia **por definir**.
- **Brasil:** expansión futura, **sin equipo activo verificado**.

Ningún nombre de este plan implica horas comprometidas, remuneración, comisiones o participación societaria. MasterTech debe acordar explícitamente toda responsabilidad y mantener el trabajo proporcional a disponibilidad y obligaciones legales.

## 5. Evidencia semanal obligatoria

Registrar repo SHA, prueba efectivamente ejecutada, resultado, benchmarks con versiones, entrevistas realizadas (solo anónimas en reportes públicos), objeciones, decisión comercial, costos medidos y cambios de alcance. Los datos individuales y contratos deben mantenerse en espacio privado/CRM, **nunca en CSV público**.

## 6. Revisión del roadmap actual

Metas documentadas de 100 % bloqueos PII, 99,9 % uptime y menos de 45 ms latencia son **objetivos aspiracionales no probados**; al negociar solo se deben mencionar como futuros umbrales sujetos a pruebas y presupuesto, no SLA.

**Próxima actualización:** después de resolver importaciones/autenticación y recoger primeras entrevistas. No afirmar progreso operativo por la sola incorporación de documentos.
