# DELIA — Inteligencia de mercado, estrategia SaaS de seguridad IA y prospección comercial B2B/B2C (Chile, México, Colombia y Bolivia)

**Corte:** 31 de octubre de 2026 · **Versión:** 1.0, revisión por Dirección pendiente · **Responsable:** análisis estratégico para MasterTech SpA · **Fuente técnica:** `main` de [andres-olguin/DELIA](https://github.com/andres-olguin/DELIA).  
**Naturaleza:** investigación secundaria con fuentes públicas; **no** entrevista real, prueba de compra ni auditoría de seguridad ejecutada.  
**Declaración de integridad:** entre *hecho verificado* (HV), *dato de estudio* (DE), *estimación propia* (EP), *hipótesis* (HP) y *no verificado* (NV). Se evitará presentar predicciones, interés de empresas o certificaciones como hechos.

## Resumen ejecutivo (una página)

**Decisión:** priorizar **descubrimiento B2B con integradores y SaaS que ya operen aplicaciones sobre APIs LLM**, antes que ofrecer un supuesto «firewall universal para ChatGPT» o perseguir bancos grandes. La necesidad de controlar datos enviados a terceros y auditar el uso de modelos es plausible y está respaldada por la expansión de IA y obligaciones de seguridad; la compra de DELIA **no está validada**. La evidencia de adopción de IA no equivale a utilización de gateways, presupuesto ni intención de pagar [F001] [F006].

**Hallazgo técnico decisivo:** el código observado no es un producto vendible para producción. Hay un motor de patrones PII y algunos tests escritos; pero la API tiene importaciones incompatibles con el árbol, referencias a modelos de log dispares, endpoints de auditoría sin autenticación visible, una URL de PostgreSQL con credenciales embebidas y ausencia de integración verificable entre redacción PII y proxy. **No prometer seguridad, cumplimiento ni pilotos con datos reales**. Deben corregirse P0, ejecutar pruebas desde clon limpio y evaluar con datos sintéticos.

**Diferenciación candidata (HP, no ventaja validada):** detección exhaustiva y medida de RUT chileno, NIT/cédula colombianos, CURP/RFC mexicanos y CI/NIT bolivianos, con políticas localizadas, auditoría minimizada, opción de despliegue privado, documentación/soporte en español e integración simple. Hoy **solo existe código parcial** para RUT/NIT/cédula colombianos, email, teléfono y tarjetas; **no** existe cobertura CURP/RFC/identificadores bolivianos, cifrado reversible, bóveda, certificaciones ni comparativa reproducible.

**Competencia fuerte:** Cloudflare AI Gateway y LiteLLM tienen funciones base gratuitas; Portkey publica US$49/mes; Google Model Armor tiene **2 millones tokens mensuales gratis y US$0,10/millón adicional** en condiciones publicadas; Presidio es OSS. Por ello, no hay justificación para vender únicamente regex o enrutamiento genérico [F053] [F055] [F056] [F066].

**Mercados:** Chile primero por proximidad de MasterTech; México por integradores y SaaS con uso explícito de agentes; Colombia por software contable y fintech; Bolivia como piloto de investigación y alianzas técnicas, evitando sobrestimar adopción o madurez. Son preferencias de ejecución y **no** rankings estadísticos de conversión.

**Prospección:** [60 cuentas observables documentadas](PROSPECTOS_B2B_CL_MX_CO_BO_2026-10-31.csv) (**15/país**), todas **«no contactada»**, ninguna con compra DELIA confirmada. Algunas solo exhiben APIs/datos digitales, no uso LLM: conservan la etiqueta de baja certeza para evitar falsas oportunidades.

**90 días:** 60 cuentas iniciales; objetivo interno de 20-30 entrevistas **realizadas** y voluntarias, benchmark con datos sintéticos y, si P0 se resuelve, 2-3 pilotos técnicamente autorizados. Meta aspiracional 1 primer pago y decisión explícita continuar/pivotar; **no es pronóstico**.

**TAM/SAM/SOM:** no se pudo determinar de manera empírica tamaño monetario regional de compradores de *gateways independientes*; las fuentes no miden conjuntamente número de integraciones LLM, exposición sensible, control previo ni presupuesto. Se incluye un embudo bottom-up y escenarios explícitos, no un TAM inventado.

**Regla comercial inmediata:** vender ahora **descubrimiento, entrevistas y capacidades de servicios técnicos ya comprobadas por MasterTech**, no garantías de protección basadas en DELIA actual. Cualquier piloto con datos reales requiere corrección y validación de seguridad.

---

## Índice
1. Metodología y lectura de código · 2. Brechas para vender · 3. Mercado regional y regulaciones · 4. Competencia (12+ jugadores) · 5. Propuesta de valor y buyer personas · 6. Países y puntuación de segmentos · 7. Las 60 cuentas · 8. Precios y TAM/SAM/SOM · 9. Canales y discursos de venta · 10. Promoción, eventos y financiación · 11. Plan de 90 días · 12. Refutadores y criterios de decisión · 13. Auditoría y registro de investigación · 14. Bibliografía numerada.

## 1. Ronda 1 — auditoría de repositorio: lo que DELIA **hace** y **no hace**

**Fuentes internas consultadas directamente en `main`:** README, `docs/` (estudios anteriores CL/CO/MX, roadmap, normas y evolución), `research/` (análisis de tokenización), `CONTRIBUTING.md`, 15 archivos de aplicación/backend/proxy/modelos/pruebas, Docker, .env.example, árbol completo y los 20 commits más recientes. Fecha de inspección: 31/10/2026. No se ejecutaron tests, Docker ni solicitudes de red del producto; **las ejecuciones siguen NV**.

| Capacidades | Evidencia literal del código | Estado al corte |
|---|---|---|
| Reglas PII | `backend/dlp/pii.py` define `detect`, `redact`, validaciones RUT/NIT, reglas email/teléfono/tarjeta/cédula | **Código presente**, precisión, cobertura e integración no verificadas |
| Sanitización con requests | `backend/network_utils/replay_session.py` transforma solo cuerpos de texto de `requests.Session.send`; excluye URL/headers/binarios | **Implementación parcial aislada**, no integrada con HTTPX del gateway |
| API FastAPI | `app/main.py`, `app/api/proxy.py`, `services/proxy.py` | Archivos presentes; **arranque esperado bloqueado por importaciones incompatibles**, no probado |
| Gestión de auditoría | `app/models.py` define `AuditLog` con `prompt` y `response` en texto; `/audit/` GET/POST no incorpora auth | **Riesgo crítico de exposición de datos**, no apto para clientes |
| «Bloqueo» de prompt | `services/audit.py` solo bloquea cadena de prueba `PROMPT_BLOCK_TEST` | **No es motor DLP**, no sanitiza llamadas HTTPX |
| Credenciales y DB | `app/database.py` fija conexión `postgres:postgres@localhost:5432/talia_logs` | Configuración sensible embebida; no apta producción |
| Streaming, fallback multi-LLM | Upstream único OpenAI en `services/proxy.py`; no implementación visible de SSE/fallback | **No implementado/verificado** |
| Límites, costos, autenticación/tenants | Entidades de datos/modelos existen, no enforcement de llaves por API, cuota, control multitenant | **No implementado/verificado** |
| Vault, cifrado reversible y tokens | Investigación extensa en `research/`, no código de bóveda o restitución | **Solo diseño/investigación**, no prometer «encryption» |
| CURP/RFC, CI/NIT Bolivia | No existen reglas detectadas en `backend/dlp/pii.py` | **No implementado** |
| Pruebas | `tests/test_pii.py`, `tests/test_api.py` y otras contienen assertions | **Archivos existentes; resultados de ejecución NV** |
| Documentación | README extenso y estudios de mercado con numerosas URLs, roadmap | **Disponible**, algunas afirmaciones aspiracionales y antecedentes TALIA |

**Bloqueadores específicos observados:**

- **P0 — API no fiable:** `app/api/proxy.py` usa `from app.models.chat` y `from app.services.*`, pero árbol real tiene `app/models.py`, `models/chat.py`, `services/*`. El modelo `AuditLog` definido no admite los kwargs `request_id`, `model`, `prompt_preview`, `action`, `reason` que usa el proxy. Reconciliar imports/esquemas y probar desde un clon limpio.
- **P0 — autorización y aislamiento:** los endpoints `GET/POST /audit/` tienen dependencias DB pero no autenticación explícita ni filtros por tenant; `prompt`/`response` completos almacenables/consultables. No habilitar fuera de laboratorio.
- **P0 — protección de datos y secretos:** el upstream recibe `request.model_dump()` sin invocar `redact`; token bearer del cliente pasado al proveedor; `app/database.py` incluye contraseña literal; logs pueden incluir contenido sensible.
- **P0 — operación segura:** sin gestión verificada de secretos, validación de políticas fail-closed, TLS, aislamiento, control de egress o prueba de despliegue. Requiere threat model y revisión de seguridad antes de cualquier dato real.
- **P1 — medición y fiabilidad:** benchmark sintético por país, clasificación contextual, falsos positivos/negativos, fallbacks, timeout, errores, versiones y pruebas automatizadas en CI.
- **P1 — experiencia de integración:** documentación de API validada, guía quickstart funcional, autoalojado reproducible, compatibilidad de proveedor y límites de soporte.
- **P2 — funciones de roadmap:** dashboard, cuotas Redis, billing, analítica, agentes, CURP/RFC, CI/NIT Bolivia y otras reglas localizadas una vez haya evidencia de demanda.

**Contradicciones que deben corregirse:** `app/main.py` anuncia TALIA, `roadmap.md` define metas de 100 % detección PII, 99,9 % disponibilidad y latencia <45 ms: **no están medidas**, deben decir «objetivo aspiracional no verificado». El título «Data Encryption» es marca, no declaración de que exista cifrado funcional.

### Ruta de comercialización técnica

**Puerta 0 (ahora):** revisión de riesgos y refactor P0 sin datos reales. **Puerta 1:** arranque reproducible, tests ejecutados, autenticación e integración redaction-before-egress verificada. **Puerta 2:** benchmark sintético y comparación contra Presidio/Cloudflare/Model Armor. **Puerta 3:** auditoría de vulnerabilidades, prueba controlada autorizada. **Puerta 4:** oferta de piloto pagado con acuerdos y condiciones limitadas. Ninguna puerta implica aprobación automática de producción.

## 2. Ronda 2 — competencia y sustitutos (fuentes oficiales)

**Precios:** USD de oferta pública consultada en octubre 2026, sin impuestos, infraestructura ni servicios externos; cambian por plan, región, volumen y fecha. «Cotización» significa cifra no verificada, no US$0.

| Competidor/sustituto | Función pública comprobable | Precio público / límite | Diferencia y amenaza DELIA |
|---|---|---|---|
| Cloudflare AI Gateway | Analytics, caching, rate limits; DLP en prompt/respuesta | Gateway base **gratis**; DLP con perfiles/limitaciones de plan, costos de logs/servicios relacionados | Sustituto directo para gateway+DLP genérico [F053] [F054] |
| LiteLLM OSS | Multi-provider, virtual keys, budgets, cuotas, fallback | **US$0 licencia OSS**; hosting y operación no gratis; enterprise cotización | Proxy multiproveedor no diferencia DELIA [F055] |
| Portkey | Gateway, guardrails, trazas y routing | **Production US$49/mes** publicado; enterprise cotización | Producto comparable comercialmente a precio visible [F056] |
| Lakera Guard | Defensa prompt injection / abuso IA | Comunidad gratuita con topes publicitados; enterprise **cotización**; límites exactos de plan deben reconfirmarse | No equivalente a PII total, pero sustituye controles de amenaza [F057] |
| Nightfall | DLP de SaaS, cloud y asistentes IA | Tarifas comerciales según paquete/usuario; **precio monetario público NV** | Mayor amplitud de detección y operación DLP [F058] |
| Microsoft Presidio | Detección/anonymización extensible de PII | OSS gratuito; operación no gratuita | Detección local puede ampliarse en OSS; benchmark esencial [F059] |
| Microsoft Purview | Clasificación, gobernanza, riesgo y auditoría IA | Licencias/métricas por capacidad; **precio comparable NV** | Empresas M365 pueden contar con DLP ya pagado [F061] |
| Azure AI Gateway (API Management) | Auth, políticas, cuotas, routing, telemetría; **preview** | **Precio y modelo aún por anunciar**, regiones limitadas en preview | Gateway nativo en Microsoft; no confundir preview con producción estable [F063] |
| AWS Bedrock Guardrails | PII, seguridad contenido y protección configurada | **US$0,10/1.000 unidades texto** para filtro PII según tarifa; cobro por uso/región | Precio marginal bajo y compras ya consolidadas [F064] |
| Google Cloud Model Armor | Inspección amenazas/PII para prompts, respuestas y herramientas | **2 millones tokens/mes gratis; US$0,10/millón adicional** independiente; definición propia de tokens y condiciones | Fuerte presión sobre precios de sanitización aislada [F066] |
| Langfuse | Observabilidad/trazas LLM y evaluación | OSS/autohospedado, cloud por plan; precio por plan en web | Sustituye observabilidad, no DLP completo [F068] |
| Helicone | Proxy, gateway y observabilidad | Free hasta 10k solicitudes; plan profesional anunciado US$79/mes en sitio | Compite en telemetría y developer experience [F070] |

**Prueba de posicionamiento, no hecho:** ser «más barato» carece de evidencia mientras el stack competidor ofrece entradas gratis. El benchmark objetivo medirá precisión/recall en español, latencia, seguridad de errores, costo total de operación y tiempo de integración bajo el mismo dataset.

## 3. Diferenciación defendible — aspiracional y verificable

1. **PII regional comprobable:** soporte validado de RUT, NIT y cédula Colombia (parcial); **por construir** CURP/RFC México y CI/NIT Bolivia. Diferenciar por dataset público sintético, métricas precision/recall y límites, no slogans.
2. **Política por flujo/tenant con decisión explicable:** bloquear/enmascarar por aplicación y destino, rastrear motivo sin texto sensible. **Por implementar**; debe integrarse al request real.
3. **Despliegue privado y minimización operativa:** opción autoalojada con secretos del cliente y control del egress. **Potencial**, no disponible certificada hoy.
4. **Evidencia de gobernanza local, no «certificación legal»:** mapeo de controles técnicos a marcos locales, retención y logs bajo autorización; revisión por abogados por país.
5. **Integración y soporte en español:** onboarding medible y asistencia técnica regional; costo y SLA deben sustentarse con capacidad real antes de prometerlos.

**Propuesta de valor (versión de investigación):** «DELIA busca ayudar a equipos que integran modelos de IA a controlar los datos que envían, aplicar políticas por aplicación y generar evidencia técnica de su uso; empezamos por identificadores y necesidades latinoamericanas, con capacidades sujetas a pruebas».

**Elevator pitch 30 s (no afirmar producto listo):** «Cada vez más aplicaciones envían información de clientes a APIs de IA. Eso abre preguntas prácticas: ¿qué datos salen, quién lo autorizó y dónde queda la evidencia? En MasterTech estamos desarrollando DELIA, una capa intermedia enfocada en revisar información sensible y aplicar controles antes de llegar al modelo. Estamos validando las reglas locales y el diseño técnico con empresas que ya construyen agentes. Buscamos entrevistas y pruebas con datos sintéticos para descubrir qué controles les aportan valor».

**Mensajes por persona (HIPÓTESIS de comunicación):**
- **CTO:** «Si hoy integras dos o más proveedores LLM, ¿cuánto esfuerzo implica mantener controles de PII, llaves y observabilidad coherentes? Buscamos entender dónde falla tu solución actual».
- **CISO / DPO:** «¿Qué evidencia tienen de que los agentes no envían identificadores o prompts innecesarios? ¿Cómo documentan excepciones y retención? No ofrecemos cumplimiento automático».
- **Gerencia general:** «¿Qué costo tangible tienen los incidentes y el trabajo manual de supervisar IA? Antes de hablar de software queremos entender el impacto de negocio».
- **Integrador B2B2B:** «¿Repetís la implementación de DLP para cada cliente o ya tenés una capa reusable? ¿Cómo compararías un componente regional con tus herramientas actuales?».

**Casos de uso a demostrar (no funciones disponibles):** atención al cliente con RUT/NIT/CURP; asistente contable que consulta facturas; chatbot de RR.HH. con datos de postulantes; integrador de múltiples marcas con separación de acceso; empresa con política de proveedores IA autorizados.

## 4. Ronda 3 — adopción, regulación y oportunidad por país

**No mezclar métricas:** ILIA 2026 reporta estimaciones regionales de adopción por tamaño (**grandes 27,6 %, medianas 12,8 %, pequeñas 6,8 %**) mediante un modelo; los índices nacionales son puntuaciones del ecosistema, no tasas de compra. AI Index recoge un **88 % en una encuesta internacional de uso organizacional**. Los censos de INEGI y muestras Endeavor miden universos distintos [F001] [F003] [F006].

### Chile (fuentes primarias [F007]–[F018], más sectoriales)

- **Madurez:** ILIA 2026 sitúa el índice chileno en **71,4 puntos** (índice compuesto, no porcentaje). Una encuesta empresarial SONDA 2026 reportó **88 % en adopción/exploración** dentro de su muestra privada, no universo nacional. Son fenómenos no equivalentes; el censo de compañías con **APIs LLM en producción no está verificado** [F003] [F017].
- **Regulación:** Ley 19.628 y reforma Ley 21.719; entrada en vigor señalada en texto de ley para el **1/12/2026**. El proyecto de aplazamiento Boletín **18.623-07** fue aprobado en general y particular en Senado el **28/10/2026**, **no implica promulgación** al corte. Verificar estado antes de usar argumento comercial de plazo. CMF evaluaba cambios a RAN 20-7 sobre servicios externos; un producto no proporciona cumplimiento normativo automáticamente [F007] [F009] [F010].
- **Verticales a descubrir:** SaaS RR.HH., integradores IA, software contable y fintech. **Primer movimiento sugerido:** entrevistas en Chile aprovechando presencia operativa de MasterTech, sin presumir presupuesto.
- **Fuentes principales contrastadas:** BCN, Senado, CMF, Banco Central, Economía, CORFO y ProChile; las encuestas privadas se identifican por separado.

### México (fuentes oficiales [F019]–[F027])

- **Madurez:** INEGI Censos Económicos 2024 (dato 2023): **2,1 %** de unidades económicas que *ya usaban herramientas digitales* reportó «sistemas de IA»; **denominador no son todas las unidades económicas**. No representa adopción GenAI de 2026. Banxico recoge respuestas empresariales más recientes, pero con encuesta y definición distinta; comparar solo en sus marcos [F019] [F023].
- **Regulación:** nueva LFPDPPP publicada en **marzo 2025**, con reforma en 2025; no usar como vigente el texto de 2010 ni la estructura institucional antigua sin verificar actualización. No existe obligación específica de usar DELIA [F024] [F025].
- **Verticales a descubrir:** agentes conversacionales, SaaS contable, open banking/fintech, integradores de marketing. Se hallaron plataformas que **publican** agentes o APIs (Auronix, Clara, Yalo, Alegra, Belvo), pero no interés demostrado en DELIA.
- **Fuentes:** INEGI (censos, DENUE, ENAFIN), Banxico encuesta y FIX, Cámara Diputados y Secretaría competente (referencias numeradas).

### Colombia (fuentes oficiales y gremiales [F028]–[F038], y encuesta privada)

- **Madurez:** Endeavor AI Pulse 2026: **493 organizaciones de la muestra**, **61 %** dijo IA prioridad estratégica y **0,2 %** nivel avanzado según su metodología. La muestra autoseleccionada **no** representa población empresarial nacional. Se necesita medir específicamente uso de APIs LLM entre SaaS locales [F037].
- **Regulación:** Ley 1581/2012 y SIC Circular Externa **002/2024** sobre tratamiento de datos en IA, además de circular sectorial fintech **001/2025**; DNP CONPES 4144/2025 es **política pública**, no licencia ni ley especial vigente que exija comprar un gateway [F028] [F029] [F034].
- **Verticales a descubrir:** proveedores de ERP/contabilidad (Siigo MCP, Alegra), integradores (Pragma), pagos y fintech. Verificar si usan LLM externo, permisos actuales y controles existentes; una API de pagos no basta para calificarlos.
- **Fuentes:** SIC, DANE, DNP, SFC y cámaras gremiales, todas con alcance y fecha.

### Bolivia (fuentes primarias y eventos [F039]–[F052])

- **Madurez:** **porcentaje representativo de empresas con IA API: no verificado**. AGETIC y UNESCO iniciaron evaluación de preparación IA en 2026; ello es una iniciativa estatal, no prueba de adopción empresarial. Estadísticas de INE sobre **hogares** o registro de empresas de SEPREC **no pueden sustituir** una encuesta de uso de LLM empresarial [F039] [F047] [F048].
- **Regulación:** Constitución, Ley 164 y obligaciones sectoriales, más **anteproyectos** de protección de datos. **No se verificó una ley integral de protección de datos promulgada equivalente a la chilena**; nunca atribuir vigencia a un borrador. Validar requisitos bancarios y de telecomunicaciones con asesoría local [F040] [F042] [F043].
- **Verticales a descubrir:** desarrolladoras de software nearshore en Cochabamba (AssureSoft/Jalasoft/TRUEXTEND), integradores, pagos y bancos digitales. El Banco Ganadero publica contratación para IA; no implica compra de DELIA [F098].
- **Fuentes:** AGETIC, ATT, INE, SEPREC, BCB, y Constitución, con límites explícitos.

### 4.1. Matriz de atractivo por vertical y país — **estimación propia de ejecución**, NO dato medido

Puntaje 1–5 para **tamaño/expansión (T)**, **dolor probable por datos (D)**, **capacidad de pago presunta (P)**, **facilidad de acceso de MasterTech (A)**, **ciclo de venta presumible (C; 5=corto)**. Pesos **20 %, 30 %, 20 %, 20 %, 10 %**, respectivamente. `score=.2T+.3D+.2P+.2A+.1C`. Son hipótesis para organizar entrevistas; ajustar después de resultados.

| País y vertical | T | D | P | A | C | Score /5 EP | Interpretación |
|---|---:|---:|---:|---:|---:|---:|---|
| Chile — integradores de IA | 3 | 4 | 3 | 5 | 4 | **3,8** | Canal inicial B2B2B, no demanda comprobada |
| Chile — SaaS RR.HH./contable | 3 | 5 | 3 | 4 | 3 | **3,8** | Datos sensibles y operaciones repetidas |
| Chile — banca enterprise | 5 | 5 | 5 | 1 | 1 | **3,8** | Alto valor teórico; entrada lenta y requisitos difíciles |
| México — integradores agentes | 4 | 4 | 3 | 3 | 4 | **3,6** | Alianzas y pruebas sin datos reales |
| México — SaaS/fintech mediana | 4 | 5 | 4 | 2 | 2 | **3,7** | Acceso y compras sujetos a confirmar |
| Colombia — SaaS contable | 4 | 5 | 3 | 3 | 3 | **3,8** | Casos de uso públicos, diferenciación no probada |
| Colombia — integradores TI | 3 | 4 | 3 | 3 | 4 | **3,4** | Podrían ya usar proveedores consolidados |
| Bolivia — software nearshore | 3 | 4 | 3 | 3 | 4 | **3,4** | Menor costo exploratorio con aliados técnicos |
| Bolivia — banca y pagos | 3 | 5 | 4 | 2 | 1 | **3,4** | Casi nunca venta inicial sin auditoría |
| Cualquier país — B2C developers | 3 | 2 | 1 | 4 | 4 | **2,6** | Canal de comunidad, no motor de ingresos inicial |

**Auditoría de la matriz:** Chile integradores = 0,6+1,2+0,6+1+0,4=3,8; SaaS=0,6+1,5+0,6+0,8+0,3=3,8; banca=1+1,5+1+0,2+0,1=3,8; México integradores=0,8+1,2+0,6+0,6+0,4=3,6; México SaaS=0,8+1,5+0,8+0,4+0,2=3,7; Colombia contable=0,8+1,5+0,6+0,6+0,3=3,8; Colombia integrador=0,6+1,2+0,6+0,6+0,4=3,4; Bolivia software=0,6+1,2+0,6+0,6+0,4=3,4; Bolivia banca=0,6+1,5+0,8+0,4+0,1=3,4 **(corrección: 3,4)**; B2C=0,6+0,6+0,2+0,8+0,4=2,6. **Scores derivados se deben comprobar con las fórmulas; tabla posterior sustituirá cualquier error.**

### 4.2. Ecosistema y sustitutos regionales

- **Chile:** Cloudflare, Azure/Purview, AWS, soluciones integradoras (SONDA, AcidLabs, Rocketbot), clasificación existente de HR. Comprobar stack real por cuenta.
- **México:** Cloudflare/LiteLLM/Azure/Google, proveedores de mensajería/agentes (Auronix, Yalo); algunos integradores pueden convertirse en canal o sustituto.
- **Colombia:** Microsoft/Google/AWS, equipos de ingeniería SaaS y proveedores integradores (Pragma), APIs de ERP con controles existentes.
- **Bolivia:** integradores nearshore, cloud empresarial ENTEL/Tigo/VIVA y controles bancarios propios. La presencia comercial de cada proveedor internacional en una cuenta específica es **NV**.

## 5. Ronda 4 — cuentas objetivo observables (15 por país)

**Archivo operativo:** [PROSPECTOS_B2B_CL_MX_CO_BO_2026-10-31.csv](PROSPECTOS_B2B_CL_MX_CO_BO_2026-10-31.csv) · **60 organizaciones, 15 por país**. CSV incluye: país, empresa, segmento, tamaño (solo donde perfil público observado), stack tecnológico visible (y faltantes), decisor objetivo por rol, señal pública específica con URL, hipótesis de valor, canal, estado, LinkedIn y verificación de prensa.

**TODAS: estado «no contactada».** «Señal pública» significa adopción/solución/vacante/contexto observable y **no «comprará DELIA»**. Donde no se pudo confirmar uso de LLM, stack, tamaño, perfil LinkedIn o un artículo de prensa individual, se indica **no verificado**. Una web institucional no confirma presupuesto de compra.

**Chile (15):** Buk, Rankmi, Talana, Defontana, Nubox, Fintual, Fintoc, Acid Labs, Adereso AI, Rocketbot, Keirón, ElipseLab, Banco de Chile, Falabella y SONDA.

**México (15):** Yalo, Auronix, Clara, Belvo, Conekta, Facturama, Clip, Kueski, Stori, Konfío, BBVA México, Alegra México, Finerio Connect, Bitso y Nu México.

**Colombia (15):** Siigo, Alegra Colombia, Pragma, Nequi, Wompi, Bold, Rappi, Addi, Treble.ai, Finaktiva, Bancolombia, Seguros SURA, Habi, Platzi y PayU Colombia.

**Bolivia (15):** AssureSoft, Jalasoft, TRUEXTEND, Banco Ganadero, BancoSol, Banco FIE, Banco BISA, Banco Unión, Síntesis, Linkser, ENTEL Bolivia, Tigo Business Bolivia, VIVA Bolivia, BISA Seguros y Banco Nacional de Bolivia.

### Cuentas de investigación prioritaria — no ventas confirmadas

| País | Cuenta | Señal fuerte documentada | Hipótesis a contrastar | Fuente |
|---|---|---|---|---|
| CL | **Buk** | Buk AI y política de tratamiento con LLM | Falta control adicional de PII / qué resuelve su stack existente | [F072] |
| CL | **Rankmi** | Genius/OpenAI y trabajo Ley 21719 ya documentados | Probablemente tiene controles; preguntar por brechas, no asumirlas | [F073] |
| CL | **Adereso AI** | Atención automatizada GenAI para empresas | Posible alianza integradora; observar competidores existentes | [F075] |
| MX | **Auronix** | Plataformas bots y agentes empresariales | Gateway de terceros con políticas por cliente | [F080] |
| MX | **Clara** | Clara Intelligence | Datos financieros en asistentes; controles existentes desconocidos | [F082] |
| MX | **Clip** | Señales corporativas de IA y contrataciones | Caso de uso LLM para PII por confirmar | [F084] |
| CO | **Siigo** | Integración MCP documentada | Permisos de acceso y minimización de datos hacia asistentes | [F088] |
| CO | **Alegra** | Actividad corporativa IA-contabilidad 2026 | Resguardo de facturas/NIT en agentes | [F094] |
| CO | **Pragma** | Ingeniería de IA para clientes | Canal B2B2B, podría tener su propio gateway | [F091] |
| BO | **AssureSoft** | Servicios de ingeniería con aplicaciones LLM | Alianza técnica, control regional para clientes | [F095] |
| BO | **Jalasoft** | Ingeniería IA y presencia técnica | Evaluación benchmark o alianza, no necesariamente compra | [F096] |
| BO | **Banco Ganadero** | Oferta laboral técnica IA | Averiguar si hay uso de LLM externo en producción | [F098] |

**Tamaño de empresa:** solo se anotan bandas públicas de LinkedIn cuando fueron consultadas; no convertirlas en facturación, capacidad de compra o tamaño del equipo dedicado a IA. **Stack:** no atribuir Python, Azure, OpenAI ni OpenAI API a una empresa por pertenecer al sector; registrar exclusivamente tecnologías citadas por ella. **Verificación multifuente:** el CSV documenta búsquedas/observaciones de sitios y perfiles LinkedIn disponibles; **la cobertura completa de LinkedIn + prensa individual para las 60 firmas no pudo completarse**. Los campos «no verificado» son **trabajo pendiente**, no prueba negativa.

### Calificación de lead (sin atribuir interés)

- **I0**: cuenta identificada, ninguna interacción (todas hoy).
- **I1**: caso de uso LLM confirmable mediante fuente o diálogo y rol técnico identificable, sin contacto.
- **I2**: reunión aceptada, diagnóstico y problema existente documentados (solo si sucede).
- **I3**: necesidad, alternativa actual, autoridad presupuestaria, urgencia y piloto autorizado (solo tras entrevista).
- **I4**: oferta solicitada/contrato (solo con evidencia).
- **I5**: pago efectivamente recibido (no presente).

El tratamiento de datos personales, contactos profesionales e información de clientes debe mantenerse en CRM privado con acceso controlado, no GitHub público.

## 6. Ronda 5 — canales, precios, escenarios y dimensionamiento

### 6.1. ICP y compradores

**ICP-A — partner integrador:** firma tecnológica con aplicaciones LLM operativas para terceros. Comprador socio/CTO; usuario arquitecto; compra si el componente regional reduce tiempo/costo de integraciones y soporta contratos. Principal canal de descubrimiento.

**ICP-B — SaaS de contabilidad/RRHH:** producto con datos personales y necesidad real de interoperar con LLM; comprador CTO/CISO; compliance puede vetar. Detectar costes actuales y cobertura propia.

**ICP-C — fintech/seguros:** alto riesgo potencial y presupuesto supuesto mayor, pero auditoría exhaustiva, SLAs y procurement largos. No primera referencia comercial.

**B2C desarrolladores:** uso en comunidad, OSS CLI/benchmark y educación; **no primer motor de ingresos**, porque existen gateways gratuitos y OSS. Requiere documentación excelente y seguridad demostrada para credibilidad.

### 6.2. Alianzas

- **Integradores/SI:** revender componente o desarrollar integración en contrato claro; sin prometer comisiones/equity antes de modelo legal y financiero.
- **Proveedores SaaS vertical:** integración como módulo configurable con responsabilidad compartida.
- **Partners cloud:** evaluar programas de AWS, Google Cloud, Microsoft solo cuando existan requisitos técnicos y elegibilidad; **MasterTech no posee estado de partner verificado**.
- **Comunidades de desarrolladores:** demos de redacción con datos sintéticos, talleres en español, publicaciones transparentes de pruebas y límites.
- **Eventos:** ENEXPRO TECH 2026, EtM Day, incMTY 2026, Santa Cruz Tech Week y Fintech Summit Bolivia; verificar fechas y postulaciones, algunas ya cerradas. Colombia Tech Week y Colombia 4.0 como redes a monitorear; **no se verificó apertura actual de inscripción en Colombia**.

### 6.3. Tres escenarios de precio para investigar (NO precios aprobados)

A fecha 31/10/2026 el mercado ofrece opciones gratis de Cloudflare, LiteLLM OSS y Google Model Armor, y Portkey Production US$49/mes. No hay **costos reales medidos** de infraestructura, incidentes, soporte ni WTP DELIA; los siguientes números son **anclas experimentales** para entrevistas, no un tarifario.

| Escenario HP | USD/mes (rango) | Entregables condicionados | Comprador objetivo | Justificación y riesgo |
|---|---|---|---|---|
| **Técnico** | **49–99** | Instalación autogestionada y reportes básicos *solo tras desarrollo/verificación* | Dev teams | Precio comparable con referencia Portkey; debe explicar valor adicional frente a gratis |
| **Equipo** | **199–499** | Políticas, equipos y métricas auditables *futuras* | SaaS / integrador | Requiere controles y soporte que hoy faltan; benchmarking y entrevistas |
| **Empresa/privado** | **799–1.500** | Despliegue acordado, aislamiento, contrato/SLA tras validación | SaaS regulado | Sin auditoría/seguros/SLA verificados sería una promesa indebida |

**Piloto acotado:** preguntar por un **importe total US$300–1.500** con duración/entregables/costos pactados para benchmarking sin datos sensibles; cifra exploratoria de conversación, **no oferta vigente ni pago recibido**. Separar instalación/servicio de suscripción y gastos de terceros.

#### Conversión a monedas locales (referencial, NO precio comercial ni fiscal)

Tipos de cambio oficiales usados: **30/10/2026** Chile USD/CLP **993,22** (BCCh), **30/10/2026** México FIX USD/MXN **18,7962** (Banxico), **31/10/2026** Colombia USD/COP **3.182,99** (SFC), **31/10/2026** Bolivia USD/BOB **12,09** (BCB). Solo referencia nominal; no incorporar IVA, comisiones, diferencias de tipo de cambio bancario, impuestos o normativa cambiaria [F018] [F026] [F038] [F050].

| Concepto | USD | CLP aprox. | MXN aprox. | COP aprox. | BOB aprox. |
|---|---:|---:|---:|---:|---:|
| Técnico mínimo | 49 | 48.668 | 921 | 155.967 | 592 |
| Técnico máximo | 99 | 98.329 | 1,861 | 315.116 | 1.197 |
| Equipo mínimo | 199 | 197.651 | 3,740 | 633.415 | 2.406 |
| Equipo máximo | 499 | 495.617 | 9,379 | 1.588.312 | 6.033 |
| Empresa mínimo | 799 | 793.583 | 15,018 | 2.543.209 | 9.660 |
| Empresa máximo | 1500 | 1.489.830 | 28,194 | 4.774.485 | 18.135 |

**Economía unitaria antes de poner precio:** `Margen bruto = Precio - (hosting + almacenamiento + salida red + logs + proveedores + soporte variable + monitoreo + incidentes provisionados + comisiones y cobro)`. **Ninguno de esos componentes está medido en DELIA**; publicar precios definitivos sin presupuestarlos sería engañoso. Testear costo de autoalojado contra costos de soporte a partners.

### 6.4. TAM / SAM / SOM — método sin inflación de cifras

- **TAM teórico del problema:** empresas de 4 países con integraciones LLM productivas, datos sensibles y necesidad de un gateway nuevo. **Conteo NV**: ninguna estadística mide simultáneamente esas variables; no inventar monto.
- **SAM:** subconjunto de TAM con recursos para integrar middleware, necesidades no resueltas, cumplimiento técnico y posibilidad de compra en mercados atendidos. **Tamaño NV**.
- **SOM:** clientes que MasterTech podría captar con equipo/canal/tiempo reales y seguridad aprobada. **NV** hasta tasa de entrevistas, pilotos y cierres.

**Modelo transparente para cohorte inicial de 60 cuentas (NO TAM regional):** para escenario *conservador* asumir (HP) `60×0,20(usa LLM API)×0,25(dolor no cubierto)×0,20(conversación efectiva)×0,20(piloto)×0,20(pago)=0,024 contratos esperados`. **No representa tasa empírica**. Escenario *expansivo* `60×0,60×0,50×0,50×0,40×0,30=1,08 contratos esperados`. Números **estimados propios por multiplicación de supuestos, no predicciones**; un compromiso pagado efectivo será mejor evidencia que la fórmula. Los 60 incluyen cuentas grandes, integradores y software sin LLM probado; la cohorte no es representativa.

### 6.5. Canales y textos de primer contacto

**LinkedIn (CTO integrador):** «Hola, estamos investigando cómo las empresas que integran asistentes IA gestionan RUT/NIT/CURP, secretos y permisos antes de llamar a modelos externos. No quiero ofrecerte un producto sin validar: ¿tendrías 15 minutos para conocer cómo lo están resolviendo hoy y qué les falta? Si ya lo resolvieron, también nos ayudaría aprender por qué».

**Correo institucional:** *Asunto: Investigación sobre protección de datos en integraciones de IA*. «Hola. Desde MasterTech estamos desarrollando DELIA, un proyecto de capa de control para aplicaciones que usan APIs LLM. Nos interesa hablar con su área de arquitectura/seguridad para entender qué datos salen, qué controles ya emplean y si existen brechas reales frente a soluciones actuales. Es una entrevista de investigación de 15–20 minutos, no una demostración comercial ni una promesa de cumplimiento. ¿Podrían indicarnos el canal apropiado?».

**WhatsApp (únicamente contacto legítimo/consentido):** «Hola, estamos haciendo entrevistas breves con equipos que integran modelos de IA en software empresarial. Queremos entender cómo gestionan datos sensibles y controles de acceso. ¿Te puedo compartir dos preguntas técnicas? Si no es un buen momento, ningún problema». **No recolectar teléfonos privados mediante scraping**.

**Seguimiento:** uno a los 4–6 días hábiles con referencia útil, segundo cierre cortés a los 10–14 días; no insistencia repetida ni secuencias abusivas. Registrar opt-outs.

### 6.6. Guion de descubrimiento (20–30 minutos)

1. ¿Qué producto integra APIs LLM hoy, en qué entorno y desde cuándo?
2. ¿Qué datos entran/salen y quién los clasifica?
3. ¿Qué proveedores, gateways y políticas ya usan?
4. ¿Cuál fue el último incidente, caso de riesgo o revisión que costó tiempo?
5. ¿Qué controles fallan al incluir identificadores locales o herramientas?
6. ¿Qué registros pueden presentar al CISO/DPO sin divulgar contenido sensible?
7. ¿Quién decide el presupuesto, bajo qué proceso?
8. ¿Qué soluciones compararon y por qué eligieron la actual?
9. ¿Qué tipo de despliegue y tratamiento de datos es aceptable?
10. ¿Qué criterio técnico demostraría valor suficiente para un piloto?
11. ¿Qué costo real de herramientas/operación soportan hoy (si pueden compartir)?
12. ¿Estarían dispuestos a una prueba sintética con contrato y alcance escritos? ¿Qué tendría que pasar para pagar?

**Pregunta de cierre neutral:** «¿Cuál es la razón principal por la que **no** usarían un gateway independiente como DELIA?».

### 6.7. Objeciones y respuestas

| Objeción realista | Respuesta responsable | Prueba necesaria |
|---|---|---|
| «Cloudflare/Google gratis lo hace» | Puede ser suficiente; investigar necesidad regional adicional y comparar | Benchmark e integración |
| «Usamos Azure/Purview» | No reemplazar lo cubierto; preguntar por brechas entre aplicaciones/modelos | Diagrama de flujos y controles |
| «No podemos enviar datos a un tercero» | No pedir datos reales, evaluar autoalojado cuando esté probado | Arquitectura revisada y contratos |
| «No tienen certificaciones/SLA» | Correcto, hoy no; no vender protección crítica | Auditoría, respaldo, operaciones |
| «Regex no detecta todo» | Correcto, no prometer cobertura universal | Precision/recall contextual |
| «No hay presupuesto» | Registrar y detener prospección o proponer aprendizaje no comercial | Partida real y fecha de revisión |
| «¿Qué retorno?» | Medir esfuerzo evitado/incidentes/costo integración en piloto antes de declarar ROI | Métricas reales de piloto |

### 6.8. Promoción y fondos (estado temporal)

- **Chile:** ProChile **ENEXPRO TECH 16–19 noviembre 2026**; el plazo publicado de postulación fue **20/10**, cerrado al corte salvo nueva convocatoria; no sugerir que aún está abierto. EtM Day **19–21 noviembre** para comunidad/networking. CORFO programas según elegibilidad y bases; Viraliza Biobío 2026 está **cerrado** [F015] [F104] [F016].
- **México:** incMTY 13 noviembre (ver agenda), encuentros fintech y AI en CDMX/Monterrey. Programas de fondos de México, NAFIN/organismos estatales **elegibilidad y convocatorias concretas NV**; no presentarlos como subvenciones aprobadas [F027].
- **Colombia:** Colombia Tech Week **10–16 agosto de 2026 ya finalizó**; Colombia 4.0 y cámaras/fintech son redes para investigar futuras ediciones. Convenios o fondos de iNNpulsa **no verificados como abiertos hoy**. Usar contactos sectoriales para entrevistas antes de buscar subsidios.
- **Bolivia:** **Santa Cruz Tech Week 3–7 noviembre** y **Fintech Summit Bolivia 5 noviembre** según organizadores, espacios de conversación B2B; CITC AGETIC septiembre/octubre y Expocruz septiembre ya pasaron. Programas de crédito/fondos específicos **no verificados** [F052] [F106] [F051].

### 6.9. Plan de 90 días

| Ventana | Tareas concretas | Metas de gestión internas (NO pronóstico) | Puerta |
|---|---|---|---|
| Días 1–15 | Corregir P0, pruebas de arranque/auth, crear dataset sintético y 60 cuentas | 60 fichas I0 auditadas; 10 invitaciones a entrevistas por país (40 total) | Sin seguridad no hay pilotos |
| Días 16–30 | Entrevistas CTO/CISO, documentar competidores | 8–12 entrevistas celebradas, no «solicitadas» | Problema repetido |
| Días 31–45 | Priorizar caso de uso, benchmark con controles y comparación | Acumular 20–30 entrevistas y benchmark verificable | ¿Diferencia frente gratis? |
| Días 46–60 | Probar con integradores y datos sintéticos, formalizar alcance piloto | 2–3 cartas de pilotaje **si** aceptan, jamás asumirlo | Piloto legal y técnico |
| Días 61–75 | Pilotos autorizados y medición de error, costos y soporte | Registro de resultados y costos, sin datos de terceros en GitHub | ¿Presupuesto? |
| Días 76–90 | Ofertas escritas tras valoración y cierre/pausa | Meta aspiracional **primer pago**, no compromiso ni forecasting | GO/PIVOT/STOP |

**Métricas:** contacto→respuesta, respuesta→entrevista, entrevista→dolor validado, dolor→piloto aceptado, piloto→pago; mediana de días y causa de rechazo; precisión/recall, latencia p50/p95, fugas de PII, costo por 1.000 solicitudes, horas de integración. Todas **NV hoy**.

## 7. Ronda 6 — auditoría, riesgos y refutaciones

**Refutarían una tesis comercial:** más de la mitad de compradores entrevistados demuestran solución suficiente con herramientas gratis; nadie puede indicar pérdida/costo actual; fallas técnicas impiden reducción de PII; benchmark es peor que Presidio/Model Armor en identificadores locales; compradores rechazan introducir proxy tercero; costo de soporte supera precio; no aparece autoridad de compra; pilotos requieren garantías que MasterTech no puede ofrecer.

**GO**: código estable, controles P0 cerrados, al menos dos organizaciones con criterios de prueba acordados y una evidencia de pago real (antes de hablar de PMF). **PIVOT**: dolor visible pero resuelto por soluciones generales: considerar servicio de implementación, benchmark/localización o plugins con licencias claras. **STOP**: fuga de datos sin mitigación, responsabilidad no asumible o ninguna demanda tras entrevistas de calidad.

### Auditoría de afirmaciones y consistencia

- **Código ≠ producto:** las capacidades del roadmap no se presentaron como hechas. Los commits de documentación recientes **no** prueban nuevas funciones técnicas.
- **Ley Chile:** propuesta de aplazamiento aprobada en Senado 28/10, **no** vigente hasta publicación de ley modificatoria.
- **Bolivia:** proyecto de ley de datos **no** promulgación demostrada.
- **Compuestos de encuestas:** tamaños, selección y definición difieren; no promedio de adopción.
- **Precios:** oficiales rivales y umbrales gratis documentados; valores DELIA solo HP.
- **Prospección:** todas las cuentas I0 no contactadas; sitio web no significa IA LLM; Linkedin/stack/prensa individual **no verificados** si no constan.
- **TAM:** no se inventaron «US$ millones de mercado»; cohortes y reglas de multiplicación son HP ilustrativas.
- **Pruebas:** **no ejecutadas**. Antes de cualquier publicación de demo técnica se requiere ejecución reproducible y correcciones P0.
- **Fuentes:** bibliografía numerada con categoría y fecha; algunas páginas se leyeron mediante resultados indexados/síntesis de búsqueda y **no todas** pudieron auditarse integralmente, ni verificarse HTTP 200 individualmente. Ningún enlace debe llamarse «auditado integralmente» sin abrirlo y comprobar contenido.

### Registro de investigación, búsquedas y vacíos

| Ronda | Acciones de investigación | Evidencia | Límite pendiente |
|---|---|---|---|
| 1 | Árbol `main`, README, docs, research, 20 commits, código/pytest | Archivos específicos y divergencias import/DB/audit | Ejecución tests y deploy no realizados |
| 2 | Comparación de competidores y páginas de precios/doc oficiales, gateways y DLP | Tabla con rivales, planes abiertos y precio NV | Límites enterprise negociados y costos efectivos |
| 3 | Estadísticas CEPAL/BID/INEGI/DANE/INE/BC, SIC/BCN/Senado/AGETIC/ATT y normas | Países y muestras con alcances separados | Universo nacional de empresas LLM API productivas |
| 4 | Cuentas en sitios oficiales, páginas públicas LinkedIn y anuncios sectoriales | 60 filas, 15 por país, señal de TI/IA o NV | **No se logró triple corroboración web/LinkedIn/prensa para las 60** |
| 5 | Comparación de precios, FX, eventos públicos, entrevistas y embudo | 3 escenarios HP, FX oficiales, plan 90d | Costos operativos reales y apertura fondos |
| 6 | Revisión de aritmética de embudos, metas, atribución y estados | Riesgos y citas | Verificación externa de cada URL completa y prospectos B2B reales |

**Fuentes internacionales revisadas:** 108 URLs únicas listadas abajo (reguladores, estadísticas, documentos comerciales, perfiles públicos y convocatorias). **El conteo es un inventario de materiales consultados o examinados en resultados de investigación; no significa que todos fueran abiertos manualmente hasta el final, que todos sean fuentes primarias ni que todos tengan la misma calidad.** Debe señalarse esta diferencia al usarlo para decisiones.

**Entrevistas realizadas:** 0. **Compradores DELIA interesados confirmados:** 0. **Precios DELIA validados por compradores:** 0. **Tests del repositorio ejecutados en esta auditoría:** 0. **Contratos DELIA en producción:** no verificados. **Seguridad de producción:** no aprobada.

---

## 8. Bibliografía numerada — URLs examinadas, fechas y procedencia

> Las referencias **F001–F108** están numeradas de forma consecutiva. Incluyen fuentes regulatorias primarias, documentos empresariales (evidencia de lo que la empresa publica), informes de muestra privada y documentación comercial (precio ofrecido, no precio pagado). Fechas anteriores a octubre 2025 se conservan por ser textos normativos o antecedentes, no indicadores de mercado 2026.

[F001]: CEPAL — ILIA 2026, lanzamiento 20/10/2026 — 2026-10-20 — https://www.cepal.org/es/comunicados/ilia-2026-america-latina-caribe-debe-apropiarse-la-inteligencia-artificial-generar-valor — categoría REG.
[F002]: CEPAL — publicación ILIA 2026 — 2026-10 — https://www.cepal.org/es/publicaciones/90413-indice-latinoamericano-inteligencia-artificial-ilia-2026 — categoría REG.
[F003]: CENIA — ILIA 2026, países y metodología — 2026-10-20 — https://cenia.cl/2026/10/20/ilia-2026-4ta-edicion-revela-que-america-latina-y-el-caribe-se-juegan-su-futuro-en-ia-en-la-colaboracion-regional-para-datos-talento-y-computo/ — categoría REG.
[F004]: BID — Startups x AI: adopción en Latinoamérica — 2026-05 — https://publications.iadb.org/es/startups-x-ai-un-panorama-de-la-adopcion-en-america-latina-y-el-caribe — categoría REG.
[F005]: BID — IA productividad y desigualdad — 2026-07 — https://www.iadb.org/es/blog/analisis-economico/inteligencia-artificial-motor-de-productividad-o-de-desigualdad — categoría REG.
[F006]: Stanford HAI — AI Index Economy 2026 — 2026 — https://hai.stanford.edu/ai-index/2026-ai-index-report/economy — categoría REG.
[F007]: BCN Chile — Ley 21.719, publicación y vigencia — 2024/2026 — https://www.bcn.cl/leychile/Navegar/imprimir?idNorma=1209272 — categoría CH.
[F008]: Senado Chile — proyecto que busca postergar Ley 21.719 — 2026-10-20 — https://www.senado.cl/comunicaciones/noticias/proteccion-de-datos-personales-avanza-proyecto-que-busca-postergar-entrada — categoría CH.
[F009]: Senado Chile — últimos proyectos tratados, Boletín 18.623-07 — 2026-10-28 — https://tramitacion.senado.cl/appsenado/index.php?ac=ultimos_vistos&mo=tramitacion — categoría CH.
[F010]: CMF — consulta sobre capítulo RAN 20-7 — 2026-04 — https://www.cmfchile.cl/portal/prensa/625/w4-article-109289.html — categoría CH.
[F011]: Banco Central Chile — Encuesta de percepciones de negocios — 2026 — https://www.bcentral.cl/areas/encuestas-economicas/encuesta-de-percepciones-de-negocios — categoría CH.
[F012]: Banco Central Chile — EPN febrero 2026 — 2026-02 — https://www.bcentral.cl/documents/33528/8120134/Resultados%2BEncuesta%2BPercepciones%2Bde%2BNegocios%2BFebrero%2B2026.pdf/4688e6d6-8e2c-144b-6f0c-bdfa05474967?t=1773061997431 — categoría CH.
[F013]: Ministerio Economía Chile — creación empresas septiembre — 2026-10-26 — https://www.economia.gob.cl/2026/10/26/informe-de-creacion-de-empresas-y-cooperativas-septiembre-2026.htm — categoría CH.
[F014]: CORFO — encuentro Impacta IA 2026 — 2026-08-31 — https://www.corfo.gob.cl/sites/cpp/regional/lideres-de-la-industria-se-reuniran-en-impacta-ia-2026-para-acelerar-la-adopcion-estrategica-de-la-inteligencia-artificial-en-chile/ — categoría CH.
[F015]: ProChile — ENEXPRO TECH 2026, convocatorias — 2026-11 — https://www.prochile.gob.cl/enexpro-tech-2026/inicio — categoría CH.
[F016]: CORFO — Viraliza Eventos Biobío, cerrado — 2026-09 — https://www.corfo.gob.cl/sites/cpp/convocatoria/viraliza-eventos-biobio-2026/ — categoría CH.
[F017]: SONDA — Tech Trends 2026, estudio propio de la empresa — 2026-08-13 — https://www.sonda.com/detalle-noticia/2026/08/13/estudio-sonda-tech-trends-la-ia-ya-es-parte-del-88-de-las-empresas-chilenas — categoría CH.
[F018]: Banco Central de Chile — USD/CLP 30/10 — 2026-10-30 — https://si3.bcentral.cl/Bdemovil/BDE/Series/MOV_ID_TC1 — categoría CH.
[F019]: INEGI — Censos Económicos 2024 resultados definitivos (datos 2023) — 2025-07-24 — https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/ce/CE2024_def.pdf — categoría MX.
[F020]: INEGI — DENUE consulta pública — 2026 consulta — https://www.inegi.org.mx/app/mapa/denue/Default.aspx — categoría MX.
[F021]: INEGI — API DENUE metodología y acceso — 2026 consulta — https://www.inegi.org.mx/servicios/api_denue.html — categoría MX.
[F022]: INEGI — ENAFIN 2024, marco muestral — 2024/2026 — https://www.inegi.org.mx/programas/enafin/2024/ — categoría MX.
[F023]: Banco de México — Encuesta Actividad Económica Regional IA 2026 — 2026-04-06 — https://www.banxico.org.mx/TablasWeb/reportes-economias-regionales/abril-junio-2026/0F2C4F64-4E90-4BAF-8DDD-CAECA5FBA337.html — categoría MX.
[F024]: Cámara Diputados México — LFPDPPP texto vigente 2025 — 2025/2026 — https://www.diputados.gob.mx/LeyesBiblio/pdf/LFPDPPP.pdf — categoría MX.
[F025]: Gobierno México — diálogo actualización marco datos particulares — 2026-01 — https://www.gob.mx/buengobierno/prensa/arrancan-los-dialogos-para-la-actualizacion-del-marco-normativo-en-materia-de-proteccion-de-datos-personales-en-posesion-de-particulares?idiom=es — categoría MX.
[F026]: Banco de México — FIX 30/10 — 2026-10-30 — https://www.banxico.org.mx/tipcamb/tipCamMIAction.do?idioma=sp — categoría MX.
[F027]: incMTY — Summit 2026 agenda — 2026-11 — https://incmty.com/es/summitagenda — categoría MX.
[F028]: SIC — Circular 002/2024 datos personales e IA — 2024-08-21 — https://sedeelectronica.sic.gov.co/transparencia/normativa/circular-externa-2-de-2024-de-la-superintendencia-de-industria-y-comercio-lineamientos-sobre-el-tratamiento-de-datos — categoría CO.
[F029]: SIC — Circular externa 001/2025 fintech — 2025-09-18 — https://sedeelectronica.sic.gov.co/transparencia/normativa/circular-externa-001-del-18-de-septiembre-de-2025 — categoría CO.
[F030]: SIC — tratamiento de datos fintech — 2025/2026 — https://sedeelectronica.sic.gov.co/noticias/la-superintendencia-de-industria-y-comercio-emite-instrucciones-sobre-el-tratamiento-de-datos-personales-en-el-sector-fintech — categoría CO.
[F031]: DANE — Directorio Estadístico de Empresas — 2026 consulta — https://www.dane.gov.co/index.php/servicios-al-ciudadano/servicios-informacion/registro-estadistico-de-empresas/directorio-estadistico-de-empresas — categoría CO.
[F032]: DANE — geoportal directorio de empresas — 2026 consulta — https://geoportal.dane.gov.co/geovisores/economia/directorio-estadistico-de-empresas/ — categoría CO.
[F033]: DANE — TIC empresas, año 2024 — 2026-08-28 — https://www.dane.gov.co/index.php/estadisticas-por-tema/tecnologia-e-innovacion/tecnologias-de-la-informacion-y-las-comunicaciones-tic/indicadores-basicos-de-tic-en-empresas — categoría CO.
[F034]: DNP Colombia — CONPES 4144 política IA — 2025-02-14 — https://www.dnp.gov.co/publicaciones/Planeacion/Paginas/conpes-4144-hoja-de-ruta-colombia-inteligencia-artificial-retos-actuales-transformacion-futura.aspx — categoría CO.
[F035]: SFC — Circular Externa nube historial — 2019/2025 — https://www.superfinanciera.gov.co/publicaciones/10099659/normativanormativa-generalcirculares-externas-cartas-circulares-y-resoluciones-desde-el-ano-circulares-externascirculares-externas-10099659/ — categoría CO.
[F036]: Colombia Fintech — Snapshot 2026 — 2026-04-23 — https://colombiafintech.co/2026/04/23/fintech-snapshot-informe-sectorial-2026/ — categoría CO.
[F037]: Endeavor Colombia — AI Pulse muestra 493 — 2026-08-25 — https://colombia.endeavor.org/colombia-ai-pulse/ — categoría CO.
[F038]: Superfinanciera Colombia — TRM 31/10/2026 — 2026-10-31 — https://www.superfinanciera.gov.co/CargaDriver/ — categoría CO.
[F039]: AGETIC Bolivia — evaluación UNESCO preparación IA — 2026-08-27 — https://agetic.gob.bo//node/14025 — categoría BO.
[F040]: AGETIC Bolivia — anteproyecto protección datos — 2025-09 — https://agetic.gob.bo//node/7702 — categoría BO.
[F041]: AGETIC Bolivia — reunión ley datos y política — 2026 — https://agetic.gob.bo//node/13922 — categoría BO.
[F042]: Constitución Bolivia — derechos y garantías — 2009/2026 — https://www.senapi.gob.bo/normativas/constitucion-politica-del-estado/constitucion-politica-del-estado-plurinacional-de-bolivia — categoría BO.
[F043]: ATT Bolivia — Ley 164 telecomunicaciones — 2011/2026 — https://www.att.gob.bo/static/LEY164.pdf — categoría BO.
[F044]: AGETIC Bolivia — agenda digital 2030 — 2025/2026 — https://agetic.gob.bo/node/4304 — categoría BO.
[F045]: AGETIC Bolivia — ciberseguridad — 2026-08-24 — https://agetic.gob.bo//node/14020 — categoría BO.
[F046]: AGETIC Bolivia — capacitación IA — 2026 — https://agetic.gob.bo//node/14026 — categoría BO.
[F047]: INE Bolivia — TIC encuesta hogares (NO empresas) — 2026 consulta — https://www.ine.gob.bo/index.php/encuesta-de-hogares-tics/ — categoría BO.
[F048]: SEPREC Bolivia — datos Registro de Comercio — 2026 consulta — https://www.seprec.gob.bo/index.php/datos/ — categoría BO.
[F049]: INE Bolivia — MYPES tablas históricas — 2026 consulta — https://www.ine.gob.bo/index.php/estadisticas-economicas/industria-manufacturera-y-comercio/mypes-cuadros-estadisticos/ — categoría BO.
[F050]: BCB Bolivia — cotización oficial USD BOB 31/10 — 2026-10-31 — https://www.bcb.gob.bo/librerias/indicadores/otras/ultimo.php — categoría BO.
[F051]: AGETIC — Congreso CITC 2026 — 2026-09 — https://citc.agetic.gob.bo/ — categoría BO.
[F052]: Santa Cruz Tech Week 2026 — 2026-11-03 — https://scztechweek.com/ — categoría BO.
[F053]: Cloudflare AI Gateway — precios y límites — 2026-10 — https://developers.cloudflare.com/ai-gateway/reference/pricing/ — categoría COMP.
[F054]: Cloudflare AI Gateway — DLP — 2026-09-25 — https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/ — categoría COMP.
[F055]: LiteLLM — precios OSS/enterprise — 2026-10 consulta — https://www.litellm.ai/pricing — categoría COMP.
[F056]: Portkey — precios — 2026-10 consulta — https://portkey.ai/pricing — categoría COMP.
[F057]: Lakera — precios Guard — 2026-10 consulta — https://us-east-1-internal.platform.lakera.ai/pricing — categoría COMP.
[F058]: Nightfall — precios DLP — 2026-10 consulta — https://www.nightfall.ai/pricing — categoría COMP.
[F059]: Microsoft Presidio — entidades soportadas — 2026-10 consulta — https://microsoft.github.io/presidio/supported_entities/ — categoría COMP.
[F060]: Microsoft Presidio — extensibilidad recognizers — 2026-10 consulta — https://github.com/microsoft/presidio — categoría COMP.
[F061]: Microsoft Purview — modelos de facturación — 2026-10 consulta — https://learn.microsoft.com/purview/purview-billing-models — categoría COMP.
[F062]: Microsoft Purview — seguridad datos IA — 2026-10 consulta — https://learn.microsoft.com/en-us/purview/data-security-posture-management-setup — categoría COMP.
[F063]: Azure API Management AI Gateway preview — límites/precios — 2026-10 consulta — https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview — categoría COMP.
[F064]: AWS Bedrock — precios guardrails — 2026-10 consulta — https://aws.amazon.com/bedrock/pricing/ — categoría COMP.
[F065]: AWS Bedrock — Guardrails documentación — 2026-10 consulta — https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html — categoría COMP.
[F066]: Google Model Armor — precios — 2026-10 consulta — https://cloud.google.com/security-command-center/pricing — categoría COMP.
[F067]: Google Model Armor — producto/precios — 2026-10 consulta — https://cloud.google.com/security/products/model-armor — categoría COMP.
[F068]: Langfuse — precios cloud — 2026-10 consulta — https://langfuse.com/pricing — categoría COMP.
[F069]: Langfuse — precios OSS autohospedado — 2026-10 consulta — https://langfuse.com/pricing-self-host — categoría COMP.
[F070]: Helicone — precios observabilidad — 2026-10 consulta — https://www.helicone.ai/pricing — categoría COMP.
[F071]: Buk AI — solución RRHH IA — 2026 — https://www.buk.cl/productos/buk-ai — categoría LEAD.
[F072]: Buk — seguridad y privacidad IA — 2026-09-21 — https://supportcenter.buk.cl/hc/es-419/articles/53619330726043-Buk-AI-Seguridad-Privacidad-y-Tratamiento-de-Datos — categoría LEAD.
[F073]: Rankmi — documentación Ley 21719/Genius/OpenAI — 2026 — https://www.rankmi.com/adaptacion-ley-no21719-chile — categoría LEAD.
[F074]: Talana — producto reclutamiento — 2026 consulta — https://web.talana.com/software-para-reclutamiento-y-seleccion-de-personal — categoría LEAD.
[F075]: BancoEstado — startups Adereso, Rocketbot, Keirón, Elipse — 2026 consulta — https://nwm.bancoestado.cl/content/bancoestado-public/cl/es/home/inicio---bancoestado-pequena-empresa/productos/comunidad-start---bancoestado-pequenas-empresas/conoce-nuestro-portafolio-de-startups-que-ya-son-parte-de-start-.html — categoría LEAD.
[F076]: Fintual — IA para atención — 2026 consulta — https://ayuda.fintual.cl/es/articles/4340530-quiero-hablar-con-alguien — categoría LEAD.
[F077]: Acid Labs — vacante AI Engineer — 2026 — https://acidlabs.com/jobs/cjp914-ai-engineer-4923 — categoría LEAD.
[F078]: Banco Chile — IA generativa Microsoft — 2025-10-16 — https://sitiospublicos.bancochile.cl/nuestro-banco/es/sala-de-prensa/detalle/banco-de-chile-es-la-primera-empresa-privada-del-pais-en-sellar-alianza-estrategica-en-inteligencia-artificial-con-microsoft — categoría LEAD.
[F079]: Grupo Falabella — inversión IA y datos — 2026-09-03 — https://investors.grupofalabella.com/blog/2026/09/03/cio-de-falabella-anticipa-que-inversion-tecnologica-seguira-subiendo-este-ano-crecio-60-y-ia-y-data-son-nuestras-apuestas-fuertes/ — categoría LEAD.
[F080]: Auronix LinkedIn — chatbots/agentes — 2026 consulta — https://mx.linkedin.com/company/auronix — categoría LEAD.
[F081]: Yalo LinkedIn — agentes conversacionales — 2026 consulta — https://mx.linkedin.com/company/yalo — categoría LEAD.
[F082]: Clara — Clara Intelligence — 2026 consulta — https://www.clara.com/es-mx/platforma/clara-intelligence — categoría LEAD.
[F083]: Belvo — LinkedIn API/MCP — 2026 consulta — https://mx.linkedin.com/company/belvofinance — categoría LEAD.
[F084]: Clip — LinkedIn vacante IA y plataforma — 2026-10 — https://mx.linkedin.com/company/payclip — categoría LEAD.
[F085]: Alegra México — agente contable — 2026-10-22 — https://prensa.alegra.com/llega-un-nuevo-agente-de-ia-para-transformar-la-gestion-contable-de-las-empresas-en-mexico — categoría LEAD.
[F086]: BBVA México — IA generativa atención — 2025-08-13 — https://www.bbva.com/es/mx/innovacion/bbva-mexico-adopta-inteligencia-artificial-generativa-para-transformar-la-atencion-a-clientes-y-eliminar-la-marcacion-por-tonos-ivr/ — categoría LEAD.
[F087]: Kueski — fintech fraude — 2026-02-26 — https://kueski.another.co/kueski-nombra-a-pablo-baragiola-ex-ejecutivo-de-robinhood-nubank-y-capital-one-como-vicepresidente-de-fraude — categoría LEAD.
[F088]: Siigo — MCP documentación — 2026-10 — https://developers.siigo.com/docs/siigoapi/MCP/1-documentation/ — categoría LEAD.
[F089]: Siigo LinkedIn — tamaño — 2026 consulta — https://co.linkedin.com/company/siigo-colombia — categoría LEAD.
[F090]: Alegra LinkedIn — tamaño — 2026 consulta — https://co.linkedin.com/company/alegra — categoría LEAD.
[F091]: Pragma LinkedIn — GenAIOps — 2026 consulta — https://co.linkedin.com/company/somospragma — categoría LEAD.
[F092]: Wompi Colombia — docs sandbox — 2026 consulta — https://docs.wompi.co/docs/colombia/ambientes-y-llaves/ — categoría LEAD.
[F093]: Nequi LinkedIn — perfil — 2026 consulta — https://co.linkedin.com/company/nequi/ — categoría LEAD.
[F094]: Alegra Colombia — Tech Week IA — 2026-08-11 — https://prensa.alegra.com/de-registro-financiero-a-inteligencia-de-negocio-alegra-conectara-la-contabilidad-con-la-ia-en-colombia-tech-week — categoría LEAD.
[F095]: AssureSoft LinkedIn — IA y sedes bolivianas — 2026 consulta — https://bo.linkedin.com/company/assuresoft — categoría LEAD.
[F096]: Jalasoft LinkedIn — IA y software Bolivia — 2026 consulta — https://bo.linkedin.com/company/jalasoft — categoría LEAD.
[F097]: Truextend LinkedIn — I+D Bolivia — 2026 consulta — https://bo.linkedin.com/company/truextend — categoría LEAD.
[F098]: Banco Ganadero — vacante IA — 2026-10 — https://bancoganadero.evaluar.com/trabajo/especialista-ia/ — categoría LEAD.
[F099]: BancoSol — banca digital y chatbot — 2026 consulta — https://www.bancosol.com.bo/ — categoría LEAD.
[F100]: Banco Unión Bolivia — servicios digitales — 2026 consulta — https://bancounion.com.bo/ — categoría LEAD.
[F101]: VIVA — MOU cloud plataformas IA — 2026-08-18 — https://symphony.rakuten.com/newsroom/rakuten-symphony-and-viva-explore-strategic-collaboration-to-accelerate-digital-transformation-in-bolivia — categoría LEAD.
[F102]: Tigo Business — cloud IaaS — 2026 consulta — https://www.tigo.com.bo/medianas/cloud — categoría LEAD.
[F103]: Síntesis — soluciones de pagos — 2026 consulta — https://sintesis.com.bo/pagos/ — categoría LEAD.
[F104]: EtM Day Chile — 19-21 noviembre — 2026-11 — https://iab.cl/actividad-iab/etm-day/ — categoría EVENT.
[F105]: CITC Bolivia 2026 — congreso ciberseguridad — 2026-09 — https://agetic.gob.bo//node/14033 — categoría EVENT.
[F106]: Fintech Summit Bolivia 2026 — 5 noviembre — 2026-10-30 — https://boliviaemprende.com/eventos/fintech-summit-bolivia-2026-reunira-al-ecosistema-financiero-y-tecnologico-para-analizar-el-futuro-de-las-finanzas — categoría EVENT.
[F107]: Expocruz Bolivia 2026 (evento pasado) — 2026-09 — https://www.fexpocruz.com.bo/expocruz-2026 — categoría EVENT.
[F108]: México AI Cloud Data Summit, evento pasado — 2026-10-20 — https://openit.com/es/event/mexico-ai-cloud-data-summit-2026/ — categoría EVENT.

## Historial
- **31/10/2026 v1.0:** auditoría documental de `main`, competencia, cuatro países, 60 cuentas, modelo comercial, scoring HP, 90 días y registro de evidencias. Pendiente de aprobación de Dirección.
- Estudios de referencia previos: [Chile/Colombia regulatorio](DELIA_viabilidad_mercado_regulatoria.md) y [Chile/México/Colombia 31-10](ESTUDIO_MERCADO_B2B_B2C_CHILE_MEXICO_COLOMBIA_2026-10-31.md), complementarios; nuevas verificaciones no borran historia.
