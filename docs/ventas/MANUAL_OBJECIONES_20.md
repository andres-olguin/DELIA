# DELIA — Manual de veinte objeciones comerciales

**Corte:** 31/10/2026 · **Objetivo:** respuestas correctas que no exageren capacidades ni invoquen multas sin causalidad. Si una objeción es una condición eliminatoria, retirarse de la oportunidad.

## 1. Ya utilizamos Cloudflare AI Gateway

**Respuesta recomendada:** Reconocerlo: si DLP/observabilidad resuelve el riesgo, DELIA no agrega valor. Proponer benchmark sintético RUT/NIT/RFC cuando exista código seguro.

**Evidencia para contrastar / referencia:** https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 2. LiteLLM es gratis

**Respuesta recomendada:** OSS tiene coste cero de licencia pero hosting/mantenimiento; no equiparar gratuidad con falta de controles. Calcular costo total y precisión regional.

**Evidencia para contrastar / referencia:** https://www.litellm.ai/pricing.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 3. Presidio detecta datos personales

**Respuesta recomendada:** Correcto, es extensible. Una mejora local solo sería válida si mide más precisión o menos trabajo de mantenimiento.

**Evidencia para contrastar / referencia:** https://microsoft.github.io/presidio/supported_entities/.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 4. Ya pagamos Microsoft Purview

**Respuesta recomendada:** Preguntar qué productos y flujos cubre la licencia existente; no añadir middleware sin brecha.

**Evidencia para contrastar / referencia:** https://learn.microsoft.com/en-us/purview/data-security-posture-management-setup.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 5. AWS Bedrock ya tiene guardrails

**Respuesta recomendada:** Comparar reglas realmente usadas y límites, no oponerlos sin test.

**Evidencia para contrastar / referencia:** https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 6. Google Model Armor es muy barato

**Respuesta recomendada:** Reconocer precio oficial y plan gratis; benchmark antes de hablar de ventaja.

**Evidencia para contrastar / referencia:** https://cloud.google.com/security/products/model-armor.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 7. No podemos instalar proxy de tercero

**Respuesta recomendada:** No solicitar datos reales; evaluar solo diseño privado en futuro tras auditoría. Hoy no está listo.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/docs/INTELIGENCIA_MERCADO_GO_TO_MARKET_CL_MX_CO_BO_2026-10-31.md.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 8. No tienen SOC 2 / ISO 27001

**Respuesta recomendada:** Confirmar que DELIA no posee certificación verificada. Si es requisito obligatorio, descartar oportunidad por ahora.

**Evidencia para contrastar / referencia:** https://www.iso.org/standard/27001.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 9. No muestran resultados de precisión

**Respuesta recomendada:** Reconocer que faltan benchmarks ejecutados; especificar dataset sintético y métricas antes de demo productiva.

**Evidencia para contrastar / referencia:** https://microsoft.github.io/presidio/supported_entities/.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 10. Regex da falsos positivos

**Respuesta recomendada:** Sí. Medir precision y recall por categoría, contexto y formato; no prometer 100 %.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/backend/dlp/pii.py.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 11. ¿Soportan CURP y RFC hoy?

**Respuesta recomendada:** No: reglas MX no presentes en pi i.py revisado. Proponer validación de necesidad y pruebas futuras.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/backend/dlp/pii.py.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 12. ¿Soportan CI/NIT Bolivia?

**Respuesta recomendada:** No hay detectores bolivianos verificados en main; se incluyen como roadmap potencial.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/backend/dlp/pii.py.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 13. ¿Cifran y restablecen datos?

**Respuesta recomendada:** No hay bóveda/cifrado reversible implementados en el código revisado; un estudio de tokenización no es producto.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/research/TALIA_%20evaluaci%C3%B3n%20t%C3%A9cnica%20del%20modelo%20de%20datos%20basado%20en%20tokens%20para%20la%20protecci%C3%B3n%20de%20datos%20sensibles.md.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 14. ¿Aseguran cumplimiento de ley?

**Respuesta recomendada:** No. Es una obligación organizacional; cualquier control sería complementar al marco legal y contrato.

**Evidencia para contrastar / referencia:** https://cancilleria.gov.co/normograma/compilacion/docs/circular_superindustria_0002_2024.htm.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 15. ¿Puedo probar con datos de clientes?

**Respuesta recomendada:** Por ahora no: hay P0 de autenticación, almacenamiento de texto y conexión de sanitización.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/app/main.py.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 16. ¿Ofrecen streaming y fallback?

**Respuesta recomendada:** No están implementados y verificados en main; solo previstos en roadmap.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/docs/roadmap.md.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 17. ¿Qué SLA ofrecen?

**Respuesta recomendada:** No hay SLO/SLA demostrado ni acuerdo operativo; no se ofrece disponibilidad garantizada.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/docs/roadmap.md.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 18. ¿Cómo calculan precio y ROI?

**Respuesta recomendada:** Se usan supuestos editables y gastos reales que el cliente comparta; no usar multas de otras empresas como ahorro.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/docs/MODELO_FINANCIERO_EDITABLE_RONDA2.csv.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 19. ¿Quién mantiene los logs?

**Respuesta recomendada:** En producción aún no hay esquema seguro demostrado; definir retención mínima, acceso por tenant, borrado y evidencias antes de piloto.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/app/models.py.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## 20. ¿Por qué pagarían por algo sin clientes?

**Respuesta recomendada:** No corresponde solicitar compra de seguridad crítica hoy. Entrevistar y validar caso de uso, luego piloto limitado solo si hay P0 resueltos.

**Evidencia para contrastar / referencia:** https://github.com/andres-olguin/DELIA/blob/main/docs/ESTUDIO_RONDA2_PROFUNDIZACION_COMERCIAL_2026-10-31.md.

**Acción interna:** registrar en CRM categoría, si se demostró la objeción, qué prueba permitiría resolverla y si se debe descartar la cuenta.

## Principios finales

- La versión actual tiene importaciones inconsistentes, logs con texto personal y falta de controles efectivos en el proxy. No solicitar datos productivos.
- «No verificado» no significa «el competidor no lo tiene».
- Si no existe comprador, presupuesto o problema real, cerrar contacto cordialmente.
