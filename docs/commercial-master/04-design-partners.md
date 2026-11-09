# 04 — Programa de design partners: aprender con clientes, no usarlos como publicidad

## Definición

Design partner = organización que acepta colaborar explícitamente en evaluar un problema concreto, comparte feedback permitido y acuerda métricas y responsabilidades. **No significa cliente pagador ni alianza comercial** hasta contrato y cobro verificados. No prometer funcionalidades en desarrollo ni exigir exclusividad.

## Etapa de ingreso

1. Verificar el problema con una persona que participa en la operación.
2. Confirmar al comprador económico, alternativa y costo del problema.
3. Verificar si el compromiso es entrevista, evaluación pagada, LOI no vinculante o contrato de piloto; registrar estado exacto.
4. Revisar derechos de propiedad intelectual y uso de materiales.
5. Si hay datos/servicios externos: seguridad, legal, privacidad, contrato, autorización del dueño del sistema y runbook antes de comenzar.
6. Aplicar un contrato de experimentación de duración definida, nunca una promesa implícita de soporte 24/7.

## Paquete de evaluación propuesto (solo sandbox)

**Un proceso:** clasificación o lectura de un ticket CRM con política de límites. **Una integradora y un cliente sintético:** no compartir cuentas reales. **Plazo tentativo:** 2–4 semanas acordadas. **Artefactos:** threat model, diagrama, 3 casos permitidos y 7 denegados, salida reproducible con SHA, registro de fallos, comparación contra stack actual y recomendaciones.

### Criterios que deben pactarse antes del piloto

- Integración sin datos reales y sin escribir en CRM productivo.
- Permisos y roles de prueba, explícitos y revisados.
- Resultado de cada caso y forma de verificarlo independientemente.
- Tiempo máximo acordado para instalación con equipo del partner.
- Protocolo de incidentes, límites de responsabilidad, retención/borrado y quién controla infraestructura.
- Costo real de trabajo y entregables de cierre.
- Opción de **No-Go** gratuita en decisión comercial si la prueba muestra que DELIA no aporta valor; no tergiversar hallazgos.

## Matriz de pruebas inicial

| Caso | Esperado | Evidencia |
|---|---|---|
| Leer ticket autorizado | Permitido en entorno sintético | Identidad demo, decisión y prueba |
| Intento de exportar contactos | Denegado | No ejecutar adapter de prueba |
| Cliente B intenta leer A | Denegado | Test cross-tenant con auth real cuando exista |
| Cambian argumentos tras aprobación | Denegado | Hash/versión e idempotencia |
| La política desaparece | Falla cerrada | Test upstream mock |
| El proveedor no responde | HOLD/UNKNOWN | No reportar completado |
| El CRM confirma un resultado distinto | MISMATCH | Comparación con fuente autorizada |
| Reinicia el proceso | No duplicar efectos | Test DB/transacción por construir |
| Reintenta mismo ID | Sin doble efecto | Idempotencia durable pendiente |
| Log de auditoría | Sin PII cruda | Test de canary y retención pendiente |

## Acuerdo preliminar — lista para asesoría legal, NO contrato final

Objeto, nombres legales, NDA si aplica, alcance técnico, datos permitidos y lugar de almacenamiento, autorización de pruebas, acceso restringido, propiedad intelectual, licencias abiertas existentes, prohibición de datos sensibles sin gate, límites de responsabilidad, recursos de cada parte, cronograma, entregables, aceptación, tratamiento de incidentes, salida y borrado, pago y responsabilidades fiscales. La titularidad del software escrito por colaboradores debe verificarse y documentarse por separado.

## Reglas del programa de partner

- No regalar desarrollo bespoke ilimitado.
- No incorporar instrucciones privadas de clientes como funciones generales sin analizar IP y confidencialidad.
- No usar clientes como testimonios/logo sin permiso firmado.
- Registrar tanto los fallos como los casos aprobados.
- No declarar éxito del piloto si el comprador solo estuvo en una reunión.
- Ningún evaluador puede hacer que DELIA sea «seguro» marcando un checkbox comercial; gate técnico independiente.

## Fin del experimento

Entregar informe con versión/SHA, casos realmente ejecutados, resultados y limitaciones, tiempo de instalación, soporte consumido, comparación contra alternativa, costo total estimado, recomendación seguir/pausar/pivot y fechas de eliminación de datos. Si no hay comprador dispuesto a avanzar o pagar por una función útil, contabilizar como aprendizaje, no como pipeline firme.

## Conversión opcional

Solo luego de S3, propuesta específica con alcance, precio, soporte y contrato. Asegurar continuidad operativa y salida sin lock-in: exportar políticas/evidencias mínimas cuando esté soportado, sin revelar secretos ni datos privados.
