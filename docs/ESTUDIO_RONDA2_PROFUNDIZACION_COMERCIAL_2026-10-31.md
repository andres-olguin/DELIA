# DELIA — Ronda 2: profundización comercial, competencia, incidentes y regulación

**Corte: 31 de octubre de 2026** · Extensión al [estudio v1](INTELIGENCIA_MERCADO_GO_TO_MARKET_CL_MX_CO_BO_2026-10-31.md), sin sustituirlo. Investigaciones secundarias, no reuniones ni ofertas de DELIA. Clasificación: **HV** hecho de fuente oficial, **EP** cálculo o estimación propia, **HP** hipótesis, **NV** no verificado.

## Resumen ejecutivo

La prioridad para MasterTech es vender primero **entrevistas y pilotos de descubrimiento solo cuando la capa técnica sea segura**, con integradores y SaaS con aplicaciones LLM existentes. Las 160 organizaciones de la [base ampliada](PROSPECTOS_RONDA2_160_CL_CO_MX_BO_2026-10-31.csv) son cuentas para **investigación**, no oportunidades abiertas. Se agregaron [25 potenciales aliados de canal](ALIANZAS_CANAL_25_RONDA2_2026-10-31.csv), todos sin contacto comercial confirmado. La puntuación no estima probabilidad de cierre. El núcleo DELIA tiene brechas P0 (imports, autenticación, logs PII y sanitización desacoplada del proxy) que impiden afirmar protección de producción. El competidor gratis/OSS define un umbral alto: DELIA debe demostrar rendimiento incremental sobre stack existente, no solo prometer seguridad.

## Índice
1. Metodología y límites; 2. universo y scoring; 3. socios de canal; 4. incidentes; 5. regulación por país; 6. competencia; 7. implicaciones para ventas; 8. brechas de investigación; 9. fuentes.

## 1. Metodología y límites

Se revisó la rama main y los documentos anteriores. La expansión de 60 a **160 cuentas** incorporó 100 referencias iniciales de directorios sectoriales (como [Proyecto IA, metodología](https://proyectoia.com/metodologia)), que son **fuentes de identificación, NO validación independiente de operaciones, tecnologías o compradores**. Varias empresas fueron comprobadas mediante sus sitios, otras páginas no pudieron abrirse. El CSV distingue evidencia por registro. No se consultaron contratos internos, ingresos, decisores nominativos, necesidades de compra ni presupuestos. Ausencia de señal ≠ ausencia de IA.

Los casos de incidentes se seleccionaron por resoluciones o comunicados **regulatorios primarios**. Muchos no involucran LLM; **está prohibido alegar que DELIA habría prevenido el hecho o evitado la multa**. Sirven para preguntas de gobierno y privacidad, no para inducir miedo con cifras no vinculadas al producto.

## 2. Prospectos y scoring

[CSV 160 cuentas, 40 por país](PROSPECTOS_RONDA2_160_CL_CO_MX_BO_2026-10-31.csv), 10 en ola 1 por país. Fórmula **EP/HP:** `0,30×dolor + 0,25×encaje + 0,20×accesibilidad + 0,15×capacidad de pago + 0,10×ciclo`, todos 1–5, y ciclo 5 significa corto. Valores **heurísticos de clase de empresa y señales documentadas**, no hechos sobre presupuesto o riesgo. Un empate se resuelve alfabéticamente, y la ola 1 es **orden de investigación**, no prioridad irreversible. Confirmar cada empresa/país, sitio, verdadero flujo LLM, protección existente y rol de comprador **antes** de contacto.

Las empresas grandes pueden recibir puntaje elevado por dolor y capacidad de pago, pero tener accesibilidad 1–2 y requerir licitaciones, certificaciones o SLA inexistentes. **No priorizar automáticamente bancos aunque aparezcan en ola 1**. Las cuentas nuevas procedentes solo de directorio deben verificarse en web corporativa antes de utilizarlas en secuencias.

## 3. Canal B2B2B: integradores

[25 firmas para investigación](ALIANZAS_CANAL_25_RONDA2_2026-10-31.csv). Modelo potencial (HP): `costo de controles repetidos por proyecto > costo de integración componente validado + precio + soporte`. Nunca se midió ahorro, no hay programa de partners aprobado, exclusividad, comisiones ni márgenes pactados. Consultar primero si usan LiteLLM/Cloudflare/Presidio propios; si están satisfechos, podría existir **cero valor diferencial de DELIA**. Estructuras a estudiar: referidos, reventa con operación del integrador y OEM/white-label con responsabilidades, privacidad e IP definidas. No comprometer recursos financieros de MasterTech sin contrato.

## 4. Diez expedientes reales de sanciones, acuerdos y riesgos de datos

| Organización y territorio | Fuente y fecha | Hecho documentado | Interpretación comercial lícita y limitación |
|---|---|---|---|
| **Rite Aid** · Estados Unidos | 2023-12-19, [autoridad](https://www.ftc.gov/legal-library/browse/cases-proceedings/2023190-rite-aid-corporation-ftc-v) | FTC resolvió prohibir por 5 años reconocimiento facial de vigilancia tras fallas de control y sesgos; acuerdo y proceso | No implica que hubiera LLM o fuga por prompt; ejemplo de obligación de evaluar IA y gestionar datos, no de algo que DELIA evite. |
| **Amazon Alexa** · Estados Unidos | 2023-05-31, [autoridad](https://www.justice.gov/archives/opa/pr/amazon-agrees-injunctive-relief-and-25-million-civil-penalty-alleged-violations-childrens) | DOJ/FTC anunciaron acuerdo con pago civil US$25 millones por privacidad infantil y retención de grabaciones | Retención y consentimiento no se resuelven con un proxy de prompts; usar como costo de fallos de gobernanza. |
| **OpenAI ChatGPT** · Italia | 2024-12-20, [autoridad](https://www.gpdp.it/home/docweb/-/docweb-display/docweb/10150195) | Garante italiano aplicó multa de €15 millones por tratamiento de datos y obligaciones de información | No prometer que DELIA ofrece cumplimiento completo ni que hubiera fuga a través de API. |
| **Clearview AI** · Italia | 2022-03-09, [autoridad](https://www.edpb.europa.eu/news/national-news/2022/facial-recognition-italian-sa-fines-clearview-ai-eur-20-million_en) | La autoridad italiana impuso multa €20 millones por tratamiento biométrico ilícito | Caso biométrico no LLM; ilustra límites legales a reutilización de datos. |
| **Meta Facebook** · Irlanda/UE | 2024-12-17, [autoridad](https://dataprotection.ie/en/news-media/press-releases/irish-data-protection-commission-fines-meta-eu251-million) | DPC anunció multa €251 millones por fallo de seguridad de tokens | Control de tokens y seguridad es distinto de DLP de prompts. Ejemplo de que la seguridad requiere múltiples controles. |
| **Meta contraseñas** · Irlanda/UE | 2024-09-27, [autoridad](https://dataprotection.ie/en/news-media/press-releases/DPC-announces-91-million-fine-of-Meta) | DPC anunció multa €91 millones por almacenamiento de contraseñas en texto sin cifrar | DELIA actual no cifra contraseñas ni corrige almacenamiento de credenciales. |
| **Avast** · Estados Unidos | 2024-06-26, [autoridad](https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-finalizes-order-avast-banning-it-selling-or-licensing-web-browsing-data-advertising-requiring-it) | FTC finalizó orden por venta de datos de navegación y pago de US$16,5 millones | Venta de datos es un riesgo de privacidad, no incidente atribuible a uso de LLM. |
| **GM / OnStar** · Estados Unidos | 2026-01, [autoridad](https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers) | FTC finalizó acuerdo por recolección y venta de geolocalización sin consentimiento adecuado | El caso no implica bots ni agentes; consentimiento y gobierno de datos son responsabilidad organizacional. |
| **Gravy Analytics / Venntel** · Estados Unidos | 2025-01, [autoridad](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-prohibiting-gravy-analytics-venntel-selling-sensitive-location-data) | FTC finalizó orden que prohíbe vender datos de ubicación sensibles | No LLM; uso para discutir minimización de datos sensibles. |
| **Mobilewalla** · Estados Unidos | 2025-01, [autoridad](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-banning-mobilewalla-selling-sensitive-location-data) | FTC finalizó orden sobre venta de datos de ubicación sensibles | No LLM; evitar narrativa falsa sobre incidentes causados por IA generativa. |

**Caso adicional en seguimiento:** DeepSeek y autoridad PIPC Corea (2025, [fuente oficial](https://pipc.go.kr/eng/user/ltn/new/noticeDetail.do?bbsId=BBSMSTR_000000000001&nttId=2819)): requiere comprobar resolución exacta y medidas antes de usarlo en una presentación. No sumar como sanción verificada sin revisar. Distinguir siempre **multa definitiva, acuerdo administrativo, orden y acusación**; los expedientes son jurídicamente distintos.

**Uso autorizado en conversación:** «Los reguladores examinan prácticas de privacidad y seguridad incluso cuando la tecnología es nueva. ¿Qué controles y evidencias tienen hoy?». **Uso prohibido:** «DELIA hubiera evitado estas diez multas» o «estas empresas sufrieron filtraciones por IA generativa», pues es falso en numerosos casos.

## 5. Mapa regulatorio aplicado a la oferta

| País | Norma/autoridad | Obligación real / estado | Fecha y fuente | Parte técnica que podría ayudar (HP, futura) | Qué NO resuelve DELIA |
|---|---|---|---|---|---|
| Chile | Ley 19.628 actual y Ley 21.719 publicada | Obligaciones de tratamiento legítimo, información, seguridad, derechos titulares y régimen reformado cuando entre en vigor. **Estado:** Ley 21.719 fecha legal 01-12-2026 al 31-10; prórroga 2027 era proyecto sin publicación final | [Texto oficial](https://www.bcn.cl/leychile/Navegar/imprimir?idNorma=1209272) | Sanitizar datos antes de API podría ayudar a minimización si se integra y valida | No sustituye bases de licitud, información al titular, contratos, gestión derechos, autoridad ni cumplimiento automático |
| Chile | CMF outsourcing y capítulo RAN 20-7 | Diligencia de terceros, gestión de proveedores y continuidad en entidades sujetas. **Estado:** RAN vigente; actualización consultada durante 2026 | [Texto oficial](https://www.cmfchile.cl/portal/prensa/625/w4-article-109289.html) | Trazabilidad técnica futura ayudaría a evidencias complementarias | No entrega autorizaciones, reportes CMF, política de proveedores ni certificación |
| México | LFPDPPP 2025 reformada 2025 | Deberes de aviso privacidad, finalidades, seguridad, transferencias, derechos ARCO según rol. **Estado:** Publicada 20-03-2025, reformada 14-11-2025, vigente al corte | [Texto oficial](https://www.te.gob.mx/legislacion/media/files/3cc41f81a66fca1.htm) | Reducción de datos transmitidos a terceros, solo tras integración y pruebas | No produce avisos, consentimiento, atención ARCO, evaluación jurídica ni elimina obligación de seguridad |
| Colombia | Ley 1581/2012 y Circular SIC 002/2024 | Tratamiento transparente, seguridad, finalidad, necesidad/proporcionalidad, responsabilidad demostrada en IA. **Estado:** Ley vigente; Circular SIC publicada 21-08-2024 | [Texto oficial](https://cancilleria.gov.co/normograma/compilacion/docs/circular_superindustria_0002_2024.htm) | Minimización y registro auditado pueden apoyar parte de salvaguardas en futuro | No sustituye autorización, contratos transmisión, DPIA, derechos titular ni ley especial |
| Colombia | Circular SIC 001/2025 sector fintech | Instrucciones sectoriales de tratamiento datos fintech. **Estado:** Publicada 18-09-2025 | [Texto oficial](https://sedeelectronica.sic.gov.co/transparencia/normativa/circular-externa-001-del-18-de-septiembre-de-2025) | Políticas DLP futuras pueden complementar controles organizacionales | No es una autorización para usar modelos ni certificación |
| Bolivia | Constitución y Ley 164 (marco sectorial) | Derechos y obligaciones existentes en sectores pertinentes. **Estado:** Marco vigente; debe ser interpretado según sector | [Texto oficial](https://www.att.gob.bo/static/LEY164.pdf) | Posible minimización técnica por contrato | No garantiza cumplimiento sectorial ni transfronterizo |
| Bolivia | Proyecto Ley de Protección Datos PL538 2025–2026 | Borrador plantea obligaciones de datos personales; analizar si se promulga. **Estado:** Al 31-10-2026 listado como proyecto 'en tratamiento', **NO una ley integral promulgada verificada** | [Texto oficial](https://diputados.gob.bo/proyectos-de-ley-en-tratamiento/) | Adaptación futura si se aprueba | No comercializar cumplimiento de texto todavía no vigente |

**Especial Chile:** estado legal al corte **no equivale** a promesa de que la prórroga ocurrirá; consultar el [texto BCN](https://www.bcn.cl/leychile/Navegar/imprimir?idNorma=1209272) y [tramitación Senado](https://www.senado.cl/comunicaciones/noticias/proteccion-de-datos-personales-avanza-proyecto-que-busca-postergar-entrada) antes de cada discurso. **Especial Bolivia:** el proyecto de ley se mantiene como proyecto en la [Cámara de Diputados](https://diputados.gob.bo/proyectos-de-ley-en-tratamiento/), no invocar protección de datos «aprobada» cuando no esté promulgada.

**Núcleo ético:** anonimización/seudonimización **no siempre saca datos del ámbito de protección personal**. El cliente necesita base de tratamiento, contratos, limitación de acceso, gobernanza y revisión por profesional local. DELIA, si se desarrolla y valida, podría ser un **control técnico de apoyo**, no el cumplimiento completo.

## 6. Quince fichas comparativas de competidores y sustitutos

Las tarifas son **precios anunciados al corte**, sujetos a cambios y límites. No son gasto real LATAM ni WTP de DELIA. **NV** significa que no se confirmó precio o cobertura específica. No afirmar debilidad de español/LatAm si el proveedor soporta personalización o no se revisó un benchmark.

### C01 — Cloudflare AI Gateway

- **Qué ofrece públicamente (HV proveedor):** Gateway, caching, analytics, rate limits y DLP con opciones gratuitas.
- **Precio y límites consultados:** Base gratis; costes de registros/políticas según plan y funciones. [Fuente oficial](https://developers.cloudflare.com/ai-gateway/reference/pricing/).
- **Español y LATAM:** No se verificó falta de soporte RUT/NIT; se debe benchmarkear.
- **Respuesta ante objeción del cliente:** Si ya resuelve necesidad, reconocerlo; comparar precisión de IDs regionales y costo total.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C02 — LiteLLM

- **Qué ofrece públicamente (HV proveedor):** Proxy multiproveedor, tokens, presupuestos, routing/fallback.
- **Precio y límites consultados:** OSS sin costo de licencia; infraestructura y soporte no gratuitos; enterprise cotizar. [Fuente oficial](https://www.litellm.ai/pricing).
- **Español y LATAM:** Falta de IDs LatAm no verificada; plugins/extensibilidad disponibles.
- **Respuesta ante objeción del cliente:** Distinguir control LLM estándar del diferencial regional medible.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C03 — Portkey

- **Qué ofrece públicamente (HV proveedor):** Gateway, guardrails, logs, routing.
- **Precio y límites consultados:** Production desde US$49/mes en página comercial; términos según plan. [Fuente oficial](https://portkey.ai/pricing).
- **Español y LATAM:** No afirmar ausencia de controles locales.
- **Respuesta ante objeción del cliente:** Comparar pruebas PII en español, retención logs y costo total.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C04 — Lakera Guard

- **Qué ofrece públicamente (HV proveedor):** Clasificación de prompt injection y seguridad LLM.
- **Precio y límites consultados:** Community gratis limitada; plan enterprise a cotizar. [Fuente oficial](https://us-east-1-internal.platform.lakera.ai/pricing).
- **Español y LATAM:** No es sustituto completo de gobierno de PII.
- **Respuesta ante objeción del cliente:** Complementariedad potencial; no prometer detección de ataques no implementada.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C05 — Nightfall

- **Qué ofrece públicamente (HV proveedor):** DLP datos corporativos en SaaS, cloud y asistentes.
- **Precio y límites consultados:** Cotización, no verificable tarifa fija para todos los planes. [Fuente oficial](https://www.nightfall.ai/pricing).
- **Español y LATAM:** Cobertura RUT/NIT/CURP no verificada.
- **Respuesta ante objeción del cliente:** Preguntar si ya lo usa y qué integración falta.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C06 — Microsoft Purview

- **Qué ofrece públicamente (HV proveedor):** DLP y postura de datos de M365/entorno empresarial.
- **Precio y límites consultados:** Licenciamiento por producto y uso; cifra homogénea no verificable. [Fuente oficial](https://learn.microsoft.com/en-us/purview/data-security-posture-management-setup).
- **Español y LATAM:** No afirmar que no cubra español o reguladores locales.
- **Respuesta ante objeción del cliente:** Evaluar si el stack M365 existente resuelve todo.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C07 — Microsoft Presidio

- **Qué ofrece públicamente (HV proveedor):** Motor abierto PII NER+regex extensible; bibliotecas Python.
- **Precio y límites consultados:** Código OSS sin licencia de producto; requiere operar y mantener. [Fuente oficial](https://microsoft.github.io/presidio/supported_entities/).
- **Español y LATAM:** Puede extenderse a IDs regionales, por tanto no monopolio DELIA.
- **Respuesta ante objeción del cliente:** Comparar sintéticos y esfuerzo de mantener recognizers.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C08 — Azure AI Gateway / API Management

- **Qué ofrece públicamente (HV proveedor):** Gateway con políticas y cuotas; considerar versiones preview.
- **Precio y límites consultados:** Precio dependiente de instancia/preview, no comparación homogénea. [Fuente oficial](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview).
- **Español y LATAM:** No atribuir falta de soporte español.
- **Respuesta ante objeción del cliente:** Benchmark políticas y costos incrementales sobre Azure contratado.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C09 — AWS Bedrock Guardrails

- **Qué ofrece públicamente (HV proveedor):** Filtros PII, contenido y controles en AWS.
- **Precio y límites consultados:** Precio de uso por políticas; ej. US$0.10 por 1.000 text units, verificar región. [Fuente oficial](https://aws.amazon.com/bedrock/pricing/).
- **Español y LATAM:** Soporte IDs regionales debe contrastarse en documentación.
- **Respuesta ante objeción del cliente:** En AWS nativo puede superar propuesta de DELIA; investigar lacuna concreta.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C10 — Google Model Armor

- **Qué ofrece públicamente (HV proveedor):** Inspección de prompts y respuestas.
- **Precio y límites consultados:** Standalone 2M tokens mensuales gratis y luego US$0.10/M tokens según plan publicado. [Fuente oficial](https://cloud.google.com/security/products/model-armor).
- **Español y LATAM:** No hay demostración que DELIA detecte más IDs.
- **Respuesta ante objeción del cliente:** Medir precision/recall y costo por millón, admitir paridad si la hay.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C11 — Langfuse

- **Qué ofrece públicamente (HV proveedor):** Observabilidad de traces, evaluaciones, costes.
- **Precio y límites consultados:** Hobby gratis; Core US$29/mes; Pro US$199/mes; Enterprise US$2499/mes en página. [Fuente oficial](https://langfuse.com/pricing).
- **Español y LATAM:** No es DLP universal por sí mismo.
- **Respuesta ante objeción del cliente:** Usarlo complementariamente; evitar competir por trazas solamente.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C12 — Helicone

- **Qué ofrece públicamente (HV proveedor):** LLM observability/gateway request logging.
- **Precio y límites consultados:** Free hasta 10k requests, Pro US$79/mes, Team US$799/mes, oferta sujeta cambios. [Fuente oficial](https://www.helicone.ai/pricing).
- **Español y LATAM:** No se verificó ID regional; no usar como defecto comprobado.
- **Respuesta ante objeción del cliente:** Comparar manejo de prompts sensibles y controles por equipo.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C13 — Kong AI Gateway

- **Qué ofrece públicamente (HV proveedor):** API gateway, autenticación, traffic/guardrails.
- **Precio y límites consultados:** AI Plus desde US$25/mes + consumo según página, enterprise cotizar. [Fuente oficial](https://konghq.com/pricing).
- **Español y LATAM:** Cobertura LATAM de políticas de datos no verificada.
- **Respuesta ante objeción del cliente:** El cliente Kong tal vez no necesita otro gateway.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C14 — Vercel AI Gateway

- **Qué ofrece públicamente (HV proveedor):** Gateway multi proveedor, observabilidad, créditos de uso.
- **Precio y límites consultados:** Free credit US$5/mes, pago por uso de proveedor, sin markup anunciado. [Fuente oficial](https://vercel.com/docs/ai-gateway/pricing).
- **Español y LATAM:** No verificar falta de español.
- **Respuesta ante objeción del cliente:** Conveniente para equipos Vercel; comparar extensión PII externa.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.

### C15 — OpenRouter

- **Qué ofrece públicamente (HV proveedor):** Routing de modelos y API única.
- **Precio y límites consultados:** Pago por tokens del proveedor y tarifas específicas, confirmar plan vigente. [Fuente oficial](https://openrouter.ai/pricing).
- **Español y LATAM:** No sustituye de suyo controles DLP enterprise.
- **Respuesta ante objeción del cliente:** Unificar proveedores no equivale a seguridad completa.
- **Prueba que falta:** benchmark de prompts sintéticos equivalentes, error por identificador regional, retención, integración, costos incrementales y controles existentes del cliente. **No se ha ejecutado**.


**Riesgo de sustitución:** si un cliente ya paga AWS/Azure/Google/Cloudflare con seguridad suficiente, instalar otro proxy puede aumentar superficie de ataque y costos. En tal caso ofrecer aprendizaje, no fingir diferencial.

## 7. Implicaciones comerciales y decisiones

**Recomendar primero** una oferta de descubrimiento con integradores: entrevistar responsable técnico, documentar casos reales y comparar soluciones actuales. No se deben enviar datos de clientes a servicios externos durante demostraciones. Usar [one-pager](ventas/ONE_PAGER_DELIA_ES.md), [guion de entrevista](ventas/ENTREVISTA_DESCUBRIMIENTO_30_MIN.md), [demostración segura](ventas/DEMO_SINTETICA_10_MIN.md) y [piloto](ventas/PLANTILLA_PILOTO_PAGADO_30_DIAS.md), todos marcados como materiales exploratorios. El precio y contrato están pendientes de aprobación.

**No usar incidentes como cuantificación ROI propia:** un caso de multa externa no es costo probable evitado por DELIA. La [calculadora ROI](ventas/ROI_CALCULADORA.csv) deja el costo evitado como escenario **hipotético**, configurable, y su versión conservadora debe establecer cero beneficios de incidentes hasta medirlo.

## 8. Registro de investigación y limitaciones

- **Consultado:** fuentes legales oficiales de cuatro países; documentación oficial de quince alternativas; diez expedientes regulatorios; sitios corporativos y directorios de identificación; versiones previas publicadas en main.
- **No hallado o no verificado:** evidencia de ventas de DELIA, compradores dispuestos a pagar, contactos personales/roles nominativos, contratos de partners, número nacional de integraciones productivas LLM, costo real de explotación, eficacia PII, fechas abiertas de numerosas convocatorias, stack confidencial por cuenta, validación LinkedIn+prensa de todas las 160 cuentas y páginas inaccesibles.
- **Evidencia insuficiente:** la presencia de 160 nombres no produce 160 empresas calificadas. Algunas referencias de directorio constituyen **presencia pendiente**, no prueba de funcionamiento ni identidad jurídica.
- **Siguiente auditoría:** contrastar 10 primeras cuentas de cada mercado con doble fuente y llamada voluntaria, retirar o sustituir cuentas de identidad web inconsistente, hacer benchmark de PII y corregir P0; actualizar puntuación con datos de entrevistas.

## 9. Fuentes principales adicionales (no equivalen a 150 páginas verificadas íntegramente)

1. Rite Aid — 2023-12-19: https://www.ftc.gov/legal-library/browse/cases-proceedings/2023190-rite-aid-corporation-ftc-v
2. Amazon Alexa — 2023-05-31: https://www.justice.gov/archives/opa/pr/amazon-agrees-injunctive-relief-and-25-million-civil-penalty-alleged-violations-childrens
3. OpenAI ChatGPT — 2024-12-20: https://www.gpdp.it/home/docweb/-/docweb-display/docweb/10150195
4. Clearview AI — 2022-03-09: https://www.edpb.europa.eu/news/national-news/2022/facial-recognition-italian-sa-fines-clearview-ai-eur-20-million_en
5. Meta Facebook — 2024-12-17: https://dataprotection.ie/en/news-media/press-releases/irish-data-protection-commission-fines-meta-eu251-million
6. Meta contraseñas — 2024-09-27: https://dataprotection.ie/en/news-media/press-releases/DPC-announces-91-million-fine-of-Meta
7. Avast — 2024-06-26: https://www.ftc.gov/news-events/news/press-releases/2024/06/ftc-finalizes-order-avast-banning-it-selling-or-licensing-web-browsing-data-advertising-requiring-it
8. GM / OnStar — 2026-01: https://www.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers
9. Gravy Analytics / Venntel — 2025-01: https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-prohibiting-gravy-analytics-venntel-selling-sensitive-location-data
10. Mobilewalla — 2025-01: https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-banning-mobilewalla-selling-sensitive-location-data
11. DeepSeek / PIPC — 2025: https://pipc.go.kr/eng/user/ltn/new/noticeDetail.do?bbsId=BBSMSTR_000000000001&nttId=2819
12. Cloudflare AI Gateway — ficha comercial: https://developers.cloudflare.com/ai-gateway/reference/pricing/
13. LiteLLM — ficha comercial: https://www.litellm.ai/pricing
14. Portkey — ficha comercial: https://portkey.ai/pricing
15. Lakera Guard — ficha comercial: https://us-east-1-internal.platform.lakera.ai/pricing
16. Nightfall — ficha comercial: https://www.nightfall.ai/pricing
17. Microsoft Purview — ficha comercial: https://learn.microsoft.com/en-us/purview/data-security-posture-management-setup
18. Microsoft Presidio — ficha comercial: https://microsoft.github.io/presidio/supported_entities/
19. Azure AI Gateway / API Management — ficha comercial: https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview
20. AWS Bedrock Guardrails — ficha comercial: https://aws.amazon.com/bedrock/pricing/
21. Google Model Armor — ficha comercial: https://cloud.google.com/security/products/model-armor
22. Langfuse — ficha comercial: https://langfuse.com/pricing
23. Helicone — ficha comercial: https://www.helicone.ai/pricing
24. Kong AI Gateway — ficha comercial: https://konghq.com/pricing
25. Vercel AI Gateway — ficha comercial: https://vercel.com/docs/ai-gateway/pricing
26. OpenRouter — ficha comercial: https://openrouter.ai/pricing

Para las 160 cuentas, la fuente por fila está en el [CSV](PROSPECTOS_RONDA2_160_CL_CO_MX_BO_2026-10-31.csv); para el resto de estadísticas consultar la bibliografía numerada del [estudio original](INTELIGENCIA_MERCADO_GO_TO_MARKET_CL_MX_CO_BO_2026-10-31.md).

**Registro complementario de fuentes y errores:** [REGISTRO_INVESTIGACION_RONDA2](REGISTRO_INVESTIGACION_RONDA2_2026-10-31.md).
