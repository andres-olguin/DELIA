# DELIA — Registro de investigación y ejecución: Ronda 3

**Corte:** 31 de octubre de 2026 · Versión 1.0 · Complementa Rondas 1 y 2, sin reemplazarlas.  
**Convenciones:** HV = verificado en fuente; EP = estimación propia; HP = hipótesis; NV = no verificado; NE = no ejecutado.

## 1. Qué se leyó antes de intervenir

Se consultó por GitHub `main`: README, inventario árbol recursivo, últimos commits, Issues abiertos, estudios previos y CSV 160 cuentas/235 URLs, kit `docs/ventas/`, roadmap, seguridad, código `app/`, `backend/`, `services/`, `models/`, `tests/`, Docker y `.env.example`. El código en main tiene fallos P0 de importaciones, autenticación, logs y envío upstream sin integrar redaction. **Ningún cambio funcional se hizo directamente a main.**

## 2. Bloque A — cierres y deudas reales

- [44 cuentas individualmente auditadas](VERIFICACION_44_CUENTAS_RONDA3.csv), resultado: **8 leídas completas, 10 solo snippet, 26 directorio**. No atribuir a las 26 ni ingresos ni uso LLM. Algunas 8 fueron abiertas completas en web, pero apertura no equivale a auditar legalmente.
- [235 URLs reclasificadas](REFERENCIAS_235_LECTURA_RONDA3.csv) con criterio conservador: **7 leídas completas, 224 solo snippet, 4 directorio**. Una URL no identificada como `leída completa` no necesariamente está rota; solamente no se pudo comprobar lectura íntegra en esta ronda. Las 7 abiertas completas son URLs coincidentes con la base de 235; una más en las 44 no estaba necesariamente registrada con la URL exacta.
- [40 cuentas iniciales de ola 1 reexaminadas](OLA1_40_EVIDENCIA_LLM_RECALIFICACION_RONDA3.csv): **8 conservadas como prioridad de investigación, 2 en reserva por evidencia indirecta y 30 descartadas de la ola inicial por ausencia de prueba pública suficientemente específica**. No equivale a que estas 30 empresas no utilicen IA.
- La investigación contradictoria importa: [Buk declara haber implementado enmascaramiento PII, separación de tenants y observabilidad](https://supportcenter.buk.cl/hc/es-419/articles/53619330726043-Buk-AI-Seguridad-Privacidad-y-Tratamiento-de-Datos), por lo que **su necesidad de DELIA adicional es especialmente discutible**. [Siigo](https://developers.siigo.com/docs/siigoapi/MCP/1-documentation/) ya documenta MCP con Claude/ChatGPT, pero tampoco prueba deseo de otro proveedor.
- [Normativa y prospección](MARCO_LEGAL_Y_PROSPECCION_RONDA3_2026-10-31.md): Chile Ley21.719 fecha publicada 01-12-2026 con propuesta de aplazamiento no promulgada al corte, México LFPDPPP 2025, Colombia Ley1581/2012/Circular SIC002/2024, Bolivia proyecto PL538, **no ley general vigente verificada**. Campañas de correo/WhatsApp requieren revisión jurídica y contacto legítimo; no autorización de scraping.

**Limitación:** la petición de «corroborar individualmente 44» se ejecutó como 44 fichas y búsquedas, pero **26 siguen sin corroboración independiente**. No se rellenaron con supuestos.

## 3. Bloque B — experimento local reproducible

**Dataset publicado:** [benchmarks/synthetic_pii_r3.jsonl](../benchmarks/synthetic_pii_r3.jsonl) con **172 casos, 150 entidades etiquetadas**, 22 casos sin entidades; tipos RUT, NIT CO, CEDULA CO, CURP, RFC, CI/NIT BO, tarjetas, teléfono, email y direcciones. Se generó localmente, **sin contactos reales**.

**Fuente del detector:** archivo exacto `backend/dlp/pii.py` hash blob Git **`9cdc531fc7dfb38eb05e0c53bdb2cec795a4ae82`** coincidente entre GitHub y copia evaluada. Se ejecutó localmente con Python 3.13 y se calculó coincidencia estricta tipo+span.

| Motor | TP | FP | FN | Precisión | Recall | F1 | Resultado |
|---|---:|---:|---:|---:|---:|---:|---|
| DELIA actual | 71 | 3 | 79 | 95,95 % | 47,33 % | 63,39 % | **Ejecutado** local |
| Regex básica didáctica | 60 | 6 | 90 | 90,91 % | 40,00 % | 55,56 % | **Ejecutado** local |
| Microsoft Presidio | NV | NV | NV | NV | NV | NV | **NO EJECUTADO**: paquete/entorno no disponible |
| Cloudflare DLP | NV | NV | NV | NV | NV | NV | **NO EJECUTADO**: políticas/tenant autorizados ausentes |
| Google Model Armor | NV | NV | NV | NV | NV | NV | **NO EJECUTADO**: proyecto/API credenciales no disponibles |

El corpus es **diagnóstico no representativo**, con etiquetas creadas por la misma persona/automatización y entidades sintéticas. **No hay ganador frente a tres alternativas empresariales.** DELIA pierde 79 etiquetas. La [metodología](../benchmarks/README.md) y salida JSON local se entregan en paquete anexo al solicitante; **el script no se publicó en main** porque es código.

## 4. Bloque C — Issues, branch, pruebas y PR

Se abrieron [12 Issues](https://github.com/andres-olguin/DELIA/issues) específicos: **#6–#11 P0, #12–#17 P1**, esfuerzo EP, criterios y dependencias. Se agregó [#18](https://github.com/andres-olguin/DELIA/issues/18) para reglas GitHub.

**Bloqueo concreto:** ruleset oficial de GitHub [ID 25836222](https://github.com/andres-olguin/DELIA/rules/25836222) denominado `Proteccion-Main`, configurado en **`~ALL`** ramas con reglas `creation`, `deletion`, `non_fast_forward` y bypass `never`. Crear `fix/p0-baseline-ronda3-20261031` o `fix/p0-baseline` devolvió **HTTP 422 «Reference update failed»**. Debido a esto, **rama y PR no creados**; el código **NO se subió a main**.

Se preparó localmente un paquete de código para rama futura, con auth básica de laboratorio, DTO que rechaza prompt crudo, logs de metadatos, secretos por variables, importaciones, tests FastAPI/SQLite, `requirements.txt` y workflow GitHub Actions. **Se ejecutaron seis pruebas en Python 3.13: 6 passed, 2 deprecation warnings**. Esto no significa cierre P0 completo: clave compartida de laboratorio **no da aislamiento multitenant**, falta migración de registros históricos y no se ejecutaron CI Python 3.11, tests end-to-end ni pentest. No procesar datos de clientes.

**Documentos en main:** [SECURITY.md](../SECURITY.md) y [plan TALIA→DELIA](PLAN_MIGRACION_TALIA_DELIA_2026-10-31.md), con migración por compatibilidad y sin renombrar base productiva a ciegas.

**Para desbloquear PR:** revisar GitHub Settings → Rules → `Proteccion-Main` y limitar ámbito de regla de `creation` a `main` o crear reglas separadas que **sí permitan ramas feature**, manteniendo seguridad main. Requiere acción explícita del titular; no debilitar protecciones silenciosamente.

## 5. Bloque D — hipótesis de producto

Se selecciona **integradores B2B2B** como nicho inicial de entrevistas; fintech/seguridad regulada y cumplimiento genérico son alternativas a investigar después. [Justificación y Brasil fase 2](FOCO_NICHO_Y_BRASIL_RONDA3_2026-10-31.md). No existe TAM/SAM/SOM monetario validado por buyers. Brasil LGPD vigente y ANPD Resolución 19/2024 de transferencia internacional; no hay equipo de MasterTech en Brasil y no hay soporte CPF/CNPJ ni portugués implementado.

## 6. Bloque E — activos producidos, sin campañas inventadas

Se publicaron:
- [Landing en texto y lista de espera conceptual](ventas/LANDING_ES_INTEGRADORES_WAITLIST_RONDA3.md): **sin formulario web funcional ni suscriptores**.
- [Tres artículos técnicos](articulos/) completos, editables, con fuentes oficiales y limitaciones.
- [Calendario editorial 12 semanas](ventas/CALENDARIO_EDITORIAL_12_SEMANAS.csv): **sin publicaciones hechas**.
- [Plan 24 entrevistas](ventas/PLAN_24_ENTREVISTAS_RONDA3.md): **0 entrevistas celebradas**.
- [Carta de intención no vinculante](ventas/CARTA_INTENCION_NO_VINCULANTE_RONDA3.md) y [Van Westendorp](ventas/ENCUESTA_VAN_WESTENDORP_RONDA3.md): borradores, **0 LOI firmadas, 0 encuestas aplicadas**.
- [Seis borradores de fondos](ventas/BORRADORES_6_FONDOS_ACELERADORAS_RONDA3.md): requisitos no siempre cumplidos y algunas convocatorias cerradas; **0 postulaciones enviadas**.
- [Tablero CSV 13 semanas](ventas/TABLERO_METRICAS_13_SEMANAS_RONDA3.csv): valores vacíos, no son cero ni resultados medidos.

## 7. Qué buscó el análisis sin poder demostrar

- Compradores reales o sus presupuestos, contactos nominativos y dirección de autorización de compras: **NV**. No se recopilaron datos personales.
- 44 cuentas: **26 directorio**, 10 extracto; aún carecen de corroboración profunda. Para las 235 referencias, **224 solo snippet** bajo este estándar.
- Comparación DELIA con Presidio/Cloudflare/Google: **NE**, aunque corpus y script local preparados.
- Seguridad y deployment: **no aprobado para producción**. CI y PR pendientes de resolver ruleset GitHub.
- Legislación de correos B2B y WhatsApp: se elaboró pauta conservadora, **no dictamen jurídico exhaustivo** de cada canal.
- Pago/contratos/entrevistas/marketing: **nada ejecutado** a empresas desde esta investigación.

## 8. Próxima decisión, con criterios falsables

1. Revisar ruleset #18 y habilitar ramas de desarrollo sin quitar protección main.
2. Publicar código local como **PR en borrador**, no fusionar hasta revisión humana, seguridad y CI ejecutada.
3. Completar las 26 webs de directorio y revalidar 8 cuentas de investigación prioritaria por canal de empresa.
4. Ejecutar Presidio y soluciones administradas en entornos aprobados; medir límites y documentar diferencias negativas/positivas.
5. Celebrar entrevistas reales: 12 integradores + 12 contrastes, registrar rechazo a middleware y costos reales.
6. Solo considerar piloto pagado si P0 efectivamente cerrado, datos sintéticos, responsables autorizados y valor que compradores confirmen.

**Conclusión:** se pasó de documentos a evidencia local parcial y activos preparados, pero **no a un SaaS listo para vender**. La conclusión desfavorable de recall bajo es accionable. La política GitHub impide PR y tres comparaciones siguen pendientes; se reportan sin sustituirlos por resultados ficticios.
