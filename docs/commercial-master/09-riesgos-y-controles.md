# 09 — Registro de riesgos empresariales, técnicos y reputacionales

Versión 09/11/2026. Severidad cualitativa, no porcentaje modelado. El objetivo de esta matriz es **evitar quiebras de confianza, caja y continuidad** al acelerar ventas.

| ID | Riesgo | Severidad | Señal temprana | Mitigación y dueño pendiente |
|---|---|---|---|---|
| M1 | Falta de problema que compra | Crítica negocio | Reuniones sin presupuesto/dolor | 15 entrevistas, oferta acotada, pivot |
| M2 | Competidor ya cubre todo el flujo | Alta | Comprador demuestra stack suficiente | Integrar, no competir por clones |
| M3 | Sobreconstruir 18 verticales | Alta | 5 features nuevas por 0 usuarios | Wedge único y gates |
| M4 | Servicios no escalables disfrazados de SaaS | Alta | Horas de soporte crecen por cliente | Costeo por tenant, limitar alcance |
| M5 | Discounting sin margen | Alta | Comisión/soporte > licencia | Unit economics y piso comercial |
| M6 | Confundir interés con ingresos | Alta | Presentaciones anuncian MRR sin facturas | CRM privado, contrato y cobro |
| M7 | Dependencia del fundador para ventas | Media/alta | Nadie más puede ejecutar discovery | Guiones, entrenamiento y roles aceptados |
| M8 | SLA enterprise imposible | Crítica | Cliente exige 24/7 sin guardias | Rechazar o negociar alcance |
| M9 | Falta de caja para infraestructura | Alta | Consumo/modelos superan plan | Budget, cuotas, shutdown |
| M10 | Financiamiento no adjudicado | Alta | Se gasta como si subsidio existiera | Plan sin subvención garantizada |
| S1 | Identidad/tenant falsificable | Crítica seguridad | Roles vienen de payload | Auth server-side, tests cross-tenant |
| S2 | Egress con PII | Crítica | Prompt crudo llega upstream | DLP pre-egress, fail-closed |
| S3 | Bypass de herramienta | Crítica | Agente llama tool fuera de policy | Adapter obligatorio + E2E |
| S4 | Duplicación de efectos | Crítica | Reintento emite dos pagos | Idempotencia DB y autorización exacta |
| S5 | Falsificación de resultado | Crítica | El modelo afirma éxito sin lectura | Reconciliación autoritativa |
| S6 | Logs/recibos con datos sensibles | Alta | Payloads en observabilidad | Redacción, retención, ACL |
| S7 | Licencia/PI y contribuciones sin revisión | Alta | No está clara titularidad | Acuerdos, MIT, registros |
| S8 | Regulación interpretada como venta | Alta | «Cumple la ley» sin dictamen | Revisión jurídica específica |
| S9 | Pilotos con datos privados sin autorización | Crítica | Piden acceso a CRM real | No-Go, alternativas sintéticas |
| S10 | Métricas sintéticas se publican como reales | Alta | «100% efectivo» en pitch | Claim ledger, evidence review |
| G1 | Llamadas/outbound sin permiso | Media/alta | Quejas, opt-outs ignorados | Consentimiento, contacto pertinente |
| G2 | Conflicto de canal integrador vs venta directa | Media | Partner siente que se le compite | Política de cuentas, contrato |
| G3 | Scope creep por design partners | Alta | Cada comprador pide 5 conectores | Definición de alcance y change orders |

## Riesgo tecnológico versus comercial

Una beta técnicamente exitosa y sin compradores **no** demuestra PMF. Un cliente interesado y dispuesto a pagar por una operación riesgosa **no** desbloquea producción. Exigir ambos ejes por separado.

## Límites innegociables

- P0 abiertos: no llamadas a datos reales ni herramientas con efectos en infraestructura de terceros.
- Ningún permiso dado por scoring comercial, un chatbot o un flag enviado por cliente.
- No mezclar datos de empresas bajo el mismo tenant.
- Cualquier incertidumbre de pago: HOLD, nunca reintentar automáticamente.
- No proyectar ventas con tasas arbitrarias presentadas como pronóstico.
- No usar experiencia freelance personal como facturación de MasterTech.
- Publicar límites de tests y fecha de evidencia.

## Seguridad del programa de diseño

El workshop comercial puede tratar procesos genéricos o información sintética, con contrato de servicios. Cualquier archivo o ejemplo de cliente requiere control de acceso privado, permiso y evaluación de datos. Si la empresa insiste en entregar bases con PII para «probar», detener la prueba y ofrecer un conjunto de datos sintético.

## Titularidad, marcas y licencias

DELIA ya contiene código con licencia MIT; nunca asumir que una edición futura puede retirar derechos sobre código previamente licenciado. Documentar derechos de autores, software de terceros, uso de nombre, contratos y contribuciones. Registrar marca/dominio solo tras búsqueda de disponibilidad y asesoría.

## Comunicación

**Permitido:** «laboratorio con 25 tests por versión en código de contratos», «investigamos el mercado de integradoras», «catálogo de ediciones planeadas».
**No permitido:** «25 clientes», «seguridad completa», «protección lista», «tenemos fondos», «ROI demostrado», «certificación», «el mejor gateway global».

## Protocolo de incidentes y reputación

Si surge un error técnico en demo: registrar SHA, entrada sintética, fallo, impacto y limitación; suspender demostraciones con claims afectados. Si un prospecto intenta compartir secretos, pedir que no los envíe, y gestionar por canal seguro antes de continuar. Nunca divulgar detalles explotables de clientes en GitHub.
