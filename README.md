# TALIA — AI Security Proxy & Compliance Gateway

**TALIA** es un proxy inverso y *gateway* de seguridad diseñado específicamente para equipos que desarrollan agentes de inteligencia artificial en entornos corporativos y regulados (Latinoamérica). Su función principal es interceptar las peticiones a LLMs externos para aplicar sanitización de datos (DLP), control de cuotas (*rate limiting*) y enrutamiento con *fallback* automático, asegurando el cumplimiento normativo local.

---

## 🎯 Propuesta de Valor y Viabilidad de Mercado
Frente a pasarelas genéricas en la nube (como AWS Bedrock o Azure AI), TALIA se diferencia por:
- **Identificadores Locales:** Soporte nativo y validación estricta para documentos de identidad de la región (como el RUT chileno mediante módulo 11 y cédulas/NIT colombianos).
- **Cumplimiento Normativo Local:** Adaptado para mitigar riesgos bajo la **Ley 21.719 de Protección de Datos en Chile** y las directrices de la **SIC (Circular Externa 002 de 2024)** y **SFC** en Colombia[cite: 5].
- **Enmascaramiento Reversible:** Protege la privacidad antes de enviar información a modelos externos (OpenAI, Anthropic, etc.) manteniendo la trazabilidad necesaria para los flujos de agentes autónomos.

> 📄 **Documentación Estratégica:** Para un desglose completo sobre la viabilidad regulatoria, análisis de la competencia y estrategia de entrada por país, consulta el documento en [`docs/viabilidad-mercado-colombia-chile.md`](docs/viabilidad-mercado-colombia-chile.md)[cite: 5].

---

## 🏗️ Arquitectura del Proyecto (Sprint 2)
El sistema se compone de una arquitectura modular basada en microservicios ligeros:
- **Proxy Asíncrono (`FastAPI`):** Interceptación de peticiones HTTP en tiempo real.
- **Capa DLP / Sanitización:** Detección de expresiones regulares y enmascaramiento de PII.
- **Control de Tráfico y Caché (`Redis`):** Gestión de cuotas de tokens y límites por usuario.
- **Base de Datos de Auditoría (`PostgreSQL`):** Registro de logs transaccionales y de seguridad.

---

## 🚀 Guía de Inicio Rápido (Local)

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/andres-olguin/Proyecto-TALIA.git](https://github.com/andres-olguin/Proyecto-TALIA.git)
   cd Proyecto-TALIA