# 05 — DELIA Partner: estrategia de distribución que multiplica instalaciones

## Por qué el canal podría superar a vender directo

Una integradora con varios clientes puede distribuir una configuración replicable. DELIA gana potencialmente con **una relación comercial que se expande a varios tenants**, y el integrador monetiza su trabajo profesional. Pero si cada implantación requiere semanas de trabajo único, el modelo se comporta como consultoría, no como SaaS escalable.

## Tipos de partners propuestos

**Referral:** introduce compradores, no implementa. Comisión limitada a negocio cobrado y cláusulas apropiadas.

**Implementation:** instala y adapta; factura servicios propios y puede revender bajo contrato. Requiere capacitación, responsabilidades claras de acceso/datos y soporte.

**MSP Managed:** administra clientes, revisa políticas y recibe tickets. Requiere observabilidad, RBAC real, facturación reconciliada, SLAs y auditoría; **no disponible actualmente**.

**OEM/Embedded:** integra el control dentro de su software. Requiere contrato de APIs, licencias y límites de marca, seguridad y soporte; no confundir MIT de componentes actuales con exclusividad sobre obras anteriores.

## El problema que DEBE resolver DELIA Partner

| Trabajo del partner | Antes (hipótesis) | Después deseado | Medida |
|---|---|---|---|
| Incorporar segundo cliente | Reescribir política/roles | Plantilla configurable con aislamiento | Horas y errores |
| Aprobar cambio en CRM | Implementación ad hoc | Contrato reusable y controles de revisión | Tiempo y bypass |
| Demostrar seguridad | Capturas y scripts sueltos | Evidencia versionada y pruebas negativas | Horas de preventa |
| Mantener conectores | Cambios sin control | Compatibilidad y tests de regresión | Incidentes por release |
| Cobrar a su cliente | Proyecto único | Mantenimiento + plataforma por tenant | Margen de partner |
| Gestionar fallos | No hay rastros homogéneos | Estado confirmado/unknown/rechazado | Tiempo a resolver |

Las columnas «Después» son funcionalidades por construir, **no entregas actuales**.

## Partners como fuente de producto

Los primeros dos partners podrían definir contratos de procesos y bundles reutilizables **con licencia/IP clara y sin compartir datos de sus clientes**. A cambio reciben prioridad en feedback y posibles condiciones fundacionales de precio aprobadas. No ceder monopolio regional o acceso exclusivo a propiedad intelectual sin análisis legal/económico.

## Economía del canal — no aprobar porcentajes sin números

Escenario de práctica: partner paga US$199 base + US$79 por tenant y US$0,005 por operación medida, con 3 tenants y 10.000 operaciones: **US$486/mes hipotéticos**. Comisión hipotética 15 %, nube US$80, soporte US$180, pago US$10: contribución mensual US$143,10 antes de estructura fija, impuestos, adquisición e ingeniería. No vender solo por ese margen: es un ejemplo de por qué soporte consume el negocio.

El mismo ejemplo es ejecutable con `python -m commercial_ops.demo`. Revisar sensibilidad de costos, soporte e infraestructura. El ingreso real para MasterTech depende del contrato y de quién paga/recibe cada comisión.

## Programa Partner v0

1. **Explorer:** descarga documentación y acepta usar entorno sintético; sin sellos de certificación.
2. **Design Partner:** co-diseña y ejecuta laboratorio con NDA/condiciones pertinentes.
3. **Delivery Partner:** ha superado criterios de instalación y QA en versiones productivas, con soporte pactado.
4. **Strategic Partner:** mantiene varios clientes, cumple renovaciones, participa en planificación y co-selling; solo cuando existan datos de uso/pago.

## Condiciones para lanzar Partner SaaS

- IAM con delegación a integrador y aislamiento efectivo cliente A/B.
- Facturación/medición y exportación por tenant, sin información cruzada.
- Política y aprobación versionadas con trazabilidad.
- Logs minimizados, retención, control de acceso y proceso de incidentes.
- Respuesta clara sobre API/SDK, exportabilidad, límites de uso y SLA.
- Documentación para implementador y soporte escalonado.
- Al menos 2 instalaciones independientes con benchmarks de onboarding.

## Indicadores del canal

Partners que publicaron al menos una política segura (activados), tenants activos, tiempo a primera integración, ingreso neto por partner, costo de soporte, margen de contribución, fallos de aislamiento, churn, renovaciones y porcentaje de partners económicamente rentables. No tratar empresas que piden información como partners activos.

## Plan antifracaso

Si el partner necesita demasiado soporte: reducir productos, mejorar instalación o subir precio condicionado a valor. Si el partner prefiere usar Helio/OPA/Temporal: investigar DELIA como módulo complementario y no forzar reemplazo. Si dos partners demandan soluciones incompatibles, priorizar el problema de mayor frecuencia y margen, no prometer ambas.
