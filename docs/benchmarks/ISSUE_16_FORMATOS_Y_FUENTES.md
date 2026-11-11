# Issue #16 — formatos, fuentes y límites de validación

Fecha de consulta: 7 de noviembre de 2026 (America/Santiago).

Resultado del paso 3 de la fase 2. Las fuentes describen la estructura de las
claves y sus variantes. El alcance inicial de DELIA es identificar candidatos
para enmascarar en texto, mediante comprobaciones locales de formato.

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
| MX-8 | [INE: acuerdo sobre reconocimiento de personas no binarias](https://sidof.segob.gob.mx/notas/docFuente/5686070) | El acuerdo reporta CURP emitidas por RENAPO con `X` en el marcador. |
| MX-9 | [SAT: regla de RFC genéricos en CFDI](https://wwwmat.sat.gob.mx/articulo/16302/regla-2.7.1.26) | Documenta las dos claves genéricas de facturación. |
| BO-1 | [SEGIP: Decreto Supremo 4861 de 11-01-2023](https://www.segip.gob.bo/fuent/2025/09/Decreto-Supremo-N%C2%B0-4861-de-11-de-enero-de-2023.pdf) | Extractos oficiales indexados; apertura directa devuelve 403. |
| BO-2 | [SEGIP: reglamento al DS 4861](https://www.segip.gob.bo/fuent/2025/09/REGLAMENTO-AL-D.S.-N%C2%B04861-Y-AUTORIZA-LA-ENTRADA-EN-VIGENCIA-Y-OPERACION-PLENA-DE-LA-C.I.-Y-LA-LICENCIA-PARA-CONDUCIR-EN-FORMATO-DIGITAL.pdf) | Artículo 15 indexado; apertura directa devuelve 403. |
| BO-3 | [SIN: generación del NIT](https://siatinfo.impuestos.gob.bo/index.php/requisitos-para-la-inscripcion/conceptos-generales/generacion-del-nit) | Texto oficial indexado; apertura directa devuelve 502 o timeout. |
| BO-4 | [SIN: campos de factura alcanzada por ICE](https://siatinfo.impuestos.gob.bo/index.php/facturacion-en-linea/archivos-xml-xsd-de-facturas-electronicas/factura-alcanzada-por-ice) | Tabla oficial indexada; apertura directa devuelve timeout. Describe número y complemento como campos separados. |
| BO-5 | [SIN: generación del CUF](https://siatinfo.impuestos.gob.bo/images/archivos_tecnicos/archivos_apoyo/GENERACION-CUF.pdf) | Extractos oficiales indexados; distingue representación del NIT dentro del CUF y verificador del CUF. |
| BO-6 | [ASFI: boletín normativo 29, septiembre de 2015](https://www.asfi.gob.bo/sites/default/files/2025-08/Bolet%C3%ADn%2029%20-%20Septiembre%202015.pdf) | Aclaración de SEGIP sobre los dos caracteres del complemento. |
| BO-7 | [ASFI: boletín normativo 50, diciembre de 2020](https://www.asfi.gob.bo/sites/default/files/2025-08/Bolet%C3%ADn%2050%20-%20Diciembre%202020.pdf) | La definición para el reporte crediticio distingue raíz, complemento y extensión departamental. |
| BO-8 | [SEGIP: Reglamento del Registro Único de Identificación Personal, copia en la OMS](https://platform.who.int/docs/default-source/mca-documents/policy-documents/law/BOL-CC-55-01-LAW-2018-esp-REGLAMENTO-DEL-REGISTRO-UNICO-DE-IDENTIFICACION-PERSONAL-LO-%C3%9ALTIMO-ENERO-2018.pdf) | El artículo 40 describe el guion que separa el complemento visible del número raíz. |
| BO-9 | [SIN: esquema de facturación de boleto aéreo](https://siatanexo.impuestos.gob.bo/index.php/documentos-fiscales-digitales/archivos-xml-xsd-de-facturas-electronicas/boleto-aereo) | La tabla oficial indexada especifica un máximo de 13 dígitos en campos de NIT. |

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
- Admitir `H`, `M` y `X` en el marcador. La `X` está respaldada por los casos
  que reporta MX-8.
- Comprobar que el último carácter sea numérico. La fórmula del verificador
  queda fuera del alcance inicial porque no se confirmó en una fuente primaria.

Para detección se aceptará el rango de letras A–Z de MX-3 en la posición 17,
además de los dígitos. Es una decisión de cobertura de DELIA ante la diferencia
con A–J en MX-1. Para el lugar se tomará el catálogo de MX-3 y se incluirá `QO`
como variante de detección de `QT` para Querétaro, dada la tabla de mapeo de
MX-7. `XX` queda fuera porque MX-7 lo documenta como valor auxiliar externo a la
CURP. Estas decisiones evitan perder candidatos por diferencias entre fuentes.

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
- Registrar `XAXX010101000` y `XEXX010101000` como claves genéricas de CFDI,
  según MX-9. Sus etiquetas como casos de detección se definirán en el paso 4.
- Comprobar formato y fecha. La fórmula del verificador queda fuera del alcance
  inicial porque no se confirmó en una fuente primaria. MX-6 describe un
  servicio distinto para comprobar inscripción.

## CI — Bolivia

BO-1 y BO-2 reconocen número de CI y código complemento cuando corresponda.
BO-2 distingue el número de serie y la sección del número de CI. BO-4 separa
el campo del complemento, BO-6 precisa que ocupa dos caracteres alfanuméricos
y BO-8 documenta el guion que lo separa del número raíz cuando aparece impreso.
BO-7 respalda una extensión departamental cuando consta en el documento. Esa
extensión y el complemento representan campos distintos.

Implicaciones técnicas propuestas:

- Contemplar raíz numérica, complemento opcional de dos caracteres después de
  un guion y extensión departamental opcional. El paso 4 definirá cómo se
  interpretan sufijos ambiguos como `SC` y cómo se conserva el intervalo completo.
- Adoptar **5 a 10 dígitos** para la raíz como rango inicial de captura de DELIA.
  La evidencia consultada no fija un rango universal de emisión. Medir los dos
  límites y los casos fuera de rango en el corpus sintético.

## NIT — Bolivia

BO-3 describe generación para persona natural nacida en Bolivia y empresa
unipersonal a partir de CI + 01 + un dígito aleatorio de 1 a 9. Para personas
jurídicas describe terminación 02 + un dígito aleatorio de 1 a 9; para persona
natural nacida en el extranjero con CI de extranjero describe terminación 04 +
un dígito aleatorio de 1 a 9. Esto no acredita que todos los NIT históricos
deban rechazarse si no siguen esos sufijos.

BO-5 usa un campo numérico de longitud 13 dentro del CUF y ordena completar sus
campos. BO-9 respalda un máximo de 13 dígitos en su esquema de facturación.
El módulo 11 de BO-5 se aplica a la cadena del CUF antes de su codificación.

Implicaciones técnicas propuestas:

- Adoptar **8 a 13 dígitos** como rango inicial de DELIA. El mínimo se deriva
  del piso de 5 dígitos de CI más los tres de la variante personal descrita en
  BO-3. El máximo se toma de BO-9. Es un rango de detección, con cobertura
  histórica sin confirmar.
- Mantener separado `NIT_BO` del `NIT` colombiano. Reconocer los sufijos de
  BO-3 como variantes documentadas y conservar la cobertura de otras terminaciones
  cuando el contexto identifique un NIT boliviano. El paso 4 definirá ese contexto.

## Base para el paso 4

El paso 3 termina con una base de validación estructural. Los rangos bolivianos
y la tolerancia de variantes mexicanas son decisiones iniciales de DELIA que se
evaluarán con casos sintéticos. La comprobación matemática de los verificadores
de CURP y RFC queda aplazada hasta contar con fórmula y vectores de referencia.
El paso 4 definirá el contexto, la política para RFC genéricos, la precedencia
entre tipos, los límites de cada coincidencia y el enmascaramiento resultante.

## Comprobación y cambios

La revisión de este paso se limita al documento y sus fuentes. Las pruebas del
detector y el benchmark corresponden a la implementación posterior.
