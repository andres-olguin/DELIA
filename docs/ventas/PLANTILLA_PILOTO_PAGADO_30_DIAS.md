# DELIA — Modelo de propuesta para piloto pagado de 30 días

**Documento de trabajo para negociación; NO es contrato listo para firmar ni asesoría legal.**  
**Fecha de plantilla:** 31/10/2026 · **Proveedor potencial:** MasterTech SpA · **Cliente:** [RAZÓN SOCIAL], [PAÍS], [ID FISCAL] · **Responsable técnico cliente:** [ROL].

> **Condición suspensiva obligatoria:** este modelo **NO debe firmarse ni ejecutarse con datos empresariales reales** mientras sigan abiertos los riesgos P0 de autenticación, autorización multitenant, almacenamiento de prompts, credenciales embebidas, importaciones incoherentes o sanitización desacoplada del proxy. La oferta de seguridad de DELIA está en investigación. El primer ensayo solo puede evaluarse **con datos completamente sintéticos**, en entorno aislado y después de revisión de seguridad.

## 1. Objetivo del piloto

**Problema observado en entrevista:** [describir evidencias propias del cliente, no supuestos].  
**Solución actual:** [gateway/DLP/observabilidad ya utilizados].  
**Hipótesis experimental:** [por ejemplo, mejorar detección RUT, NIT o gestión de flujos en escenario de laboratorio frente a baseline].  
**Comportamiento que descartaría el piloto:** [ejemplo, falsos negativos críticos, fuga o overhead inaceptable].

## 2. Alcance y exclusiones

**Dentro:** descubrimiento, análisis de arquitectura a alto nivel sin secretos, diseño de casos de prueba sintéticos, benchmark comparativo autorizado, informe de hallazgos y plan de integración condicionado a cierre de P0.  
**Fuera:** procesamiento de información real de clientes; instalación productiva; captura o acceso a credenciales; transmisión de datos a terceros; auditoría legal; garantía de cumplimiento; certificaciones; compromiso de protección exhaustiva; uso de logos como referencias públicas.  
**Dependencias:** aceptación por responsable de seguridad, privacidad y operaciones del cliente; entorno de ensayo aislado; fechas de hitos. La entrega concreta se negociará de acuerdo con capacidades realmente verificadas en `main`.

## 3. Duración y calendario propuesto

| Día | Hito | Evidencia |
|---|---|---|
| 1–3 | Acta de alcance y requisitos; aprobación de seguridad | Documento firmado por partes autorizadas |
| 4–7 | Benchmark de alternativas y corpus sintético aprobado | Lista de casos, fuente, versiones |
| 8–14 | Ejecución de herramientas instaladas y pruebas verificadas | Logs **sin PII**, resultados reproducibles |
| 15–21 | Revisión de falsos positivos/negativos, costo/latencia | Métricas y límites reales |
| 22–26 | Informe comparación y condiciones para producto | Recomendaciones y riesgos abiertos |
| 27–30 | Cierre, aceptación/rechazo de hipótesis y siguiente decisión | Acta de cierre, sin obligación de compra |

## 4. Criterios medibles (acordar antes)

| Métrica | Base | Umbral pactado | Evidencia |
|---|---|---|---|
| Precision por ID y país | Baseline contra alternativa existente | [X] (por consensuar) | Dataset sintético, TP/FP |
| Recall por ID y país | Baseline contra alternativa existente | [Y] | Dataset, FN |
| Redacción antes del egress | Línea base simulada | Ningún dato de test sensible sale sin política aprobada | Pruebas integración |
| Autenticación y autorización | Pruebas aisladas | Sin acceso transversal entre tenants en pruebas | Suite e informes |
| Latencia p50/p95 | Herramienta comparable | [Z] medido, no inventado | Instrumentación |
| Costo de ejecutar controles | Coste real de prueba | [presupuesto máximo] | Gasto documentado |
| Aceptación del cliente | Comité designado | Acta firmada, no solo comentario oral | Firma de aceptación |

**Si P0 no está resuelto, se suspenden las pruebas que requieran operar DELIA como proxy**, y el alcance se limitará a consultoría/benchmark de herramientas aisladas. No alterar de facto el alcance sin acuerdo.

## 5. Precio y pagos

**Tarifa total del piloto:** [USD/CLP/MXN/COP/BOB acordado] + impuestos si aplican.  
**Valor referencial exclusivamente para negociación:** US$300–1.500 como hipótesis del estudio, **NO tarifa vigente ni precio aceptado por comprador**.  
**Forma de pago:** [anticipo] / [entrega] / [aceptación], por acordar.  
**Gastos de nube y APIs:** [por cuenta de quién y límite por escrito].  
**Alcance adicional:** requiere orden de cambio firmada antes de ejecutar.

## 6. Cláusulas a revisión jurídica previa

1. **Confidencialidad recíproca:** acuerdos vigentes firmados y autorización para cualquier intercambio reservado; hasta entonces solo datos ficticios.
2. **Tratamiento de datos:** roles controlador/responsable/encargado, finalidad, localización, autorizaciones y obligaciones; si se proponen datos reales, firmar DPA y pasar evaluación separada.
3. **Propiedad intelectual:** código previo de ambas partes sigue siendo de su titular; especificar entregables y licencias de uso; **no** hay cesión automática.
4. **Seguridad, subprocesadores y retención:** procedimiento incidentes, límites de acceso, registros, plazos, eliminación y bloqueo en caso de riesgo.
5. **No garantía de cumplimiento:** el piloto no certifica normas ni sustituye prácticas organizacionales.
6. **Límites de responsabilidad:** negociar bajo normativa aplicable, asesoría jurídica y seguros, sin cláusulas desproporcionadas.
7. **Salida:** puede detenerse si surge fuga, incumplimiento de alcance o riesgo; protocolo de devolución/borrado de datos sintéticos y cierre financiero.
8. **Jurisdicción y resolución controversias:** acordar según país y relación contractual; no deducir jurisdicción por domicilio de MasterTech.
9. **Uso comercial y marcas:** sin permiso escrito, el nombre del cliente no se publicará como caso ni se usará en presentaciones.
10. **Aceptación y no exclusividad:** prueba de valor no implica renovación, producción, comisión, equity ni contratación laboral.

## 7. Autorización y trazabilidad

- Responsable MasterTech: [NOMBRE Y CARGO AUTORIZADOS]
- Representante cliente: [NOMBRE, CARGO Y FACULTADES POR VALIDAR]
- Fecha, versión, anexos seguridad, precio, plazo, criterios, contingencias y registros de reuniones.
- **Estado:** BORRADOR NO ENVIADO / NO APROBADO / NO FIRMADO hasta constancia documental.

**Checklist de liberación:** [ ] P0 corregidos y testeados · [ ] alcance aceptado · [ ] datos sintéticos revisados · [ ] proveedor/seguridad autorizados · [ ] contrato y DPA aprobados si aplica · [ ] facturación e impuestos revisados.
