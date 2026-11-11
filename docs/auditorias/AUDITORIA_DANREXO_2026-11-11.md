# Auditoría integral de preparación comercial y diferenciación — DANREXO / DELIA

**Fecha:** 11/11/2026 · **Repo auditado:** `andres-olguin/DELIA` público · **SHA congelado:** `8bee51e627c0e9844f49f688d686de873857f19f` (merge PR #20).
**Método:** lectura de árbol completo (300 archivos rastreados), revisión focalizada de código crítico, pruebas, CI publicado, planes, licenciamiento y competidores con fuentes originales. **No** es pentest, prueba de penetración, revisión formal de cada línea, ejecución independiente local, auditoría jurídica ni comprobación del software frente a sistemas externos. Se consultaron GitHub Actions, pero no se ejecutó un clon local por falta de conectividad de red en el entorno de inspección. Las afirmaciones de competidores derivan de sus sitios/documentos, no de ensayos de sus productos.

## Decisión ejecutiva

**Etapa actual: R&D / laboratorio sintético avanzado con detector PII regional funcional en pruebas; NO MVP de gateway de seguridad operativo.**

1. **GO condicional ahora (noviembre):** discovery B2B y **servicio profesional delimitado** de diagnóstico de un flujo CRM/ticketing, con datos ficticios, propuesta escrita, costo/horas, facultades del equipo, contrato y responsabilidad definidos. Esto **no** se vende como software DANREXO seguro; la entrega tiene valor aunque el comprador escoja Cerbos, Helio u otra alternativa. Referencia de precio para investigar: US$250–750 o CLP $290.000 netos según el simulador, **no precio oficial ni validado**.
2. **GO condicional después (diciembre o posterior):** laboratorio/piloto técnico **pagado únicamente en sandbox** con acuerdos explícitos, datasets sintéticos, adaptadores ejecutados y test de que las acciones DENY no provocan efectos; todavía no producción. Hipótesis de precio US$750–2.500 o CLP $790.000 según alcance y costo; no prometer disponibilidad en diciembre por calendario.
3. **NO-GO ahora para SaaS / API productiva / protección de PII real / certificación / suscripción por tenant:** los 8 controles SEC P0 siguen sin estado VERIFIED, `/proxy/v1/chat`, `/audit/` y `forward_request` responden 503 por diseño, no hay auth/tenant enforce, DLP HTTP pre-egress ni reconciliación de sistemas de registro reales. No procesar datos sensibles de clientes ni afirmar conformidad legal.
4. **Diferenciador:** atractivo como hipótesis económica de integradoras multicliente, **todavía NO demostrado ni exclusivo**. No ganar intentando replicar todas las capacidades de OpenShell, Pruvz y Helio.

**No cerrar los issues P0** ni aumentar el porcentaje por cantidad de tests/documentos. Fechas de beta en enero son **gates condicionales**.

## 1. Evidencia técnica actual

| Área | Estado confirmado en main | Lo que NO prueba | Evidencia |
|---|---|---|---|
| DLP regional | `backend/dlp/pii.py` detecta y enmascara RUT Chile, NIT/cédula Colombia, CURP/RFC México, CI/NIT Bolivia, email, teléfono y tarjetas con validaciones parciales; `redact` sustituye por `[[TIPO]]` | Cobertura real, políticas por campo, cifrado reversible, redacción completa de JSON/headers/URLs | `backend/dlp/pii.py`, PR #20 |
| Benchmark | Histórico sintético 172 casos con 150 entidades: **130 TP, 0 FP, 20 FN**, precisión observada 100 % y recall 86,67 % **solo de ese conjunto**. 12 FN direcciones, 4 CURP inválidas y 4 RFC genéricos; 2 errores FP T0162/T0163 corregidos | Métrica de campo o generalización; corpus diseñado/ajustado junto al trabajo no es holdout externo | PR #20, `benchmarks/` |
| CI | En `main` commit `8bee51e`: tres workflows pasaron. Job general **611 passed, 12 warnings** en Python 3.14.4; jobs regionales **455 passed en 3.11 y 3.13**; 4.440 verificaciones generadas en general | Suite completa 611 automatizada en 3.11/3.13, E2E externo, análisis de seguridad/coverage total | Run #42949757043, #42949757015, #42949757090 |
| Rama #11 CI | `feat/11-ci-reproducible` con 3 commits no fusionados: ajustes de workflow, dependencias compat y baseline | Que 611 tests ya hayan pasado en GitHub Actions para Python 3.11/3.13; no había PR en revisión al corte | Issue #11, rama, `docs/foundation/ISSUE_11_BASELINE_CI.md` |
| API / proxy | `app/main.py` declara `production_ready:false`, `proxy_enabled:false`; `app/api/proxy.py` y `services/proxy.py` responden HTTP 503 y no envían datos por esa ruta | Proxy que permita peticiones seguras, verdadero enforcement, rendimiento bajo carga | `app/main.py`, `app/api/proxy.py`, `services/proxy.py`, PR #58 |
| Identidad y tenants | Esquema ORM contiene Company/User/Agent/AgentPreset, pero API está bloqueada, sin login ni verificación scoped real | aislamiento entre clientes, permisos por tenant, IAM, revocación | `app/models.py`, #7 |
| DB / auditoría | DB URL externa o indisponible; se retiró create_all del arranque. El ORM tiene campos `prompt`/`response` y no hay Alembic en árbol; los endpoints no guardan mientras estén bloqueados | migraciones reales, minimización/retención, auditoría multi-tenant operativa | `app/database.py`, `app/models.py`, #6/#8 |
| Otro helper de red | `backend/network_utils/replay_session.py` enmascara cuerpo textual de requests, pero **no** revisa URL, headers ni cuerpo binario; imprime URL y envía con `requests.Session.send` | DLP universal o cobertura de todos los paths de egreso | Archivo y su comentario de limitación |
| Resultado de negocio | Motor de invariantes/refunds simulado con `ELIGIBLE_FOR_AUTHORIZATION` y `VERIFIED_SIMULATED`; no conexión autenticada a sistemas de registro | autorización de pagos, reconciliación real, idempotencia durable, balance de dinero | `experiments/contract_assurance/` |
| Contratos entre gateways | `competitive_assurance.compat_lab` contrasta dos adaptadores **ficticios** para tickets con ALLOW/REVIEW/DENY e INDETERMINATE | funcionalidad en Helio/Cerbos/OPA, tool calls reales, validación externa | `competitive_assurance/`, contrato `MOCK_ONLY_NO_ENFORCEMENT` |
| Frontend | Landing `site/` HTML/CSS/JS con tres ejemplos prefijados y CTA a GitHub/email; GitHub Pages tuvo workflow correcto anteriormente | SaaS, login, captura de leads medible o una demo conectada al motor | `site/app.js`, `site/README.md` |
| Marketing y demanda | Plan, borradores y forecast determinista. La cuenta Metricool consultada **no tiene redes conectadas**; no hay contratos/clientes cobrados demostrados por los archivos revisados | publicaciones sociales realizadas, leads reales, MRR, PMF | #48/#49, `docs/growth/` |

### Riesgos P0 que impiden facturar SOFTWARE protector

**SEC-001:** arranque reproducible completo y migraciones DB; **SEC-002:** pre-egress DLP aplicado y ensayado; **SEC-003:** autenticación, autorización y aislamiento tenant; **SEC-004:** logs mínimos y secretos; **SEC-005:** esquema/Alembic; **SEC-006:** control de ejecución real y sin bypass; **SEC-007:** aprobación vinculada a argumentos, expiración/revocación e idempotencia duradera; **SEC-008:** resultado comprobado por fuente independiente de verdad. Todos OPEN en `docs/foundation/readiness-controls.json` (evidencia congelada del 09/11 y registrada en este informe al 11/11). Algunos pasos de contención se hicieron pero el estado aceptado sigue pendiente. Validación externa/pentest independiente necesaria antes de un servicio que proteja sistemas empresariales.

### Riesgos técnicos P1 detectados

- `backend/logger.py` conserva un nombre por defecto `TALIA APP`; documentación `SECURITY.md` del 31/10 describe imports inestables que ya fueron mitigados en PR #58: **drift documental**.
- `app/schemas.py` admite payloads con `prompt` y `response`; `app/models.py` tiene columnas correspondientes: no reutilizar en producción sin rediseño de retención/minimización. La API está apagada, por lo que no hay evidencia de fuga actual de esos endpoints.
- Dos bases de dependencias Python diferentes (3.14 general y 3.11/3.13 limitada); workflow #11 debe unificar cobertura de pruebas y medir coverage por módulo.
- Se observan **300 archivos rastreados**, **150 bajo docs/** y **51 en .agents/** frente a **26 módulos Python de núcleo/laboratorios** y **20 archivos tests/**. La documentación es abundante; la prioridad no debe ser crear más planes sino implementación E2E, documentación sincronizada, pruebas independientes y delivery externo.
- El repositorio público declara licencia MIT **Copyright (c) 2026 andres-olguin**; el plan comercial prevé explotación por **MasterTech SpA**. MIT admite uso comercial y forks, pero conviene formalizar titularidad, contribuciones, cesión/licencias, dependencias y marca; no asumir exclusividad del código ni de features abiertas. Consultar profesional jurídico cuando sea necesario.
- `SECURITY.md` publica `contacto@mastertechg.com`; validar que sea un buzón operativo y coherente con el contacto corporativo antes de usarlo para vulnerabilidades. No incluir secretos en GitHub.
- No se verificó despliegue externo con respuesta HTTP 200 de GitHub Pages ni funcionamiento end-to-end de una landing MasterTech; el éxito histórico del workflow no equivale a uptime.

## 2. Diferenciación: comparación competitiva actualizada al 11/11

**Evaluación documental únicamente**, basada en claims públicos de proveedores y repositorios, sin prueba técnica de sus instalaciones.

| Proveedor / alternativa | Cubierta competitiva | Implicación para DANREXO |
|---|---|---|
| [Pruvz](https://pruvz.ai/) | Según proveedor, producto de *outcome verification* operativo y pilotos abiertos, readback Stripe/HubSpot test, snapshots de política y evidencia | «Comprobamos resultados del agente» **no es nuevo**, y Pruvz documenta madurez mayor en verificación real |
| [ACPT](https://www.acpt.cloud/) | Contratos de resultado, verificación contra registros, detección de desviaciones y trazabilidad; programa de design partners | Evidencia por workflow y guardrails tampoco son exclusivos |
| [AgentTrustOps](https://github.com/teresaliu90/AgentTrustOps) | SDK código abierto para autoridad, aprobación, idempotencia y reconciliación; sus propios límites de producción están publicados | Idempotencia, aprobación y transacciones seguras no justifican construir middleware entero desde cero |
| [Helio](https://github.com/gethelio/helio/) | Proxy MCP con tool-call governance, aprobación de argumentos, presupuestos y controles fuera del modelo | La hipótesis no puede ser «inventamos firewall/approval MCP» |
| [NVIDIA OpenShell](https://www.nvidia.com/en-us/ai/openshell/) | Sandbox/seguridad fuera del agente, egress, identidad y credenciales; [pasó a CNCF Sandbox 09/11](https://nvidia.github.io/OpenShell-Research/dev-notes/posts/2026-11-09-donated-openshell-to-cncf/) | No competir por runtime completo; integrar y evaluar |
| [OWASP Agent Control Standard](https://owaspacs.org/docs/acs/) | Especificación abierta de Guardian/permitir/denegar/alterar por canal autenticado | Portabilidad de control puede ser requisito estándar, no propiedad exclusiva |
| [Cerbos](https://docs.cerbos.dev/cerbos/latest/policies/evaluation.html) | autorización de políticas versionadas deny-by-default | Usar como baseline de política, no reimplementar RBAC genérico |
| [LangSmith](https://www.langchain.com/langsmith/evaluation) | Evals offline/online, regresiones y CI de agentes | No vender evaluación genérica como diferencial |
| [Beyryl](https://marketplace.microsoft.com/en-us/product/beyryl.beyryl_ms_2026?tab=overview), [AIRA](https://www.cinderlabs.ai/aira/msp) | Multi-tenancy, reportes para MSP, white label y canal | Ser B2B2B/partner por sí solo tampoco es singular |

**Juicio:** EL DIFERENCIADOR NO ESTÁ PROBADO. Lo mejor de la propuesta es una **combinación específica**, no una capacidad inédita:

> Para integradoras de agentes CRM/ticketing en Chile/México, DANREXO busca convertir reglas de permisos y resultados del negocio en contratos y pruebas portables entre clientes/infraestructuras, con evidencia y métricas de horas/costos que muestren si incorporar el siguiente cliente se vuelve más barato.

**Hipótesis para defender:** menor coste de QA y puesta en marcha del **segundo tenant**, manteniendo o mejorando la cobertura de casos críticos frente al stack actual del comprador. **Por demostrar** con 2 integradoras independientes, 2 stacks instrumentados, una base comparativa, tests de no bypass y costos internos reales. Si no disminuye costos o mejora una necesidad pagable, pivotar hacia test harness/consultoría o abandonar el enfoque de gateway.

**Moat potencial (a construir):** biblioteca reproducible de casos reales sanitizados/anotados con consentimiento, plantillas de control sectorial LATAM, experiencia de onboarding por partner, conectores mantenidos, calidad de soporte, evidencia de ROI y confianza de implementadores. **No moat hoy:** nombre, regex, esquema de contratos, claims de seguridad genéricos o número de publicaciones.

## 3. Etapas de venta y puerta de salida

| Fase | Oferta comercial | Estado al corte | Condiciones de activación |
|---|---|---|---|
| E0 | Investigación, demo sintética pública, interviews | **Disponible** con disclaimers | Fuentes, mock rotulado, CTA válido, consentimiento en entrevistas |
| E1 | **Servicio profesional** de diagnóstico de un solo workflow CRM/ticketing | **Vendible ahora CON CONDICIONES**; no como software protector | SOW/contrato, capacidad equipo y costo/horas, alcance claro, datos ficticios, IP y facturación correctas; dos alternativas incluidas y no-fit honesto |
| E2 | Laboratorio de diseño/validación **pagado en sandbox** | **Todavía no demostrado como oferta repetible; posible tras prueba técnica de entrega** | un adapter real controlado, prueba DENY sin efectos, autorización del titular del entorno de prueba, revisión de seguridad, acuerdo de datos y costo |
| E3 | Partner Beta con API y varios tenants | **NO-GO** | 8 SEC P0 VERIFICADOS; auth/segregación, controles sin bypass, revisión independiente, soporte, costos, pilotos y contrato |
| E4 | SaaS/Enterprise general y licencias recurrentes | **NO-GO** | E3 probado, billing, SLO, backups, recuperación, retención, monitoreo, gobernanza/IP, soporte, cohortes pagadas y margen |

**Precios de investigación, no tarifas públicas:** E1 US$250–750 en `docs/commercial-master/02-ofertas-y-precios.md`, y CLP $290.000 en simulador; E2 US$750–2.500, con escenario CLP $790.000 de sandbox. Cualquier presupuesto debe recalcular horas reales, costo completo, impuestos, soporte y capacidad. Las simulaciones dic-ene (conservador 290k / base 1,66M / expansión 3,32M CLP acumulados) **no son forecast calibrado ni ventas reales**. SaaS MRR previsto en ese modelo es **0**.

### Oferta E1 que proponemos cotizar

**DANREXO Workflow Readiness Lab por MasterTech SpA** — servicio de consultoría de riesgo de IA agentic sobre un proceso CRM/ticketing:

1. Entrevista técnica con el implementador, diagrama de acciones y límite de datos ficticios.
2. Matriz de acceso / autorización / revisión humana / resultados desconocidos.
3. Hasta 10 casos sintéticos positivo/negativo, instrucciones de reproducción y hallazgos.
4. Comparativa stack actual vs 1–2 soluciones alternativas; recomendar NO usar DANREXO si no aporta.
5. Informe de riesgo residual, costo estimado de mejoras y plan de PoC.
6. Alcance, entregables, confidencialidad y límites de responsabilidad contratados, sin certificado de seguridad, acceso productivo o garantía de cumplimiento legal.

**No vender** «DANREXO bloquea fugas», «certificado» o «100 % privacidad» ni demo preprogramada como funcionalidad real.

## 4. Compliance, derechos, marca y canales

- **Chile:** Ley **21.719** figura en Biblioteca del Congreso Nacional con entrada en vigencia **1 de diciembre de 2026**. Validar modificaciones vigentes y obligaciones con profesional antes de tratar datos reales y jamás vender detectores como cumplimiento automático. Fuente: https://www.bcn.cl/leychile/Navegar/imprimir?idNorma=1209272
- **Marca:** nombre DANREXO fue elegido, **no registrado ni jurídicamente despejado**; doc de marca identifica ~98 semejanzas en IMPI MARCia, incluyendo REXO. Revisar clases, titulares y derechos en Chile/México antes de gasto de marca definitivo. No afirmar búsqueda internacional concluyente.
- **Licencia y titularidad:** MIT y copyright individual en `LICENSE`. Validar acuerdos con colaboradores de GitHub, cesiones/uso por MasterTech SpA y dependencias antes de ventas exclusivas, licenciamiento empresarial y solicitudes de financiación. MIT no impide vender servicios/SaaS, pero un competidor puede reutilizar el código MIT conforme a su licencia.
- **Distribución:** website sintético `site/`, orgánico LinkedIn y GitHub planificados. Metricool no tiene redes conectadas en la marca consultada el 11/11; no se verificó publicación social ni captura de leads. Activar campaña con prueba reproducible + seguimiento de contactos real, no anuncios masivos.
- **Comercial:** no se encontró evidencia en el repo de entrevistas de compradores completadas, propuestas firmadas, contratos/invoices del producto o MRR. Eso es **ausencia de evidencia en fuentes revisadas**, no afirmación de que no existan en otros sistemas. Separar trabajo personal freelance y facturación de MasterTech.
- **Financiación:** Start-Up Chile BIG13 Build/Ignite/Growth abre 03/11 y cierra **24/11/2026 13:00 CL**; revisar elegibilidad y expediente, no asumir postulación ni adjudicación. Fuente: https://startupchile.org/postula/

## 5. Prioridad ejecutable (sin otro megaplan)

**Próximos 7 días (11–18 noviembre):** (a) PR para alinear modelos/Alembic y prueba de arranque limpio, (b) #11 CI de Benjamín: 611 tests por Python y coverage con PR nuevo, (c) diseñar auth/tenant/egress sin reactivar 503, (d) entrevista de 5 integradoras pertinentes y ficha E1 costeada, (e) verificar dueño del producto, mailbox de seguridad y marca, (f) no aumentar backlog de 18 sectores.

**Hasta 22/11 (cierre del Sprint 3):** (a) suite E2E con `httpx.MockTransport` y 0 requests para DENY, (b) definición de transporte IAM server-side sin secretos en payload, (c) validación de contratos de negocio con casos negativos y `INDETERMINATE`, (d) una demo de 2–3 minutos que ejecute realmente el código *del laboratorio*, sin sugerir producto real, (e) propuesta E1 a comprador solo si equipo y precio son viables, (f) acta Go/No-Go.

**Diciembre–enero:** primer adapter real en sandbox autorizado, segundo stack, instalación externa, comparación de tiempo/resultado, dos compradores independientes y costos de cada entrega. **Beta real solo tras gates; 15/01 es revisión, no promesa.**

### Indicadores que deben mandar la decisión

1. **Seguridad:** 0 efectos no autorizados en suite negativa y ausencia de bypass; 0 entregas productivas con SEC P0 abiertos.
2. **DLP:** matriz por país/campo, FP/FN en holdout independiente y tests de URL/headers/body/JSON/errores/streaming.
3. **Producto:** tiempo desde clon limpio a primera prueba exitosa; dos stacks reales; costo para añadir tenant 1 vs 2; pruebas de incidentes y recuperación.
4. **Comercial:** entrevistas con comprador identificable y permiso, propuesta escrita y aprobación, dinero efectivamente cobrado, horas reales, contribución neta de costo directo, frecuencia de uso y no-fit.
5. **Marca/operación:** clearance, derechos de contribución, mailbox validado, herramientas de soporte, política de retención y documentación concordante con el SHA desplegado.

## 6. Dictamen final

**Fortalezas:** contribución técnica comprobada de Benjamín, 611 pruebas en rama principal (3.14), validadores regionales y benchmark explícito, arquitectura fail-closed, documentación de límites responsable, laboratorios con outputs bien separados, hipótesis de compra bien acotada y apertura a integración con soluciones existentes.

**Debilidades:** sin proxy protector operativo, IAM/tenant, DLP HTTP, integración real, migraciones, contratos/ventas acreditados, ventaja económica observada o marca depurada; alta proporción de documentación respecto de implementación; MIT/IP comercial requiere orden.

**Decisión:** **GO** para *discovery* y oferta E1 (consultoría de alcance verificable), **GO condicionado** para E2 en laboratorio **cuando realmente esté implementado**, **NO-GO** para vender una licencia o plataforma SaaS productiva ahora. La diferenciación es **interesante como estrategia B2B2B enfocada en ROI del segundo cliente**, pero **debilidad competitiva actual** hasta pruebas entre proveedores, implementaciones reales y compradores que paguen.

**Fuentes principales internas:** SHA `8bee51e`, PR #20/#58, runs #42949757043/#42949757015/#42949757090, issues #6–#12/#34/#45/#46/#49/#54, `docs/foundation/readiness-controls.json`, `docs/competitive-assurance/`, `docs/commercial-master/`, `docs/branding/`. **Externas:** OWASP ACS, Pruvz, ACPT, Helio, NVIDIA OpenShell, Cerbos, LangSmith, Beyryl, AIRA, Biblioteca del Congreso Nacional y Start-Up Chile.

---

**Control editorial:** cualquier actualización futura de los controles requiere PR con SHA, ejecución real de tests y revisor. Este informe por sí mismo no cierra un P0, vende un servicio, contrata personas, publica una red social ni cambia la marca.
