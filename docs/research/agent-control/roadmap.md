# DELIA Agent Control Research — Roadmap y criterios de publicación

**Fecha base:** 09/11/2026. Objetivos condicionados y sujetos a priorización del equipo, no compromisos ni tareas asignadas.

| Fecha objetivo | Resultado | Gate |
|---|---|---|
| **13/11/2026** | Registro de 14 riesgos y fuentes científicas con estados honestos | Revisión humana de amenazas y límites |
| **20/11/2026** | Congelar fixture sintético, amenaza prioritaria y pruebas para 3 controles P0 | Sin datos reales; revisor independiente |
| **27/11/2026** | Revisión técnica #6–#9/#11, IAM/egress y credenciales | Ningún bypass a producción |
| **04/12/2026** | Primer adapter de prueba con ejecución bloqueada fuera de policy | Test: prohibida = cero efecto |
| **11/12/2026** | Aprobación exacta y revocación/rollback bajo mocks | Test replay/revocation y concurrencia |
| **18/12/2026** | Reconciliación de resultado desde una API de prueba separada y monitor de eventos | Unknown nunca convertido en éxito |
| **08/01/2027** | Evaluación independiente de 10+ escenarios, SHA, resultados y límites | Publicar falsos positivos y no ejecutados |
| **15/01/2027** | Go/No-Go beta avanzada (proyecto base), sin comprometer seguridad P0 | Veto si auth, egreso o tool bypass fallan |
| **31/03/2027** | Decisión comercial sobre evaluación como servicio y valor incremental | Entrevistas, precio y costo de test real |

**Estándares/referencias**: OWASP Agentic Top 10 y ACS, NIST AI RMF, MITRE ATLAS, ControlArena, International AI Safety Report y ONU, todos verificados como publicaciones públicas. No implica conformidad certificada.

## Puertas de investigación

R0 **Mapa teórico**: fuente y caso reproducible diseñado.
R1 **Lab**: script sintético y test con fixture, resultado limitado.
R2 **Integración aislada**: adapter obligatorio y efectos observables.
R3 **Evaluación adversarial externa**: revisor separado y variantes de ataque.
R4 **Piloto contractual**: IAM, privacidad, responsabilidades, soporte y SLO acordados, datos solo cuando autorizados.

## Qué NO se hará

- No entrenar modelos frontier para «ganar» un benchmark a cualquier costo.
- No aumentar autonomía de agentes de producción sin gates.
- No construir un botón «kill switch universal» imposible de respaldar.
- No modificar PR #19/#20/#21 sin coordinar revisión y preservar autoría.
- No anunciar prevención de pérdida global de control como promesa comercial.
- No usar el video ni las voces sin revisión de derechos y contexto.

## Primer paquete pagable a investigar

`DELIA Agent Control Readiness Pack`: revisión de un proceso de CRM de prueba con matriz de herramientas, 3 decisiones de permiso, 3 negativos de acceso/exfiltración, propuesta de cambio y reporte con limitaciones. Cotización y demanda requieren comprador real; no existe tarifa definida ni ventas.
