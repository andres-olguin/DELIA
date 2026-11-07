# Issue #16 — comportamiento de detección y enmascaramiento

Paso 4 de la fase 2. La [investigación de formatos](ISSUE_16_FORMATOS_Y_FUENTES.md)
define la base de estas decisiones de diseño. El paso 5 convertirá la
especificación en casos sintéticos con tipos e intervalos esperados.

## Contrato de salida

`detect(text)` devuelve hallazgos `Finding(type, start, end)` ordenados por
posición y sin solapes. Los índices se refieren a caracteres del texto original
con inicio inclusivo y fin exclusivo. `redact(text)` reemplaza cada intervalo
por `[[TIPO]]` y devuelve el texto enmascarado junto con los mismos hallazgos.
Las etiquetas, comillas y signos externos al identificador se conservan. El
intervalo incluye el complemento y la extensión de una CI cuando se reconocen
como parte del valor.

Los cuatro tipos nuevos son `CURP`, `RFC`, `CI_BO` y `NIT_BO`. Las etiquetas
existentes, entre ellas `CEDULA` y `NIT` de Colombia, conservan sus contratos.
`LoggedSession` seguirá usando el texto devuelto por `redact()` para el cuerpo
de la solicitud.

## Reglas por tipo

| Tipo | Requisitos para enmascarar | Contexto |
|---|---|---|
| `CURP` | 18 caracteres con los bloques del paso 3. Cuatro letras iniciales con vocal o `X` en segunda posición, fecha real, marcador `H/M/X`, lugar del catálogo acordado, tres consonantes internas, diferenciador y dígito final. Para la fecha, un diferenciador numérico usa 1900–1999 y uno alfabético usa 2000–2099 como ventanas del detector. | Basta la estructura completa de un valor independiente. |
| `RFC` | Bloque inicial de 3 o 4 caracteres entre `A–Z`, `Ñ` y `&`, fecha AAMMDD posible y tres caracteres alfanuméricos. Una fecha es posible si existe en 1900–1999 o 2000–2099, dado que el RFC solo incluye dos cifras del año. Las dos claves genéricas se tratan aparte. | Basta la estructura completa de un valor independiente. |
| `CI_BO` | Raíz de 5 a 10 dígitos, con complemento de dos caracteres alfanuméricos tras guion cuando aparezca y extensión opcional. | Exige `CI`, `C.I.`, `CI Bolivia`, `CI BO` o `cédula boliviana` como etiqueta inmediata. La etiqueta genérica `cédula` conserva su uso actual. |
| `NIT_BO` | Secuencia continua de 8 a 13 dígitos. Las terminaciones de emisión del paso 3 sirven para estratificar las pruebas, mientras que la detección admite también otras terminaciones con el contexto indicado. | Exige `NIT Bolivia`, `NIT BO`, `NIT boliviano` o `NIT` como etiqueta inmediata. Con `NIT` sin país, la secuencia continua es la señal de formato boliviano de DELIA. El NIT colombiano con guion y dígito verificador conserva su regla. |

La validación de CURP y RFC se limita al formato y al calendario. El cálculo de
sus verificadores y la comprobación de titularidad o inscripción quedan fuera
del alcance inicial descrito en el paso 3. Los dos RFC genéricos del SAT,
`XAXX010101000` y `XEXX010101000`, se conservan tal cual y no producen hallazgo
`RFC`, incluso si vienen etiquetados. Son claves públicas de uso compartido y el
objetivo de esta regla es proteger identificadores de titulares. El corpus
revisado los tratará como negativos deliberados.

## Contexto e intervalos

- Admitir etiquetas y valores sin distinguir mayúsculas de minúsculas. Usar
  dígitos ASCII y conservar los ceros iniciales. Evaluar una copia normalizada
  del candidato y calcular el intervalo sobre el texto original.
- La etiqueta boliviana debe preceder al valor en la misma línea. Admitir un
  espacio o tabulador, o un separador `:`, `=` o `#` con espacios opcionales.
  Admitir comillas dobles en claves y valores, como en un cuerpo JSON serializado.
  La etiqueta debe ser completa y el separador debe estar presente, de modo que
  una palabra que contenga `CI` o `NIT` y un rótulo en otra línea no activen la regla.
- Para CI, un tramo `-XY` de dos caracteres alfanuméricos unido a la raíz
  se enmascara completo. Si ambos caracteres coinciden con una abreviatura
  departamental, como `SC`, la misma salida sirve para ambas interpretaciones.
  Si hay un segundo tramo departamental, capturarlo también. Los códigos
  admitidos tras un espacio o después del complemento son `BE`, `CB`, `CH`,
  `LP`, `OR`, `OU`, `PD`, `PT`, `SC` y `TJ`. Es una lista operativa de
  DELIA basada en las abreviaturas de expedición de AJ y en la variante `OR`
  de la nomenclatura del SENASAG. Admitir espacio horizontal o guion antes del
  tramo departamental.
  [AJ, tabla del campo de expedición](https://aj.gob.bo/uploads/docs/doc_20220622_093444.pdf) ·
  [SENASAG, manual SINAVE](https://www.senasag.gob.bo/index.php/institucional/unidades-organizacionales/unidad-nacional-de-sanidad-animal/area-nacional-de-epidemiologia-veterinaria?download=3127%3Amanual-sinave)
- Impedir coincidencias parciales dentro de palabras, secuencias más largas o
  valores con sufijos unidos no admitidos. En RFC, tratar `&` como carácter
  del candidato al verificar los límites. No permitir que un número demasiado
  largo entre por recorte a 10 o 13 dígitos.
- La fecha del candidato se comprueba con calendario. Las ventanas de año son
  convenciones para detección y admiten, por ejemplo, el 29 de febrero de 2000
  cuando la variante permite ese siglo. No se contrasta la fecha con un padrón.

## Precedencia

Conservar el orden actual por inicio más temprano y, al compartir inicio, por
intervalo más largo. Un identificador mexicano dentro de un correo reconocido
queda cubierto por el enmascaramiento del correo completo. Cuando un `CI_BO`
o `NIT_BO` contextual y una regla existente produzcan **el mismo inicio y fin**,
gana la categoría respaldada por la etiqueta. Esto resuelve, por ejemplo, un
NIT de 13 dígitos que también pasa Luhn. Si solo coincide una regla existente,
aplica el comportamiento actual, aunque el rótulo sugiera otro tipo.

## Casos para el corpus y las pruebas

Los ejemplos siguientes expresan salidas esperadas una vez implementado el
diseño. Las cadenas numéricas se eligieron para los casos de prueba y no se
vincularon a personas ni se consultaron en padrones.

| Entrada | Salida esperada | Qué cubre |
|---|---|---|
| `CURP: AEXZ000229XQOBCDZ7` | `CURP: [[CURP]]` | Marcador `X`, código `QO` y fecha bisiesta. |
| `CURP: AEXZ000229XQOBCD07` | Sin hallazgo nuevo | Diferenciador numérico y fecha imposible en 1900. |
| `RFC: A&Z0002291A2` | `RFC: [[RFC]]` | Persona moral, `&` y fecha posible en 2000. |
| `RFC: XAXX010101000` | Sin hallazgo nuevo | Clave genérica pública. Repetir con la clave genérica extranjera. |
| `"ci": "12345678-2B SC"` | `"ci": "[[CI_BO]]"` | Contexto JSON, complemento y extensión. |
| `Pedido 12345678-2B` | Sin hallazgo nuevo | Número parecido sin etiqueta de identidad. |
| `NIT BO: 1234567890128` | `NIT BO: [[NIT_BO]]` | Límite superior y colisión exacta con tarjeta. |
| `NIT: 800197268-4` | `NIT: [[NIT]]` | Regresión del NIT colombiano. |
| `NIT: 12345678901234` | Sin hallazgo nuevo | Exceso de longitud para `NIT_BO`. |
| `NIT:\n12345018` con salto real | Sin hallazgo nuevo | El contexto no atraviesa líneas. |

El corpus histórico conserva sus etiquetas para reproducir la medición inicial.
En el corpus del paso 5 se revisarán los positivos genéricos de RFC y los
negativos de CURP que solo dependían de la ausencia de una etiqueta. Un valor
completo que satisfaga la forma de CURP seguirá siendo candidato dentro de una
referencia de inventario. Añadir casos negativos con fecha, caracteres o límites
inválidos y medir los falsos positivos estructurales como limitación del diseño.

La comprobación inicial se ejecutó con
`.venv/bin/python -m pytest -q tests/test_pii.py` y obtuvo **6 pruebas aprobadas**.
También se comprobó que el detector actual clasifica la cadena sintética de
13 dígitos de la tabla como `TARJETA`. Los ejemplos de salida nueva quedan como
criterios de aceptación para la implementación.
