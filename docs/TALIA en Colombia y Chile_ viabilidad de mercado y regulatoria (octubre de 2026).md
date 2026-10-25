# TALIA en Colombia y Chile: viabilidad de mercado y regulatoria (octubre de 2026)

Hay demanda real y un hueco competitivo, pero es estrecho. Mi recomendación es **avanzar en Chile como primer mercado** y **avanzar en Colombia cambiando el argumento de venta**. En Colombia el mensaje no debe ser "legalizar la transferencia", sino "minimización, responsabilidad demostrada y cumplimiento de la nube de la SFC". El cliente inicial no debe ser un banco grande. Debe ser una fintech o aseguradora mediana, o un integrador de software que ya construye agentes de IA para el sector financiero.

## TL;DR
- **Chile: avanzar.** La Ley 21.719 sigue fijada para el 1 de diciembre de 2026. Un proyecto que la aplaza a diciembre de 2027 fue aprobado en general el 19 de octubre de 2026 en la Comisión de Constitución del Senado, pero todavía no es ley. La Agencia no tiene consejo y, por tanto, no hay lista de países adecuados ni cláusulas tipo. Eso hace atractivo enmascarar antes de enviar datos a un modelo en el extranjero.
- **Colombia: avanzar con otro argumento.** La SIC considera a EE. UU. país con nivel adecuado de protección desde 2017, así que enviar datos a OpenAI o Anthropic no es ilegal de por sí. El valor de TALIA está en tres frentes: los principios de la Circular 002 de 2024 de la SIC sobre IA (necesidad, proporcionalidad, estudio de impacto de privacidad, responsabilidad demostrada), las reglas de nube de la SFC y una SIC que sí sanciona (cierre definitivo de Worldcoin, confirmado en junio de 2026).
- **El hueco competitivo existe, pero se puede copiar.** Bedrock, Azure, Cloudflare, Portkey y LiteLLM/Presidio ya enmascaran datos personales genéricos y de forma barata. Bedrock cobra USD 0,10 por cada 1.000 unidades de texto. No encontré soporte nativo para cédula, NIT o RUT chileno, salvo una entidad de cédula chilena en Azure. Tampoco encontré un actor latinoamericano de este tipo. La ventaja defendible está en el paquete de cumplimiento local, la exactitud en español, la auditoría ya redactada y el canal, no en la detección en sí.

## Resumen ejecutivo (máx. 10 líneas)
1. **Chile, avanzar:** la ventana regulatoria (Ley 21.719 + reglas de nube de la CMF) es la más fuerte de los dos países, y la fecha de entrada en vigor sigue en disputa.
2. **Colombia, avanzar con otro argumento:** hay menos presión legal sobre la transferencia, pero la SIC exige gobernanza de IA y fiscaliza; la SFC exige requisitos estrictos de nube.
3. Adopción de IA en empresas: 45% en Chile\[1\] y 42% en Colombia según los estudios de AWS/Strand de 2026.\[2\] El paso a agentes autónomos está empezando.
4. El riesgo principal es comercial, no regulatorio: la nube que el cliente ya usa ofrece enmascaramiento básico casi gratis.
5. El primer cliente debe ser una entidad regulada mediana, con agentes ya en producción y un DPO o CISO con presupuesto propio.
6. Antes de escribir más código, valida con 20–30 entrevistas que alguien pague más de USD 1.500 al mes por el paquete local.

## Hallazgos clave

### Hechos verificados que más pesan en la decisión
- **Chile, Ley 21.719:** publicada en el Diario Oficial el 13 de diciembre de 2024. Su artículo primero transitorio fija la entrada en vigor el 1 de diciembre de 2026 (guía de Figueroa & Streit, consultada en octubre de 2026).\[3\]
  - El Ejecutivo ingresó el Boletín 18.623-07 el 1 de septiembre de 2026, con suma urgencia. Propone aplazar la vigencia al 1 de diciembre de 2027 y subir el consejo de la Agencia de tres a cinco miembros (Carey Abogados, septiembre de 2026).\[4\]
  - El 19 de octubre de 2026 la Comisión de Constitución lo aprobó en general por 5 votos a 0. Se discutieron dos variantes: aplazar toda la ley, o aplazar solo las facultades de fiscalización y sanción de la Agencia y dejar que esta empiece a funcionar de inmediato (Jara del Favero, octubre de 2026).\[5\]
  - Al 21 de octubre de 2026 no había votación en Sala (The Next Security, 21 de octubre de 2026). **La fecha legal hoy es el 1 de diciembre de 2026.**\[6\]
- **Chile, sanciones:** infracciones leves, hasta 5.000 UTM; graves, hasta 10.000 UTM; gravísimas, hasta 20.000 UTM. En reincidencia, las empresas que no son de menor tamaño enfrentan el triple de la multa, o el 2% (graves) o el 4% (gravísimas) de sus ingresos anuales (GlobalSuite Solutions, 2026, sobre el texto en BCN).\[7\]\[8\]
- **Chile, Agencia sin consejo:** el Senado rechazó la primera propuesta de consejeros el 19 de mayo de 2026 (LexAlert, septiembre de 2026). Sin consejo no hay lista de países adecuados, cláusulas modelo ni instrucciones generales (GlobalSuite Solutions, 2026).\[4\]\[7\]
- **Colombia, transferencia internacional:** el artículo 26 de la Ley 1581 de 2012 prohíbe transferir datos a países sin nivel adecuado de protección. La Circular Externa 005 del 10 de agosto de 2017 de la SIC incluye a Estados Unidos en la lista de países adecuados (Holland & Knight, agosto de 2017; normograma DIAN).\[9\]\[10\]
- **Colombia, IA:** la Circular Externa 002 del 21 de agosto de 2024 de la SIC pide aplicar a la IA los criterios de idoneidad, necesidad, razonabilidad y proporcionalidad. También exige un estudio de impacto de privacidad, documentado antes de diseñar y desarrollar sistemas de alto riesgo (Cuatrecasas, noviembre de 2024).\[11\] Ante la duda sobre posibles daños, el responsable debe abstenerse o adoptar medidas preventivas (CERLatam).\[12\]
- **Colombia, la SIC sanciona:** la Resolución 78798 del 3 de octubre de 2025 ordenó el cierre definitivo de las operaciones de tratamiento de datos de World Foundation y Tools for Humanity (Worldcoin). La Resolución 45710 del 18 de junio de 2026 la confirmó y reafirmó que la SIC es competente sobre empresas extranjeras sin domicilio en Colombia (comunicado de la SIC; Mobile Time, 7 de julio de 2026).\[13\]\[14\]
- **SFC:** en 2025 el 81% de los establecimientos de crédito ya usaba IA en sus procesos (comunicado de la SFC, 5 de marzo de 2026).\[15\]

## Detalle por eje

### 1. Marco regulatorio

**Colombia**
- **Ley 1581 de 2012 y Decreto 1377 de 2013:** las normas son tecnológicamente neutrales y aplican a todo tratamiento de datos para desarrollar, probar o usar sistemas de IA (texto de la CE 002 de 2024 de la SIC).\[16\]
  - Enviar datos a EE. UU. está permitido por la lista de la CE 005 de 2017. Aun así, el responsable debe poder demostrar que trata bien los datos que transfiere (CPDP LatAm, julio de 2023, citando las circulares 5 y 8 de 2017 de la SIC).\[17\]
  - Cuando el proveedor del modelo actúa como encargado, la operación es una "transmisión": el art. 3.5 del Decreto 1377 de 2013 la define como la comunicación de datos "cuando tenga por objeto la realización de un Tratamiento por el Encargado por cuenta del Responsable", y su art. 24 dispone que las transmisiones internacionales "no requerirán ser informadas al Titular ni contar con su consentimiento cuando exista un contrato en los términos del artículo 25" (Gestor Normativo de Función Pública, Decreto 1377 de 2013).
- **SIC sobre IA:** CE 002 de 2024 (principios, estudio de impacto, responsabilidad demostrada, medidas de seguridad).\[18\]
  - La SIC emitió además la CE 001 del 18 de septiembre de 2025 para fintech que tratan datos en productos de financiación y depósitos de bajo monto (sede electrónica de la SIC).\[19\]
- **SFC (sector financiero):** la Circular Externa 005 de 2019 (11 de marzo de 2019) regula la computación en la nube (texto del anexo consultado por el subagente; copia de Globbal, abril de 2019).\[20\] Exige:
  - avisar a la SFC dentro de los 15 días anteriores al inicio del procesamiento, indicando proveedor, subcontratistas, tipos de datos y "la ubicación física o región donde se procesarán y almacenarán los datos";\[21\]
  - verificar que el proveedor tenga "al menos, la certificación ISO 27001" y disponga de informes SOC1, SOC2 o SOC3;\[21\]
  - que las jurisdicciones de procesamiento tengan normas de protección de datos "equivalentes o superiores";\[21\]
  - cifrado en tránsito y en reposo;\[21\]
  - que el contrato diga que los datos "no se pueden usar para ningún propósito diferente al establecido en el contrato".\[21\]
  - La CE 006 de 2025 (25 de junio de 2025) reexpidió toda la Circular Básica Jurídica.\[22\] El subagente no pudo confirmar que el texto de nube se mantuviera palabra por palabra.
- **SFC sobre IA:** no encontré una circular específica de la SFC sobre IA generativa.
  - En 2025 la SFC publicó documentos como "Caracterización de la IA para la gestión del riesgo de crédito" (listado de publicaciones de 2025).\[23\] No revisé su contenido.
- **Ley de IA:** no hay ley aprobada.
  - El proyecto unificado de MinCiencias (PL 043/2025 Senado – 324/2025 Cámara) se archivó el 19 de junio de 2026 sin debate (Contexto, 1 de octubre de 2026).\[24\]
  - En julio y agosto de 2026 se radicaron nuevos proyectos (PL 025 de 2026, PL 065/2026 Senado y otros; Cámara de Representantes y Observatorio Uniandes, agosto de 2026).\[25\]\[26\]
  - El CONPES 4144 de febrero de 2025 es política pública, no una norma obligatoria (Mentora Colombia, 2026).\[27\]

**Chile**
- **Ley 19.628 (vigente hasta que rija la 21.719):** multas de 1 a 10 UTM, o de 10 a 50 UTM si se trata de datos financieros o bancarios, impuestas por un juez civil, y sin autoridad de control propia (Carey Abogados).
- **Ley 21.719:** sanciones y estado descritos arriba.
  - **Transferencia internacional:** es lícita hacia países que la Agencia declare adecuados, o con garantías como cláusulas contractuales tipo, normas corporativas vinculantes o certificaciones. Quien transfiere carga con la prueba (GlobalSuite Solutions; Idónea, 2026).\[7\]\[8\]
  - El reglamento de modelos de prevención de infracciones (D.S. 662) se publicó el 9 de septiembre de 2026 (LexAlert).\[4\]
- **CMF:** el capítulo 20-7 de la Recopilación Actualizada de Normas (RAN), sobre externalización de servicios, rige el uso de proveedores en el extranjero y en la nube (texto de 2017 con reforma de 2019, revisado por el subagente).\[28\] Exige:
  - conocer la jurisdicción y "la ciudad donde operan los centros de datos";\[29\]
  - acceso permanente de la CMF a los datos del proveedor, en el país o en el exterior;\[29\]
  - datos cifrados "manteniéndose las llaves de desencriptación en poder de la entidad";\[29\]
  - para servicios críticos en la nube, "certificaciones independientes, reconocidas internacionalmente" (sin nombrar ISO 27001 ni SOC 2);\[29\]
  - autorización previa de cada cliente cuando se transmiten datos protegidos por secreto bancario fuera del país.\[29\]
  - En abril–mayo de 2026 la CMF sometió a consulta una reescritura completa del capítulo 20-7, con enfoque de riesgo de terceros. La publicación definitiva sigue pendiente (página de normativa en trámite de la CMF).\[30\]\[31\]
  - La presidenta de la CMF, Catherine Tornel, advirtió que la IA "podría reconfigurar el mapa de riesgos" (Diario Financiero, 29 de abril de 2026).\[32\]
  - La NCG 538 exige autenticación reforzada desde el 1 de agosto de 2026 (NetProvider, 2026).\[33\]
- **Proyecto de ley de IA (Boletín 16.821-19):** la Cámara lo aprobó el 13 de octubre de 2025. Está en segundo trámite en la Comisión de Desafíos del Futuro del Senado; el Ejecutivo renovó la urgencia simple el 1 de septiembre de 2026 (IA Experta, 28 de septiembre de 2026; Parlamento.ai).\[34\]
  - Propone cuatro niveles de riesgo. Los sistemas de alto riesgo tendrían que gestionar riesgos, mantener registros (logging) y supervisión humana (Regulations.ai, 2026).\[35\] No está vigente.

**Qué dicen sobre enviar datos a modelos en el extranjero y sobre trazabilidad**
- **Colombia:** a EE. UU. está permitido. La SIC exige principios, estudio de impacto y "estrategias demostrables", lo que equivale a trazabilidad. En banca, la SFC exige además declarar la región de procesamiento y limitar el uso de los datos a lo que dice el contrato.
- **Chile:** hoy, con la Ley 19.628, no hay reglas específicas. Con la Ley 21.719 hará falta un país adecuado o garantías,\[36\] y aún no existen listas ni cláusulas tipo. En banca, la RAN 20-7 pide conocer la jurisdicción, garantizar acceso de auditoría y obtener autorización del cliente para datos bajo secreto bancario.
- *Inferencia:* el enmascaramiento reversible hace que el proveedor del modelo no reciba datos personales identificables. Eso reduce, aunque no siempre elimina, la exposición en ambos regímenes. Que los datos seudonimizados sigan siendo "datos personales" es una pregunta abierta en ambos países.

### 2. Demanda

**Adopción de IA**
- **Chile:**
  - 45% de las empresas usa IA (35% el año anterior). El 58% de ellas solo con herramientas básicas, y solo el 18% se siente preparado para la IA agéntica (Strand Partners para AWS; Pauta, 25 de septiembre de 2026).\[37\]
  - SONDA reporta 88% de uso, pero el 53% de las empresas tiene solo lineamientos generales sobre IA (ANDA, 21 de agosto de 2026).\[38\]
  - Más del 80% de las grandes empresas usa IA (Entel Digital y CENIA).\[39\]\[40\]
- **Colombia:**
  - 42% de las empresas usa IA, frente a 34% el año anterior (AWS/Strand, agosto de 2026, citado por Ofima).\[2\]
  - Solo el 18% la incorpora formalmente en su cadena de valor (Cintel, en Bloomberg Línea, 2026).\[2\]\[41\]
  - Endeavor (25 de agosto de 2026, 493 empresas) da a Colombia 45,6/100 en sofisticación, y 1 de cada 2 empresas señala la ciberseguridad como barrera.\[42\]\[43\]
  - En el sector de software, el 66,3% tiene IA en producción, el 81% prioriza los agentes y Claude lidera en programación con 60,6% (Fedesoft y Cenisoft, en El Colombiano, 2026).\[44\]

**Sectores más expuestos (inferencia a partir de la regulación y de los datos que manejan)**
- Banca y fintech: SFC/CMF, secreto bancario.
- Seguros y salud: datos sensibles.
- Contact centers y BPO: alto volumen de datos personales.
- Telecomunicaciones.
- Legal: secreto profesional.
- Retail con brazo financiero.
- Gobierno: compra lenta, no es buen primer cliente.

**Preocupación por fugas de datos:** la barrera de ciberseguridad aparece en Endeavor, y la falta de gobernanza en SONDA.\[43\] No encontré encuestas locales específicas sobre fugas de datos hacia modelos de lenguaje; es una hipótesis por validar.

**Incidentes y sanciones:** el caso más relevante es Worldcoin en Colombia (biometría, IA). No encontré sanciones públicas en Chile ni en Colombia por fugas de datos hacia modelos de lenguaje.

### 3. Competencia

| Solución | Qué hace | Precio público | Identificadores locales / español |
|---|---|---|---|
| Amazon Bedrock Guardrails | Filtro de datos personales en entrada y salida (bloquear o anonimizar); aplicable a modelos externos vía ApplyGuardrail | USD 0,10 por 1.000 unidades de texto; filtros por expresión regular gratis (página de precios de AWS, 2026) | Sin RUT, cédula ni NIT nativos; hay que crear expresiones regulares propias. Según Beri.net (13 de octubre de 2026), el registro de invocaciones guarda la petición original sin redactar y no enmascara los datos dentro de las llamadas a herramientas\[45\]\[46\]\[47\] |
| Azure AI Language PII | Detección y redacción de datos personales y de salud | De USD 1,00 por 1.000 registros, bajando por volumen (Beri.net, octubre de 2026) | Incluye la cédula chilena (CLIdentityCardNumber) y el DNI argentino (documentación de Microsoft, junio de 2026). No vi una entidad para Colombia. Su nota de transparencia dice que las entidades internacionales solo funcionan sobre texto en inglés\[47\]\[48\]\[49\] |
| Microsoft Presidio (código abierto) | Motor de detección extensible; integrado en LiteLLM | Gratis | Trae reconocedores para España, Italia y otros países, pero no para Chile ni Colombia (documentación de Presidio, 2026). Se pueden añadir\[50\]\[51\] |
| Cloudflare AI Gateway / AI Security for Apps | DLP sobre prompts y respuestas; detección de datos personales e inyección de prompts | DLP del Gateway gratis, con perfiles predefinidos; la detección de IA del WAF es un complemento Enterprise de pago (documentación de Cloudflare, septiembre de 2026) | Perfiles genéricos; no verifiqué identificadores latinoamericanos\[52\]\[53\] |
| Portkey (ahora Prisma AIRS, de Palo Alto Networks) | Gateway con más de 50 guardrails y redacción de datos personales | Gratis hasta 10.000 registros; USD 49 al mes en Production; Enterprise a medida, con SOC 2 e ISO 27001 (documentación de Portkey, 2026) | No verificado\[54\]\[55\]\[56\] |
| LiteLLM | Proxy de código abierto con integración de Presidio | Código abierto gratis; Enterprise a cotizar | Depende de Presidio\[57\] |
| Protecto | Enmascaramiento reversible que conserva el sentido del texto | Desde USD 250 al mes por 5.000 llamadas (Enigma Vault, 2026) | No verificado\[58\]\[59\] |
| Limina (antes Private AI) | Más de 50 tipos de entidad en 52 idiomas, en contenedor | Plan gratuito con límite; Enterprise a cotizar | Español sí; identificadores locales no verificados\[58\]\[59\] |
| Nightfall | DLP con gateway de IA/MCP | Por usuario al año, a cotizar | No verificado\[60\] |
| Lakera | Seguridad de prompts | No verifiqué precio ni funciones en esta investigación | — |

**Actores locales:** ni yo ni el subagente encontramos una startup latinoamericana que ofrezca un gateway de enmascaramiento para modelos de lenguaje. Lo más cercano fue avantGate (código abierto, origen sin confirmar) y privacy-gateway-es (España).\[61\]\[62\] Esto es "no encontrado", no "no existe".

**Hueco competitivo (inferencia):**
1. **Identificadores locales con validación de dígito verificador:** RUT/RUN (módulo 11), cédula y NIT colombianos (con DV), además de cuentas, placas y números de póliza locales.
2. **Detección de entidades en español latinoamericano:** nombres compuestos y direcciones colombianas como "Cra 7 # 72-41".
3. **Restitución de los valores reales en flujos de agentes:** dentro de llamadas a herramientas y argumentos, justo donde Bedrock declara límites.\[47\]
4. **Auditoría ya redactada:** los registros de Bedrock guardan el original.\[47\]
5. **Paquete de cumplimiento local:** plantillas de estudio de impacto para la SIC, documentación para el aviso de nube a la SFC y evidencia para la RAN 20-7 de la CMF.
6. **Facturación en COP/CLP, soporte en español y despliegue en nube local o en el entorno del cliente:** Amazon anunció el 7 de mayo de 2025 una inversión de más de USD 4.000 millones para lanzar la región AWS South America (Chile) "by the end of 2026", con tres zonas de disponibilidad; desde 2023 existe una Local Zone en Santiago que depende de US East (N. Virginia) (comunicado de prensa de Amazon, 7 de mayo de 2025).

**Riesgo:** los puntos 1 y 2 se replican con unas cuantas expresiones regulares. Lo defendible son los puntos 3 a 6.

### 4. Cliente y compra
- **Quién decide (inferencia):**
  - En entidades reguladas, quien patrocina la compra suele ser el CISO o el DPO.
  - El área de innovación o el equipo de IA es quien siente el dolor: proyectos bloqueados por cumplimiento.
  - Legal da el visto bueno y compras gestiona el registro del proveedor.
  - En fintech y empresas de software decide el CTO.
- **Cómo compran (inferencia):**
  - Banca y seguros: registro como proveedor, evaluación de seguridad (cuestionarios, ISO 27001/SOC 2, cláusulas de la CE 005 de la SFC o de la RAN 20-7 de la CMF) y pilotos de 60–90 días. Muchas veces compran a través de integradores (en Chile, SONDA y Entel Digital publican estudios de IA y venden a la gran empresa).
  - Gobierno: licitación, no recomendable para empezar.
- **Disposición a pagar (estimación):**
  - Referencia de mercado: el enmascaramiento genérico en la nube cuesta centavos por millón de caracteres, Portkey parte en USD 49 al mes y Protecto en USD 250 al mes.\[47\]\[55\]\[63\]
  - Un paquete con valor de cumplimiento local podría sostener unos USD 1.500–5.000 al mes en empresas medianas y USD 40.000–120.000 al año en grandes cuentas reguladas, con despliegue en el entorno del cliente.
  - *Estimación sin validar.* Modelo sugerido: tarifa de plataforma más tramos por volumen de peticiones. El precio por usuario no encaja con agentes autónomos.

### 5. Riesgos
- **Certificaciones:** la SFC exige al menos ISO 27001 al proveedor de nube y disponibilidad de informes SOC.\[21\] La CMF exige certificaciones internacionales para servicios críticos.\[29\] *Inferencia:* para vender a banca, TALIA necesitará como mínimo SOC 2 Tipo I o ISO 27001 en 12–18 meses, o desplegarse dentro del entorno del cliente para heredar sus controles.
- **Residencia de datos:** ninguno de los dos países exige localización general. Chile exige conocer la ciudad del centro de datos y, para banca, un sitio de contingencia en Chile que el directorio puede dispensar desde 2019.\[29\]\[64\]
- **TALIA como encargado del tratamiento:** TALIA ve los datos en claro y guarda el mapa entre tokens y valores reales. Por eso es encargado del tratamiento en ambos países y queda sujeto a deberes de seguridad, confidencialidad y notificación.
  - En Chile, la Ley 21.719 extiende obligaciones a los encargados y obliga a reportar brechas a la Agencia "por los medios más expeditos posibles y sin dilaciones indebidas" (art. 14 sexies), sin fijar un plazo numérico como las 72 horas del RGPD (guía de Prey Project).
  - Una fuga en TALIA concentraría el riesgo de todos sus clientes.
  - *Recomendación:* bóveda de tokens en el entorno del cliente, sin conservar valores en claro en el servicio gestionado, y contrato de encargo estándar.
- **Riesgo regulatorio a la baja:** si Chile aplaza la ley a 2027, la urgencia de compra cae. Mitigación: vender por seguridad de agentes y por la RAN 20-7 de la CMF, no solo por la Ley 21.719.
- **Riesgo de que lo absorba la plataforma:** Bedrock, Azure o Cloudflare podrían añadir identificadores latinoamericanos en cualquier momento.

## Tabla comparativa Colombia vs Chile

| Dimensión | Colombia | Chile |
|---|---|---|
| Regulación de datos | Ley 1581/2012 vigente; SIC activa y sancionadora | Ley 19.628 vigente; Ley 21.719 desde el 1-dic-2026, con aplazamiento a 2027 en trámite |
| Transferencia al extranjero | EE. UU. es país adecuado (CE 005/2017) | Con la Ley 21.719: país adecuado o garantías; aún no hay listas ni cláusulas |
| Guía sobre IA | SIC CE 002/2024 (estudio de impacto, proporcionalidad, responsabilidad demostrada) | Sin guía de autoridad de datos; proyecto de ley de IA en el Senado |
| Sector financiero | SFC CE 005/2019 (aviso 15 días antes, ISO 27001, SOC, región de datos) | CMF RAN 20-7 (jurisdicción y ciudad, auditoría, llaves de cifrado, secreto bancario); reforma en consulta |
| Sanciones | Ley 1581: multas, suspensión y cierre (caso Worldcoin) | Hasta 20.000 UTM; 2–4% de ingresos en reincidencia |
| Demanda (adopción de IA) | 42% de empresas (AWS); 18% formal (Cintel) | 45% de empresas (AWS); más del 80% de grandes empresas (Entel/CENIA)\[2\]\[40\] |
| Competencia | Global, sin actor local identificado | Global, sin actor local; Azure reconoce la cédula chilena\[48\] |
| Barreras | Menor urgencia legal en la transferencia; compras lentas en banca | Fecha de vigencia incierta; mercado más pequeño |
| Recomendación | Avanzar con otro argumento (gobernanza IA + nube SFC) | Avanzar (primer mercado) |

## 5 primeros clientes objetivo por país

*Los nombres concretos son ejemplos de cada perfil, elegidos por inferencia. No encontré evidencia pública de que estas empresas usen IA generativa con datos personales ni de que tengan presupuesto asignado.*

**Chile**
1. **Fintech con licencia de la CMF (p. ej., Tenpo, Fintual o Mach):** sujetas a la CMF y a la Ley 21.719, con equipos técnicos que ya construyen agentes. Ciclo de compra corto.
2. **Aseguradoras y salud previsional (isapres, clínicas privadas):** datos sensibles de salud, que son la categoría más protegida por la Ley 21.719.
3. **Retail con brazo financiero (p. ej., Falabella o Cencosud):** grandes volúmenes de datos de clientes, atención con IA y regulación CMF en su parte financiera.
4. **Integradores (SONDA, Entel Digital):** canal hacia la gran empresa; ya publican estudios de adopción de IA.
5. **Contact centers y BPO que atienden a banca:** procesan datos de terceros como encargados y tienen que demostrar controles a sus clientes.

**Colombia**
1. **Fintech vigiladas por la SIC según la CE 001/2025 (crédito digital, pagos):** marco específico de la SIC\[65\] y presión por automatizar con IA.
2. **Fábricas de software y BPO que construyen agentes para banca (socios de Fedesoft):** 66,3% ya tiene IA en producción y 81% prioriza los agentes.\[44\] TALIA sirve como componente de cumplimiento que entregan a sus clientes.
3. **Aseguradoras y salud (p. ej., grupos Sura o Bolívar):** datos sensibles, y en seguros reglas de nube de la SFC.
4. **Bancos medianos o digitales vigilados por la SFC:** el 81% de los establecimientos de crédito ya usa IA; necesitan evidencia de cumplimiento de nube y de la SIC.
5. **Firmas de abogados y legaltech grandes:** secreto profesional y documentos con cédula y NIT; compra rápida por socios.

## Hipótesis sin validar y cómo validarlas

| Hipótesis | Cómo validarla | Preguntas concretas |
|---|---|---|
| H1: Los equipos de IA tienen proyectos frenados por cumplimiento | 10 entrevistas a líderes de IA o innovación por país | "¿Qué proyecto con modelos externos frenó legal o seguridad en los últimos 6 meses? ¿Por qué?" |
| H2: El CISO o DPO pagaría más de USD 1.500 al mes por el paquete local frente a Bedrock o Azure | 8 entrevistas a CISO/DPO; prueba de precio con tres niveles | "¿Ya usan los guardrails de su nube? ¿Qué les falta? ¿Cuánto pagaron por su DLP?" |
| H3: Los datos seudonimizados reducen la carga de transferencia ante la SIC, la Agencia chilena, la SFC y la CMF | 2–3 opiniones de abogados por país; consulta informal al regulador | "¿Un token reversible cuyo mapa queda en Chile o Colombia constituye transferencia de datos personales?" |
| H4: La RAN 20-7 hace que los bancos chilenos necesiten autorización del cliente para mandar datos bajo secreto bancario a un modelo | Revisión del capítulo vigente y de la versión en consulta, más entrevista con cumplimiento de 2 bancos | "¿Cómo están resolviendo la autorización del cliente para usar modelos en el extranjero?" |
| H5: Los integradores revenderían TALIA | 5 entrevistas con integradores | "¿Qué margen esperan? ¿Prefieren marca blanca?" |
| H6: Exigirán SOC 2 o ISO 27001 desde el primer piloto | Revisar cuestionarios de proveedores de 3 entidades | "¿Qué piden para un piloto, y qué para producción?" |
| H7: La exactitud en español e identificadores locales es mejor que la de Presidio, Azure o Bedrock | Prueba comparativa con 1.000 documentos sintéticos colombianos y chilenos | Medir recall y precisión por entidad (RUT, cédula, NIT, direcciones, nombres) |
| H8: Si la Ley 21.719 se aplaza, la demanda en Chile se mantiene | Seguir el Boletín 18.623-07 y repetir las entrevistas después de la votación | "Si la ley se aplaza a 2027, ¿cambia su prioridad presupuestaria?" |

## Advertencias
- Varios datos de Chile sobre la Ley 21.719 vienen de despachos y consultoras que citan BCN y el Senado. No leí directamente la ficha oficial del Senado.
- Los textos de la RAN 20-7 son la versión de 2017 con la reforma de 2019 resumida. Falta confirmar el texto consolidado vigente y si la CMF ya publicó la reforma de 2026.
- No pude verificar si el texto de nube de la CE 005/2019 de la SFC se mantuvo palabra por palabra en la CE 006/2025.
- Las cifras de adopción vienen de estudios patrocinados por proveedores (AWS, SONDA, Entel) y miden cosas distintas; no son comparables entre sí.
- No encontré datos sobre Lakera ni encuestas locales específicas sobre fugas de datos hacia modelos de lenguaje.

## Fuentes

1. [Según AWS: Cada Tres Minutos Una Empresa Chilena Adopta IA](https://www.zoomtecnologico.com/2026/09/29/estudio-aws-empresa-chilena-ia/)
2. [IA En Empresa Mediana Colombiana 2026: Dónde Aplicarla Y Dónde No](https://www.ofima.com/blog/ia-empresa-mediana-colombiana-donde-implementarla/)
3. [Ley N°21.719 de datos personales: ¿qué debe tener resuelto su empresa antes del 1 de diciembre de 2026? - Figueroa & Streit Abogados](https://fys.legal/ley-21719-proteccion-datos-personales-empresas/)
4. [Ley 21.719 de datos personales: guía para empresas](https://www.lexalert.cl/recursos/ley-21719-datos-personales)
5. [Comisión de Constitución aprueba en general la postergación de la entrada en vigencia de la Ley N°21.719 sobre Protección de Datos Personales - JDF Jara del Favero](https://jdf.cl/en/comision-de-constitucion-aprueba-en-general-la-postergacion-de-la-entrada-en-vigencia-de-la-ley-n21-719-sobre-proteccion-de-datos-personales/)
6. [Ley 21.719: la Comisión de Constitución aprobó en general el proyecto que propone postergarla a 2027](https://www.thenextsecurity.cl/insights/ley-21719-comision-senado-propone-postergar-2027/)
7. [Ley 21.719 Chile: resumen, vigencia y multas](https://www.globalsuitesolutions.com/es/claves-ley-organica-proteccion-de-datos-personales-chile/)
8. [Ley 21.719: reforma de protección de datos en Chile](https://idonea.cl/ley-proteccion-datos-personales-chile-guia/)
9. [Cambios en la transferencia de datos personales a otros países](https://www.hklaw.com/en/insights/publications/2017/08/cambios-en-la-transferencia-de-datos-personales-a)
10. [Jurinfo - Circular 5 de 2017 SIC](https://jurinfo.jep.gov.co/normograma/compilacion/docs/circular_superindustria_0005_2017.htm)
11. [Guía para el uso responsable de IA y datos personales en Colombia](https://www.cuatrecasas.com/es/spain/tecnologia-medios-digitales/art/guia-uso-responsable-ia-datos-personales-colombia)
12. [SIC, Circular Externa 002 de 2024 - Centro de Estudios Regulatorios](https://www.cerlatam.com/normatividad/sic-circular-externa-002-de-2024/)
13. [Colombia ratifica cierre definitivo de las operaciones de Worldcoin Foundation](https://mobiletime.la/noticias/07/07/2026/cierre-worldcoin-foundation/)
14. [La SIC confirma la sanción de cierre inmediato y definitivo de la operación de tratamiento de datos sensibles adelantada por World Foundation y Tools for Humanity Corporation en territorio colombiano](https://sedeelectronica.sic.gov.co/comunicado/la-sic-confirma-la-sancion-de-cierre-inmediato-y-definitivo-de-la-operacion-de-tratamiento-de-datos-sensibles-adelantada-por-world)
15. [Sistema financiero acelera implementación de canales digitales](https://www.superfinanciera.gov.co/publicaciones/10116043/sistema-financiero-acelera-implementacion-de-canales-digitales/)
16. [Circular Externa 002 de 2024 de la SIC](https://tramites.cc/normatividad-de-colombia/circular-externa-002-de-2024-de-la-sic/)
17. [07.2023 H Luca Belli, Ana Brian Nougrères, Jonathan Mendoza Iserte,](https://cpdp.lat/wp-content/uploads/2023/07/doc-discusion-cpdplatam23-2.3.pdf)
18. [Circular 002 de 2024 de la SIC: Conoce las nuevas Directrices para el Tratamiento de Datos en Inteligencia Artificial - MS LEGAL - Protección de Datos Personales y Derecho comercial y corporativo](https://mslegal.com.co/circular-002-de-2024-de-la-sic-conoce-las-nuevas-directrices-para-el-tratamiento-de-datos-en-inteligencia-artificial/)
19. [Circular Externa 001 del 18 de septiembre de 2025](https://sedeelectronica.sic.gov.co/transparencia/normativa/circular-externa-001-del-18-de-septiembre-de-2025)
20. [Circular 005, uso de servicios de computación en la nube](https://www.icef.com.co/component/k2/item/3818-circular-005-uso-de-servicios-de-computacion-en-la-nube)
21. <https://globbal.co/wp-content/uploads/2019/04/45-Circ-Ext-SUPERFINANCIERA-00005-2019-Computaci%C3%B3n-en-la-nube-ANEXO.pdf>
22. [Compilación Jurídica SuperSalud - Circular 6 de 2025 SF](https://normograma.supersalud.gov.co/compilacion/docs/circular_superfinanciera_0006_2025.htm)
23. [Circulares Externas 2025](https://www.superfinanciera.gov.co/publicaciones/10115459/circulares-externas-2025/)
24. [¿Pagará Colombia el precio de no tener una Ley para la Inteligencia Artificial? - Contexto](https://contextomedia.com/pagara-colombia-el-precio-de-no-tener-una-ley-para-la-inteligencia-artificial/)
25. [Proyecto de Ley, Por medio de la cual se regula integralmente la inteligencia artificial y se dictan otras disposiciones - Sistemas de Algoritmos Públicos](https://algoritmos.uniandes.edu.co/proyecto-de-ley-por-medio-de-la-cual-se-regula-integralmente-la-inteligencia-artificial-y-se-dictan-otras-disposiciones/)
26. [Bogotá, 21 de julio de 2026 Doctor MIGUEL ÁNGEL SÁNCHEZ VÁSQUEZ](https://www.camara.gov.co/wp-content/uploads/2026/07/proyectos-ley/documentos/proyecto-36127/P.L.025-2026SC-INTELIGENCIA-ARTIFICIAL.pdf)
27. [IA en pymes de Colombia 2026: CONPES 4144 y ley de IA](https://mentoracolombia.com/ia-pymes-colombia-conpes-4144-ley-ia-2026/)
28. [REF.: EJECUTA ACUERDO DEL CONSEJO DE LA COMISIÓN PARA EL MERCADO](https://www.cmfchile.cl/sitio/aplic/serdoc/ver_sgd.php?s567=40a8d5968565ff67158cb80b867370abVFdwQmVVNXFRVEJOUkVsNlQwUkpNMDUzUFQwPQ%3D%3D&secuencia=-1&t=1775614202)
29. <https://www.imerc.cl/wp-content/uploads/2019/04/RAN-20-7.pdf>
30. [CMF pone en consulta actualización del Capítulo 20-7 de la RAN sobre externalización de servicios - Carey Abogados](https://www.carey.cl/cmf-pone-en-consulta-actualizacion-del-capitulo-20-7-de-la-ran-sobre-externalizacion-de-servicios)
31. [Normativa en consulta cerrada](https://www.cmfchile.cl/institucional/legislacion_normativa/normativa_tramite_cerrada.php?tpl=alt)
32. [Presidenta de la CMF: “Las aplicaciones y desarrollos de la IA podrían reconfigurar el mapa de riesgos”](https://www.df.cl/mercados/banca-fintech/presidenta-de-la-cmf-pone-foco-en-la-inteligencia-artificial-va-a-agregar)
33. [Ciberseguridad Bancaria en Chile: El Triple Frente 2026](https://www.netprovider.com/post/ciberseguridad-bancaria-chile-triple-frente-2026)
34. [Ley de IA en Chile: en qué va el proyecto](https://iaexperta.cl/ia-legal/ley-inteligencia-artificial-chile/)
35. [Chile AI Regulation Overview](https://regulations.ai/regulations/RAI-CL-NA-SUMMARY-2026)
36. [Protección de datos personales en Chile: guía completa de la Ley 21.719](https://xmslatam.com/ley-21719-proteccion-datos-chile/)
37. [Uso de inteligencia artificial en Chile: 45% de las empresas la adopta, según estudio de AWS](https://www.pauta.cl/tendencias/2026/09/25/el-45-de-las-empresas-chilenas-usa-inteligencia-artificial-pero-la-mayoria-aun-la-ocupa-para-tareas-basicas.html)
38. [Inteligencia artificial en empresas chilenas: 88% ya la usa](https://anda.cl/inteligencia-artificial-empresas-chilenas-adopcion-2026/)
39. [Chile lidera la IA en Latinoamérica, pero solo el 3,6% de sus empresas la escala](https://www.esghoy.cl/consejo-ia-en-el-trabajo-adopcion-chile-2026/)
40. [Estado de la Automatización con IA en Chile 2026: Reporte de Datos · Muze AI Blog](https://muze.cl/blog/reporte-estado-automatizacion-ia-empresas-chile-2026)
41. [Cuatro razones por las que las personas usan más la IA que las empresas en Colombia](https://www.bloomberglinea.com/latinoamerica/colombia/cuatro-razones-por-las-que-las-personas-usan-mas-la-ia-que-las-empresas-en-colombia/)
42. [La IA ya es prioridad para las empresas colombianas, pero solo 4 de cada 10 la integran - Infobae](https://www.infobae.com/tecno/2026/09/21/la-ia-ya-es-prioridad-para-las-empresas-colombianas-pero-solo-4-de-cada-10-la-integran/)
43. [Colombia AI Pulse: Adoptar ya no basta - Endeavor Colombia](https://colombia.endeavor.org/colombia-ai-pulse/)
44. [Dos de cada tres empresas de software en Colombia ya usan IA: así va la adopción de tecnología en el país](https://www.elcolombiano.com/tecnologia/empresas-software-colombia-agentes-ia-fedesoft-2026-HO42080412)
45. [Amazon Bedrock pricing](https://www.aws.eu/bedrock/pricing/)
46. [Amazon Bedrock Guardrails: Essential AWS AI Safety Guide 2026](https://techjacksolutions.com/ai-tools/aws/what-is-bedrock-guardrails/)
47. [PII Redaction Pricing: Comprehend Bills 40x the Model It Guards](https://www.beri.net/article/pii-redaction-pricing-comprehend-azure-google-presidio-cost-per-million-characters)
48. [Entity categories recognized by Personally Identifiable Information (PII) and Protected Health Information (PHI) detection in Azure Language in Foundry Tools - Foundry Tools](https://learn.microsoft.com/en-us/azure/ai-services/language-service/personally-identifiable-information/concepts/entity-categories)
49. [Transparency note - Personally Identifiable Information (PII) feature of Azure Language in Foundry Tools - Foundry Tools](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/language-service/transparency-note-personally-identifiable-information)
50. [presidio/docs/analyzer/adding\_recognizers.md at main · data-privacy-stack/presidio · GitHub](https://github.com/data-privacy-stack/presidio/blob/main/docs/analyzer/adding_recognizers.md)
51. [PII entities supported by Presidio - Presidio](https://presidio.dataprivacystack.org/supported_entities/)
52. [What is an AI firewall, and does it stop ChatGPT leaks?](https://jazz.security/dlp-explained/dlp-basics/what-is-an-ai-firewall/)
53. [Cloudflare AI Gateway: Free Tier, Pricing & Limits](https://pipelab.org/learn/cloudflare-ai-gateway/)
54. [LiteLLM vs Portkey vs Bedrock Gateway: Enterprise Comparison](https://atlan.com/know/litellm-vs-portkey-vs-bedrock-gateway/)
55. [Feature Comparison - Portkey (Prisma AIRS AI Gateway) Docs](https://portkey.ai/docs/product/product-feature-comparison)
56. [Best LLM Gateways (2026): 9 Compared on Cost and Risk](https://aitoolsbakery.com/blog/best-ai-llm-gateways/)
57. [AI Model Router Pricing Compared 2026: OpenRouter, LiteLLM, Portkey, Cloudflare, and What You Actually Pay — TheRouter.ai](https://therouter.ai/blog/ai-model-router-pricing-cost-comparison-2026/)
58. [9 Best Tools for PII Redaction in LLM Calls (2026)](https://www.lyzr.ai/blog/best-tools-for-pii-redaction-in-llm-calls)
59. [Best PII Tokenization Software for LLMs (2026)](https://www.enigmavault.io/blog/best-pii-tokenization-software-for-llms/)
60. [Plans and Pricing](https://www.nightfall.ai/pricing)
61. [GitHub - rafarq/privacy-gateway-es: Pseudonimizacion de datos personales espanoles (NIF/NIE, CIF, telefonos, matriculas, catastro, NUSS, pasaporte) para el plugin privacy-gateway de Hermes Agent. Instalador con motor spaCy espanol y verificacion end-to-end. · GitHub](https://github.com/rafarq/privacy-gateway-es)
62. [The Cleaner: sanitización de datos en LLM](https://blog.donweb.com/sanitizacion-de-datos-en-llm-the-cleaner-avantgate/)
63. [Show HN: Protecto](https://news.ycombinator.com/item?id=46215692)
64. [CMF publica cambios a normativa sobre externalización de servicios en bancos e instituciones financieras - Transtecnia](https://transtecnia.cl/articulo-contable/cmf-publica-cambios-a-normativa-sobre-externalizacion-de-servicios-en-bancos-e-instituciones-financieras/)
65. [SIC emite Circular Externa 001 de 2025: nuevos lineamientos en sector Fintech - MS LEGAL - Protección de Datos Personales y Derecho comercial y corporativo](https://mslegal.com.co/circular-externa-001-de-2025-y-fintech/)
