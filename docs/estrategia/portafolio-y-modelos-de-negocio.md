# DELIA — Portafolio de productos y modelos de negocio

**Corte:** 09-11-2026. Todas las líneas comerciales son **propuestas**, no productos disponibles para compra. La arquitectura busca un solo núcleo modular con múltiples empaquetados, NO veinte stacks paralelos.

## 1. Productos nucleares compartidos

| Producto/módulo | Problema comprador | Función objetivo | Estado actual |
|---|---|---|---|
| DELIA Guard | Agentes con acceso a herramientas sensibles | Auth, scopes, deny/allow/approval, enforce antes de ejecución | Prototipo de políticas en PR #21, sin auth/adapters reales |
| DELIA Protect | Fugas de datos y divulgación innecesaria | PII LATAM, DLP contextual, pseudónimos y multimodal | Regex parciales en main; MX/BO en PR #20 |
| DELIA Verify | No hay pruebas de comportamiento ni auditoría útil | Corpus, evaluación adversarial, recibos, métricas | Benchmark histórico, CI separada y recibo HMAC en laboratorio |
| DELIA Flow | Políticas incoherentes entre agentes, apps y países | Policy Studio, data passports, rutas autorizadas | Modelos experimentales, UI y enforcement pendiente |
| DELIA Connect | Integración difícil con stack del cliente | API/SDK, MCP, LLM gateways, CRM, ERP y ticketing | Por diseñar/adaptar en prototipo controlado |

## 2. Modalidades de comercialización (distintas de los módulos)

### DELIA Developer — licencia/SDK y comunidad
**Comprador:** desarrolladores individuales e integradores que evalúan. **Modalidad:** librería / CLI / API de laboratorio, documentación y ejemplos sintéticos. **Ingreso potencial:** soporte adicional, mantenimiento contractual, servicios de integración, conversión a nube. **Condición:** el repositorio tiene licencia MIT; estudiar con abogado y titulares los términos de licencias futuras y contribuciones. No reetiquetar retrospectivamente software MIT como propietario.

### DELIA Cloud — SaaS multiempresa
**Comprador:** SaaS B2B, startups y medianas empresas. **Ingreso:** cuota por organización/mes + uso de ejecuciones, controles o eventos (con límites, transparencia y consentimiento). **Costo:** infraestructura, retención, soporte, monitoreo, backups y auditoría. **Gate:** tenant isolation, autenticación, protección de información, facturación, recuperación e incident response. **Estado:** propuesto.

### DELIA Partner — B2B2B / OEM / marca blanca
**Comprador:** integradoras, agencias tecnológicas, MSP y proveedores de automatización. **Ingreso:** plataforma base + tarifas por organización activa, uso, soporte y capacidades premium; licencias de reventa o revenue share contractuales. **Valor:** la integradora administra múltiples clientes, políticas separadas y evidencia exportable sin replicar infraestructura. **Gate:** RLS/cifrado, responsabilidades por datos, conciliación y soporte L2/L3. **Estado:** propuesto.

### DELIA Enterprise — self-hosted, private cloud o instalación dedicada
**Comprador:** organizaciones con requisitos específicos de control, residencia o integración. **Ingreso:** licencia anual de software + puesta en marcha + soporte/mantenimiento + desarrollo de conectores cuando proceda. **Costos/riesgos:** despliegues privados son menos escalables y requieren QA de versiones, backup, monitoreo y dependencias. **Gate:** seguridad, soporte y acuerdos de servicio verificables. **Estado:** propuesto.

### DELIA API & usage-based control
**Comprador:** desarrolladores con uso variable. **Ingreso:** facturación por decisiones de política, invocaciones protegidas o volúmenes de evaluación, separando tráfico LLM de terceros. **Riesgo:** cobro doble, uso impredecible, fraude de medición; definir idempotencia, límites y precios antes de activar. **Estado:** propuesto.

### DELIA Assurance — plataforma + servicios
**Comprador:** empresas que necesitan evaluación de riesgo y asistencia técnica. **Servicios posibles:** inventario de agentes, diseño de políticas, simulaciones controladas, integración, pruebas de regresión, soporte y talleres. **Ingreso:** setup/piloto/proyecto, retainer y mantenimiento. **No es auditoría acreditada o certificación legal automática.** **Estado:** paquete comercial por definir.

### DELIA Academy — formación
**Comprador:** equipos internos y partners. **Ingreso futuro:** cursos empresariales, talleres y entrenamiento en diseño seguro de agentes, documentación o capacitación de preventa, siempre sin usar casos de clientes sin permiso. **Importante:** un diploma interno no equivale a certificación profesional reconocida. **Estado:** documentación de entrenamiento en PR #21.

### DELIA Sector Packs — plantillas y conectores
**Comprador:** verticales con procesos repetibles. **Ingreso:** complemento por sector, conectores mantenidos y soporte especializado. **Valor:** disminuir días de parametrización y demostrar una batería específica de pruebas. **Condición:** evidencia independiente, revisión del sector, consentimiento y términos comerciales claros.

### DELIA Marketplace — ecosistema de terceros
**Comprador:** empresas y partners que requieren controles certificados internamente. **Ingreso eventual:** comisión por bundles/conectores, programa de partners y soporte; requiere demanda real, firma de artefactos, revisión de seguridad, licencias claras y control de revocación. **No recomendar abrir marketplace antes de controles P0 y base de usuarios.**

## 3. Embudo de monetización (no ventas obtenidas)
Contenido técnico y comunidad → laboratorio libre → entrevista de problema → evaluación sintética → piloto seguro con contrato → suscripción Cloud/Partner/Enterprise → expansión por agentes/clientes/verticales → servicios y adopción.

## 4. Qué se vende primero y qué NO
**Primera oferta realista cuando se cierre P0:** paquete de integración y validación técnica limitada con una operación de alto valor, 1–2 herramientas, evidencia verificable y criterios Go/No-Go. **Luego:** DELIA Partner para integradoras con varios clientes.

**No vender inicialmente:** gestión clínica autónoma, pagos en producción, decisiones crediticias, personal de RR. HH. automatizado sin supervisión ni proveedores de gobierno sin proceso de contratación, aunque se usen como ejemplos sintéticos.

## 5. Arquitectura comercial de una sola plataforma
Un mismo control plane soporta auth, tenant, políticas, evaluaciones y evidencia; los módulos no duplican lógica y los packs son configuraciones firmadas, con fixtures y adaptadores; Cloud y Enterprise comparten contratos de API. Esto reduce costo de mantenimiento y facilita una combinación de **ARR de plataforma + NRR por expansión + servicios iniciales + canal OEM**.

## 6. Prohibición de sobreventa
Todas las ediciones y precios futuros deben incluir: versión y fecha, funciones comprobadas, limitaciones, infraestructura y tratamiento de datos, soporte pactado, costos de modelo externo, retención, responsabilidades del cliente y plan de reversión. Los precios de investigación no se publican como tarifas oficiales.
