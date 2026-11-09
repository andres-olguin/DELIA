# 18 — DELIA Trust Center de etapa temprana y proceso de compras

**Objetivo:** reducir fricción de compra sin fingir certificaciones. Documento de transparencia, **no plataforma de seguridad certificada ni página comercial productiva**. Corte 09/11/2026.

## Mensaje para CTO/CISO

DELIA está en investigación y desarrollo. Existen módulos sintéticos de contratos y políticas, pero **no hay un gateway productivo verificado para PII o herramientas**. Las pruebas de CI solo acreditan el comportamiento de casos del laboratorio; no certifican cumplimiento normativo, aislamiento o defensa frente a atacantes reales.

Un comprador debe poder distinguir entre:
- **Función declarada:** diseño o aspiración.
- **Código disponible:** ruta de repositorio, PR, SHA.
- **Prueba automatizada:** comando, ejecución y entorno.
- **Integración E2E:** prueba real contra un adapter/control.
- **Operación de producción:** política, retención, contrato, monitoreo y respuesta a incidentes.
- **Certificación o auditoría externa:** solo cuando exista evidencia formal verificable.

## Checklist de seguridad del proveedor (estado inicial)

| Control | Estado inicial de DELIA | Para declararlo listo |
|---|---|---|
| Auth de clientes y roles | Pendiente P0 | Test JWT/OIDC/clave + scopes |
| Tenant isolation | Pendiente | Negativos cross-tenant y revisión DB |
| Protección de salida PII | Pendiente P0 | Proxy E2E y conjuntos independientes |
| Control de ejecución de tools | LAB en PR #21 | Adapter único y no bypass |
| Aprobación humana | LAB en memoria | Identidad de aprobador + transacción durable |
| Idempotencia de operaciones | LAB de detección previa | Almacenamiento y concurrency tests |
| Reconciliación de resultado | Solo comparación de estructuras ficticias | Lectura de fuente autoritativa y manejo de incertidumbre |
| Audit trail durable | Pendiente | Persistencia, retención, integridad, exportación segura |
| Secret management | P0 | Vault/KMS/rotación y análisis de repos |
| Continuidad/backup | No acreditado | Restore test, RTO/RPO medidos |
| Vulnerability disclosure | Política en repositorio a revisar | Proceso asignado y canal seguro |
| SBOM/escaneo dependencias | No acreditado para producto completo | Herramientas y reportes por release |
| ISO 27001 / SOC2 / certificaciones | **No acreditadas** | Certificador/alcance/evidencia real |
| SLA y 24/7 | **No ofrecidos** | Equipo, métricas, contrato y soporte |

Actualización requiere verificar GitHub y archivar evidencia con fecha; este documento queda obsoleto con cada release hasta editarlo.

## Cuestionario de procurement — respuestas de etapa

1. **Qué datos reciben?** En el demo, solo datos ficticios. Producto SaaS aún no existe; no aceptar información real sin acuerdo.
2. **Dónde se alojan?** El laboratorio corre local/CI. No hay promesa de residencia cloud.
3. **Son multitenant?** Hay separación lógica de reglas en laboratorio; no aislamiento productivo.
4. **Quién accede a prompts y herramientas?** No hay entorno SaaS; diseño futuro requiere RBAC/ABAC, retención y mínimo privilegio.
5. **Cómo tratan incidentes?** No afirmar SOC; revisar canal de seguridad y asignar responsable antes de piloto.
6. **Qué certificaciones poseen?** Ninguna acreditada por esta documentación.
7. **Pueden firmar DPA?** Necesita revisión legal cuando exista tratamiento de datos y contrato.
8. **Tienen backup, disponibilidad y exportabilidad?** Pendiente de versión/medición.
9. **Qué diferencia hay frente a gateways existentes?** Contratos sectoriales por demostrar; no afirmar liderazgo.
10. **Por qué confiar ahora?** Evaluación pequeña con código/suites reproducibles, límites públicos y derecho a concluir no-fit.

## Programa de confianza de 90 días

- Semana 1: inventario de claims, documentación de P0, canal de seguridad y política de datos sintéticos.
- Semanas 2–4: pruebas auth/egress/tenant, revisión independiente, suite adversarial de laboratorio.
- Semanas 5–8: adapter con no bypass, idempotencia y trazas minimizadas; simulación de incidente.
- Semanas 9–12: documentación de despliegue, reversión, privacidad, SBOM y revisión comercial de requisitos de comprador.
- Beta Go/No-Go: no usar verde si falta P0.

## Información pública y confidencialidad

Este documento es público. Cuestionarios de clientes y respuestas adaptadas que contengan datos de negocio deben conservarse fuera de GitHub; compartir solo bajo autorización y confidencialidad. No copiar certificados de otra empresa o asociar el logo de terceros sin acuerdo.
