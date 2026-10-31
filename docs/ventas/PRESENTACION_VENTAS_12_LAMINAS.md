# DELIA — Guion de presentación comercial (12 láminas)

**Uso:** reunión de descubrimiento / propuesta técnica exploratoria, no venta de controles aún no terminados. Fecha 31/10/2026. Ninguna cifra interna es caso de cliente verificado.

## Lámina 1 — Portada
**Título:** DELIA — control de información en integraciones con IA.  
**Texto:** «Un proyecto de MasterTech SpA. Estamos validando un enfoque técnico para gobernar llamadas a LLM con criterios locales y evidencia».  
**Visual sugerido:** aplicación → punto de decisión → proveedor LLM, con bloque de validación aún en construcción.  
**Nota:** decir explícitamente «investigación y desarrollo».

## Lámina 2 — Problema operativo
**Título:** La IA introduce nuevas salidas de datos.  
**Texto:** «Una integración puede enviar identificadores, textos de clientes, presupuestos o información comercial a servicios externos. ¿Qué controles se aplican y quién responde por ellos?».  
**Pregunta:** «¿En qué flujos ya ocurre esto en su empresa?».

## Lámina 3 — Soluciones actuales
**Título:** La mayoría de equipos no parte de cero.  
**Texto:** «Cloudflare, LiteLLM, Portkey, Presidio, Azure, AWS y Google ofrecen controles, observabilidad o DLP».  
**Mensaje:** «No buscamos reemplazar controles suficientes. Investigamos carencias verificables».  
**Fuente:** [competidores oficiales](../ESTUDIO_RONDA2_PROFUNDIZACION_COMERCIAL_2026-10-31.md).

## Lámina 4 — Problemas latinoamericanos concretos
**Título:** La detección debe funcionar con identificadores locales.  
**Texto:** «RUT (Chile), NIT/cédula (Colombia), RFC/CURP (México), CI/NIT (Bolivia); precisión y falsos positivos por medir».  
**Estado:** «Solo categorías parciales CL/CO existen en el código».

## Lámina 5 — Visión del producto
**Título:** DELIA como capa de política entre aplicación y LLM.  
**Texto:** «Objetivo de producto: clasificación, decisión permitir/enmascarar/bloquear, auditoría mínima, límites y costo».  
**Estado visible:** «Arquitectura objetivo; no toda implementada».

## Lámina 6 — Estado del prototipo
**Título:** Lo que podemos mostrar responsablemente.  
**Texto:** «Código de detección/redacción de PII y casos de prueba escritos. Importaciones, autenticación y conexión al proxy presentan brechas P0».  
**Prohibición:** no afirmar tests pasados sin ejecución.

## Lámina 7 — Caso de uso 1
**Título:** Integrador de agentes para varias empresas.  
**Texto:** «¿Cómo mantener políticas específicas por cliente sin replicar componentes?».  
**Criterio futuro:** tiempo de integración y separación de datos medidos.

## Lámina 8 — Caso de uso 2
**Título:** Asistente contable/RR.HH.  
**Texto:** «¿La API del LLM necesita todos los identificadores presentes en una factura o contrato?».  
**Criterio futuro:** reducción comprobable de campos expuestos, errores y cobertura.

## Lámina 9 — Seguridad y privacidad
**Título:** Sin auditoría del control, no hay confianza.  
**Texto:** «Rutas, autentificación, secretos, errores, política de logs y retención deben verificarse antes de tratar datos reales».  
**Advertencia:** DELIA aún no cumple este gate.

## Lámina 10 — ¿En qué se diferenciaría?
**Título:** Cinco hipótesis comprobables.  
**Texto:** «IDs regionales; políticas por tenant; despliegue privado; evidencia auditable; onboarding y soporte en español».  
**Métrica:** benchmark con Presidio, Cloudflare y Model Armor y coste de despliegue.

## Lámina 11 — Validación propuesta
**Título:** Conversación → benchmark sintético → piloto controlado.  
**Texto:** «Entrevista; umbrales y flujos de alto valor; sin datos de clientes; corregir riesgos P0; acuerdo escrito y piloto pagado si corresponde».  
**Precio:** cotización caso por caso, sin lista definitiva.

## Lámina 12 — Próximo paso
**Título:** Queremos aprender de su situación real.  
**Texto:** «¿Qué API LLM usan? ¿Qué control tienen? ¿Qué falta? Si no existe brecha, lo registraremos y no insistiremos».  
**CTA:** entrevista de 30 min con arquitectura/seguridad, no demo de seguridad de producción.  
**Contacto:** contacto@mastertechg.com / mastertechg.com.

---

### Instrucciones del presentador
- No usar logos de empresas prospectadas como clientes.
- No afirmar ahorros, precisión, SLA, certificaciones, casos pagados ni cumplimiento de DELIA.
- Mostrar cifras de incidentes solo con fuente y contexto; jamás atribuir prevención de incidentes al producto.
- Adaptar la lámina 7 u 8 al segmento, sin inventar aplicaciones del prospecto.
- Registrar objeciones y herramientas actuales en CRM privado, no en GitHub público.
