# DELIA — Estudio de mercado y prospección comercial B2B/B2C: Chile, México y Colombia

**Fecha de corte:** 31 de octubre de 2026  
**Versión:** 1.0 — investigación documental, propuesta para revisión de Dirección  
**Proyecto:** DELIA (MasterTech SpA)  
**Tipo de evidencia:** investigación secundaria con fuentes originales, resultados de encuestas publicadas y declaraciones corporativas verificables. **No constituye investigación primaria de clientes de DELIA.**  
**Clasificación:** análisis comercial público; sin datos personales ni contratos de clientes.  
**Estado de decisiones:** recomendaciones e hipótesis, no aprobación de precios, promesas de producto ni compromisos de ventas.

> **Conclusión ejecutiva.** Hay señales cuantificables de adopción de IA y de necesidad de gobernanza, pero **todavía no hay evidencia de clientes de DELIA, intención de compra, disposición de pago, demanda validada ni ventaja competitiva probada**. Recomendamos primero un proceso B2B de descubrimiento con desarrolladores de software e integradores que operan aplicaciones LLM, más pilotos técnicos controlados, antes de ofrecer DELIA como solución terminada. Las grandes entidades financieras son referentes de necesidad, no necesariamente el primer cliente accesible.

## 1. Pregunta de negocio, alcance y límites

**Pregunta:** ¿qué tipos de organizaciones de Chile, México y Colombia podrían tener razones para evaluar y eventualmente pagar un control de seguridad y gobernanza de solicitudes a modelos de IA, qué alternativas ya utilizan y qué debe probar DELIA para competir?

El producto considerado es el definido en el [README de DELIA](../README.md): capa intermediaria de seguridad entre aplicaciones y proveedores LLM; objetivos de detección/sanitización de PII, control de consumo, encaminamiento/fallback, trazabilidad y panel. Los módulos y su disponibilidad deben verificarse en código y pruebas; **no** asumimos que el proxy, los controles de autorización, el dashboard o la anonimización sean hoy un producto operable y seguro para terceros.

Separamos cuatro niveles:
- **H = hecho documentado:** fuente primaria u organización identificada, con fecha, alcance y cita.
- **D = dato de encuesta o modelo:** resultados sujetos a muestras, preguntas, estimaciones y sesgos específicos; no equivalen a población total ni intención de compra.
- **I = inferencia:** oportunidad plausible deducida de hechos, sin confirmación de la empresa aludida.
- **HV = hipótesis por validar:** precio, buyer persona, tasa de conversión, diferenciación y diseño comercial propuestos por MasterTech.

Este estudio es **desk research empírico de fuentes secundarias**, no un estudio empírico primario de disposición de pago. No se entrevistó a compradores, no se solicitaron cotizaciones, no se levantó un censo propio y no se ejecutaron pruebas de DELIA. Al comunicarlo externamente, no emplear expresiones como «mercado comprobado», «clientes interesados» o «cumplimiento garantizado».

**Mercados:** Chile, México y Colombia. **Canales evaluados:** B2B directo; B2B2B vía integradores/agencias tecnológicas; B2C directo a profesionales individuales (solo como contraste). Se excluyen del TAM cuantificado el gasto gubernamental, número total de empresas y presupuestos empresariales por falta de denominadores válidos para el caso de uso.

## 2. Evidencia cuantitativa: qué sabemos realmente

| Indicador | Resultado observado | Año / población / limitación | Lectura para DELIA | Fuente |
|---|---:|---|---|---|
| Uso de IA en empresas grandes de Latinoamérica | **27,6 %** | **Estimación econométrica** del ILIA 2026; no censo homogéneo ni clientes de gateways | Empresas grandes más expuestas a múltiples flujos IA, pero también con mayor exigencia y competencia | [R01], [R02] |
| Uso de IA en empresas medianas de Latinoamérica | **12,8 %** | Mismo modelo, alcance regional | Segmento a entrevistar; no asumir presupuesto de seguridad | [R01] |
| Uso de IA en empresas pequeñas de Latinoamérica | **6,8 %** | Mismo modelo, alcance regional | B2C y micropymes no parecen primer foco para un proxy especializado | [R01] |
| Índice general ILIA 2026 | **Chile 71,4; Colombia 56,8; México 52,0 puntos** | Índices compuestos de ecosistema; **no** porcentajes de uso ni de gasto | Capacidad y contexto regional, no ranking de oportunidades comerciales | [R02] |
| Organizaciones que usan IA al menos en una función | **88 %** | Encuesta McKinsey 2025 citada por Stanford AI Index 2026; muestra internacional no representativa de todas las empresas de los tres países | Señal global de expansión; no extrapolar a LATAM | [R03] |
| Chile: empresas que incorporaron tecnologías en últimos cinco años | **59 %** | Encuesta de Percepciones de Negocios octubre 2025 del Banco Central; mide **toda tecnología digital**, no IA específicamente | Digitalización existente puede facilitar adopción, no confirma uso de LLM | [R04] |
| México: unidades económicas con uso de «sistema de IA» | **2,1 %** | Censos Económicos 2024, datos 2023. **Denominador: subconjunto de 1.266.352 unidades que usaban herramientas digitales**, no todas las unidades económicas | Señal de baja penetración en el universo medido; no multiplicar por todas las empresas | [R05] |
| Colombia: IA como prioridad estratégica o pilar | **61 %** | Encuesta privada Endeavor Colombia, **n=493** organizaciones participantes, julio 2026; sesgo de selección posible | Interés estratégico en muestra, no compra de protección LLM | [R06] |
| Colombia: nivel avanzado de madurez IA | **0,2 %** | Mismo estudio privado y muestra (93,5 % en exploración/desarrollo) | Posible brecha de gobernanza; no implica intención de adquirir DELIA | [R06] |

**Precaución metodológica clave.** La diferencia entre el 88 % internacional, el 27,6 % regional para empresas grandes, el 2,1 % mexicano del subconjunto tecnológico y el 61 % colombiano de una encuesta de madurez **no es una contradicción que pueda resolverse promediando**. Cambian país, fecha, tamaño, definición de IA, pregunta, muestra y metodología. No sumar, promediar ni convertir estas cifras en «clientes potenciales pagadores».

En Chile, Buk reportó en una encuesta sobre prácticas laborales de IA realizada en 2026 que muchos trabajadores perciben falta de políticas de IA. Es indicio de brecha organizacional en **esa muestra**, no una estimación censal; se considera como señal secundaria, no base para tamaño de mercado [R07].

### 2.1. Tamaño de mercado: por qué no se proporciona un TAM monetario

No es metodológicamente válido calcular «número de empresas × porcentaje que usa IA × precio hipotético»: las encuestas citadas no miden uso de **APIs LLM con datos sensibles** ni intención de pago de un **gateway independiente**. Un SAM debería exigir, como mínimo, número de empresas con LLM en producción, sistemas a integrar, autoridad de compra, presupuesto y solución alternativa. Ninguna fuente regional aporta esas cinco variables con consistencia.

Se propone calcular **SOM operativo** a partir de cuentas identificadas y entrevistas reales, no de una cifra grandilocuente: cuentas alcanzables → organizaciones con caso de uso comprobado → conversaciones con decisores → pilotos consentidos → ofertas → contratos pagados. Los números se incorporarán **después** de observar resultados.

## 3. Tesis comercial y segmentación

### 3.1. Clientes que resuelven el problema con mayor intensidad (I/HV)

1. **Integradores, software factories y consultoras de automatización/IA B2B** que crean chatbots, copilotos, flujos RAG o agentes para clientes finales y quieren un control reutilizable. **Cliente pagador:** líder técnico, socio, CTO; **usuario:** desarrolladores y SRE; **beneficiarios:** clientes de la integradora. Hipótesis de acceso inicial **alta** por ciclo comercial potencialmente más simple; no cuantificada.
2. **SaaS B2B medianos que procesan datos personales, financieros, laborales o contractuales**, con integración propia a modelos. **Comprador:** CTO / CISO / director de producto; **dolor:** controles, trazas, secretos y costo por aplicación. Probable mejor opción para renovación recurrente, sujeto a pruebas.
3. **Fintech, seguros, servicios profesionales contables y plataformas de RR.HH.** con procesos automáticos que manipulan identificadores locales. **Comprador:** seguridad, ingeniería y compliance; mayor necesidad de evidencia, pero ciclo de compra más exigente.
4. **Contact centers/BPO con asistentes IA**, cuando operen con datos de terceros, multimodelo y políticas heterogéneas. Necesitan alta disponibilidad y operación consistente; integración en telefonía/CRM no debe suponerse implementada en DELIA.
5. **Bancos, retail grandes y hospitales** como cuentas estratégicas de largo plazo. Casos públicos de IA demuestran actividad, **no** necesidades descubiertas para DELIA; barreras de procurement, integraciones existentes, infraestructura, revisión legal y ciberseguridad elevadas.

**No cliente prioritario:** restaurantes, comercio pequeño sin IA conectada por API, personas que usan una interfaz web pública de ChatGPT sin control técnico de API, o negocios que solo quieren un chatbot. DELIA no gestiona automáticamente todos los usos de IA de una organización ni intercepta productos de terceros sin integración y permisos.

### 3.2. ¿Qué compra el decisor realmente?

No «un proxy inverso», sino un resultado verificable:
- **Reducir exposición de identificadores** en llamadas LLM autorizadas; comparar precisión con casos sintéticos, especialmente RUT, cédula y NIT.
- **Controlar usuarios, aplicaciones, destinos y consumo** en API; demostrar que las reglas no se eluden fácilmente.
- **Obtener evidencias operativas útiles** para seguridad y auditoría sin almacenar el prompt sensible de manera innecesaria.
- **Simplificar la integración para un equipo técnico pequeño** sin asumir cumplimiento legal automático.

**Condición imprescindible:** demostrar al menos uno de estos resultados frente a alternativa gratuita o existente. Si un comprador ya cubre su necesidad con Cloudflare, LiteLLM, Azure o proveedores propios, DELIA no tiene una propuesta comprobada para esa cuenta.

## 4. Evaluación específica por país

### 4.1. Chile — primer mercado propuesto para validación (HV)

**Contexto documentado.** Chile registra 71,4 puntos en ILIA 2026, con adopción empresarial estimada de 13,5 % según CENIA; estos números representan dimensiones distintas y **no** intención de compra [R02]. Banco de Chile anunció en octubre de 2025 una alianza de IA generativa con Microsoft [R12]. Grupo Falabella comunicó en septiembre de 2026 que IA y datos eran apuestas de inversión tecnológica, con casos operativos [R13]. Buk publica investigaciones de aplicación de IA en RR.HH. [R14]. Una nota de la Cámara de Comercio de Santiago describe una oferta de agentes conversacionales de indigitall para empresas chilenas [R15].

**Regulación: cuidado con el calendario.** La **Ley 21.719** figura en la Biblioteca del Congreso con entrada en vigor el **1 de diciembre de 2026** [R08]. El Ejecutivo presentó una postergación y **el Senado aprobó una iniciativa de modificación el 28 de octubre**, que continuaba su trámite legislativo; por tanto **no anunciar como definitiva una prórroga a 2027** [R09]. La seguridad de datos y las normas aplicables requieren evaluación jurídica por organización; DELIA no «hace cumplir» la ley por instalarse.

**Primer nicho sugerido:** empresas de software B2B e integradores de asistentes con datos comerciales/personales; abrir después fintech mediana y plataformas HR. **Por qué Chile primero:** proximidad operativa de MasterTech, conocimiento de identificadores locales y facilidad para realizar entrevistas en el mercado de origen (ventajas estratégicas internas, no estadísticas de demanda).

**Hipótesis de mensaje comercial:** «¿Cómo validan que los datos personales de sus clientes no terminen innecesariamente en las solicitudes a proveedores LLM, y cómo prueban esos controles?».

**Riesgos:** adopción empresarial aún limitada, plazos regulatorios cambiantes y alternativas incluidas en plataformas ya contratadas.

### 4.2. México — mercado de expansión y aprendizaje, no compra asumida (HV)

**Contexto documentado.** Los Censos Económicos 2024 de INEGI registraron 2,1 % de uso de sistemas IA **entre unidades económicas que declararon usar herramientas digitales**, con información de 2023 [R05]. Es un indicador histórico de una clasificación específica, no una medición de «GenAI en empresas» de 2026. Las empresas formales medianas y grandes deben identificarse por madurez real, no por la enorme población total de negocios.

**Señales corporativas públicas:** BBVA México informó un asistente generativo en su atención telefónica (agosto 2025) [R16]; Kueski declaró uso de decisiones basadas en IA y mayor inversión en gestión de fraude (febrero 2026) [R17]; Konfío explica el uso de analítica e IA en sus servicios financieros [R18]; Alegra presentó el 22 de octubre de 2026 un agente de IA para operaciones contables en México [R19]. Son **organizaciones observables**, no leads confirmados, presupuestos identificados ni clientes que estén buscando DELIA.

**Marco normativo:** la nueva Ley Federal de Protección de Datos Personales en Posesión de los Particulares fue publicada el **20 de marzo de 2025**, con reformas posteriores de noviembre de 2025 [R10]. No confundirla con la antigua versión de 2010. Evaluar jurídicamente rol, transferencias, avisos, medidas de seguridad, bases de tratamiento y relación con cada proveedor.

**Primer nicho sugerido:** integradoras mexicanas de automatización, proveedores SaaS contables y fintech medianas con ingeniería propia; bancos son casos de estudio y posibles alianzas posteriores, no primer objetivo de cierre.

**Mensaje de entrevista:** «¿Cuántos productos usan APIs de modelos y qué se envía hacia ellos? ¿Cómo diferencian PII mexicana y otros secretos comerciales antes de transferir el prompt?».

**Riesgos:** mayor distancia operativa, soluciones globales y capacidades internas de empresas grandes; todavía no existen referencias comerciales de DELIA.

### 4.3. Colombia — nicho de SaaS contable/fintech con datos estructurados (HV)

**Contexto documentado.** Endeavor Colombia entrevistó a **493 organizaciones participantes** en julio de 2026; 61 % llamó estratégica a la IA, pero solo 0,2 % apareció en madurez avanzada en su metodología [R06]. No extrapolar esa muestra a todas las empresas. El DANE publicó estadísticas TIC 2024 de establecimientos manufactureros; su marco muestral y sus indicadores tampoco son directamente intercambiables con Endeavor [R20]. El **CONPES 4144/2025** es política nacional de IA, **no una certificación ni una ley que obligue a comprar DELIA** [R21].

**Señales corporativas públicas:** Siigo describe un producto contable potenciado con IA y documentó una integración MCP con asistentes externos, que interactúa con clientes, facturas y productos [R22]; Seguros SURA/Suramericana documenta inversión tecnológica y transformación digital [R23]; Alegra comunicó actividades de integración entre contabilidad e IA durante Colombia Tech Week (agosto 2026) [R24].

**Marco normativo:** la SIC publicó la **Circular Externa 002 del 21 de agosto de 2024** sobre tratamiento de datos en sistemas IA [R11], en el marco colombiano de protección de datos (Ley 1581 de 2012). La existencia de la circular no prueba que cada integración requiera un intermediario concreto. Revisar también el régimen contractual, protección de datos y condiciones del sector si corresponde.

**Primer nicho sugerido:** integradores de IA para despachos contables, software de facturación/ERP que conecta a asistentes y fintech con sistemas conversacionales. **Ventaja por probar:** RUT/NIT/cédula con menor tasa de error en español y política demostrable de minimización.

**Mensaje de entrevista:** «Cuando un asistente consulta facturas, clientes y NIT, ¿qué parte de los datos llega al modelo, cómo se autoriza y qué auditoría conserva el proveedor?».

**Riesgos:** dificultad de atribuir ahorros; integraciones de terceros ya disponen de permisos; la calidad de detección contextual no puede depender exclusivamente de expresiones regulares.

## 5. Lista inicial de cuentas observables — NO son leads confirmados

La siguiente lista contiene **entidades con actividad documentada** relacionada con IA, datos o integración; su inclusión no implica contacto, interés, capacidad de contratación, búsqueda de proveedores ni disposición a pagar. Prioridad de conversación: **E = exploración técnica/alianza**, **L = referencia de comprador grande/largo plazo**. No hay puntajes numéricos de propensión a compra.

| País | Organización / evidencia pública | Posible pregunta de descubrimiento (I) | Entrada sugerida | Clase | Fuente |
|---|---|---|---|---|---|
| Chile | **Banco de Chile**, alianza con Microsoft para IA generativa | ¿Qué controles ya cubre su stack empresarial y cuáles faltan? | Tecnología / riesgo / innovación | L | [R12] |
| Chile | **Falabella**, inversión anunciada en IA y datos | ¿Cómo gobiernan asistentes y agentes en distintos procesos? | Arquitectura / seguridad / innovación | L | [R13] |
| Chile | **Buk**, tecnología y estudios de IA en RR.HH. | ¿Qué PII laboral entra a asistentes y cómo se minimiza? | Ingeniería / seguridad / producto | E | [R14] |
| Chile | **indigitall**, oferta de agentes IA multicanal | ¿Qué controles adicionales solicitan sus clientes corporativos? | Alianzas / ingeniería de integraciones | E | [R15] |
| México | **BBVA México**, asistente de atención basado en IA | ¿Qué protección está cubierta por tecnologías internas y contratadas? | Seguridad / arquitectura | L | [R16] |
| México | **Kueski**, decisiones IA y control de fraude | ¿Qué uso de modelos externos justifica un control adicional? | Seguridad / plataformas / datos | L | [R17] |
| México | **Konfío**, negocio financiero digital impulsado por analítica | ¿Qué flujos usan LLM frente a ML tradicional? | Arquitectura / CTO | E | [R18] |
| México | **Alegra México**, agente contable lanzado en octubre 2026 | ¿Cómo limitan exposición de CFDI y datos contables en llamadas LLM? | Producto / seguridad / integraciones | E | [R19] |
| México | **Sinergy Solutions**, integradora de IA y análisis empresarial | ¿Necesitan una capa local reutilizable para clientes? | Dirección técnica / alianzas | E | [R25] |
| Colombia | **Siigo**, integración MCP y software contable con IA | ¿Cómo limitan contexto enviado y permisos sobre facturas y terceros? | Integraciones / seguridad / producto | E | [R22] |
| Colombia | **Suramericana / Seguros SURA**, transformación digital | ¿Hay casos LLM concretos, presupuestos e infraestructura aprobada? | Innovación / ingeniería / seguridad | L | [R23] |
| Colombia | **Alegra Colombia**, integración contabilidad e IA | ¿Dónde ocurre minimización de documentos antes de un asistente? | Integraciones / seguridad / alianzas | E | [R24] |

**Regla de prospección:** confirmar siempre por conversación (1) producto con LLM en producción, (2) sensibilidad de datos, (3) control existente, (4) autoridad de decisión, (5) urgencia y presupuesto. Sin esas cinco verificaciones, la cuenta es **objetivo de investigación**, no «prospecto calificado». No recolectar datos personales de ejecutivos ni inferir correos.

## 6. Entorno competitivo — comparación con fuentes oficiales

| Alternativa | Capacidades publicadas | Precio público verificable | Implicación para DELIA |
|---|---|---|---|
| **Cloudflare AI Gateway** | Analítica, caché y límites; **DLP de prompts y respuestas**, reglas de flag/block y perfiles PII [R26] | Funciones centrales gratuitas; costos y límites de logs dependen de plan/fecha de alta [R27] | Un gateway + DLP genérico **no basta** para diferenciarse |
| **LiteLLM** | Gateway autoalojable para múltiples modelos, llaves virtuales, presupuestos, rate limits, fallbacks, registros [R28] | Open Source **US$0 de licencia**, pero operación/infraestructura no gratuita; Enterprise bajo cotización [R28] | Riesgo de sustitución con software libre; se necesita mejor experiencia/reglas/servicios |
| **Portkey** | Gateway, fallback, observabilidad, guardrails y gobierno por plan [R29] | **US$49/mes** plan Production anunciado; Enterprise personalizado [R29] | Referencia verificable de precio de oferta, **no WTP de clientes LATAM** |
| **Microsoft Azure API Management / AI Gateway** | Políticas, controles de uso y centralización de modelos y herramientas; nuevas funcionalidades en preview según servicio [R30] | Depende de servicio/plan; no se utilizó cotización comparable | Cliente Azure puede preferir integración nativa |
| **Microsoft Purview** | Protección, clasificación y controles de datos relacionados con IA [R31] | Licencias y métricas variables; no comparable directamente con gateway puro | El comprador corporativo puede ya contar con medidas incluidas |

**Conclusión competitiva (I):** la diferenciación es potencialmente más defendible en **calidad demostrada para identificadores latinoamericanos + controles verificables de salida y acceso + integración local + soporte especializado**, no en ser «un proxy para muchas IA», ofrecer regex comunes o prometer cumplimiento. La calidad de detección debe compararse con estos competidores bajo un benchmark reproducible; aún no existe evidencia de que DELIA los supere. Tampoco se garantiza que rivales no incorporen reglas regionales.

## 7. Propuesta de valor y producto mínimo comercializable

### Perfil de comprador inicial (hipótesis)

- **ICP-A (preferente para entrevistas):** integradora de 10–100 personas que desarrolla 2 o más soluciones LLM B2B y ya tiene un responsable de arquitectura. El tamaño y número de proyectos son **filtros exploratorios**, no distribución empírica.
- **ICP-B:** SaaS B2B con datos de clientes y llamadas externas a modelos, presupuesto y equipo técnico para integrar.
- **ICP-C:** fintech/aseguradora mediana o proveedor especializado; posible mayor ticket, pero revisión de seguridad y adquisición más exigentes.

**Rechazos tempranos:** cliente no usa APIs LLM; no autoriza poner un proxy intermedio; ya dispone de cobertura suficiente; no puede medir el problema; exige certificaciones o SLA inexistentes; solicita procesar datos reales sin controles verificados.

### Alcance propuesto del MVP demostrable

1. API y sanitización de categorías efectivamente soportadas, con pruebas sintéticas Chile/México/Colombia.
2. Reglas explícitas **fail closed o fail open según riesgo**, configuradas y documentadas; no dejar la conducta indefinida.
3. Registro mínimo con identificador de evento y sin prompts en texto claro por defecto; controles de acceso verificados.
4. Pruebas de compatibilidad con proveedor simulado y al menos un proveedor autorizado en entorno de ensayo.
5. Procedimiento de integración reproducible, manejo de fallos y reversibilidad segura cuando corresponda (si se implementa).
6. Limitaciones y benchmark comparativo público, sin certificaciones de seguridad ni promesas de cumplimiento inventadas.

**No ofrecer hoy**: «100 % PII bloqueado», soporte universal de agentes, proxy de producción multi-tenant, certificaciones, cobertura legal garantizada o compatibilidad ya probada con todos los modelos, salvo que existan pruebas y documentación actualizadas.

## 8. B2B, B2B2B y B2C

| Canal | Dolor que podría monetizar | Evaluación inicial | Condición de éxito |
|---|---|---|---|
| **B2B directo** | Control de riesgos y costos de uno o varios productos LLM | Prioritario tras MVP verificable | Comprador identificado, necesidad explícita, integración real |
| **B2B2B integradores** | Componente reutilizable para múltiples clientes corporativos | **Primer canal de descubrimiento recomendado** | Partner con proyectos existentes, acuerdos claros de responsabilidades y soporte |
| **B2C desarrolladores individuales** | Probar filtros/reglas, depurar integraciones | **No priorizar monetización masiva** por fuertes alternativas gratuitas | Experiencia notablemente más sencilla o casos regionales no cubiertos; validar conversiones |
| **Gobierno / salud / banca grande** | Cumplimiento contractual, controles y auditoría estrictos | Largo plazo, no vía inicial para empresa sin certificaciones ni casos | Referencias, seguridad auditada, SLA, requisitos legales y compras formales |

La etiqueta «B2C» no debe confundirse con empresas muy pequeñas: un programador individual que paga una licencia es consumidor final de una herramienta de desarrollo; un negocio que compra integración sigue siendo B2B.

## 9. Precios: evidencia competitiva y experimentos de voluntad de pago

**Lo que sí sabemos:** Cloudflare anuncia funciones base gratis [R27]; LiteLLM es gratuito de autoalojar [R28]; Portkey publica **US$49/mes** para Production y cotización empresarial [R29]. Esos son **precios de proveedores**, no precios pagados por empresas chilenas/mexicanas/colombianas ni indicadores de su disposición a pagar por DELIA.

**Hipótesis de test comercial, no lista aprobada:**

| Concepto a testear | Rango exploratorio US$ | Qué habría que entregar | Evidencia requerida |
|---|---:|---|---|
| Piloto corto acotado (integración y medición) | Cotización caso por caso; **sin tarifa pública aún** | Alcance, duración, datos sintéticos, soporte, criterios de éxito | Compromiso escrito o pago efectivo; evitar trabajo sin alcance |
| Plan técnico pequeño | **49–99/mes** (HV) | Funciones verificadas, límites claros, soporte definido | Al menos 5 conversaciones sobre alternativas y sensibilidad al precio |
| Plan equipo B2B | **199–499/mes** (HV) | Integraciones, multiusuario/auditoría en la medida desarrollada | Pilotos con uso recurrente y acuerdos sobre responsabilidades |
| Corporativo / privado | **A cotizar** | Arquitectura, despliegue, seguridad, soporte y SLA negociados | Due diligence, costos y contrato específico |

**Estos rangos fueron propuestos para ENTREVISTAR y CONTRASTAR, no obtenidos de una encuesta ni justificados por ROI demostrado.** No publicar precios comerciales de DELIA hasta validar costos de servidores, monitoreo, soporte, incidentes, almacenamiento, proveedores, impuestos, trabajo de integración, churn y margen. Un cliente puede tener una alternativa gratuita; no asumir que un descuento provoca demanda.

**Preguntas de WTP:** «¿Qué solución paga hoy y cuánto cuesta en total operarla?»; «¿Quién autoriza una compra?»; «¿Qué cambio concreto justificaría pagar?»; «¿Preferirían implementación única o suscripción?»; «¿Firmarían un piloto pagado bajo estos criterios?». Evitar «¿pagarías US$399?» sin contexto: produce sesgo hipotético.

## 10. Protocolo empírico de validación: 90 días

**El objetivo es obtener evidencia de compradores y de uso, no generar un porcentaje ficticio de adopción.** Las cantidades son metas operativas sugeridas, no pronósticos.

**Días 1–15 — investigación de clientes y control de narrativa**
- Fijar baseline técnico: ejecutar y documentar pruebas, funcionalidades realmente disponibles, infraestructura y fallas conocidas.
- Construir 45–60 cuentas de investigación: 15–20 por país, mezcla de integradores, SaaS y regulados; separar cuentas sin identificación de comprador.
- Preparar oferta de **descubrimiento**, sin prometer seguridad ni solicitar datos de clientes.
- Entrevistar inicialmente **5 decisores por país** si aceptan: CTO, CISO, líder de plataforma, dueño de software o ingeniería de datos.

**Días 16–35 — entrevistas y segmentación**
- Meta: **15–24 entrevistas efectivamente realizadas** en tres países, registrando fechas, tamaño, sector, solución, coste del problema, competencia y objeciones.
- Registrar evidencia de un problema *actual y costoso* frente a la respuesta de «solo sería útil algún día».
- Clasificar cada cuenta: desconocida / problema documentado / comprador identificado / pilotable / oferta solicitada / cerrado.
- No registrar nombres privados, contratos o datos personales en el repositorio público; mantener un CRM interno con permisos.

**Días 36–60 — benchmark y pilotos no sensibles**
- Benchmark PII con **dataset sintético consentido y reproducible** por país; medir precisión, recall, falsos positivos, falsos negativos y latencia, con intervalos por categoría.
- Comparar al menos una alternativa abierta y una administrada si su licencia/entorno lo permiten.
- Proponer **hasta 3 pilotos** controlados a organizaciones que demostraron interés, con acuerdo, alcance y criterios de éxito.
- Evitar producción con datos de salud/financieros/personales hasta superar revisión técnica y legal correspondiente.

**Días 61–90 — prueba comercial**
- Emitir propuestas con alcance, límites, servicio, plazos, presupuesto, uso de datos y resultados verificables.
- Registrar conversaciones sobre precios, objeciones, competidores, tiempos de decisión y, solo cuando suceda, contratos firmados/cobros efectivamente percibidos.
- Decidir continuar, pivotar nicho o pausar con base en actas y resultados; ningún número de entrevistas sustituye una compra.

### 10.1. Umbrales de decisión internos propuestos (no estadística de mercado)

- **Seguir explorando:** al menos 5 decisores relatan incidentes/retrasos/costos de manejo de datos que pueden documentar y declaran una alternativa actual insuficiente.
- **Construir piloto:** al menos 2 organizaciones confirman entorno de prueba, responsable técnico, criterios de aceptación y colaboración explícita.
- **Validación comercial inicial:** al menos **1 compromiso pagado real** y repetición de la necesidad en más de una cuenta. Una carta de interés no equivale a venta.
- **Pausar/pivotar:** predominan respuestas «ya lo cubre Azure/LiteLLM/Cloudflare»; sin control diferencial medible; el costo de integrar DELIA supera el valor percibido; no hay patrocinador presupuestario.

Estos umbrales son reglas de gestión para la primera ronda, no hipótesis estadísticas contrastadas ni garantía de product-market fit.

## 11. Guion de entrevistas B2B (12 preguntas abiertas)

1. ¿Qué productos o servicios usan actualmente modelos generativos mediante API? ¿Desde cuándo y con qué usuarios?
2. ¿Qué información llega al modelo y cuáles categorías consideran confidenciales o personales?
3. ¿Qué proveedor(es) y gateway usan hoy, si alguno? ¿Por qué lo eligieron?
4. ¿Han tenido problemas verificables de información expuesta, claves, cuotas, latencia o auditoría? ¿Cuándo y qué pasó?
5. ¿Qué políticas internas o requisitos contractuales deben satisfacer?
6. ¿Quién mantiene controles de privacidad y qué porcentaje de tiempo operativo les consume?
7. ¿Cómo se detectan/ocultan identificadores locales (RUT, cédula, NIT u otros) y cómo miden errores?
8. ¿Qué ocurre ante una caída del proveedor, del control o de la base de datos?
9. ¿Qué cambiarían de la solución actual? ¿Qué no cambiarían?
10. Si una herramienta resolviera una sola carencia, ¿cuál tendría más valor y cómo lo medirían?
11. ¿Quién decide comprar, cuál sería el proceso y qué presupuesto/contrato existe?
12. ¿Aceptarían una prueba con datos sintéticos y criterios acordados? ¿Qué tendría que pasar para convertirla en una compra?

**No inducción:** preguntar por problemas y gasto real antes de mostrar DELIA o preguntar «¿lo compraría?». Registrar citas breves solo con autorización, separar entrevistado de comprador y guardar datos identificativos fuera de GitHub público.

## 12. Matriz de señales y prioridades

| Criterio | Evidencia necesaria | Si no existe |
|---|---|---|
| Problema específico | Incidente, exposición real o trabajo manual medible | Tratar como curiosidad, no venta |
| Uso actual del producto objetivo | Llamadas a APIs LLM, datos y volumen comprobables | No ofrecer proxy |
| Diferencia frente a competidores | Benchmark o costo total menor para la misma función | No afirmar ventaja |
| Comprador y presupuesto | Persona con autoridad + proceso + partida o pago aceptado | Continuar investigación |
| Seguridad para el piloto | Datos sintéticos, permisos, términos, aislamiento, logs adecuados | No procesar datos reales |
| Repetibilidad | Más de una organización con necesidades similares | Puede ser desarrollo a medida, no SaaS repetible |

**Priorización estratégica provisional** (no ranking de mercado derivado de estadísticas):
- **1. Chile:** entrevistas locales con software factories y SaaS B2B; proximidad y riesgo regulatorio que motiva conversaciones.
- **2. México:** expansión comercial e integradores con agentes ya desplegados, especialmente SaaS/fintech; mercado de casos públicos amplio, pero ventas no comprobadas.
- **3. Colombia:** integradores de ERP/contabilidad y soluciones IA que interactúan con NIT, facturas y datos de terceros; legislación SIC como contexto.

La secuencia es una **decisión de ejecución para MasterTech**, no conclusión de que un país pagará más. Se cambiará si las entrevistas muestran más urgencia o facilidades de compra en otro mercado.

## 13. Riesgos que pueden invalidar la tesis

1. **Comoditización:** Cloudflare y LiteLLM ya ofrecen partes sustantivas del gateway; diferencial local insuficiente.
2. **Seguridad y reputación:** una regla regex puede omitir datos contextuales; un proxy inseguro puede aumentar superficie de ataque. No cobrar por protección sensible sin verificación rigurosa.
3. **Responsabilidad de cumplimiento:** tratamiento transfronterizo y obligaciones sectoriales no se resuelven con sustitución de texto; pseudonimización puede seguir siendo dato personal.
4. **Economía de implementación:** soporte, disponibilidad, despliegue por cliente y gestión de incidentes pueden costar más que la suscripción.
5. **Ciclo de ventas y confianza:** sin casos publicados, certificaciones ni equipo de soporte, grandes bancos son difíciles como primeros clientes.
6. **Confusión del comprador:** «seguridad para ChatGPT» puede inducir la idea de que intercepta cualquier aplicación de terceros; delimitar a integraciones técnicas controladas.
7. **Datos de marketing:** porcentajes de «uso de IA» de encuestas no son porcentajes de «API LLM» ni presupuestos de gateways.
8. **Riesgo legal temporal:** Chile tiene discusión legislativa sobre fecha de vigencia; comprobar cambios antes de cada propuesta.

## 14. Plan operativo de prospección con recursos limitados

**Entregable 1 — CRM interno** (no público): fuente, empresa, país, segmento, evidencia de uso LLM, hipótesis del problema, rol del comprador, fecha del primer contacto, respuesta y estado. Evitar teléfonos y correos extraídos sin base o consentimiento, y no revelar contactos actuales.

**Entregable 2 — ficha por país y vertical**: un problema real, ejemplo sintético, arquitectura esperada, controles disponibles vs pendientes y un guion técnico de 2 minutos.

**Entregable 3 — demostración verificable**: repo/procedimiento + dataset sintético + resultados medidos + limitaciones; no prometer certificación ni preproducción.

**Entregable 4 — informe de entrevistas**: muestra efectiva, tasa de respuesta observada, alternativa utilizada, presupuesto si se revela, voluntad real de piloto, objeciones y decisión continuar/pivotar.

**Responsabilidades recomendadas para coordinación posterior:** dirección comercial define ICP y entrevistas; responsables técnicos validan código, pruebas y seguridad; Operaciones documenta acuerdos e hitos. **No asigna tareas, cargos ni compromisos a personas concretas ni presupone su disponibilidad.**

## 15. Decisión recomendada a la Dirección (31/10/2026)

**GO condicional para descubrimiento B2B; NO-GO para prometer comercialización de DELIA como protección completa hoy.** Validar un problema específico y la diferencia frente a los proveedores instalados antes de invertir intensivamente en un SaaS amplio. Primer canal sugerido: integradores y proveedores SaaS que ya ejecutan casos de IA para terceros. A la par, asegurar que las pruebas técnicas actuales sean reproducibles y evitar añadir funciones por intuición comercial.

**Próxima revisión de este estudio:** después de al menos 15 entrevistas reales y un benchmark documentado, o si cambia legislación/competencia de forma material. Versionar cambios con fecha y no reemplazar las conclusiones actuales silenciosamente.

---

## 16. Referencias y trazabilidad de fuentes

**Convención:** se indica origen, año/fecha, naturaleza y URL directa. Acceso de investigación: **31 de octubre de 2026**. Las fuentes corporativas son evidencia de sus anuncios, **no auditoría independiente** de resultados declarados. Precios y características de software pueden cambiar.

- **[R01] CEPAL/CENIA**, *ILIA 2026* (20/10/2026), comunicado metodológico con adopción por tamaño; **estimación econométrica regional**, no censo: https://www.cepal.org/es/comunicados/ilia-2026-america-latina-caribe-debe-apropiarse-la-inteligencia-artificial-generar-valor
- **[R02] CENIA**, *ILIA 2026* (20/10/2026), puntos Chile/Colombia/México y Chile 13,5 % empresarial; fuente del índice: https://cenia.cl/2026/10/20/ilia-2026-4ta-edicion-revela-que-america-latina-y-el-caribe-se-juegan-su-futuro-en-ia-en-la-colaboracion-regional-para-datos-talento-y-computo/
- **[R03] Stanford HAI**, *AI Index Report 2026 – Economy*; incorpora resultados McKinsey 2025, encuesta internacional de organizaciones: https://hai.stanford.edu/ai-index/2026-ai-index-report/economy
- **[R04] Banco Central de Chile**, *Informe de Percepciones de Negocios, noviembre 2025*, recuadro de adopción de tecnologías; encuesta de percepciones, no medición de LLM: https://www.bcentral.cl/documents/33528/7828837/Informe%2Bde%2BPercepciones%2Bde%2BNegocios%2BNoviembre%2B2025.pdf/ce21b9ab-4e51-4240-8657-32d1924cd3d6?t=1762375262763
- **[R05] INEGI**, *Censos Económicos 2024, resultados definitivos* (24/07/2025), **página 8**, datos de 2023 y denominador condicionado a uso de herramientas digitales: https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/ce/CE2024_def.pdf
- **[R06] Endeavor Colombia**, *Colombia AI Pulse* (25/08/2026), encuesta **n=493** recolectada en julio 2026, muestra participante no nacional representativa: https://colombia.endeavor.org/colombia-ai-pulse/
- **[R07] Buk**, *IA en el trabajo en Chile, encuesta de capacitación* (2026), encuesta a personas/organizaciones; no censo: https://www.buk.cl/blog/ia-trabajo-chile-aprendizaje-capacitacion
- **[R08] Biblioteca del Congreso Nacional de Chile**, Ley N.º 21.719, texto de vigencia diferida y fecha legal publicada: https://www.bcn.cl/leychile/Navegar/imprimir?idNorma=1209272
- **[R09] Senado de Chile**, noticia oficial sobre tramitación de postergación (20/10/2026); seguimiento del debate, no ley promulgada: https://www.senado.cl/comunicaciones/noticias/proteccion-de-datos-personales-avanza-proyecto-que-busca-postergar-entrada ; noticia sobre aprobación en Sala el 28/10: https://www.df.cl/senado-aprueba-modificaciones-al-proyecto-que-posterga-la-entrada-en
- **[R10] México, Tribunal Electoral/DOF**, Ley Federal de Protección de Datos Personales en Posesión de los Particulares (publicada 20/03/2025, reformas 14/11/2025): https://www.te.gob.mx/legislacion/media/files/3cc41f81a66fca1.htm
- **[R11] Superintendencia de Industria y Comercio (Colombia)**, Circular Externa 002 (21/08/2024), tratamiento de datos en IA: https://sedeelectronica.sic.gov.co/transparencia/normativa/circular-externa-2-de-2024-de-la-superintendencia-de-industria-y-comercio-lineamientos-sobre-el-tratamiento-de-datos
- **[R12] Banco de Chile**, anuncio de acuerdo con Microsoft e IA generativa (16/10/2025): https://sitiospublicos.bancochile.cl/nuestro-banco/es/sala-de-prensa/detalle/banco-de-chile-es-la-primera-empresa-privada-del-pais-en-sellar-alianza-estrategica-en-inteligencia-artificial-con-microsoft
- **[R13] Falabella / relación inversionistas**, noticia sobre inversión en tecnología/IA (03/09/2026), información de la propia empresa: https://investors.grupofalabella.com/blog/2026/09/03/cio-de-falabella-anticipa-que-inversion-tecnologica-seguira-subiendo-este-ano-crecio-60-y-ia-y-data-son-nuestras-apuestas-fuertes/
- **[R14] Buk**, estudio de tendencias de RR.HH. 2026, investigación cualitativa de IA y gestión de personas: https://www.buk.cl/recursos/estudios/estudio-tendencias-hr-2026
- **[R15] Cámara de Comercio de Santiago**, nota de socio comercial indigitall sobre agentes IA (12/08/2025); es **declaración comercial**, no auditoría: https://www.ccs.cl/2025/08/12/indigitall-lanza-sus-agentes-ia-con-integracion-total-a-whatsapp-y-plataformas-digitales/
- **[R16] BBVA México**, anuncio de Blue y atención generativa (13/08/2025), declaración corporativa: https://www.bbva.com/es/mx/innovacion/bbva-mexico-adopta-inteligencia-artificial-generativa-para-transformar-la-atencion-a-clientes-y-eliminar-la-marcacion-por-tonos-ivr/
- **[R17] Kueski**, anuncio de inversión en gestión de fraude/decisiones IA (26/02/2026), declaración corporativa: https://kueski.another.co/kueski-nombra-a-pablo-baragiola-ex-ejecutivo-de-robinhood-nubank-y-capital-one-como-vicepresidente-de-fraude
- **[R18] Konfío**, explicación corporativa de IA y tecnología financiera (27/09/2024), información de la propia empresa: https://konfio.mx/blog/soluciones-financieras/tarjeta-empresarial/tecnologia-financiera-al-servicio-de-las-pymes-la-evolucion-de-konfio/
- **[R19] Alegra México**, comunicado de agente contable IA (22/10/2026), anuncio de la empresa: https://prensa.alegra.com/llega-un-nuevo-agente-de-ia-para-transformar-la-gestion-contable-de-las-empresas-en-mexico
- **[R20] DANE**, *Indicadores básicos TIC empresas, información 2024* (actualizado 28/08/2026), marco sectorial manufacturero, no estimación nacional de comprador LLM: https://www.dane.gov.co/index.php/estadisticas-por-tema/tecnologia-e-innovacion/tecnologias-de-la-informacion-y-las-comunicaciones-tic/indicadores-basicos-de-tic-en-empresas
- **[R21] Departamento Nacional de Planeación, Colombia**, política nacional IA CONPES 4144 (14/02/2025), política pública: https://www.dnp.gov.co/publicaciones/Planeacion/Paginas/conpes-4144-hoja-de-ruta-colombia-inteligencia-artificial-retos-actuales-transformacion-futura.aspx
- **[R22] Siigo Colombia**, portal oficial y documentación MCP de integración con asistentes externos, fuente del proveedor: https://developers.siigo.com/docs/siigoapi/MCP/1-documentation/ ; descripción corporativa: https://www.siigo.com/p_nosotros/
- **[R23] Suramericana**, informe anual 2025 y transformación digital, fuente de la empresa: https://suramericana.com/nosotros/relacion-con-inversionistas/informe-anual-2025/
- **[R24] Alegra Colombia**, actividad Colombia Tech Week sobre contabilidad/IA (11/08/2026), comunicado corporativo: https://prensa.alegra.com/de-registro-financiero-a-inteligencia-de-negocio-alegra-conectara-la-contabilidad-con-la-ia-en-colombia-tech-week
- **[R25] Konfío**, caso de empresa mexicana Sinergy Solutions que desarrolla soluciones IA (octubre 2026), testimonio publicado por tercero comercial: https://konfio.mx/blog/historias-konfio-sinergy/
- **[R26] Cloudflare**, documentación oficial de DLP para AI Gateway (25/09/2026): https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/
- **[R27] Cloudflare**, página oficial de precios AI Gateway (última revisión visible 15/10/2026): https://developers.cloudflare.com/ai-gateway/reference/pricing/
- **[R28] LiteLLM**, precios/licencia y capacidades de su gateway; documentación comercial del proveedor: https://www.litellm.ai/pricing
- **[R29] Portkey**, página oficial de planes y precios (consulta 31/10/2026); condiciones sujetas a cambios: https://portkey.ai/pricing
- **[R30] Microsoft Learn**, capacidades Azure AI Gateway/API Management; algunas funcionalidades están en preview: https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview
- **[R31] Microsoft Learn**, Microsoft Purview y controles de datos para aplicaciones IA: https://learn.microsoft.com/en-us/purview/data-security-posture-management-setup

### Historial documental

- **31/10/2026, v1.0:** análisis conjunto Chile/México/Colombia, fuentes y sesgos, 12 cuentas observables, competencia con precios verificados, B2B/B2C y protocolo de validación primaria.
- Complementa, **no reemplaza**, el documento existente [DELIA: viabilidad de mercado y regulatoria de Chile y Colombia](DELIA_viabilidad_mercado_regulatoria.md). Cuando existan diferencias de fecha, estado legal o precio, prevalece la fuente primaria actualizada y debe registrarse una revisión explícita.
