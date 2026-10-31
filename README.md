# DELIA — Data Encryption & Limiting Intelligence Agent

**Proyecto en investigación y desarrollo: capa intermediaria de control para aplicaciones que integran APIs de modelos de IA.** El nombre histórico no significa que exista cifrado reversible implementado o verificado.

> **Security and governance layer for AI applications.**
>
> DELIA es un proyecto de software en desarrollo activo que busca proporcionar una capa intermediaria de seguridad entre aplicaciones corporativas y proveedores de modelos de lenguaje (LLMs). Su objetivo es reducir la exposición de datos sensibles, centralizar controles de tráfico y facilitar la trazabilidad de interacciones con sistemas de inteligencia artificial.

<p align="center">
  <img src="https://img.shields.io/badge/status-active%20development-orange" alt="Estado: desarrollo activo">
  <img src="https://img.shields.io/badge/current%20sprint-2-blue" alt="Sprint actual: 2">
  <img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white" alt="Python 3.11 o superior">
  <img src="https://img.shields.io/badge/FastAPI-backend-009688?logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/Docker-development-2496ED?logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/License-MIT-yellow" alt="Licencia MIT">
</p>

**Estado declarado:** Sprint 2 — motor de sanitización de información personal (PII).  
**Cronograma inicial:** 12 de octubre de 2026 – 17 de enero de 2027.  
**Repositorio:** [github.com/andres-olguin/DELIA](https://github.com/andres-olguin/DELIA)

### Ronda 3 — Evidencia, benchmark local y primeros activos para validación (31/10/2026)

**Estado real:** benchmark sintético ejecutado localmente con el detector exacto de `main`: **71 TP, 3 FP y 79 FN** en 150 entidades etiquetadas (precision **95,95 %**, recall **47,33 %**, F1 **63,39 %**). **No cumple una garantía de sanitización productiva**. Presidio, Cloudflare DLP y Google Model Armor **NO FUERON EJECUTADOS**; no se ha demostrado ventaja ante esos proveedores.

**Código:** 12 Issues P0/P1 creados; una propuesta de parche se preparó y probó localmente (6 tests lab pasaron, 2 warnings) pero **no existe rama ni PR**: el [ruleset `Proteccion-Main`](https://github.com/andres-olguin/DELIA/rules/25836222) prohíbe crear ramas por estar dirigido a `~ALL`, incluso ramas nuevas. [Issue #18 solicita corrección humana](https://github.com/andres-olguin/DELIA/issues/18). **No se subió código funcional a `main`**.

| Auditoría, evidencia y seguridad | Material comercial y validación |
|---|---|
| [Registro de investigación completo — Ronda 3](docs/REGISTRO_INVESTIGACION_RONDA3_2026-10-31.md) | [Foco comercial: integradores B2B2B; Brasil LGPD como fase 2](docs/FOCO_NICHO_Y_BRASIL_RONDA3_2026-10-31.md) |
| [Verificación de las 44 cuentas pendientes (CSV)](docs/VERIFICACION_44_CUENTAS_RONDA3.csv) | [One-pager para integradores](docs/ventas/ONE_PAGER_INTEGRADORES_RONDA3.md) |
| [235 fuentes clasificadas según lectura (CSV)](docs/REFERENCIAS_235_LECTURA_RONDA3.csv) | [Pitch de 30 segundos y mensajes](docs/ventas/PITCH_INTEGRADORES_RONDA3.md) |
| [Recalificación de 40 cuentas de ola 1 con evidencia LLM (CSV)](docs/OLA1_40_EVIDENCIA_LLM_RECALIFICACION_RONDA3.csv) | [Landing en español, lista de espera conceptual](docs/ventas/LANDING_ES_INTEGRADORES_WAITLIST_RONDA3.md) |
| [Marco legal de protección de datos y prospección por país](docs/MARCO_LEGAL_Y_PROSPECCION_RONDA3_2026-10-31.md) | [Tres artículos técnicos](docs/articulos/01_FUGAS_PII_PROMPTS_Y_MITIGACIONES.md) · [Artículo 2](docs/articulos/02_BENCHMARK_RUT_NIT_CURP.md) · [Artículo 3](docs/articulos/03_COMPARACION_HONESTA_GATEWAYS_IA.md) |
| [Corpus sintético etiquetado — 172 pruebas (JSONL)](benchmarks/synthetic_pii_r3.jsonl) | [Calendario editorial — 12 semanas (CSV)](docs/ventas/CALENDARIO_EDITORIAL_12_SEMANAS.csv) · [guía](docs/ventas/CALENDARIO_EDITORIAL_12_SEMANAS.md) |
| [Método y resultados del benchmark](benchmarks/README.md) | [Plan de reclutamiento — 24 entrevistas](docs/ventas/PLAN_24_ENTREVISTAS_RONDA3.md) |
| [Política de seguridad](SECURITY.md) · [plan TALIA→DELIA compatible](docs/PLAN_MIGRACION_TALIA_DELIA_2026-10-31.md) | [Carta de intención no vinculante](docs/ventas/CARTA_INTENCION_NO_VINCULANTE_RONDA3.md) · [encuesta Van Westendorp](docs/ventas/ENCUESTA_VAN_WESTENDORP_RONDA3.md) |
| [Issues P0/P1 #6–#17](https://github.com/andres-olguin/DELIA/issues) · [bloqueo de ramas #18](https://github.com/andres-olguin/DELIA/issues/18) | [Seis borradores de postulación a fondos](docs/ventas/BORRADORES_6_FONDOS_ACELERADORAS_RONDA3.md) · [tablero 13 semanas (CSV)](docs/ventas/TABLERO_METRICAS_13_SEMANAS_RONDA3.csv) |

**Calidad de evidencia:** 44 revisiones individuales → 8 páginas legibles, 10 extractos y 26 cuentas solo de directorio; 235 URLs → solo 7 páginas comprobadas íntegras en esta ronda, 224 con fragmentos o estado legado y 4 directorios. De la antigua ola 1 (40 cuentas), **8** se priorizan para investigación, **2** quedan en reserva, **30** se descartan de la primera ola por falta de señal pública suficientemente específica. Ninguna está confirmada como compradora DELIA.

**NO han ocurrido**: entrevistas con compradores, ensayos con datos reales de clientes, pilotos, contratos, cobros DELIA, despliegue productivo, postulación a fondos o lanzamiento de lista de espera. Los documentos de ventas son borradores, no campañas publicadas.

---

### Ronda 2 — Investigación comercial y kit de ventas (31/10/2026)

**Continuación de los estudios anteriores, sin sustituirlos.** Se amplió la prospección de 60 a **160 cuentas de investigación** (40 por país), con 25 posibles integradores de canal, puntuaciones exploratorias, fuentes con fechas y estados de comprobación explícitos, materiales de contacto y criterios para pilotos. **Ninguna empresa está clasificada como cliente interesado; todas las cuentas permanecen «no contactada».** La puntuación es una hipótesis operativa, no probabilidad estadística de compra.

| Investigación y planificación | Ventas y trabajo con compradores |
|---|---|
| [Estudio Ronda 2: incidentes, normativas, 15 competidores y estrategia](docs/ESTUDIO_RONDA2_PROFUNDIZACION_COMERCIAL_2026-10-31.md) | [One-pager comercial en español](docs/ventas/ONE_PAGER_DELIA_ES.md) |
| [160 cuentas B2B, 40 por país, puntuación y ola 1 (CSV)](docs/PROSPECTOS_RONDA2_160_CL_CO_MX_BO_2026-10-31.csv) | [Presentación comercial: guion de 12 láminas](docs/ventas/PRESENTACION_VENTAS_12_LAMINAS.md) |
| [25 integradores y consultoras, canal B2B2B (CSV)](docs/ALIANZAS_CANAL_25_RONDA2_2026-10-31.csv) | [Secuencias de 4 mensajes: 144 variantes por rol, país y canal](docs/ventas/SECUENCIAS_CONTACTO_4_PASOS.md) |
| [Financiación, aceleradoras, eventos y comunidades](docs/FONDOS_EVENTOS_COMUNIDADES_RONDA2_2026-10-31.md) | [Entrevista de descubrimiento: 30 minutos](docs/ventas/ENTREVISTA_DESCUBRIMIENTO_30_MIN.md) |
| [Modelo de costos y márgenes editable (CSV)](docs/MODELO_FINANCIERO_EDITABLE_RONDA2.csv) | [Demo de 10 minutos: datos sintéticos, no producción](docs/ventas/DEMO_SINTETICA_10_MIN.md) |
| [TAM/SAM/SOM: escenario editable sin denominadores inventados (CSV)](docs/ESCENARIOS_TAM_SAM_SOM_RONDA2.csv) | [Manual de 20 objeciones](docs/ventas/MANUAL_OBJECIONES_20.md) |
| [Riesgos P0/P1, puertas de validación y plan de 13 semanas](docs/RIESGOS_VALIDACION_PLAN_90_DIAS_RONDA2.md) | [Calculadora de ROI parametrizable (CSV)](docs/ventas/ROI_CALCULADORA.csv) |
| [Registro de investigación, vacíos y correcciones](docs/REGISTRO_INVESTIGACION_RONDA2_2026-10-31.md) | [Plantilla de piloto pagado de 30 días, sujeta a seguridad y revisión legal](docs/ventas/PLANTILLA_PILOTO_PAGADO_30_DIAS.md) |
| [Catálogo de 235 referencias con estado de comprobación (CSV)](docs/REFERENCIAS_Y_ESTADO_VERIFICACION_RONDA2.csv) | [CRM de entrevistas vacío (CSV): para utilizar solamente en espacio privado](docs/ventas/CRM_ENTREVISTAS.csv) |

**Cautela documental:** 202 enlaces del catálogo no figuraban en las 108 referencias del estudio anterior, pero **no son 202 fuentes íntegramente verificadas**: existen páginas solo identificadas, indexadas o pendientes de contrastación. Se revisó el contenido web corporativo de 116 de las 160 cuentas; para las otras 44 se indica expresamente la limitación. No se ejecutaron pruebas técnicas de DELIA ni entrevistas comerciales durante esta ronda.

**Bloqueo crítico:** no habilitar DELIA para datos reales o pilotos productivos antes de corregir inconsistencias de importación/API, autenticación y aislamiento, almacenamiento de prompts/secretos y falta de sanitización en el flujo de salida. Todo el material comercial identifica esas limitaciones.

---

**Investigación de mercado y estrategia comercial ampliada (31/10/2026):** [Estudio integral Chile, México, Colombia y Bolivia — 108 fuentes y auditoría del código](docs/INTELIGENCIA_MERCADO_GO_TO_MARKET_CL_MX_CO_BO_2026-10-31.md) · [60 empresas para investigación — CSV (15 por país)](docs/PROSPECTOS_B2B_CL_MX_CO_BO_2026-10-31.csv). **Todas las cuentas están no contactadas y no hay interés de compra de DELIA confirmado.**

**Investigación comercial (31/10/2026):** [Estudio de mercado B2B/B2C — Chile, México y Colombia](docs/ESTUDIO_MERCADO_B2B_B2C_CHILE_MEXICO_COLOMBIA_2026-10-31.md) · [Base de 12 cuentas observables para investigación (CSV)](docs/PROSPECTOS_OBSERVABLES_CL_MX_CO_2026-10-31.csv). Estos materiales presentan hipótesis de segmentación, fuentes y un protocolo de entrevistas; **no** acreditan compradores interesados ni demanda de DELIA validada.

> **Aviso de estado:** DELIA está en desarrollo. Los objetivos descritos en este documento no implican que todas las funciones estén implementadas, que el sistema esté listo para producción ni que garantice cumplimiento normativo. Los estados deben actualizarse a partir del código, las pruebas y las revisiones del equipo.

---

## ¿Por qué investigar DELIA?

Las empresas que integran APIs LLM deben decidir **qué datos envían al modelo, qué autorizaciones aplican, a qué proveedor llegan y qué evidencia conservan**. DELIA investiga una capa intermedia para centralizar esos controles en integraciones autorizadas. Su propuesta específica para Latinoamérica es medir la detección de identificadores locales y documentación de riesgos. **No intercepta conversaciones privadas de ChatGPT ni garantiza cumplimiento regulatorio.**

### Estado técnico y comercial al 31/10/2026

| Componente | Lo observado en el código `main` | Limitaciones |
|---|---|---|
| Detección de datos personales | Utilidades de patrones en `backend/dlp/pii.py` (RUT, NIT/cédula colombianos, email, teléfonos CL/CO, tarjetas) | Cobertura parcial; métricas de precisión y pruebas ejecutadas **no verificadas** |
| API/proxy/auditoría | Archivos FastAPI, HTTPX y modelos presentes | **Bloqueos P0**: importaciones/esquemas inconsistentes, rutas auditoría sin auth explícita, texto sensible en modelos y redacción no conectada con reenvío |
| México/Bolivia | Casos y documentos en investigación | CURP/RFC y CI/NIT bolivianos **no implementados** |
| Controles empresariales | Arquitectura y roadmap documentados | Autenticación multitenant, rate limiting real, fallback, dashboard, tokenización reversible, cifrado/vault **no demostrados** |
| Mercados y clientes | Investigación documental; 160 cuentas en lista de investigación (40 por país) | **0 compradores DELIA verificados**, no existen precios DELIA validados |

**Prioridad de entrega:** corregir P0, reproducir la suite de pruebas, medir sanitización en datos sintéticos, ejecutar un benchmark honesto y recién entonces discutir pilotos autorizados. Ver [informe integral y mapa de riesgos](docs/INTELIGENCIA_MERCADO_GO_TO_MARKET_CL_MX_CO_BO_2026-10-31.md).

### Casos de uso a validar, no funciones disponibles

- Un SaaS de RR.HH. que quiera impedir el envío accidental de identificaciones a un proveedor LLM.
- Una integración contable con NIT/RUT/CURP que necesite reglas documentadas para asistentes.
- Un integrador que deba configurar políticas independientes por cliente y monitorear uso.
- Un equipo de seguridad que requiera evidencia de decisiones de bloqueos sin guardar prompts sensibles.

### Comparación comercial honesta de alternativas

| Referente | Capacidades declaradas públicamente | Barrera para DELIA |
|---|---|---|
| [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/reference/pricing/) | Gateway central con funciones gratis, DLP con condiciones | Proxy y DLP genérico ya existen |
| [LiteLLM](https://www.litellm.ai/pricing) | Proxy multiproveedor OSS y herramientas de administración | OSS sin licencia pagada, pero requiere infraestructura |
| [Portkey](https://portkey.ai/pricing) | Gateway/guardrails; Production anunciado US$49/mes | Competidor comercial consolidado |
| [Google Model Armor](https://cloud.google.com/security-command-center/pricing) | Inspección de entradas/salidas; 2 millones de tokens/mes gratis, luego US$0,10/millón en modalidad publicada | Sanitización aislada enfrenta coste alternativo bajo |
| [Microsoft Presidio](https://microsoft.github.io/presidio/supported_entities/) | Detectores PII extensibles, software abierto | Reglas locales deben demostrar mejora real |
| [Azure AI Gateway (preview)](https://learn.microsoft.com/en-us/azure/api-management/ai-gateway-overview) | Auth, políticas, routing y telemetría, versión preliminar | Precio de preview por anunciar; capacidades del ecosistema |

**No se declara que DELIA iguale o supere estas soluciones.** Comparativa de doce alternativas, fechas, precios y límites: [informe ampliado](docs/INTELIGENCIA_MERCADO_GO_TO_MARKET_CL_MX_CO_BO_2026-10-31.md).

---

## Tabla de contenidos

- [1. Visión y propuesta de valor](#1-visión-y-propuesta-de-valor)
- [2. Problema y alcance](#2-problema-y-alcance)
- [3. Estado de implementación](#3-estado-de-implementación)
- [4. Arquitectura objetivo](#4-arquitectura-objetivo)
- [5. Flujo de procesamiento](#5-flujo-de-procesamiento)
- [6. Sanitización y tratamiento de PII](#6-sanitización-y-tratamiento-de-pii)
- [7. Seguridad por diseño](#7-seguridad-por-diseño)
- [8. Marco regulatorio de referencia](#8-marco-regulatorio-de-referencia)
- [9. Stack tecnológico](#9-stack-tecnológico)
- [10. Inicio rápido](#10-inicio-rápido)
- [11. Ejemplo conceptual](#11-ejemplo-conceptual)
- [12. Pruebas y criterios de aceptación](#12-pruebas-y-criterios-de-aceptación)
- [13. Roadmap y Carta Gantt](#13-roadmap-y-carta-gantt)
- [14. Objetivos y métricas de éxito](#14-objetivos-y-métricas-de-éxito)
- [15. Equipo y metodología](#15-equipo-y-metodología)
- [16. Riesgos y limitaciones conocidas](#16-riesgos-y-limitaciones-conocidas)
- [17. Contribuciones](#17-contribuciones)
- [18. Licencia](#18-licencia)

## 1. Visión y propuesta de valor

Las aplicaciones basadas en LLMs pueden procesar información personal, datos comerciales confidenciales y secretos operativos. Si esos datos se envían a servicios externos sin controles apropiados, una organización puede perder visibilidad sobre qué información se comparte, cómo se aplican sus políticas y qué evidencia conserva para investigar incidentes.

DELIA busca centralizar controles técnicos en una capa intermedia entre las aplicaciones cliente y los proveedores de modelos de lenguaje. La propuesta combina detección y sanitización de datos sensibles, control de consumo, intermediación con proveedores y registro de eventos de seguridad.

### Capacidades objetivo

- **Sanitización de PII:** detectar patrones definidos y sustituir los valores antes de remitir la solicitud al proveedor.
- **DLP para flujos de IA:** reducir la exposición accidental de datos cubiertos por las reglas configuradas.
- **Rate limiting:** aplicar cuotas por cliente, identidad o política.
- **Proxy de proveedores:** normalizar el acceso a distintos proveedores de LLMs.
- **Streaming:** transmitir respuestas progresivamente cuando el adaptador y el proveedor lo permitan.
- **Fallback:** gestionar fallos del proveedor primario según políticas explícitas.
- **Auditoría:** registrar eventos operativos y de seguridad minimizando el contenido sensible almacenado.
- **Panel de control:** facilitar la supervisión de métricas y alertas en una fase posterior.

Estas capacidades son objetivos del proyecto. Su disponibilidad depende de la implementación y validación de cada módulo.

### Principio rector

**No se avanza por calendario; se avanza por evidencia.** Los sprints definen el rumbo y las fechas objetivo. La aceptación de cada entrega depende de criterios verificables, pruebas y revisión del equipo.

## 2. Problema y alcance

DELIA se orienta inicialmente a equipos que integran LLMs en aplicaciones corporativas y necesitan controles técnicos más centralizados sobre los datos enviados a proveedores externos.

Entre los datos que pueden requerir protección se encuentran:

- identificadores personales, como RUT chileno, cédulas y NIT colombianos;
- correos electrónicos y números de teléfono;
- credenciales, claves API y otros secretos;
- información comercial o contractual confidencial;
- otros datos que una organización clasifique como sensibles.

Un proxy no elimina por sí solo todos los riesgos asociados al uso de IA. La detección por patrones no cubre necesariamente información expresada en lenguaje natural, el tratamiento que realiza un proveedor externo depende de sus condiciones y configuración, y la seguridad también depende de autenticación, gestión de claves, políticas de registro, controles de salida y operación.

El alcance inicial prioriza una base técnica que pueda validarse progresivamente, sin presentar como resueltas capacidades que aún están planificadas.

## 3. Estado de implementación

La siguiente matriz combina el estado declarado y el cronograma maestro. Debe revisarse al cerrar cada tarea y no sustituye la comprobación del repositorio.

| Módulo | Estado declarado | Alcance y criterio general |
|---|---|---|
| Naming y estructura del repositorio | Completado — Sprint 1 | Repositorio organizado bajo la identidad DELIA. |
| Documentación regulatoria inicial | Completado — Sprint 1 | Documento de viabilidad para Chile y Colombia en `/docs/`, sujeto a revisión periódica. |
| Entorno base de Docker Compose | Completado — Sprint 1 | Configuración inicial, `.env.example` y conectividad base; debe validarse desde un clon limpio. |
| Regex para cédula y NIT colombianos | En desarrollo — Sprint 2 | Reglas por tipo de identificador, casos borde y validación según corresponda. |
| Validación de RUT chileno | En desarrollo — Sprint 2 | Algoritmo de dígito verificador y pruebas unitarias. |
| Script inicial de sanitización | En desarrollo — Sprint 2 | Sanitización de texto plano antes del envío al LLM. |
| Modelos de auditoría y migraciones | Planificado dentro del Sprint 2 | Modelos relacionales en PostgreSQL mediante SQLAlchemy y Alembic. La persistencia de eventos se completa en etapas posteriores. |
| Interfaz de middleware de sanitización | Planificado dentro del Sprint 2 | Integración de la lógica de sanitización en FastAPI y revisión de código. |
| Redis: rate limiting y caché | Planificado — Sprint 3 | Cuotas por usuario/cliente, caché y pruebas de carga iniciales. |
| Proxy HTTP asíncrono y SSE | Planificado — Sprint 4 | Adaptador mediante HTTPX, streaming y manejo de errores. |
| Fallback entre proveedores | Planificado — Sprint 4 | Reintentos y selección alternativa sujetos a política, timeout y compatibilidad. |
| Auditoría y endpoints de consulta | Planificado — Sprint 5 | Registro de eventos, consultas protegidas y revisión de seguridad. |
| Dashboard | Planificado — Sprint 6 | Frontend React para métricas de tráfico y alertas. |
| Pruebas de carga y release | Planificado — Sprint 6 | Pruebas con herramientas como Locust, optimización y empaquetado. |
| Piloto controlado Chile/Colombia | Planificado — Sprint 7 | Despliegue, onboarding, seguimiento de incidencias y evaluación del piloto. |

**Regla de estado:** una tarea no se considera completada solo porque exista un archivo. Debe cumplir sus criterios de aceptación y contar con evidencia de prueba o revisión adecuada.

## 4. Arquitectura objetivo

El diseño ubica a DELIA entre la aplicación cliente y el proveedor de LLM. Los componentes discontinuos representan integraciones que, según el roadmap, todavía deben implementarse.

```mermaid
flowchart TD
    C[Aplicación cliente / agente IA] -->|Solicitud HTTP| P[DELIA Proxy Core]
    P --> A[Validación y controles de acceso]
    A --> Q[Políticas y cuotas]
    Q -.-> R[(Redis: cuotas y caché)]
    Q --> S[Motor de sanitización PII]
    S --> H[Adaptador HTTP asíncrono]
    H --> L[Proveedor LLM externo]
    L --> H
    H --> P
    P -.-> E[Servicio de eventos de auditoría]
    E -.-> D[(PostgreSQL)]
    P --> C
    P -.-> UI[Dashboard React]
```

El diagrama representa la arquitectura prevista, no una afirmación de que todas las conexiones estén operativas actualmente.

### Responsabilidades propuestas

- **Proxy Core:** coordinar el ciclo de vida de una solicitud y su respuesta.
- **Validación y acceso:** validar esquemas y, cuando esté implementado, autenticar y autorizar clientes.
- **Políticas y cuotas:** aplicar límites de consumo y decisiones de política.
- **Motor de sanitización:** detectar y sustituir patrones admitidos.
- **Adaptador HTTP:** aislar las diferencias entre APIs de proveedores, gestionar timeouts y traducir errores.
- **Auditoría:** producir eventos con minimización de datos y controles de acceso.
- **Dashboard:** exponer métricas y alertas autorizadas sin revelar contenido sensible innecesario.

### Decisiones de arquitectura pendientes

Antes de una versión de piloto se deben definir y probar: comportamiento ante fallo del sanitizador; timeouts y límites de tamaño; autenticación de clientes; gestión de claves de proveedores; destinos de salida permitidos; tratamiento de errores; retención de logs; aislamiento entre clientes; y comportamiento de seguridad cuando Redis, PostgreSQL o un proveedor no estén disponibles.

## 5. Flujo de procesamiento

El flujo funcional objetivo es:

1. **Recepción:** aceptar una solicitud HTTP en un endpoint documentado.
2. **Validación:** comprobar el esquema, tipos, campos y límites de tamaño.
3. **Autenticación y autorización:** verificar identidad y permisos según la configuración disponible.
4. **Políticas de consumo:** aplicar cuotas y restricciones, una vez implementadas.
5. **Sanitización:** detectar patrones cubiertos por las reglas y reemplazar valores según la política.
6. **Reenvío:** enviar el contenido procesado al proveedor seleccionado.
7. **Respuesta:** procesar la respuesta y aplicar controles de salida cuando estén implementados.
8. **Auditoría:** registrar eventos relevantes evitando guardar prompts, respuestas o secretos completos por defecto.
9. **Entrega:** devolver al cliente una respuesta con códigos y formato definidos.

Los pasos que dependen de módulos planificados no deben considerarse disponibles en la versión actual.

## 6. Sanitización y tratamiento de PII

El motor inicial utiliza expresiones regulares para identificar patrones estructurados. Las reglas deberán ser específicas por país y categoría, y contar con pruebas positivas y negativas.

### Ejemplo conceptual

**Entrada:**

```text
Analiza el caso del cliente con RUT 12.345.678-5 y correo contacto@empresa.cl.
```

**Salida deseada hacia el proveedor:**

```text
Analiza el caso del cliente con RUT [RUT_OCULTO] y correo [EMAIL_OCULTO].
```

Este ejemplo ilustra el resultado esperado. No demuestra que la implementación actual detecte correctamente esos valores; debe validarse con una ejecución real y pruebas automatizadas antes de presentarlo como evidencia.

### Reglas de diseño

- Separar detección sintáctica de validación semántica.
- Validar el dígito verificador del RUT chileno mediante el algoritmo correspondiente.
- Tratar cédula y NIT colombianos como categorías distintas, sin asumir que comparten un formato universal.
- Documentar formatos admitidos y casos no cubiertos.
- Medir falsos positivos y falsos negativos con datos sintéticos.
- Evitar registrar el texto original o los valores detectados innecesariamente.
- Versionar las reglas y conservar pruebas de regresión.

### Sanitización no es cifrado

- **Sanitización:** reemplaza valores por marcadores.
- **Enmascaramiento:** oculta total o parcialmente un valor.
- **Tokenización:** sustituye un valor por un token asociado mediante un mecanismo controlado.
- **Cifrado:** transforma datos mediante un algoritmo criptográfico y claves.

La sustitución por `[RUT_OCULTO]` no es cifrado. Si DELIA incorpora tokenización reversible, deberá definir dónde se guarda la correspondencia, quién puede recuperarla, cómo se protegen las claves y cómo se separan los entornos de clientes. No debe anunciarse cifrado funcional hasta que exista una implementación verificable.

Las expresiones regulares tampoco garantizan detectar nombres, datos contextuales, secretos arbitrarios ni toda forma de información personal.

## 7. Seguridad por diseño

Los siguientes puntos son requisitos que deben implementarse y verificarse antes de considerar DELIA adecuado para un entorno sensible.

| Área | Control requerido |
|---|---|
| Acceso | Autenticación y autorización de clientes. |
| Secretos | Claves API y contraseñas fuera del código y del control de versiones. |
| Transporte | TLS en despliegues fuera de un entorno local controlado. |
| Entrada | Validación de esquema, tamaño y contenido permitido. |
| Salida | Definición de controles para respuestas y errores. |
| Logs | Minimización, redacción de datos y política de retención. |
| Persistencia | Permisos mínimos y acceso restringido. |
| Egreso de red | Lista de destinos permitidos y mitigación de SSRF. |
| Disponibilidad | Timeouts, límites de tamaño y concurrencia. |
| Dependencias | Revisión de vulnerabilidades y actualizaciones. |
| Aislamiento | Separación lógica y de permisos entre clientes. |
| Pruebas | Casos de abuso, fallos parciales y regresiones de seguridad. |

### Modelo de amenazas inicial

El análisis debe incluir clientes no autorizados, abuso de cuotas, exposición de claves API, evasión de reglas de sanitización, prompt injection, registro accidental de datos sensibles, respuestas inesperadas de proveedores, destinos externos no autorizados, fallos de dependencias y errores de aislamiento entre clientes.

DELIA no debe presentarse como defensa completa contra prompt injection o exfiltración de datos sin controles específicos y pruebas que respalden esa afirmación.

## 8. Marco regulatorio de referencia

DELIA considera inicialmente los marcos de protección de datos de Chile y Colombia. El objetivo es desarrollar controles técnicos que puedan contribuir a las obligaciones de las organizaciones, no certificar cumplimiento por medio del software.

### Chile

- [Ley N.º 21.719 — Biblioteca del Congreso Nacional](https://www.bcn.cl/leychile/navegar?idNorma=1209272): reforma el marco de protección y tratamiento de datos personales.
- [Ley N.º 19.628 — Biblioteca del Congreso Nacional](https://www.bcn.cl/leychile/navegar?i=141599): marco legal de referencia cuya aplicación debe revisarse conforme a la legislación vigente y sus modificaciones.
- Para organizaciones financieras, deben revisarse también las reglas aplicables de la Comisión para el Mercado Financiero (CMF), incluida la normativa de externalización y servicios en la nube que corresponda.

### Colombia

- [Ley Estatutaria 1581 de 2012 — SIC](https://sedeelectronica.sic.gov.co/transparencia/normativa/ley-estatutaria-1581-de-2012): marco general de protección de datos personales.
- [Superintendencia de Industria y Comercio (SIC)](https://www.sic.gov.co/): fuente para consultar normativa, instrucciones y orientaciones vigentes.
- Para entidades financieras, deben revisarse además las instrucciones pertinentes de la Superintendencia Financiera de Colombia (SFC).

### Alcance de cumplimiento

El uso de sanitización, cifrado, auditoría o controles de acceso no garantiza por sí solo cumplimiento legal. La aplicabilidad depende del contexto, los roles de los actores, las finalidades del tratamiento, los contratos, las transferencias de datos y la configuración operacional.

Antes de un piloto con datos reales se recomienda validar con asesoría jurídica especializada: categorías de datos tratados, roles de responsable/encargado, flujos y destinos, retención, gestión de incidentes y obligaciones sectoriales.

El documento de investigación de mercado y viabilidad regulatoria debe mantenerse en `/docs/` y revisarse conforme cambie la normativa. Las conclusiones de ese documento son análisis de trabajo, no asesoría jurídica.

## 9. Stack tecnológico

El stack oficial definido para el proyecto es el siguiente. La inclusión de una tecnología en esta tabla indica que forma parte de la arquitectura seleccionada; no significa que su integración esté completa.

| Capa | Tecnología | Uso previsto |
|---|---|---|
| Backend y API | Python 3.11+, FastAPI, Pydantic | API HTTP, lógica de aplicación y validación de datos. |
| Cliente HTTP | HTTPX | Comunicación asíncrona con proveedores; SSE cuando esté implementado. |
| Caché y rate limiting | Redis | Cuotas compartidas y caché controlada. |
| Base de datos | PostgreSQL | Persistencia de eventos y datos operativos definidos. |
| ORM y migraciones | SQLAlchemy, Alembic | Modelos relacionales y evolución del esquema. |
| Contenerización | Docker, Docker Compose | Entorno de desarrollo y servicios. |
| Servidor | Linux / Ubuntu Server | Entorno de despliegue previsto. |
| Panel de control | React, Bootstrap o Tailwind CSS | Interfaz de métricas y alertas; el framework de estilos definitivo debe quedar registrado en las decisiones del proyecto. |
| Pruebas de carga | Locust u otra herramienta validada | Medición de latencia, concurrencia y estabilidad. |

## 10. Inicio rápido

> **Nota:** los comandos siguientes son una guía inicial. Antes de declarar esta sección verificada, comprueba que los archivos y servicios nombrados existen en la rama publicada y ejecuta el procedimiento desde un clon limpio.

### 10.1 Clonar el repositorio

```bash
git clone https://github.com/andres-olguin/DELIA.git
cd DELIA
```

### 10.2 Inspeccionar la configuración

```bash
git status
git branch --show-current
```

Comprueba si el repositorio utiliza `compose.yaml`, `compose.yml`, `docker-compose.yml`, `pyproject.toml` o `requirements.txt`. Sigue el gestor de dependencias y el archivo Compose presentes, sin asumir que todos existen.

### 10.3 Variables de entorno

Si existe `.env.example`, crea una copia local.

Linux/macOS:

```bash
cp .env.example .env
```

Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

Configura únicamente las variables documentadas por la aplicación. No guardes claves API, contraseñas ni datos reales en el repositorio. `.env` debe estar excluido del control de versiones.

### 10.4 Entorno Python opcional

Si el proyecto permite ejecutar el backend localmente y declara dependencias en `requirements.txt`:

```bash
python -m venv .venv
```

Activación en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Activación en Linux/macOS:

```bash
source .venv/bin/activate
```

Instalación de dependencias:

```bash
python -m pip install -r requirements.txt
```

Si el proyecto utiliza otro gestor, sigue la configuración que realmente exista.

### 10.5 Docker Compose

Si existe un archivo Compose válido:

```bash
docker compose up --build -d
docker compose ps
docker compose logs --tail=100
```

Para detener el entorno:

```bash
docker compose down
```

El resultado depende de los servicios, puertos y variables configurados en el repositorio.

### 10.6 Documentación de API

Si FastAPI está configurado para publicar Swagger UI, la ruta suele ser `/docs` en el host y puerto configurados, por ejemplo `http://127.0.0.1:8000/docs`. Confirma el puerto y la disponibilidad en la configuración real.

## 11. Ejemplo conceptual

El siguiente ejemplo representa el comportamiento deseado de una futura interfaz. No se afirma que exista un endpoint con este esquema en la versión actual.

**Solicitud original:**

```json
{
  "message": "Analiza el caso del cliente con RUT 12.345.678-5 y correo contacto@empresa.cl."
}
```

**Contenido esperado tras la sanitización:**

```json
{
  "message": "Analiza el caso del cliente con RUT [RUT_OCULTO] y correo [EMAIL_OCULTO]."
}
```

Para convertir este ejemplo en evidencia funcional se necesita un endpoint implementado, una ejecución reproducible, una prueba automatizada y una comprobación de que los registros no guardan el contenido sensible innecesariamente.

## 12. Pruebas y criterios de aceptación

### Pruebas unitarias

- RUT con dígito verificador válido e inválido.
- Formatos admitidos de cédula y NIT colombianos.
- Puntos, guiones, espacios y variaciones de escritura.
- Múltiples datos sensibles en un mismo texto.
- Entradas vacías, malformadas y casos límite.
- Falsos positivos y patrones no reconocidos.

### Pruebas de integración

- Validación de solicitudes HTTP.
- Coordinación entre middleware y sanitizador.
- Comunicación con proveedores simulados.
- Timeouts, respuestas inválidas y errores de proveedor.
- Persistencia de eventos cuando el módulo esté disponible.
- Comportamiento cuando una dependencia no responde.

### Pruebas de seguridad

- Acceso sin credenciales válidas.
- Abuso de cuotas y concurrencia.
- Exposición de secretos en logs y errores.
- Entradas excesivamente grandes o malformadas.
- Destinos de salida no autorizados.
- Aislamiento entre clientes.
- Fallos del sanitizador y política de fallo seguro.

### Criterio de aceptación

Una tarea puede declararse completada cuando cumple sus criterios de aceptación, tiene pruebas pertinentes, maneja errores previstos, dispone de documentación reproducible y ha pasado la revisión acordada. Las pruebas reducen riesgos conocidos, pero no demuestran ausencia total de vulnerabilidades.

## 13. Roadmap y Carta Gantt

Las fechas son objetivos de planificación. Los entregables pueden cambiar si aparecen riesgos, dependencias o resultados de validación que lo justifiquen.

| Sprint | Período | Objetivo y entregables principales | Hito |
|---|---|---|---|
| **1. Fundación, naming y viabilidad** | 12–25 oct. 2026 | Naming DELIA, estructura del repositorio, documento inicial de viabilidad regulatoria, Docker Compose base, `.env.example` y conectividad del entorno. | Completado según el roadmap; verificar los entregables en el repositorio. |
| **2. Sanitización PII y regex** | 26 oct.–8 nov. 2026 | Regex para cédula/NIT colombianos; algoritmo Módulo 11 para RUT chileno; script de sanitización de texto plano; modelos PostgreSQL con SQLAlchemy/Alembic para auditoría; interfaz de middleware FastAPI y code review. | **Hito 1 — 8 nov.:** validación ejecutiva y del alcance regulatorio inicial del motor PII. |
| **3. Tráfico, rate limiting y caché** | 9–22 nov. 2026 | Redis en Docker Compose; límites por minuto; caché para consultas repetidas con políticas de aislamiento; integración con rutas asíncronas; pruebas iniciales de estrés y latencia. | **Hito 2 — 22 nov.:** revisión de costos proyectados y umbrales de latencia. |
| **4. Proxy inverso y fallback de LLMs** | 23 nov.–6 dic. 2026 | Cliente HTTP asíncrono con HTTPX; soporte SSE; fallback ante fallos o timeouts; pruebas E2E con mocks de proveedores. | **Hito 3 — 6 dic.:** aprobación del flujo funcional para demostración interna. |
| **5. Auditoría y persistencia de logs** | 7–20 dic. 2026 | Registro transaccional de eventos críticos; endpoints seguros para consultar logs; documentación de despliegue, arquitectura e integración; revisión del almacenamiento y cifrado de registros. | **Hito 4 — 20 dic.:** revisión interna de seguridad de auditoría. |
| **6. Dashboard y pruebas de carga** | 21 dic. 2026–3 ene. 2027 | Panel React con métricas y alertas; pruebas de carga (por ejemplo, Locust); optimización de índices; release inicial y revisión de manuales/variables. | **Hito 5 — 3 ene.:** aprobación para entorno de pruebas controlado y definición de métricas del piloto. |
| **7. Piloto comercial Chile/Colombia** | 4–17 ene. 2027 | Despliegue en servidor cloud, dominio y TLS; onboarding de usuarios de prueba; monitoreo de incidencias, falsos positivos y rendimiento; evaluación de resultados. | **17 ene.:** cierre del ciclo inicial y evaluación del piloto. |

### Dependencias importantes

- El motor de sanitización del Sprint 2 debe integrarse con el pipeline de tráfico del Sprint 3.
- El proxy y el fallback del Sprint 4 dependen de contratos de interfaz estables y pruebas con proveedores simulados.
- Los modelos de datos iniciados en Sprint 2 no equivalen a auditoría funcional completa: la captura de eventos, consultas y revisión de seguridad se completan progresivamente.
- El piloto del Sprint 7 solo debe procesar datos reales si se han aprobado los controles, la configuración, el alcance contractual y el análisis de riesgos necesarios.

El desglose de tareas, responsables y fechas debe mantenerse en [`docs/roadmap.md`](docs/roadmap.md), siempre que ese archivo exista en la rama publicada. La investigación de mercado y viabilidad regulatoria debe mantenerse en un documento separado dentro de `/docs/`.

## 14. Objetivos y métricas de éxito

El roadmap propone objetivos iniciales. No son resultados alcanzados ni garantías de servicio.

| Métrica | Objetivo provisional | Cómo debe medirse |
|---|---|---|
| Sobrecarga de latencia | Promedio inferior a 45 ms por solicitud procesada | Definir punto de medición, tamaño de solicitud, proveedor simulado/real, concurrencia y percentiles. |
| Sobrecarga en streaming | No superar 50 ms según el objetivo del roadmap | Precisar si se mide el tiempo hasta el primer byte/token, la latencia por fragmento o la sobrecarga total. |
| Disponibilidad | ≥ 99,9 % | Definir período, exclusiones, endpoint de salud y método de cálculo. |
| Detección de PII | 100 % en el conjunto de documentos normados de prueba | Delimitar el corpus, categorías, formatos y criterios; medir también falsos positivos. No equivale a 100 % de detección en todos los datos del mundo real. |
| Resiliencia de proveedor | Fallback ante fallos cubiertos por la política | Pruebas reproducibles de timeout, errores HTTP y proveedor no disponible. |
| Seguridad de logs | Sin exposición de valores sensibles en casos de prueba definidos | Pruebas de redacción, revisión de logs y verificación de permisos. |

### Resolver una discrepancia de latencia

El roadmap contiene dos objetivos: menos de 45 ms de latencia promedio y un máximo de 50 ms de sobrecarga en streaming. No son necesariamente contradictorios, pero **no son comparables hasta definir exactamente qué mide cada uno**. Antes de declarar cumplimiento, el equipo debe especificar si la métrica es promedio, p95/p99, tiempo hasta el primer token o sobrecarga atribuible exclusivamente a DELIA.

### Cómo informar resultados

Cuando existan pruebas, publicar la configuración del entorno, la versión del código, la carga aplicada, el tamaño de las solicitudes, el número de ejecuciones y los resultados. No presentar objetivos como benchmarks obtenidos.

## 15. Equipo y metodología

### Roles declarados

| Integrante | Rol | Responsabilidades principales |
|---|---|---|
| Andrés | Líder técnico / arquitectura y desarrollo core | FastAPI, clientes HTTP asíncronos, arquitectura e integración; dashboard según el roadmap. |
| Iván | Scrum Master y desarrollador | Ciberseguridad, DLP, expresiones regulares, documentación y coordinación de ceremonias. |
| Nilson | Backend, base de datos e infraestructura | PostgreSQL, Redis, SQLAlchemy, Alembic, Docker y contenedorización. |
| Isaac | COO | Gestión, operaciones, validación regulatoria, definición de pilotos y estrategia comercial. |

### Flujo de trabajo

1. Definir historias de usuario y criterios de aceptación.
2. Dividirlas en tareas técnicas y registrar dependencias.
3. Asignar responsables y fechas objetivo.
4. Desarrollar en cambios pequeños y revisables.
5. Ejecutar pruebas pertinentes.
6. Revisar cambios antes de integrarlos.
7. Actualizar documentación y estado de implementación.
8. Registrar bloqueos, riesgos y decisiones técnicas.

### Convenciones sugeridas

Ejemplos de ramas:

```text
feature/pii-sanitization
feature/provider-adapter
fix/rut-validation
test/security-regression
docs/architecture
```

Ejemplos de commits:

```text
feat: add initial PII sanitization rules
fix: validate supported RUT formats
test: cover sanitization edge cases
docs: clarify proxy security boundaries
```

Son convenciones sugeridas, no ramas ni funcionalidades cuya existencia se afirme.

## 16. Riesgos y limitaciones conocidas

| Riesgo | Impacto potencial | Mitigación prevista |
|---|---|---|
| Falsos positivos de PII | Bloqueo o alteración de contenido legítimo | Casos borde, corpus sintético y sensibilidad configurable cuando corresponda. |
| Falsos negativos | Exposición de datos no detectados | Ampliar categorías, medir recall y documentar límites de cobertura. |
| Latencia de streaming | Experiencia de usuario degradada | Benchmarks reproducibles y pruebas de carga en Sprints 3 y 6. |
| Caída de proveedores | Solicitudes fallidas o demora | Timeouts, clasificación de errores y fallback controlado en Sprint 4. |
| Fuga en logs | Exposición centralizada de información sensible | Minimización, redacción, permisos y revisión de seguridad. |
| Compromiso de DELIA | Exposición de datos procesados por el proxy | Mínimo privilegio, protección de secretos, segmentación y evaluación de amenazas. |
| Dependencia de plataformas | Funciones similares incorporadas por proveedores cloud | Validar diferenciación en precisión local, integración, operación y evidencia de gobernanza. |
| Cambio normativo | Controles o documentación desactualizados | Seguimiento de fuentes oficiales y revisión jurídica especializada. |

### Limitaciones técnicas

- Las regex cubren solo los patrones definidos y no detectan toda la información personal.
- Sanitizar la entrada no garantiza que la respuesta del modelo no contenga información sensible.
- El proveedor externo sigue sujeto a sus propias condiciones de procesamiento y retención.
- La seudonimización reversible puede seguir implicando tratamiento de datos personales, según el contexto y la normativa aplicable.
- No se han establecido garantías de rendimiento hasta ejecutar pruebas reproducibles.
- No se debe considerar DELIA listo para producción solo porque finalice el Sprint 7; el piloto requiere aprobación de seguridad, operación y alcance legal.

## 17. Contribuciones

Las contribuciones deben mejorar la seguridad, mantenibilidad, documentación y reproducibilidad.

1. Revisar el roadmap y acordar el alcance antes de comenzar.
2. Crear una rama por cambio.
3. Añadir pruebas para el comportamiento nuevo o corregido.
4. Actualizar documentación afectada.
5. Abrir una solicitud de integración con una descripción y evidencia claras.
6. Resolver observaciones antes de integrar.

Reglas básicas:

- No incluir secretos ni datos personales reales en commits, pruebas o capturas.
- Utilizar datos sintéticos para los fixtures.
- No desactivar controles para hacer pasar pruebas.
- Justificar dependencias nuevas.
- Documentar cambios que afecten el tratamiento de datos.
- Reportar vulnerabilidades de forma responsable por el canal que el equipo defina.

## 18. Licencia

El proyecto declara la intención de utilizar la licencia MIT. Consulta [`LICENSE`](LICENSE) para los términos efectivos. Esta sección debe conservarse solo si el archivo existe y contiene el texto de la licencia correspondiente.

---

## Compromiso de DELIA

DELIA busca evolucionar hacia una capa de seguridad y gobernanza para aplicaciones basadas en inteligencia artificial. Su credibilidad dependerá de que cada capacidad se demuestre con código, pruebas, documentación y resultados reproducibles.

**La prioridad es reducir riesgos concretos y demostrar cada control antes de presentarlo como garantía de seguridad, rendimiento o cumplimiento normativo.**
