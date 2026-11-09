# DELIA — Roadmap ejecutivo y tecnológico con fechas concretas (2026–2028)

**Fecha de elaboración:** 09/11/2026. **Estado:** metas propuestas, no compromisos firmados, productos operativos ni disponibilidad laboral confirmada. El calendario **no sustituye** los gates de seguridad. Corte central: **viernes 15/01/2027**, beta avanzada sujeta a revisión.

## Noviembre 2026 – enero 2027

| Fecha límite | Entregable concreto | Criterio comprobable |
|---|---|---|
| **13/11/2026** | Catálogo de producto, 4 ICP prioritarios, brand narrative, mapa de sectores | Documentos versionados y revisión de estrategia |
| **20/11/2026** | Diseño de auth real, scopes, tenant y control P0; 10 invitaciones personalizadas a descubrimiento | Issues, test plan y permisos, sin PII pública |
| **27/11/2026** | Arranque estable; egress con DLP obligatorio en upstream mock; secretos y logs minimizados | Tests 401/403, cross-tenant, no bypass, fail-closed |
| **04/12/2026** | Primer adapter de herramientas con control previo de ejecución | Tests E2E: herramienta denegada **no ejecutada** |
| **11/12/2026** | Aprobaciones con persistencia y consumo atómico | Concurrencia, replay, expiración y cambio de argumentos |
| **18/12/2026** | Auditoría mínima persistente, políticas versionadas y primer panel de aprobación | Test de retención, RBAC, integridad y rollbacks |
| **25/12/2026** | API/SDK alpha, consola de uso y métricas por organización | Contrato OpenAPI, CI y pruebas multiempresa |
| **08/01/2027** | Release candidate de beta; 2 adapters de prueba; benchmark regional independiente | SHA + dataset + informe técnico, sin P0 abiertos |
| **15/01/2027** | **Go/No-Go beta avanzada**, demos 12/30 min, manual de instalación, límites publicados | Acta de revisión; seguridad tiene veto |
| **31/01/2027** | Hasta 3 pilotos de diseño controlados, **solo si** hay consentimiento, contrato y gates | Resultados privados, no logos/clientes inventados |
| **28/02/2027** | Iteración del producto, revisión de costo por tenant y experimentos de precio | Métricas, incidentes, propuestas comparables |
| **31/03/2027** | Elegir máximo 2 verticales y 1 canal principal; decidir seguir/pivotar | 20 entrevistas acumuladas como meta y datos de pilotos |

### Camino crítico

Arranque reproducible (#6) → identidad/tenant (#7) → secretos y auditoría (#8) → PII obligatoria pre-egress (#9) → CI estable (#11) → Agent Firewall con adapter → aprobaciones durables → evidencia → interfaz y métricas.

PR #19 y #20 se revisan independientemente; el PR #21 es una beta de laboratorio en borrador. No fusionar trabajo ajeno sin revisión. No desplazar estos controles por crear funciones especulativas.

## Abril–diciembre 2027 — producto y expansión

| Fecha | Meta de producto | Meta comercial aspiracional, NO forecast |
|---|---|---|
| **30/04/2027** | DELIA Partner piloto, 2 integradores con tenants ficticios aislados | 2 integradores evaluando, no asumir ventas |
| **30/06/2027** | DELIA Cloud/Partner operables tras gates y soporte | Hasta **6 clientes pagos** y **US$3.000 MRR** como objetivo |
| **31/07/2027** | Commerce Pack y Contact Center Pack con flujos replicables | 2 clientes con caso y disposición verificables |
| **30/09/2027** | Integraciones CL/MX/CO y API estabilizada | Meta aspiracional **15 cuentas**, **US$10.000 MRR**, 2 partners |
| **31/10/2027** | Primera evaluación Enterprise Dedicated privada | 1 ensayo de despliegue con seguridad revisada |
| **31/12/2027** | DELIA Platform v1, documentación, soporte y renovación | Meta aspiracional **25 cuentas**, **US$20.000 MRR**, 3–5 partners |

Esas metas pueden cambiar por ventas, caja, acceso a clientes y costo real. MRR proyectado no son ingresos percibidos ni ARR facturado. Una venta no procede si el producto no alcanza el umbral técnico.

## 2028 — opciones de expansión

- **31/03/2028:** evaluar entrada en Perú/Brasil con socio técnico, portugués, normas y soporte.
- **30/06/2028:** decidir oferta Enterprise Dedicated con al menos 2 instalaciones seguras replicables.
- **30/09/2028:** evaluar Marketplace y firma de packs si hay base instalada y revisión supply chain.
- **31/12/2028:** revisar alianzas, financiación y exportación global utilizando retención, margen, ARR real y contratos.

## Puertas de seguridad y producto

- **S0 Lab:** código sintético, CI, sin datos de clientes ni ejecución real.
- **S1 Alpha:** autenticación verificable, tenant real, egress DLP, adapters sin bypass y logs minimizados, todo con E2E.
- **S2 Beta avanzada:** interfaz funcional, políticas versionadas, aprobaciones durables, backups, exportación, pruebas adversariales y runbooks.
- **S3 Piloto empresarial:** contrato, autorización de datos, revisión jurídica, threat model, soporte pactado, responsables y Go/No-Go.
- **S4 Enterprise/Producción:** auditorías independientes, incident response, medidas de seguridad y SLO basados en datos, no afirmaciones.

**No-Go obligatorio** si falla aislamiento, autenticación, tratamiento de datos, aprobación atómica o enforcement de herramientas, aunque llegue el 15 de enero.

## Capacidad humana

La beta combinada de gateway, agentes, auditoría y consola puede requerir, como estimación inicial no verificada, 800–1.500 horas técnicas/QA. Cuatro colaboradores a 12 h semanales por aproximadamente 10 semanas sumarían solo 480 horas: habría que reducir módulos o ampliar capacidad. Ninguna tarea asignada aquí presupone disponibilidad, contrato o remuneración.

## Revisión semanal

Por entregable: objetivo, persona que acepta ser responsable, reviewer, fecha, evidencia de SHA/CI, fallos relevantes y próximo paso. Reportar desvíos y rechazos de producto explícitamente. No cerrar tickets automáticamente por llegar a una fecha.

## Principios de ampliación

Los 18 sectores son cartera de oportunidades, NO 18 desarrollos paralelos. Priorizar inicialmente integradoras, SaaS B2B, ecommerce y BPO. Salud, pagos, energía y gobierno requieren gates más estrictos; entrar después de seguridad acreditable.
