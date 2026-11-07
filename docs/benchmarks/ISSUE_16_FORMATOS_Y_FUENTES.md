# Issue #16 — formatos, fuentes y límites de validación

Fecha de consulta: 7 de noviembre de 2026 (America/Santiago).

Investigación del paso 3 de la fase 2. Este documento separa evidencia oficial,
inferencias de ingeniería y puntos pendientes. No cambia el detector, el corpus
ni sus etiquetas. No certifica identidad, vigencia o inscripción en un padrón.

## Fuentes consultadas

| ID | Fuente primaria | Acceso y utilidad |
|---|---|---|
| MX-1 | [SEGOB/SRE: instructivo CURP, texto con reforma de 18-10-2021](https://sre.gob.mx/component/phocadownload/category/2-marco-normativo?download=1116:instructivo-normativo-para-la-asignacion-de-la-clave-unica-de-registro-de-poblacion-dof-18-10-2021-texto-vigente) | PDF consultado; estructura y asignación. La leyenda de vigencia es la del documento, no una certificación de ausencia de reformas posteriores. |
| MX-2 | [SEGOB: modificación del instructivo de 18-10-2021](https://sidof.segob.gob.mx/notas/docFuente/5632965) | Texto consultado; incluye CURP temporal. |
| MX-3 | [SEGOB: instructivo histórico y catálogo CURP](https://ordenjuridico.gob.mx/Federal/PE/APF/APC/SEGOB/Instructivos/InstructivoNormativo.pdf) | Extractos oficiales indexados; referencia histórica, no prevalece automáticamente sobre normas posteriores. |
| MX-4 | [SAT: estructura de la clave RFC](https://wwwmat.sat.gob.mx/cs/Satellite?blobcol=urldata&blobkey=id&blobtable=MungoBlobs&blobwhere=1461176322651&ssbinary=true) | PDF de dos páginas consultado; personas físicas y morales. |
| MX-5 | [SAT: anexo técnico con patrones RFC](https://wwwmatnp.sat.gob.mx/cs/Satellite?blobcol=urldata&blobkey=id&blobtable=MungoBlobs&blobwhere=1705376561155&ssbinary=true) | Extractos oficiales indexados; caracteres y longitudes. Una fila física presenta una máscara abreviada inconsistente con su longitud; contrastar con MX-4. |
| MX-6 | [SAT: verifica si estás registrado en el RFC](https://wwwmat.sat.gob.mx/aplicacion/29073/verifica-si-estas-registrado-en-el-rfc) | Descripción oficial indexada; distingue inscripción de forma local. No se consultaron identificadores. |
| MX-7 | [DOF: publicación de 23-01-2026, tabla de mapeo CURP](https://dof.gob.mx/2026/GOBERNACION/SG_230126_VES_01.pdf) | Tabla indexada; contiene una discrepancia con MX-3 que se registra abajo. |
| BO-1 | [SEGIP: Decreto Supremo 4861 de 11-01-2023](https://www.segip.gob.bo/fuent/2025/09/Decreto-Supremo-N%C2%B0-4861-de-11-de-enero-de-2023.pdf) | Extractos oficiales indexados; apertura directa devuelve 403. |
| BO-2 | [SEGIP: reglamento al DS 4861](https://www.segip.gob.bo/fuent/2025/09/REGLAMENTO-AL-D.S.-N%C2%B04861-Y-AUTORIZA-LA-ENTRADA-EN-VIGENCIA-Y-OPERACION-PLENA-DE-LA-C.I.-Y-LA-LICENCIA-PARA-CONDUCIR-EN-FORMATO-DIGITAL.pdf) | Artículo 15 indexado; apertura directa devuelve 403. |
| BO-3 | [SIN: generación del NIT](https://siatinfo.impuestos.gob.bo/index.php/requisitos-para-la-inscripcion/conceptos-generales/generacion-del-nit) | Texto oficial indexado; apertura directa devuelve 502 o timeout. |
| BO-4 | [SIN: campos de factura alcanzada por ICE](https://siatinfo.impuestos.gob.bo/index.php/facturacion-en-linea/archivos-xml-xsd-de-facturas-electronicas/factura-alcanzada-por-ice) | Tabla oficial indexada; apertura directa devuelve timeout. Describe número y complemento como campos separados. |
| BO-5 | [SIN: generación del CUF](https://siatinfo.impuestos.gob.bo/images/archivos_tecnicos/archivos_apoyo/GENERACION-CUF.pdf) | Extractos oficiales indexados; distingue representación del NIT dentro del CUF y verificador del CUF. |

Los errores de apertura limitan la revisión íntegra de documentos bolivianos.
Los extractos indexados aportan evidencia puntual; no se afirma haber leído el
PDF completo ni todos los anexos de una página inaccesible.

## CURP — México

MX-1 describe una clave de 18 caracteres: posiciones 1–4 derivadas de nombres y
apellidos; 5–10 fecha AAMMDD; 11 sexo H/M en ese texto; 12–13 lugar de nacimiento;
14–16 consonantes internas; 17 diferenciador de siglo/homonimia; 18 verificador
numérico. Su posición 17 usa 0–9 hasta 1999 y A–J desde 2000.

Implicaciones técnicas propuestas, todavía sin implementar:

- Verificar fecha real con calendario, no solo mes y día por regex.
- Usar un catálogo explícito para el lugar y documentar excepciones de letras.
- No atribuir una CURP a una persona a partir de su estructura.
- MX-1 menciona el algoritmo verificador, pero no se obtuvo su fórmula operativa
  en esta revisión. No presentar como oficial una fórmula recordada o de terceros.

Discrepancias pendientes: MX-3 histórico permite A–Z en la posición 17. Además,
su catálogo identifica Querétaro con QT, mientras MX-7 muestra QO. MX-7 aclara que
XX es un valor auxiliar de desconocido y no parte de la CURP oficial. No copiar
una tabla reciente sin contrastar su finalidad y la fuente de emisión.

MX-2 contempla CURP temporal. Debe determinarse si el alcance inicial cubre sus
variantes y las excepciones actuales; no inferirlas de ejemplos del corpus.

## RFC — México

MX-4 confirma 13 caracteres para persona física y 12 para persona moral. La
primera usa cuatro caracteres iniciales, la segunda tres; siguen fecha AAMMDD y
tres caracteres diferenciadores. La fecha de persona moral corresponde a su
constitución. El SAT asigna la homoclave.

MX-5 admite A–Z, Ñ y & en el bloque inicial y caracteres alfanuméricos en el final.
Su fila de persona física debe contrastarse: declara longitud 13 pero muestra
una máscara con solo tres letras iniciales. MX-4 permite resolver la longitud.

Implicaciones técnicas propuestas:

- Soportar ambas longitudes; el corpus actual no demuestra variedad suficiente.
- Validar fechas sin elegir el siglo mediante un umbral arbitrario de `strptime`.
- Tratar Ñ y & explícitamente, incluidos límites de coincidencia alrededor de &.
- Investigar por separado los RFC genéricos y la fórmula del verificador antes
  de exigirlos o declararlos validados. No se cerró esa parte de la investigación.
- MX-6 ofrece verificación de inscripción: una regex local no reemplaza esa
  comprobación, y este issue no consultará datos de personas en ese servicio.

## CI — Bolivia

BO-1 y BO-2 reconocen número de CI y código complemento cuando corresponda.
BO-2 separa además número de serie y sección: no son automáticamente parte del
identificador que debemos detectar. BO-4 describe el complemento alfanumérico
como el valor asignado por SEGIP para números duplicados y lo separa del número.

Implicaciones técnicas propuestas:

- Contemplar número con y sin complemento; no confundir complemento y sufijo
  departamental, como `SC` en el corpus actual.
- Exigir contexto de identidad como opción de diseño para evitar detectar pedidos
  o inventario. La forma exacta de ese contexto corresponde al paso 4.
- No establecer todavía una longitud oficial universal, lista de complementos,
  catálogo de expedición o algoritmo verificador: no están confirmados aquí.
- Un límite de captura escogido para rendimiento debe rotularse como límite de
  DELIA y medirse; no atribuirlo a SEGIP sin fuente.

## NIT — Bolivia

BO-3 describe generación para persona natural nacida en Bolivia y empresa
unipersonal a partir de CI + 01 + un dígito aleatorio de 1 a 9. Para personas
jurídicas describe terminación 02 + un dígito aleatorio de 1 a 9; para persona
natural nacida en el extranjero con CI de extranjero describe terminación 04 +
un dígito aleatorio de 1 a 9. Esto no acredita que todos los NIT históricos
deban rechazarse si no siguen esos sufijos.

BO-5 usa un campo numérico de longitud 13 dentro del CUF y ordena completar sus
campos. Eso no demuestra que cada NIT tenga exactamente 13 dígitos impresos.
El módulo 11 descrito allí corresponde al CUF completo, no demuestra un
verificador del NIT aislado.

Implicaciones técnicas propuestas:

- Mantener separado `NIT_BO` del `NIT` colombiano y su función `nit_dv`.
- No asumir longitud fija de 10 por los ejemplos actuales del dataset.
- Documentar rango admitido, variantes históricas y contexto antes de programar.
- No rechazar por un supuesto checksum boliviano sin evidencia.

## Pendientes antes de cerrar la especificación de comportamiento

| Punto | Trabajo necesario | Consecuencia si no se confirma |
|---|---|---|
| Verificadores CURP/RFC | Obtener fórmula y vectores de una fuente primaria verificable. | Rotular validación estructural y límites; no afirmar checksum oficial implementado. |
| CURP, siglo y catálogo | Resolver divergencias A–J/A–Z y QT/QO según fuente y alcance. | Evitar una exclusión estricta basada en una tabla incongruente. |
| RFC genéricos | Confirmar variantes y política de detección/enmascaramiento. | No usarlos como únicos ejemplos ni omitir excepciones sin documentarlas. |
| CI boliviana | Confirmar longitudes, complemento y expedición en fuentes técnicas accesibles. | Cualquier subconjunto soportado debe quedar explícito, sin llamarlo universal. |
| NIT boliviano | Contrastar representación, longitudes y cobertura histórica. | No imponer al corpus completo los sufijos de una guía de generación actual. |
| Contexto y solapes | Definir política reproducible para números ambiguos y colisiones. | Es una decisión de ingeniería del paso 4, no una regla de las autoridades. |

El paso 3 tiene evidencia inicial para las cuatro categorías, pero conserva los
pendientes anteriores. No se declara una especificación oficial exhaustiva ni
se da por completada la fase 2. Se seguirá investigando lo necesario al concretar
el alcance; no se empezará a implementar reglas que dependan de suposiciones.

## Comprobación y cambios

Solo se añade este documento. No se modificaron código, dependencias, corpus ni
contratos TALIA/DELIA. No se consultaron identidades ni se copiaron ejemplos de
personas desde las fuentes. Las pruebas del detector y el benchmark no se
repitieron: esta entrega no cambia su comportamiento.
