# 02 — Oferta comercial que un comprador pueda entender y presupuestar

**Todas las cantidades son rangos para entrevistas, no precios publicados ni contratos.** Ninguna oferta puede sugerir que el código DELIA actual garantiza seguridad productiva.

## Escalera de valor y comercialización

| Etapa | Oferta propuesta | Entregable verificable | Precio a INVESTIGAR | Condición |
|---|---|---|---|---|
| E0 | Community Lab | Demo local sintética, código y documentación de uso | Gratis | Avisos de limitación, cero datos reales |
| E1 | DELIA Workflow Readiness Workshop | Sesión de alcance, mapa de flujo, matriz de riesgos, casos de test y recomendaciones (incluyendo no usar DELIA) | US$250–750 por trabajo definido | Contrato básico de consultoría, entregables y capacidad real del equipo |
| E2 | DELIA Design Partner Lab | 2–4 semanas de adaptación **en sandbox** a un proceso, matriz de pruebas y comparación con herramienta existente | US$750–2.500 por proyecto, validar disposición a pago | No PII real ni acciones en producción; acuerdo escrito de datos/resultados |
| E3 | DELIA Partner Beta | Tenants, contratos, autorización y evidencia efectivamente operativos y auditados | Base hipotética US$299–1.499/mes + tenants/uso | S2/S3, soporte y facturación verificables |
| E4 | DELIA Enterprise | Despliegue privado y soporte bajo contrato | Cotización caso a caso | S4, permisos, SLO, backup, revisión de riesgos |
| E5 | Sector Packs | Reglas y adapters con tests sectoriales versionados | Add-on negociado por valor y mantenimiento | Clientes/pilotos de sector y QA adecuados |

**Elección práctica:** E1 (servicios profesionales reales) antes de E3. Si ni E1 logra compradores con dolor comprobado, una plataforma de suscripción difícilmente se venderá simplemente por disponer de más funciones.

## Producto E1: contrato de alcance de prueba (no documento jurídico definitivo)

**Nombre corto:** Workflow Readiness Lab. **Duración indicativa:** 1–2 reuniones técnicas y un informe dentro del plazo acordado. **Incluye:** inventario de un flujo ya existente o ficticio, amenazas, matriz de permisos, propuesta de casos positivos/negativos, dos alternativas del mercado y recomendación de implementación. **Excluye:** certificación, pentest acreditado, integración productiva, operación continua, acceso a bases de datos, documentos privados sin autorización y garantías legales.

**Criterio de entrega:** el comprador puede decidir (a) no automatizar; (b) usar un gateway existente; (c) hacer un PoC controlado; (d) evaluar DELIA cuando esté listo. El servicio tiene valor aunque DELIA no sea la opción elegida.

**Piso de viabilidad:** horas de delivery × costo total horario + soporte + impuestos/costos administrativos + margen objetivo. No aceptar proyectos por debajo del costo integral; no pagar comisiones con margen negativo.

## E2: piloto acotado que no promete production readiness

**Contrato de experimentación (a revisar jurídicamente):** proceso, sistemas ficticios/sandbox, responsables, entradas permitidas, uso de datos, objetivos, medidas, plazo, criterio éxito/fracaso, tratamiento de información, propiedad intelectual, incidentes, cancelación y límite de responsabilidad negociado. Prohibir conectores que puedan ejecutar pagos, cambios irreversibles o acceder a datos sensibles antes de gates y revisión.

**Entrega:** demo reproducible, archivo de condiciones, test negativo de bypass, tiempos de instalación y conclusión Go/No-Go.

## E3: opciones de pricing que compararíamos

A. **Tarifa base + tenants activos:** alineada con integradora; comparar con software autoalojado y gateways existentes.
B. **Plataforma + flujos protegidos:** alineada con costo de operación y adopción, pero medidor auditable.
C. **Licencia privada anual:** para clientes que exigen residencia/operación privada; costoso en soporte.
D. **Servicio administrado + soporte:** márgenes dependientes de horas reales y disponibilidad.

No confundir `verified workflow` con `tool-call`: el primero requiere evidencia externa del resultado. Cobrar por «éxitos» auto-reportados podría incentivar manipular métricas. No activar billing hasta definir comprobación independiente.

## Economía de la integradora y MasterTech

```text
Ingreso nominal por partner = plataforma + tenants*tarifa + operaciones*tarifa
Comisión de canal = ingreso nominal * % contrato
Costo atribuible = nube + almacenamiento + soporte + comisión + medio de pago + integraciones atribuibles
Contribución = ingreso nominal - costo atribuible
Margen de contribución = contribución / ingreso nominal (si ingreso > 0)
```
`commercial_ops.demo` calcula escenarios **sintéticos**, sin declarar ventas. El precio debe soportar descuentos, atención, revisión de seguridad, impuestos y pérdidas de cobranza.

## Estructura de propuesta comercial lista para adaptar

1. Problema observado por comprador y fuente.
2. Cómo lo resuelven hoy (y qué hacen bien).
3. Costo/impacto medido de la brecha.
4. Un flujo de trabajo, los roles y los datos permitidos.
5. Qué hará MasterTech hoy (servicio) y qué DELIA solo podría hacer después de gates.
6. Resultado de la evaluación y formato de entrega.
7. Precio total, calendario, hitos de pago, exclusiones y garantía limitada de servicio.
8. Riesgos y reversión/cancelación.
9. Próximo paso concreto y quién puede aprobarlo.

## Reglas de descuento

Nunca ofrecer descuento automático por «exposición». Ceder valor solo por menor alcance, pago adelantado, autorización para aprendizaje técnico anonimizado, menor soporte o compromiso de colaboración explícito. No usar información de un comprador como caso público sin permiso específico. No prometer retorno de inversión antes de medirlo.

## Lista de afirmaciones que NO se pueden hacer

«DELIA es SOC2/ISO certificado», «cumple automáticamente todas las leyes», «no filtra datos», «puede hacer pagos reales seguros», «100 % de exactitud», «se ahorra 40 %», «el plan cuesta US$499 oficialmente», «tenemos socios y clientes de pago» si faltan evidencias.

## Ruta al contrato recurrente

Un comprador que pagó un workshop puede pasar al sandbox bajo una nueva decisión de compra; **no** convertir automáticamente un workshop en suscripción. En el piloto comparar con una herramienta alternativa, medir costo por operación y resolver el problema identificado. Si hay valor, proponer suscripción; si no, ofrecer la alternativa adecuada y preservar reputación.
