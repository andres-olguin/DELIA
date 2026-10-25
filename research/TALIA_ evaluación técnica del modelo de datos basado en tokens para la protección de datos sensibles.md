# TALIA: evaluación técnica del modelo de datos basado en tokens (tokenización de datos sensibles)

Para el MVP de TALIA conviene usar un modelo híbrido: una bóveda con alcance por conversación y claves por tenant, y tokens tipados y opacos con identificador estable y checksum (por ejemplo `[[PERSONA_K7Q2]]`). No conviene un FPE sin bóveda como mecanismo principal, y los sustitutos sintéticos que conservan semántica deben quedar como una evolución que se valida con experimentos antes de activarla por tipo de entidad. El riesgo técnico dominante no está en el esquema criptográfico. Está en la detección en español latinoamericano (no existe un benchmark público para Colombia o Chile) y en la restitución correcta en streaming y en tool calling, que es justo donde los gateways existentes más fallan hoy.

## TL;DR

- **Variante recomendada:** bóveda por conversación (mapa token→valor cifrado con DEK por tenant envuelta por KMS/HSM y con TTL) más tokens tipados y opacos con ID estable y checksum. FPE solo como optimización puntual para identificadores estructurados (FF1, nunca FF3/FF3-1, que NIST retiró en el borrador de febrero de 2025). Sustitutos sintéticos que conservan formato y semántica en una fase 2, por tipo de entidad, si el experimento de utilidad lo justifica.
- **Dónde está la dificultad:** restituir en streaming y en argumentos JSON parciales de herramientas. En 2026, LiteLLM acumula issues y PRs por placeholders partidos entre deltas SSE, por contadores que se reinician en cada petición y por fugas cuando se vacía un token truncado. Bedrock no enmascara en modo asíncrono y Cloudflare y Portkey acumulan toda la respuesta (o solo informan) en streaming. Ese hueco es el diferenciador posible de TALIA.
- **Qué probar primero:** (1) un benchmark sintético de detección para Colombia y Chile (cédula, NIT, RUT/RUN con dígito verificador, nombres y direcciones); (2) un A/B de utilidad entre valor real, token opaco y sustituto sintético con tres proveedores; (3) fuzzing de restitución en streaming con cortes aleatorios. Las tres pruebas llevan umbrales de éxito definidos antes de comprometer la arquitectura.

## Resumen ejecutivo

1. La tokenización reversible con bóveda es la única variante que cubre a la vez texto libre (nombres, direcciones), identificadores, credenciales y datos propios de la empresa, y que permite borrar con garantías.
2. El FPE sin bóveda sirve para campos numéricos de formato fijo. No sirve para nombres ni direcciones, exige rotar claves sobre datos ya emitidos y, si es determinista, permite análisis de frecuencia.
3. Los tokens opacos pero distintos por entidad conservan buena parte de la utilidad. Según la evidencia disponible, los sustitutos sintéticos conservan más, pero complican restituir y detectar alteraciones.
4. En streaming hace falta un buffer de retención acotado a la longitud máxima del token, cuyo costo es de milisegundos. En las herramientas, los argumentos se acumulan completos antes de restituirlos y de aplicar la política.
5. La detección debe ser en cascada: regex con validación de dígito verificador, detector de secretos y NER o un modelo de PII (OpenAI Privacy Filter o un transformer afinado en español). Presidio trae reconocedores para España, pero no para Colombia ni Chile.\[1\]\[2\]
6. La auditoría guarda texto redactado, huellas HMAC con clave, una cadena de hashes por tenant y raíces Merkle con sello de tiempo. La reconstrucción ocurre solo con control dual sobre una copia cifrada con una clave de auditoría separada.
7. Ante un fallo de la bóveda o del detector, TALIA falla cerrado, configurable por tenant y por herramienta.
8. Plan: 6–8 semanas de experimentos con métricas objetivo antes de congelar el formato del token y el contrato de la bóveda.

## Key Findings

**Hechos verificados (con fuente y fecha)**

- **Utilidad: placeholders frente a sustitutos.** SurrogateShield (arXiv 2606.29567, 28 de junio de 2026) mide un BERTScore de 94,85 % con sustitutos frente a 81,59 % con placeholders, sobre N = 1.123 consultas, y reporta F1 de detección de 98,87 % en su propio corpus en inglés. En un ataque simulado con un LLM adversario, la tasa de recuperación de valores originales fue de 0,00 % con sustitutos y de 1,53 % con placeholders.\[3\] El trabajo "Say Something Else" (arXiv 2604.06409, 2026) encuentra que la pseudonimización conserva el 98,5 % de la utilidad de la línea base sin protección, frente al 86,6 % de la supresión, y que la generalización se degrada más en seguimiento multiturno (+11,8 pp de media frente a +3,9 pp).\[4\] Un blog de proveedor (nopii, DEV Community) afirma que los placeholders genéricos bajan la calidad al 54–68 % y los tokens únicos deterministas la mantienen en el 91–96 %.\[5\] Es una fuente de proveedor, no revisada por pares, y la uso solo como indicio.
- **Por qué los placeholders genéricos fallan:** si todas las personas se convierten en `[PERSON]`, el modelo ya no distingue quién hizo qué.\[5\] Por eso, cualquier esquema de TALIA debe asignar un ID distinto por entidad.
- **Los modelos alucinan y alteran tokens.** En xolo-gateway (issue #113 y PR #152, 2026), un placeholder inventado por el modelo llegaba al cliente y, en el turno siguiente, desactivaba la pseudonimización: el contenido salía en claro.\[6\]\[7\] En llmhub (PR #135, 22 de octubre de 2026), el modelo trató `[IP_ADDRESS_1]` como dato faltante y pidió al usuario que ejecutara `whois`.\[8\] local-privacy-gateway documenta dos modos de restitución, "strict" (todo token debe ser conocido) y "lenient" (acepta variantes en minúsculas, sin corchetes o entre comillas).\[9\]
- **Streaming en LiteLLM.** El issue #42476 documenta que el tokenizador parte con frecuencia un placeholder de 12 caracteres entre dos o tres eventos `text_delta`, de modo que reemplazar por delta "nunca" coincide.\[10\] El PR #46272 corrige eventos SSE partidos entre chunks de bytes, que salían sin restituir o con valores equivocados (por ejemplo, "New York2>").\[11\] El PR #46230 deja abierta una fuga de severidad media: vaciar un token truncado puede corromper el framing SSE y dejar pasar un número de tarjeta restituido.\[12\] El issue #41600 muestra que el contador de placeholders se reinicia en cada petición, así que los tokens que el modelo copia de turnos anteriores quedan sin resolver para siempre.\[13\]
- **Bedrock Guardrails.** En el modo síncrono, que es el predeterminado, la respuesta se acumula antes de enviarse. La guía de usuario de Amazon Bedrock ("Configure streaming response behavior") advierte: "Amazon Bedrock Guardrails doesn't support the masking of sensitive information with asynchronous mode." En el PR #1080 de aws-samples/sample-aws-genai-db-modernizer, el modo síncrono evaluaba la respuesta completa y provocaba timeouts de lectura de 300 s; la "Maintainer decision (2026-10-18)" fue mantener el modo síncrono para que el enmascaramiento de datos personales siguiera funcionando y dejar el modo async como opción que lo desactiva.
- **Portkey.** Según la documentación de Portkey Guardrails, los guardrails de salida en streaming se evalúan sobre la respuesta completa cuando el stream termina y "no action is taken… results are informational only".
- **Cloudflare AI Gateway DLP.** Con escaneo de respuestas en SSE, acumula la respuesta completa antes de evaluarla, lo que aumenta el tiempo al primer token.\[14\] La acción es marcar o bloquear; no hay enmascaramiento documentado.\[15\]\[16\]
- **FPE.** El segundo borrador público de NIST SP 800-38G Rev. 1 (3 de febrero de 2025) elimina FF3 y deja FF1. La razón es una debilidad en el tweak schedule, descrita por Beyne, que afecta a FF3 y FF3-1. También refuerza la guía sobre dominios pequeños: el dominio mínimo pasa a un millón.\[17\]\[18\]\[19\] La documentación de HashiCorp Vault Transform todavía describe su FPE "via FF3-1", algo que hay que revisar si se elige Vault.\[20\]\[21\]
- **Bóveda: rendimiento.** Según HashiCorp, la tokenización de Vault Transform tiene estado: cada encode escribe en el nodo primario. FPE y Transit no escriben en almacenamiento y escalan horizontalmente con nodos standby.\[22\] Vault permite tokenización "convergente" (el mismo valor produce el mismo token), pero requiere Vault Enterprise con el módulo ADP-Transform.\[22\]\[23\]
- **Detección en español.** Presidio tiene reconocedores específicos para España (ES_NIF, ES_NIE), pero ninguno para Colombia ni Chile.\[2\] Las notas de la versión 2.2.359 de Presidio indican "Set country-specific default recognizers to enabled=false for safer defaults (#1586)", con EsNifRecognizer en la lista. OpenAI Privacy Filter (22 de abril de 2026) tiene licencia Apache 2.0, 1,5B de parámetros con 50M activos, y logra F1 de 96 % en PII-Masking-300k (precisión 94,04 %, recall 98,04 %).\[24\]\[25\] En una evaluación independiente (arXiv 2608.02616, agosto de 2026) supera a Presidio en español por +0,279 de F1,\[26\] pero es débil en nombres de persona (0,40) y direcciones (0,49) y tiende a favorecer el recall.\[26\] El benchmark REDACT (arXiv 2606.19881) reporta para Presidio un recall de solo 0,07 en entidades de alta sensibilidad.\[27\] spaCy `es_core_news_lg` declara F1 de NER de 89,72, medido sobre corpus de España (AnCora y WikiNER, anotaciones "silver").\[28\]\[29\] En des-identificación clínica en español (MEDDOCAN), el mejor sistema alcanzó F1 de 0,97033 (P 0,96999, R 0,97068), según el artículo de resumen de Marimon et al. (IberLEF 2019, CEUR-WS Vol-2421). Fuera de dominio, un modelo entrenado en radiología cae a un recall de 69,18 % cuando se evalúa en MEDDOCAN.
- **No existe un benchmark público de PII para Colombia o Chile** (resultado de la búsqueda de esta investigación; ver Caveats). ai4privacy incluye español (78.013 filas, 13,45 % en open-pii-masking-500k), pero el desglose regional visible es de España.\[30\]
- **Dígitos verificadores.** NIT (Colombia): se multiplican los dígitos, de derecha a izquierda, por los primos 3, 7, 13, 17, 19, 23, 29, 37, 41, 43, 47, 53, 59, 67 y 71, y se toma la suma módulo 11. Si el residuo es 0 o 1, ese es el DV; si no, el DV es 11 menos el residuo.\[31\]\[32\] RUT/RUN (Chile): pesos 2–7 cíclicos, se calcula 11 − (suma mod 11), y el resultado 11 se convierte en 0 y el 10 en "K".\[33\] La cédula de ciudadanía colombiana no tiene dígito verificador, así que solo admite validación por formato y contexto. python-stdnum implementa `cl.rut` y `co.nit`.\[34\]\[35\]
- **Secretos.** En SecretBench (arXiv 2307.00714), Gitleaks logra el mejor recall (88 %) con precisión de 46 %.\[36\] En otra comparación (IssueGuard, arXiv 2602.08072), TruffleHog obtiene precisión de 55,39 % y recall de 93,94 %. Los escáneres basados en regex detectan mucho pero generan muchos falsos positivos.\[37\]
- **Formatos de streaming.** Anthropic envía los argumentos de herramientas como eventos `input_json_delta` con fragmentos `partial_json`. Con fine-grained tool streaming, la API no valida ni acumula, así que pueden llegar fragmentos de JSON inválido.\[38\] OpenAI Chat Completions transmite fragmentos indexados en `delta.tool_calls`. Gemini (`streamGenerateContent?alt=sse`) envía los argumentos completos en un solo delta,\[39\] y su endpoint compatible con OpenAI omite el campo `index` en llamadas paralelas (PR #2051 de neurolink).\[40\]
- **Exfiltración en agentes.** La "trifecta letal" es la combinación de acceso a datos privados, contenido no confiable y un canal de salida; Simon Willison escribió en su weblog el 16 de junio de 2025: "If your agent combines these three features, an attacker can easily trick it into accessing your private data and sending it to that attacker."

**Inferencias propias (marcadas como tales a lo largo del informe):** el costo de latencia del buffer de retención, la elección del formato del token, los umbrales de éxito del plan de validación y las estimaciones de costo relativo son razonamiento de arquitectura, no datos medidos.

## Tabla comparativa de variantes de tokenización

| Criterio | (a) Bóveda (token→valor) | (b) FPE sin bóveda (FF1) | (c) Type/semantic-preserving (sustitutos sintéticos) | (d) Híbrido recomendado |
|---|---|---|---|---|
| Cobertura de tipos | Total: texto libre, IDs, secretos, datos propios | Solo campos de alfabeto y longitud fijos (dígitos, alfanuméricos). Nombres y direcciones salen como galimatías | Total si existe un generador por tipo (nombres, direcciones, RUT/cédula, fechas, montos) | Total |
| Reversibilidad | Búsqueda en la bóveda | Descifrado con clave; sin estado | Requiere un mapa (es decir, una bóveda) | Bóveda, con FPE opcional por campo |
| Utilidad para el LLM | Media-alta con ID distinto por entidad; baja con placeholder genérico [Hecho: SurrogateShield, nopii] | Alta en campos numéricos (conserva formato), pero el DV queda inválido salvo que se recalcule [Inferencia] | La más alta medida (BERTScore 94,85 % frente a 81,59 %) [Hecho]\[3\] | Alta, configurable por tipo |
| Robustez de la restitución | Alta: el token es inconfundible y tiene checksum | Alta, si el modelo no altera dígitos; si los altera, el resultado es un valor erróneo pero válido [Inferencia] | Baja-media: el modelo flexiona o abrevia nombres ("Ashley" → "Sra. Wise"), y el sustituto puede chocar con texto real [Inferencia] | Alta en la fase 1; se mide antes de activar (c) |
| Detección de tokens alucinados o alterados | Sí (formato y checksum) | No: cualquier valor descifra a "algo" | Difícil | Sí |
| Riesgo de inferencia | Bajo con alcance por conversación; medio si es determinista por tenant | Alto si es determinista (frecuencia, enlace entre conversaciones); comprometer la clave expone todo | Bajo; el adversario no ve que hubo sustitución [Hecho: 0 % de recuperación en 100 consultas]\[3\] | Bajo |
| Correlación entre turnos y modelos | Sí, si el mapa vive por conversación y lo comparte el router | Sí, de forma natural (determinista) | Sí, con mapa por conversación | Sí |
| Borrado y derecho al olvido | Borrado del mapa o crypto-shredding de la DEK | Imposible "olvidar" sin rotar la clave para todos | Igual que la bóveda | Crypto-shredding |
| Estado y operación | Con estado: escrituras, replicación, TTL | Sin estado: solo gestión de claves | Con estado más generadores por país | Con estado (Redis/Postgres + KMS) |
| Latencia añadida | Una lectura o escritura por entidad (en memoria o KV local: sub-ms a pocos ms) [Estimación] | Microsegundos por campo [Estimación] | Igual que la bóveda más la generación | Igual que la bóveda |
| Riesgo normativo-técnico | Ninguno especial | FF3/FF3-1 retirados en el borrador de NIST; dominio mínimo de 10^6\[18\]\[19\] | Colisión con personas reales (un RUT sintético válido puede existir) [Inferencia] | Mitigado |
| Complejidad y costo relativo | Media | Baja en el núcleo, alta en el ciclo de claves | Alta (generadores locales, coherencia de género y región) | Media en la fase 1 |

## Diseño recomendado (MVP y evolución)

### 1. Esquema de tokens

- **Formato:** `[[TIPO_ID]]`, por ejemplo `[[PERSONA_K7Q2]]`, `[[RUT_9XM4]]` o `[[SECRETO_A1B8]]`.
  - `TIPO` es un vocabulario cerrado en español (PERSONA, DIRECCION, CEDULA, NIT, RUT, EMAIL, TELEFONO, CUENTA, MONTO_SENSIBLE, SECRETO, DATO_EMPRESA). Le da al modelo una pista semántica sin revelar el valor.
  - `ID` son 3 caracteres base32 derivados de HMAC(clave_conversación, tipo‖valor_normalizado), más 1 carácter de checksum. La normalización quita puntos y guiones del RUT y pasa a minúsculas los emails, de modo que "12.345.678-5" y "12345678-5" producen el mismo token.
  - El checksum permite distinguir un token alterado de uno inventado.
  - [Inferencia] Los delimitadores ASCII dobles se tokenizan de forma predecible y casi no aparecen en texto natural. Hay que evitar formatos que el modelo "corrija", como `<PERSON>`, que se confunde con HTML.
- **Determinismo y alcance:** determinista dentro de la conversación (el mismo valor da el mismo token en todos los turnos y en todos los modelos del router) y aleatorio entre conversaciones, porque la clave HMAC es por conversación.
  - Así se evita el problema de LiteLLM #41600 (contador reiniciado en cada petición).\[13\]
  - También se evita el análisis de frecuencia entre conversaciones.
  - El alcance por tenant (tokenización convergente) solo se ofrece como opción explícita para casos de analítica, sabiendo que habilita el enlace de registros.
- **Invariante de historial:** el historial que se envía al proveedor contiene siempre tokens, nunca valores. Es el invariante I2 de SurrogateShield.\[3\] Cuando el cliente reenvía el historial ya restituido (que es lo habitual, porque solo cambia el base_url), TALIA vuelve a tokenizar y obtiene el mismo token gracias al determinismo.
- **Tokens desconocidos en la entrada:** si llega un `[[TIPO_ID]]` con checksum válido pero sin entrada en la bóveda (un token alucinado que el cliente guardó), se neutraliza escapándolo. No se aborta la tokenización del turno, a diferencia del fallo de xolo #113.\[7\]
- **Instrucción de sistema:** TALIA inyecta un mensaje breve que dice que los tokens son valores reales opacos y que deben copiarse literalmente, también dentro de los argumentos de herramientas. Así se mitiga el caso de llmhub #135.\[8\]

### 2. Restitución en streaming

- **Normalización:** cada proveedor se convierte a un modelo interno de eventos (`text_delta`, `tool_args_delta`, `tool_call_start/stop`, `reasoning_delta`, `stop`) y se re-serializa al dialecto del cliente.
  - Las fuentes son OpenAI Chat (`choices[].delta`), OpenAI Responses (`response.*`), Anthropic (`content_block_*`, `input_json_delta`) y Gemini (`candidates[].content.parts`, argumentos completos, sin `index` en el modo compatible).\[39\]
  - El parseo SSE se hace a nivel de evento completo, nunca por chunk de bytes (lección del PR #46272 de LiteLLM).\[11\]
- **Buffer de retención por bloque de contenido:** se emite todo el texto salvo el sufijo que podría ser el inicio de un token, es decir, el sufijo que contiene `[`, `[[` o `[[TIPO_…` sin cerrar.
  - La retención máxima es la longitud del token más largo, unos 24 caracteres. Si se supera sin cierre, se emite tal cual.
  - Al terminar el stream, un token truncado se marca como `[dato omitido]`. Nunca se restituye un valor parcial (fuga abierta en el PR #46230 de LiteLLM).\[12\]
  - [Estimación] La latencia añadida es de uno o dos deltas cuando hay un token en curso y de cero el resto del tiempo. Es despreciable frente al TTFT del modelo.
- **Modo de restitución:** lenient con lista blanca de variantes (minúsculas, sin corchetes, entre backticks). Los tokens desconocidos se reemplazan por un marcador neutral y se registran en la auditoría.
- **Escaneo de salida (opcional):** se detecta PII nueva que el modelo genere, por ejemplo un RUT completado por inferencia. En streaming hay que elegir entre una ventana deslizante con detector ligero (regex más checksum) y acumular la respuesta completa, como hacen Bedrock en modo síncrono y Cloudflare.\[14\]\[41\] Recomendación: regex en línea y NER solo en modo acumulado configurable.

### 3. Tool calling y agentes

- **Acumular y luego restituir:** los fragmentos de argumentos se acumulan por índice de llamada hasta `content_block_stop` o `finish_reason=tool_calls`. Luego se parsea el JSON, se restituye sobre el árbol (valores string) y se aplica la política. No se restituye sobre JSON parcial porque los tokens pueden caer partidos y el JSON puede llegar inválido.\[38\]\[42\]
  - Si el cliente necesita ver los argumentos en vivo, se le reenvían tokenizados con el mismo buffer de retención, y la versión restituida se entrega al cierre.
- **Política por herramienta (TALIA como PEP):**
  - `allow_real`: la herramienta recibe valores reales, por ejemplo una consulta interna al CRM.
  - `tokens_only`: la herramienta recibe tokens, por ejemplo búsqueda web o envío de email externo.
  - `deny_types`: la herramienta nunca recibe SECRETO ni CUENTA.
  - Por defecto, toda herramienta con salida a red externa es `tokens_only`. Así se rompe la "trifecta letal": los datos reales no viajan por el canal de exfiltración aunque una inyección de prompt lo pida.
  - Requisito técnico: en modo proxy, la ejecución de herramientas ocurre en el cliente. TALIA solo controla qué versión de los argumentos le entrega, así que la política necesita metadatos de herramienta declarados por el cliente o por el tenant.
- **Resultados de herramientas (`tool_result`):** se tokenizan antes de reenviarlos al modelo. Son contenido no confiable y suelen traer PII nueva.
- **Documentos, OCR y RAG:**
  - Se extrae el texto (PDF y DOCX con parser, imágenes con OCR local) y se tokeniza antes de que salga hacia el proveedor.
  - Si la política exige enviar la imagen original, se redacta la imagen (cajas negras sobre las regiones detectadas por OCR) o se bloquea.
  - En RAG, conviene tokenizar en la ingesta con alcance por tenant, de modo que el índice vectorial nunca guarde valores, y restituir solo en la salida al usuario autorizado.\[43\]
  - [Inferencia] Esto obliga a ofrecer un modo de tokenización "por corpus" distinto del modo por conversación.

### 4. Bóveda

- **Almacenamiento:** KV (Redis/Valkey con persistencia, o Postgres) con entradas `{tenant, conversación, token} → AES-256-GCM(valor)`.
  - Cifrado por envoltura: una DEK por tenant (o por tenant y día), envuelta por una KEK en KMS/HSM (AWS KMS, GCP KMS, Azure Key Vault, o Vault Transit u OpenBao en el entorno del cliente).
  - TTL por conversación (por ejemplo 24 h a 30 días, configurable) y borrado por crypto-shredding de la DEK.
- **Rendimiento:** la bóveda vive en el mismo nodo o zona que el gateway, con caché en memoria de la conversación activa. El patrón de acceso es de pocas escrituras por turno. Que Vault Transform escriba en el primario por cada encode es una razón para no usarlo como ruta caliente:\[22\] conviene una bóveda propia ligera con la KEK en un KMS.
- **Despliegue en el entorno del cliente:** un solo binario o contenedor con KV embebido o Redis del cliente y un conector KMS intercambiable. En SaaS, aislamiento por tenant (clave más namespace) y residencia de datos por región.
- **Fallar cerrado:** si fallan la bóveda, el KMS o el detector, la petición se rechaza con un error explícito, no se reenvía en claro. Si falla la restitución, se entrega el texto tokenizado, no un valor equivocado. Los tenants pueden elegir degradar a "solo regex" cuando falla el NER, siempre con alerta.
- **Bóveda frente a FPE (costo y complejidad, [Estimación]):** el FPE ahorra el almacenamiento y la replicación, pero no ahorra la gestión de claves, no cubre texto libre ni permite borrar por entidad, y obliga a vigilar el estado normativo de FF1. Para TALIA, la bóveda es necesaria de todas formas. El FPE solo añadiría valor como optimización para tenants que necesiten cédula, RUT o tarjeta con formato válido y reversibilidad sin estado, por ejemplo integraciones con bases de datos heredadas.

### 5. Detección

- **Cascada en tres capas:**
  1. Regex con validación de checksum: RUT/RUN módulo 11 con K, NIT con pesos primos, tarjetas con Luhn, IBAN, emails, teléfonos +57/+56. Para la cédula colombiana se usa regex con palabras de contexto ("C.C.", "cédula", "CC No."), porque no tiene DV.
  2. Detector de secretos con reglas tipo Gitleaks y TruffleHog, más entropía y palabras clave. Para bloquear, se prefiere el recall.
  3. Un modelo de PII o NER para nombres, direcciones y organizaciones: OpenAI Privacy Filter afinado con datos sintéticos de Colombia y Chile, o un transformer en español (XLM-R o RoBERTa-es) afinado. La evaluación de OPF sugiere que unos 100–500 ejemplos etiquetados bastan para que un modelo afinado supere al zero-shot, aunque ese dato es de otros dominios.\[26\]\[44\]
- **Datos propios de la empresa:** diccionarios por tenant (clientes, proyectos, códigos internos) con un matcher Aho-Corasick y regex definidas por el tenant.
- **Evaluación:** se genera un corpus sintético con plantillas en español de Colombia y Chile (nombres compuestos, dos apellidos, direcciones tipo "Cra. 7 # 45-10, Bogotá" o "Av. Providencia 1234, depto 56, Santiago", RUT con y sin puntos), más ruido real: tildes ausentes, mayúsculas, WhatsApp, OCR.
  - Se mide recall y precisión por entidad y por forma de mención (completa, parcial, ofuscada), siguiendo la lección de REDACT de que el F1 agregado oculta los fallos de alto riesgo.\[45\]
  - Conviene complementar con una muestra real anonimizada de un cliente piloto, porque los datos sintéticos tienden a inflar los resultados.\[46\]

### 6. Auditoría verificable

- **Registro por evento:** texto redactado (con tokens), metadatos (tenant, modelo, herramienta, política aplicada, tipos detectados, conteos, tokens desconocidos) y huellas HMAC-SHA256 con una clave de auditoría por tenant guardada en KMS.
  - Nunca se usan hashes sin clave, porque una cédula o un RUT tienen poca entropía y se pueden recuperar por fuerza bruta.
- **Integridad:**
  - Cadena de hashes por tenant (`H_n = HMAC(K, H_{n-1} ‖ JSON_canónico(E_n))`).\[47\]
  - Cada hora, raíz Merkle del lote, firmada (Ed25519 o ECDSA en KMS) y anclada con un sello de tiempo RFC 3161 o en un almacenamiento WORM (S3 Object Lock o equivalente).\[48\]
  - El hash se calcula sobre el texto redactado y el material cifrado, nunca sobre texto en claro. Así, el crypto-shredding no rompe la verificación.\[47\]
- **Reconstrucción bajo autorización:**
  - Una copia del mapa token→valor del evento se guarda cifrada con una clave de auditoría separada de la de tiempo de ejecución, con retención propia.
  - Para descifrar se necesita control dual (dos aprobadores) y la operación queda registrada en la misma cadena.
  - El auditor recibe el evento reconstruido junto con la prueba de inclusión Merkle que demuestra que el registro no fue alterado.\[49\]

### 7. Ruta de evolución

- **Fase 1 (MVP, 0–3 meses):**
  - Endpoints compatibles con OpenAI y Anthropic, con router.
  - Tokens opacos tipados por conversación y bóveda con KMS.
  - Detección por regex y checksum, secretos y un modelo de NER.
  - Buffer de retención en streaming y acumulación de argumentos de herramientas con política por herramienta.
  - Auditoría con cadena de hashes. Fallar cerrado.
- **Fase 2 (3–6 meses):**
  - Sustitutos sintéticos por tipo (empezando por fechas y montos relativos, luego nombres), solo si el experimento E2 lo justifica.
  - Gemini nativo, OCR, modo RAG por corpus.
  - Raíces Merkle con RFC 3161 y portal de auditor.
- **Fase 3 (6–12 meses):**
  - FPE FF1 opcional para identificadores estructurados.
  - Tokenización convergente por tenant para analítica.
  - Detector afinado con datos del piloto.
  - Patrón dual-LLM o cuarentena para herramientas de alto riesgo.\[50\]

## Riesgos técnicos

1. **Recall insuficiente en español latinoamericano.** No hay benchmark público. Presidio no tiene reconocedores para Colombia ni Chile, y los modelos generalistas son débiles en nombres y direcciones (OPF: 0,40 y 0,49 de F1). Cada falso negativo es una fuga.\[26\]
2. **Tokens alterados o alucinados por el modelo:** valores perdidos, marcadores visibles para el usuario o desactivación de la protección en turnos siguientes (xolo #113).\[6\]
3. **Restitución incorrecta en streaming:** tokens partidos entre eventos o chunks, tokens truncados por `max_tokens` o framing SSE corrupto (LiteLLM #42476, #46272, #46230).\[10\]\[11\]\[12\]
4. **Argumentos de herramientas:** JSON parcial o inválido (fine-grained streaming de Anthropic),\[38\] llamadas paralelas sin `index` (Gemini en modo OpenAI) y valores reales que llegan a herramientas con salida externa.\[40\]
5. **Inyección de prompt y exfiltración (trifecta letal):** se mitiga con `tokens_only` por defecto, pero no se elimina si el cliente marca herramientas externas como `allow_real`.\[51\]
6. **Re-identificación por cuasi-identificadores:** comuna, edad y cargo pueden identificar a alguien sin ninguna PII "clásica".\[3\] La tokenización por entidad no lo cubre. [Inferencia] Hace falta una capa de generalización opcional.
7. **Inferencia sobre tokens deterministas** si se activa el alcance por tenant: frecuencia y enlace entre conversaciones.
8. **Colisión de sustitutos sintéticos con personas reales:** un RUT o una cédula sintéticos con DV válido pueden pertenecer a alguien.
9. **La bóveda como punto único de fallo o de alto valor:** disponibilidad, compromiso de la DEK o la KEK, y backups con datos en claro.
10. **Deriva de los formatos de los proveedores:** nuevos tipos de eventos (reasoning, server tools, Responses API) que el normalizador no conoce y que podrían pasar sin escanear. Política: todo evento desconocido se bloquea o se escanea como texto.
11. **Caché de prompts y reasoning firmados:** reescribir el historial puede invalidar la caché del proveedor o bloques de razonamiento firmados (llmhub #135 menciona bloques "signed thinking"). El determinismo por conversación lo mitiga.\[8\]

## Plan de validación (experimentos priorizados)

Los umbrales son propuestas mías [Inferencia] y hay que ajustarlos con el piloto.

| # | Experimento | Diseño | Métrica de éxito |
|---|---|---|---|
| E1 | Benchmark de detección para Colombia y Chile | 5.000 textos sintéticos más 500 reales anonimizados del piloto. Comparar regex+checksum, Presidio con reconocedores propios, OPF zero-shot y OPF/XLM-R afinado | Recall ≥ 0,99 en IDs con checksum (RUT, NIT, tarjeta); ≥ 0,95 en cédula, email y teléfono; ≥ 0,90 en nombres y direcciones; precisión ≥ 0,85; p95 de latencia del detector ≤ 30 ms por 1.000 tokens en CPU |
| E2 | Utilidad: valor real frente a token opaco frente a sustituto | 300 tareas (resumen, extracción, redacción de cartas, cálculo con montos y fechas, conversación multiturno) en tres proveedores y un modelo local. Evaluación con LLM-juez más exactitud en tareas verificables | Token opaco ≥ 95 % de la línea base real; si los sustitutos superan a los opacos por ≥ 3 pp, se activan en la fase 2 para esos tipos |
| E3 | Fidelidad de restitución | Mismas tareas; medir tokens restituidos, alterados, alucinados y omitidos | 0 valores incorrectos restituidos; < 0,5 % de tokens desconocidos; 0 tokens sin restituir visibles en modo strict |
| E4 | Fuzzing de streaming | Respuestas con PII cortadas en puntos aleatorios a nivel de byte, evento y delta, para los cuatro dialectos, incluyendo truncado por `max_tokens` | 0 fugas o corrupciones en 10^6 casos; sobrecarga de TTFT p95 < 20 ms; sobrecarga de throughput < 5 % |
| E5 | Tool calling | Llamadas simples y paralelas con PII en argumentos; políticas `allow_real` y `tokens_only` | 100 % de cumplimiento de la política; 0 JSON corrupto entregado |
| E6 | Inyección y exfiltración | Suite de inyección indirecta (documentos, resultados de herramientas, RAG) que intenta enviar PII a una URL o herramienta externa | 0 valores reales en herramientas `tokens_only`; tasa de bloqueo registrada |
| E7 | Caos de bóveda y detector | Matar la bóveda, el KMS o el NER durante la carga | 100 % de peticiones rechazadas o degradadas según la política; 0 envíos en claro |
| E8 | Auditoría | Alterar, borrar o reordenar registros; verificar la cadena y las pruebas Merkle; ejercicio de reconstrucción con control dual | 100 % de detección de manipulación; reconstrucción en menos de 15 min con dos aprobadores |

**Orden sugerido:** E1 y E4 primero (semanas 1–3), porque son los que más pueden invalidar el diseño. Luego E2 y E3 (semanas 3–5), que deciden el formato del token. Por último, E5 a E8 (semanas 5–8).

## Caveats

- **Antigüedad y alcance de las fuentes:**
  - Varias cifras de utilidad vienen de preprints de 2026 (SurrogateShield, "Say Something Else") con corpus en inglés y métricas indirectas como BERTScore. No hay estudios equivalentes en español latinoamericano.
  - El dato de nopii es de un proveedor.
  - Los números de detección en español (spaCy, MEDDOCAN) son de España y del dominio clínico.
  - No encontré un benchmark de PII para Colombia o Chile. Es un hueco real, no una omisión de búsqueda.
- **Estado del código citado:** los issues y PRs de LiteLLM describen el estado del código en fechas concretas de 2026. Algunos ya están corregidos, y sirven como catálogo de modos de fallo, no como evaluación actual del producto.
- **Cloudflare:** la documentación de Cloudflare AI Gateway DLP indica "DLP buffers the full streamed response before scanning", y la página Set up DLP solo ofrece las acciones "Flag" y "Block", sin enmascaramiento.
- **FPE:** el estado de FF1 depende de la versión final de SP 800-38G Rev. 1. A la fecha de las fuentes consultadas era un segundo borrador público, con el periodo de comentarios cerrado el 4 de abril de 2025.\[19\]
- **Inferencias y estimaciones:** los valores de latencia y costo son estimaciones de arquitectura, no mediciones. Los umbrales del plan de validación son propuestas. Este informe no evalúa aspectos legales (Ley 1581 de Colombia, Ley 21.719 de Chile), como pediste.

## Fuentes

1. [Supported Entities](https://deepwiki.com/microsoft/presidio/4-supported-entities)
2. [PII entities supported by Presidio - Presidio](https://presidio.dataprivacystack.org/supported_entities/)
3. [SurrogateShield: Beyond Redaction for High-Utility, Privacy-Preserving LLM Interactions](https://arxiv.org/pdf/2606.29567)
4. [Say Something Else: Rethinking Contextual Privacy as Information Sufficiency](https://arxiv.org/pdf/2604.06409)
5. [We ran 109 tests to measure how PII protection methods affect LLM output quality. Here's what we learned and what we built. - DEV Community](https://dev.to/nopii_hq/we-ran-109-tests-to-measure-how-pii-protection-methods-affect-llm-output-quality-heres-what-we-1k2f)
6. [pseudonymizer: placeholders invented by the model reach the client and turn pseudonymization off on the next turn · Issue #113 · xolo-gateway/xolo · GitHub](https://github.com/xolo-gateway/xolo/issues/113)
7. [fix(pseudonymizer): neutralize placeholders the model invents instead of forwarding the next turn in clear by Bornholm · Pull Request #152 · xolo-gateway/xolo · GitHub](https://github.com/xolo-gateway/xolo/pull/152)
8. [Let the model work with PII placeholders, show restores in the log, and split internal IPs by nicolaeser · Pull Request #135 · nicolaeser/llmhub · GitHub](https://github.com/nicolaeser/llmhub/pull/135)
9. [GitHub - PLUCNT/local-privacy-gateway: Offline pseudonymization gateway and local API proxy: reversible tokens for personal data before text reaches an external LLM · GitHub](https://github.com/PLUCNT/local-privacy-gateway)
10. [\[Bug\]: Anthropic /v1/messages passthrough streams bypass post-call guardrails, so output\_parse\_pii leaks masked placeholders · Issue #42476 · BerriAI/litellm · GitHub](https://github.com/BerriAI/litellm/issues/42476)
11. [fix(presidio): unmask Anthropic SSE streams across chunk boundaries by Dmitry-Kucher · Pull Request #46272 · BerriAI/litellm · GitHub](https://github.com/BerriAI/litellm/pull/46272)
12. [fix(guardrails): restore streamed PII placeholders on Anthropic /v1/messages by VimarshDwivedi · Pull Request #46230 · BerriAI/litellm · GitHub](https://github.com/BerriAI/litellm/pull/46230)
13. [\[Feature\]: Presidio output\_parse\_pii — derive placeholders from the value so tokens stay stable across requests · Issue #41600 · BerriAI/litellm · GitHub](https://github.com/BerriAI/litellm/issues/41600)
14. [developers.cloudflare.com](https://developers.cloudflare.com/ai-gateway/features/dlp)
15. [TrustGate vs Cloudflare AI Gateway](https://neuraltrust.ai/blog/neuraltrust-vs-cloudflare-ai-gateway)
16. [Coding agents · Cloudflare AI Gateway docs](https://developers.cloudflare.com/ai-gateway/integrations/coding-agents/)
17. [GitHub - joelee/fpr-ff1: Implementation of FF1, the format-preserving encryption mode from NIST SP 800-38G. · GitHub](https://github.com/joelee/fpr-ff1)
18. [NIST Special Publication 800 NIST SP 800-38Gr1 2pd](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-38Gr1.2pd.pdf)
19. [Official websites use .gov](https://csrc.nist.gov/pubs/sp/800/38/g/r1/2pd)
20. [web-unified-docs/content/vault/v2.x/content/docs/secrets/transform/index.mdx at main · hashicorp/web-unified-docs · GitHub](https://github.com/hashicorp/web-unified-docs/blob/main/content/vault/v2.x/content/docs/secrets/transform/index.mdx)
21. [Transform sensitive data with Vault](https://developer.hashicorp.com/vault/tutorials/encryption-as-a-service/transform)
22. [Secure external data with Vault](https://developer.hashicorp.com/vault/docs/concepts/transform)
23. [Transform secrets engine](https://developer.hashicorp.com/vault/docs/secrets/transform)
24. [Introducing OpenAI Privacy Filter](https://openai.com/index/introducing-openai-privacy-filter/)
25. [OpenAI Releases Privacy Filter: A 1.5B-Parameter Open-Source PII Redaction Model with 50M Active Parameters - MarkTechPost](https://www.marktechpost.com/2026/04/28/openai-releases-privacy-filter-a-1-5b-parameter-open-source-pii-redaction-model-with-50m-active-parameters/)
26. [OpenAI Privacy Filter: A Cross-Lingual, Cross-Domain PII Evaluation Across 32 Benchmarks](https://arxiv.org/html/2608.02616)
27. [REDACT: A Systematically Controlled Multilingual Benchmark for Personal Information Detection](https://arxiv.org/html/2606.19881v1)
28. [spacy-models/meta/es\_core\_news\_md-2.0.0.json at master · explosion/spacy-models · GitHub](https://github.com/explosion/spacy-models/blob/master/meta/es_core_news_md-2.0.0.json)
29. [spacy/es\_core\_news\_lg · Hugging Face](https://huggingface.co/spacy/es_core_news_lg)
30. [ai4privacy/open-pii-masking-500k-ai4privacy · Datasets at Hugging Face](https://huggingface.co/datasets/ai4privacy/open-pii-masking-500k-ai4privacy)
31. [Consultar el NIT de una empresa colombiana, gratis](https://radicadouno.co/guias/consultar-nit-de-una-empresa)
32. [Validador de NIT Colombia: calcula y verifica el dígito de verificación](https://tiendli.com/herramientas/validador-nit-colombia)
33. [Chile RUT Validator](https://blog.validacuenta.com/en/validate-rut/)
34. [python-stdnum · PyPI](https://pypi.org/project/python-stdnum/1.3/)
35. [GitHub - arthurdejong/python-stdnum: A Python library to provide functions to handle, parse and validate standard numbers. · GitHub](https://github.com/arthurdejong/python-stdnum/)
36. [A Comparative Study of Software Secrets Reporting by Secret Detection Tools](https://arxiv.org/pdf/2307.00714)
37. [IssueGuard: Real-Time Secret Leak Prevention Tool for GitHub Issue Reports](https://arxiv.org/pdf/2602.08072)
38. [Fine-grained tool streaming - Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)
39. [GitHub - slegarraga/llm-sse: Parse streaming responses from OpenAI, Anthropic and Gemini into one unified event format. Text and tool-call deltas. Zero dependencies. · GitHub](https://github.com/slegarraga/llm-sse)
40. [fix(providers): keep parallel tool calls apart when SSE deltas carry no index by pcbeingused333 · Pull Request #2051 · juspay/neurolink · GitHub](https://github.com/juspay/neurolink/pull/2051)
41. [Amazon Bedrock Guardrails: Content Filters, PII, and Streaming](https://gerardo.dev/en/bedrock-guardrails.html)
42. [Claude Tool Use for Structured JSON Output — Jsonic](https://jsonic.io/guides/anthropic-tool-use-json)
43. [Skyflow for AI Agent Security: Features, Pricing, and Alternatives — WorkOS](https://workos.com/blog/skyflow-vs-workos-agentic-security)
44. [OpenAI Privacy Filter: A Cross-Lingual, Cross-Domain PII Evaluation](https://arxiv.org/pdf/2608.02616)
45. [REDACT: A Systematically Controlled Multilingual Benchmark for Personal Information Detection](https://arxiv.org/pdf/2606.19881)
46. [Utility-Preserving De-Identification for Math Tutoring: Investigating Numeric Ambiguity in the MathEd-PII Benchmark Dataset](https://arxiv.org/pdf/2602.16571)
47. [AuditLog: Designing Production-Grade, Tamper-Evident Audit Trails for Modern Cloud Architectures - DEV Community](https://dev.to/alessio99xx/auditlog-designing-production-grade-tamper-evident-audit-trails-for-modern-cloud-architectures-4fck)
48. [Merkle Trees vs Hash Chains for Audit Logs: A Practical Decision Guide - DEV Community](https://dev.to/gentlyding/merkle-trees-vs-hash-chains-for-audit-logs-a-practical-decision-guide-361l)
49. [GitHub - PalaciosLuis/audit-chain: Interactive explainer: tamper-evident audit logs with a real SHA-256 hash chain, Merkle proofs and signed exports, all running in your browser. · GitHub](https://github.com/PalaciosLuis/audit-chain)
50. [The Lethal Trifecta: How AI Agents Leak Your Data](https://cosmonic.com/ai-sandbox/principles/lethal-trifecta/)
51. [Understanding the Lethal Trifecta of AI Agents](https://www.osohq.com/learn/lethal-trifecta-ai-agent-security)
