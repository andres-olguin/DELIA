# DELIA — One-pager comercial (versión de investigación, NO oferta de producto listo)

**MasterTech SpA | DELIA (Data Encryption & Limiting Intelligence Agent)**  
**Versión:** 31/10/2026 · **Estado:** desarrollo técnico y descubrimiento de compradores.  
**Contacto corporativo:** [mastertechg.com](https://mastertechg.com) · [contacto@mastertechg.com](mailto:contacto@mastertechg.com).

## El problema

Cuando una aplicación empresarial utiliza una API de un modelo de IA, el equipo debe decidir **qué datos personales o secretos pueden salir**, qué proveedor los recibe, quién autorizó la llamada, cuánto cuesta y cómo se conserva evidencia. Muchas organizaciones ya utilizan Cloudflare, LiteLLM, Azure u otras soluciones: **no presumimos que estén desprotegidas**.

## Qué estamos construyendo

**DELIA investiga una capa de control entre aplicaciones autorizadas y proveedores LLM**, con aspiración de detectar/minimizar identificadores regionales, aplicar políticas por aplicación y documentar decisiones sin conservar prompts sensibles innecesarios.

**Lo que existe hoy:** funciones parciales en código para detectar y sustituir algunas categorías de PII (RUT CL, NIT/cédula CO, email/teléfono/tarjetas), modelos y estructura FastAPI. **Lo que NO está demostrado:** servicio listo para producción, autenticación multitenant, gateway integrado, cifrado reversible, precisión medida, soporte de CURP/RFC o Bolivia, cumplimiento normativo o certificaciones. Los hallazgos P0 están descritos en la [auditoría](../INTELIGENCIA_MERCADO_GO_TO_MARKET_CL_MX_CO_BO_2026-10-31.md).

## A quién queremos escuchar

| Perfil | Pregunta que queremos resolver | Resultado a demostrar en el futuro |
|---|---|---|
| **Integrador de agentes / CTO** | ¿Repiten filtros y logging para cada cliente LLM? | Integración más rápida y políticas compartimentadas |
| **CISO / DPO** | ¿Qué datos salen y qué pueden auditar? | Medición de minimización, bloqueos y evidencia sin PII |
| **SaaS contable / RR.HH.** | ¿RUT, NIT, CURP y documentos se envían sin necesidad? | Benchmark de identificadores locales |
| **Gerente general** | ¿Qué trabajo manual o riesgo está costando dinero hoy? | ROI sustentado en datos propios del piloto |

## Por qué hablar con MasterTech

Conocemos el contexto técnico de integraciones B2B de la región y buscamos demostrar un enfoque centrado en identificadores latinoamericanos. **No declaramos tener precisión superior ni clientes de DELIA** hasta medirlo. Inicialmente proponemos una **entrevista de 20–30 minutos**, sin pedir datos personales reales ni compartir secretos.

## Próxima conversación

1. Revisar un flujo real de IA de forma descriptiva, sin entregar prompts confidenciales.
2. Identificar qué controles ya utilizan y dónde hay una brecha concreta.
3. Evaluar si corresponde comparar alternativas con **datos 100 % sintéticos**.
4. Solo con P0 resuelto, acordar un piloto escrito y pagado, si hay interés y capacidad técnica.

**Propuesta de valor en una frase:** «DELIA busca permitir que equipos con aplicaciones LLM controlen qué datos envían, bajo qué políticas y con qué evidencia; comenzando por necesidades de identificación y gobierno en Latinoamérica».

**Nota:** la legislación de datos puede crear obligaciones para las organizaciones, **pero la instalación de DELIA no garantiza cumplimiento**. Comparativa de precios, normativa y riesgos en el [estudio completo](../ESTUDIO_RONDA2_PROFUNDIZACION_COMERCIAL_2026-10-31.md).
