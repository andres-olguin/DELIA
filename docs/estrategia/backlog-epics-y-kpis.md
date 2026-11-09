# DELIA — Backlog ejecutivo, prioridades, responsables y resultados

**Versión 09/11/2026.** Los identificadores STRAT son la nomenclatura del plan, no issues existentes automáticamente. Referencias GitHub existentes: #6/#7/#8/#9/#11, #12, #16, #22–#25, PR #19/#20/#21. No cerrar esas tareas por publicar este documento.

## Épicas de producto y negocio

| ID | Épica | Resultado esperado | Prioridad | Fecha objetivo | Dependencia |
|---|---|---|---|---|---|
| STRAT-01 | Identidad/marca DELIA | Narrativa única, uso correcto del nombre y sistema de nomenclatura | P1 | 13/11/2026 | Decisión y revisión de marca |
| STRAT-02 | Núcleo P0 | Auth, aislamiento, DLP egreso, secretos y logs seguros | **P0** | 27/11/2026 | Issues #6–#9/#11 |
| STRAT-03 | Agent Firewall real | Test E2E de tool denegada que nunca se ejecuta | **P0** | 04/12/2026 | STRAT-02 y PR #21 |
| STRAT-04 | Aprobaciones persistentes | Aprobación única, vinculada a acción y tenant, resistente a replay | P1 | 11/12/2026 | STRAT-03 / DB |
| STRAT-05 | Políticas y consola | Editor versionado y RBAC seguro | P1 | 18/12/2026 | STRAT-02/04 |
| STRAT-06 | Audit & Verify | Recibos mínimos, pruebas negativas y exportación | P1 | 25/12/2026 | #12 y almacenamiento |
| STRAT-07 | SDK y conectores | API estable con dos adaptadores de prueba | P1 | 08/01/2027 | STRAT-03/05 |
| STRAT-08 | Beta avanzada | Go/No-Go, evidencia, manual, rollback, demo | P1 | 15/01/2027 | Todos los P0 cerrados |
| STRAT-09 | DELIA Partner | Panel multiempresa, límites y billing planificado | P2 | 30/04/2027 | Seguridad y validación ICP |
| STRAT-10 | Commerce Pack | Reembolso sintético con política y aprobación | P2 | 31/07/2027 | Clientes de diseño |
| STRAT-11 | BPO Pack | Datos regionales y CRM de test | P2 | 31/07/2027 | Benchmark independiente |
| STRAT-12 | Cloud Paid | Facturación, uso, soporte y contrato | P2 | 30/06/2027 | Gates legales/financieros |
| STRAT-13 | Enterprise Dedicated | Despliegue privado y manual SRE | P2 | 31/10/2027 | Auditoría y canal |
| STRAT-14 | Academy + partner enablement | Entrenamientos reproducibles, evaluaciones y guiones | P1 | 17/12/2026 | Producto honesto en docs |
| STRAT-15 | Descubrimiento y pricing | Segmento con WTP medida, tarifa validada o pivot | P1 | 31/03/2027 | Entrevistas/pilotos |
| STRAT-16 | Protección de marca | Evaluación INAPI/IMPI, dominios y derechos de IP | P1 | 31/01/2027 | Asesoría pertinente |
| STRAT-17 | Expansión regional | Pruebas de entrada Perú/Brasil e idioma | P3 | 31/03/2028 | Canal y soporte |
| STRAT-18 | Marketplace/Trust Network | Decisión de inversión basada en base instalada | P3 | 30/09/2028 | Retención y seguridad |

**No convertir este backlog en cien tickets sin acuerdo de capacidad.** Separar cada épica aprobada en historias pequeñas con prueba y reviewer, no por nombre de marketing.

## Matriz de responsabilidades propuesta
Los cargos no implican asignación automática ni disponibilidad obligatoria:
- Arquitectura/seguridad: responsable técnico aceptado + revisor distinto.
- Integración DLP/PII: colaboradores que trabajan en #16 si aceptan, con dataset independiente revisado por otra persona.
- Backend/data: encargado de auth/persistencia y QA aceptados.
- Canales/ventas: dirección comercial y CTO integrador, con CRM privado.
- Legal/privacidad: profesional local según país cuando se formalicen pilotos.
- DRI de cada historia: se anota solo tras confirmación explícita.

## KPIs de producto — contrato de medición

**Seguridad:** acciones no autorizadas ejecutadas (meta cero en escenarios definidos), rutas de egress sin política (meta cero en fixtures), cross-tenant failures, replay aprobaciones, eventos sin rastro, secretos en logs. El valor cero en una prueba no significa riesgo cero global.

**Calidad:** TP/FP/FN por entidad y país; cobertura de tests, fallos, flakiness, latencia p50/p95/p99 por ruta, costo por 1K decisiones, disponibilidad observada y tiempo de recuperación.

**Experiencia:** onboarding hasta primera política segura, configuraciones completadas, tiempo de respuesta, fricción de permisos y accesibilidad.

**Negocio:** entrevistas, problemas validados, tiempo a piloto, pago efectivo, MRR, GRR/NRR, CAC, margen bruto/contribución, churn, soporte por tenant, concentración de ingresos y runway.

## Semáforo de hitos
- **Rojo:** P0 fallido, dato sensible, acción que pudo ejecutarse sin permiso, prueba inexistente presentada como exitosa.
- **Ámbar:** implementación en PR y CI verde solo con synthetic, reviewer pendiente, costo o precisión no medidos.
- **Verde:** gates específicos completados y verificados por revisor, tests reproducibles, operación controlada.
Cada KPI tiene: owner, fórmula, fuente de datos, versión, periodo, umbral e incertidumbre.

## Dependencias y ruta crítica
STRAT-02 → STRAT-03 → STRAT-04 → STRAT-05/06 → STRAT-07 → STRAT-08 → STRAT-09/12. Si no hay tiempo para la consola, priorizar APIs seguras y una demo reproducible, no fingir madurez.

## Gestión de cambios de roadmap
Revisión semanal con evidencias. Mantener la fecha como objetivo, ajustar alcance si falta equipo; nunca reducir seguridad para conservar la fecha. Para financiar la expansión, pedir primero pruebas de ventas y margen.
