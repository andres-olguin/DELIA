# DELIA — Arquitectura escalable, controles P0 y evidencia de producto

**Documento técnico:** DELIA-ENG-20261104-01 · **Fecha:** 2026-11-04 · **Estado:** plan de ingeniería, no certificación ni release.  
**Alcance:** complementa [revisión de seguridad Ronda 4](REVISION_SEGURIDAD_PARCHE_P0_RONDA4_2026-10-31.md), [roadmap](roadmap.md), [benchmark](../benchmarks/README.md) y [OPS-01](https://github.com/andres-olguin/DELIA/issues/18). No duplica estudios comerciales existentes.

## 1. Línea base comprobable e implicaciones

- Un benchmark sintético documentado en README informa **71 TP, 3 FP y 79 FN** entre 150 casos positivos, con precisión 95,95 %, recall 47,33 % y F1 63,39 %. La cifra procede de datos y ejecución documentados de octubre; no es una nueva validación independiente.
- La sanitización falla en numerosos casos; **la baja cobertura de detección impide garantizar protección PII en producción**. No exponer DELIA como filtro definitivo ni ofrecerlo a clientes con datos sensibles.
- El parche P0 preparado localmente en Ronda 4 no está incorporado a `main`. Su revisión enumera aislamiento de tenants, identidad, gestión de secretos, auditoría, modelo de amenazas, límites de tokens, control de streaming, integraciones y migraciones como riesgos.
- Ruleset `Proteccion-Main` selecciona `~ALL` y `creation`; bloquea ramas nuevas. La edición de documentación en `main` de este documento **no soluciona** el bloqueo para PRs de código ni implica aprobar el parche.
- Lo ya implementado, lo simulado y lo investigado se deben reportar por separado en las entregas.

## 2. Decisión de arquitectura por etapa

| Etapa | Condición de entrada | Arquitectura preferida | No adoptar aún |
|---|---|---|---|
| Laboratorio | Riesgos P0 abiertos; solo tráfico sintético | FastAPI local, adaptador upstream de prueba, SQLite/PG aislado, pytest; límites estrictos de contenido | Pilotos con PII real, clustering, multi-región, almacenamiento de prompts sin política |
| Alfa privada | P0 cerrados con evidencia de tests y threat model | Servicio FastAPI containerizado, PostgreSQL + Alembic, autenticación por tenant, registros minimizados, TLS, secretos externos; Redis solo si se necesita | Caché de prompts por defecto; disponibilidad o cumplimiento garantizados |
| Piloto B2B consentido | Contratos, controles de tratamiento de datos, 2+ revisiones técnicas, pruebas y costos | Proxy sin estado horizontalizable, PG administrado, Redis para cuotas con TTL, trazas sin texto sensible, restauración probada, alertas de SLO | Microservicios separados por cada componente, Kubernetes prematuro |
| Expansión regional | Evidencia de volumen, retención y unidad económica; requisitos legales por país documentados | Infraestructura por región solo si la residencia o latencia lo justifican; balanceadores y colas controladas con idempotencia | Réplicas globales de datos personales por defecto, prometer cumplimiento multinacional |

**Criterio:** optar inicialmente por un monolito modular desplegable y límites de dominio explícitos; extraer servicios únicamente cuando perfiles de CPU, E/S, seguridad o equipos requieran escalado independiente. Evitar aumentar la superficie de operaciones prematuramente.

## 3. Modelo de flujo y prioridades de seguridad

```text
Cliente autorizado -> TLS -> Autenticación/tenant -> Cuota y límite de tamaño
  -> Política tenant -> DLP sobre TODAS las superficies aplicables
  -> decisión: bloquear / redactar / aprobar documentadamente
  -> cliente HTTP con timeouts, allowlist de destinos, circuito de reintentos
  -> proveedor LLM autorizado
  -> filtros de salida y metadatos -> respuesta
  -> auditoría mínima con correlación no sensible, nunca prompt crudo por defecto
```

**P0 bloqueantes antes de tráfico sensible:**
1. Identidad con separación real entre clientes, claves por tenant, scopes y RBAC; tests de acceso cruzado y rotación de secretos.
2. Política DLP por superficies: mensajes, herramientas, adjuntos, URLs, metadatos, streaming y salida; cobertura medida por jurisdicción. Ante error del detector, política explícita de `fail-closed` salvo decisiones justificadas por riesgo.
3. Prohibir que logs/trazas/auditoría persistan prompts o respuestas completos salvo consentimiento, motivo, retención y controles documentados; verificar SQL schema histórico.
4. Validación de tamaño por bytes y tokens; egress allowlist, DNS/rebinding, timeouts, cancelaciones, reintentos acotados e idempotencia donde sea pertinente.
5. Migraciones versionadas de esquema y recuperación; `create_all` dinámico no es mecanismo de producción.
6. Dependencias fijadas, SBOM cuando corresponda, análisis de secretos, pruebas negativas y reporte reproducible de cobertura y falsos negativos.

## 4. Ensayos de rendimiento honestos

Medir por separado `latencia_p50`, `latencia_p95`, `latencia_p99`, `throughput`, `errores_5xx`, latencia DLP, tokens procesados y proporción de bloqueo por política. Registrar hardware, versión de Python, modelo upstream, región, tamaño de prompt, concurrencia, duración y dataset.

**Experimentos sugeridos, no resultados ni compromisos:**
- Niveles de carga: 1, 10 y 50 solicitudes simultáneas con tráfico sintético.
- Escenarios: bypass local a upstream ficticio, detección DLP, bloqueo, error del proveedor, timeout, base de datos caída y Redis no disponible.
- Medir costo incremental por 1.000 peticiones y por 1 millón de tokens inspeccionados bajo parámetros declarados. En un proxy externo la latencia LLM suele dominar; separar sobrecarga DELIA de tiempo total.
- Al definir SLO, elegir umbrales a partir de datos medidos y expectativas de pilotos; un objetivo del 99,9 % NO está aprobado aquí. Error budget y ventanas de evaluación requieren compromiso del responsable operativo.

## 5. Economía unitaria y puertas de escalado

**Variables, no precios inventados**:
- `V`: peticiones mensuales; `T`: tokens promedio/request; `c_token`: costo por token externo si DELIA lo absorbe.
- `C_api`: costo mensual de cómputo + red + bases + backups + observabilidad.
- `C_soporte`: operación y soporte; `C_seguridad`: auditoría y cumplimiento; `C_ventas`: captación y comisiones.
- `Costo_servicio = C_api + C_soporte + C_seguridad`.
- `Margen_de_contribución = (Ingreso - costo variable atribuido) / Ingreso`; validar atribución y no contabilizar tokens upstream como ingreso propio sin contrato.
- Escalar computación cuando uso sostenido o p95 y colas lo exijan; escalar datos cuando análisis de consultas y pruebas de carga demuestren un cuello de botella. Evitar multi-región sin requisitos de residencia/SLO que justifiquen el costo.

Registrar presupuestos separados por región, nube, entornos de prueba y observabilidad, con un límite mensual aprobado y alertas de consumo.

## 6. Evidencia de mercado antes de comercializar

El segmento inicialmente investigado es **integradores B2B que incorporan IA en procesos empresariales**, no mercado de consumo masivo general. Seguir los estudios de DELIA existentes y completar, sin falsificar:
- Entrevistas de necesidad, disposición a pago y restricciones legales con interlocutor y fecha;
- Baseline de competidores con pruebas comparables (no afirmar que Presidio, Cloudflare o Model Armor fueron ejecutados);
- Dos pilotos ficticios de extremo a extremo, luego piloto real bajo contrato solo tras superar P0;
- Evidencia de integración, carga operativa y tiempo de implementación;
- Decisión explícita de seguir, pivotar o detener según fallos, costo y adopción.

## 7. Checklist de salida por producto y jurisdicción

- [ ] Benchmark con corpus reproducible y FN/FP por categoría, segmentado por país.
- [ ] Matriz de permisos, pruebas de aislamiento multiempresa y secretos rotables.
- [ ] Auditoría mínima, retención definida, recuperación probada y pruebas de fallo de proveedores.
- [ ] Threat model y revisión NIST SSDF/OWASP ASVS sobre controles aplicables.
- [ ] SLI/SLO observados; alertas accionables con responsable y runbook.
- [ ] Costos medidos y presupuestos aprobados; sin ARR, MRR, ventas o cumplimiento inventados.
- [ ] Verificación jurídica local donde proceda, sin prometer certificaciones.

## 8. Referencias externas verificadas (consultadas 2026-11-04)

1. [OWASP ASVS 5.0.0](https://asvs.owasp.org/) — requisitos de verificación de seguridad de aplicaciones.
2. [NIST SSDF SP 800-218 v1.1](https://csrc.nist.gov/pubs/sp/800/218/final) — prácticas para desarrollo seguro.
3. [Google SRE — Implementing SLOs](https://sre.google/workbook/implementing-slos/) — SLIs, error budgets y adopción de SLO.
4. [OpenTelemetry — Observability Primer](https://opentelemetry.io/docs/concepts/observability-primer/) — trazas, métricas y logs.
5. [AWS Well-Architected](https://docs.aws.amazon.com/wellarchitected/) — seguridad, fiabilidad, eficiencia y costos.

**Nota:** usar los marcos como referencias de diseño no implica cumplimiento, certificación ni pruebas ejecutadas. Todo resultado de capacidad requiere evidencia técnica registrada.
