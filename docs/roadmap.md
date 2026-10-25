# Roadmap y Carta Gantt Maestra — Proyecto DELIA

**DELIA** (**D**ata **A**ncryption & **L**imiting **I**ntelligence **A**gent) es un proxy de seguridad, cifrado y control de cumplimiento normativo (Ley 21.719 en Chile y directrices de la SIC en Colombia) para agentes de inteligencia artificial.

---

## 👥 Definición de Roles y Responsabilidades
- **Andrés (Tú):** Líder Técnico / Arquitecto de Software y Desarrollo Core (FastAPI, Clientes HTTP asíncronos y Dashboards).
- **Iván:** Scrum Master y Desarrollador (Ciberseguridad, DLP, Expresiones Regulares y Documentación).
- **Nilson:** Desarrollador Backend, Base de Datos e Infraestructura (PostgreSQL, Redis, Alembic y Contenerización).
- **Isaac:** COO (Gestión, Operaciones, Validación Regulatoria, Definición de Pilotos y Estrategia Comercial).

---

## 🏗️ Stack Tecnológico Oficial
- **Backend & API:** Python 3.11+, FastAPI, Pydantic, httpx (con soporte SSE).
- **Caché y Rate Limiting:** Redis.
- **Base de Datos y Persistencia:** PostgreSQL, SQLAlchemy, Alembic.
- **Despliegue e Infraestructura:** Docker, Docker Compose, Linux (Ubuntu Server).
- **Frontend / Panel de Control:** React, Bootstrap / Tailwind CSS.

---

## 📅 Carta Gantt y Cronograma Detallado de Entregables

### 🟢 Sprint 1: Fundación, Naming y Viabilidad (COMPLETADO)
*Período:* 12 de octubre de 2026 – 25 de octubre de 2026  
*Objetivo:* Establecer la base técnica, la identidad del proyecto y el marco legal-regulatorio inicial.

* **Entregables y Fechas:**
  * **20 de Oct 2026:** Migración de nomenclatura y estructuración oficial del repositorio bajo la identidad **DELIA** (Iván & Andrés).
  * **23 de Oct 2026:** Redacción y organización del documento de viabilidad regulatoria en `/docs/` para Chile y Colombia (Iván).
  * **25 de Oct 2026:** Configuración inicial del entorno Docker Compose, `.env.example` y resolución de conectividad del engine (Nilson & Andrés).

---

### 🚀 Sprint 2: Motor de Sanitización, PII y Expresiones Regulares
*Período:* 26 de octubre de 2026 – 8 de noviembre de 2026  
*Objetivo:* Consolidar el núcleo de enmascaramiento y detección de datos personales sensibles (PII).

* **Entregables y Asignación de Fechas:**
  * **28 de Oct 2026:** Diseño e implementación de expresiones regulares (regex) optimizadas para cédulas de ciudadanía y NIT de Colombia *(Asignado a: Iván)*.
    * *Nano-tarea:* Pruebas unitarias con casos borde (dígitos de verificación, puntos y guiones).
  * **31 de Oct 2026:** Implementación del algoritmo Módulo 11 en Python para la validación exacta del RUT chileno *(Asignado a: Iván)*.
    * *Nano-tarea:* Script de sanitización de texto plano para enmascaramiento preventivo previo al envío al LLM.
  * **04 de Nov 2026:** Estructuración de modelos relacionales en PostgreSQL mediante SQLAlchemy y migraciones con Alembic para auditoría de tráfico *(Asignado a: Nilson)*.
  * **07 de Nov 2026:** Creación de la interfaz común de middleware de sanitización en FastAPI y revisión de código (*Code Review*) *(Asignado a: Andrés)*.
  * **08 de Nov 2026:** **Hito 1:** Validación ejecutiva y de cumplimiento normativo inicial sobre el alcance del motor PII *(Responsable: Isaac)*.

---

### ⚡ Sprint 3: Capa de Tráfico, Rate Limiting y Caché (Redis)
*Período:* 9 de noviembre de 2026 – 22 de noviembre de 2026  
*Objetivo:* Garantizar la velocidad de respuesta, cuotas por usuario y persistencia transitoria.

* **Entregables y Asignación de Fechas:**
  * **12 de Nov 2026:** Configuración del clúster de Redis en Docker Compose y escritura de lógica en Python para control de peticiones por minuto (*Rate Limiting*) *(Asignado a: Nilson)*.
  * **16 de Nov 2026:** Implementación de sistema de caché para consultas repetitivas de LLM con el fin de optimizar costos de tokens *(Asignado a: Nilson)*.
  * **19 de Nov 2026:** Conexión del middleware de Redis con las rutas asíncronas del proxy e inicio de pruebas de estrés y latencia *(Asignado a: Andrés)*.
  * **21 de Nov 2026:** Integración de los filtros de PII del Sprint 2 con el pipeline de tráfico y facilitación de la ceremonia de sprint *(Asignado a: Iván - Scrum Master)*.
  * **22 de Nov 2026:** **Hito 2:** Revisión de costos proyectados de infraestructura y umbrales de latencia permitidos *(Responsable: Isaac)*.

---

### 🔄 Sprint 4: Integración de Proxy Inverso y Fallback de LLMs
*Período:* 23 de noviembre de 2026 – 6 de diciembre de 2026  
*Objetivo:* Unificar el flujo completo de reenvío, enmascaramiento y respuesta en tiempo real.

* **Entregables y Asignación de Fechas:**
  * **27 de Nov 2026:** Desarrollo del cliente proxy HTTP asíncrono con `httpx`, asegurando el manejo de *Streaming* de respuestas (Server-Sent Events - SSE) *(Asignado a: Andrés)*.
  * **02 de Dic 2026:** Implementación del mecanismo de *fallback* automático ante fallos o timeouts del proveedor LLM primario *(Asignado a: Nilson & Iván)*.
  * **05 de Dic 2026:** Pruebas de integración End-to-End (E2E) con mocks de proveedores externos (OpenAI/Anthropic) *(Asignado a: Equipo Completo)*.
  * **06 de Dic 2026:** **Hito 3:** Aprobación formal del flujo funcional completo para demostración ante stakeholders internos *(Responsable: Isaac)*.

---

### 🛡️ Sprint 5: Auditoría, Registro Forense y Persistencia de Logs
*Período:* 7 de diciembre de 2026 – 20 de diciembre de 2026  
*Objetivo:* Garantizar trazabilidad forense inmutable de los eventos de seguridad.

* **Entregables y Asignación de Fechas:**
  * **11 de Dic 2026:** Registro transaccional en PostgreSQL de eventos críticos (intentos bloqueados de fuga de PII y excesos de *rate limit*) *(Asignado a: Andrés & Nilson)*.
  * **16 de Dic 2026:** Desarrollo de endpoints seguros de consulta de logs de auditoría orientados a perfiles de administración *(Asignado a: Nilson)*.
  * **19 de Dic 2026:** Redacción de la documentación técnica de despliegue, arquitectura y manual de integración para desarrolladores en `/docs/` *(Asignado a: Iván)*.
  * **20 de Dic 2026:** **Hito 4:** Auditoría interna de seguridad sobre el almacenamiento y cifrado de los registros de auditoría *(Responsable: Isaac)*.

---

### 📊 Sprint 6: Panel de Control (Dashboard) y Pruebas de Carga
*Período:* 21 de diciembre de 2026 – 3 de enero de 2027  
*Objetivo:* Proveer una interfaz visual de monitoreo y certificar la estabilidad bajo alta concurrencia.

* **Entregables y Asignación de Fechas:**
  * **26 de Dic 2026:** Desarrollo del panel de control frontend en React/Bootstrap para visualización de métricas de tráfico y alertas de seguridad *(Asignado a: Andrés)*.
  * **30 de Dic 2026:** Ejecución de pruebas de carga avanzadas (con herramientas como Locust) y optimización de índices de bases de datos *(Asignado a: Nilson)*.
  * **02 de Ene 2027:** Empaquetado del release oficial, revisión final de manuales y estandarización de variables de entorno *(Asignado a: Iván)*.
  * **03 de Ene 2027:** **Hito 5:** Aprobación para paso a entorno de pruebas controlado y definición de métricas de éxito del piloto comercial *(Responsable: Isaac)*.

---

### 🌐 Sprint 7: Despliegue de Piloto Comercial (Chile y Colombia)
*Período:* 4 de enero de 2027 – 17 de enero de 2027  
*Objetivo:* Lanzamiento del entorno piloto en producción controlada con usuarios reales.

* **Entregables y Asignación de Fechas:**
  * **08 de Ene 2027:** Despliegue de la infraestructura en servidor cloud con dominio dedicado y certificados SSL configurados *(Asignado a: Andrés & Nilson)*.
  * **12 de Ene 2027:** Proceso de *onboarding* de los primeros usuarios de prueba seleccionados por la estrategia comercial *(Asignado a: Isaac)*.
  * **15 de Ene 2027:** Monitoreo activo de incidencias, detección de falsos positivos en regex y ajustes de rendimiento en caliente *(Asignado a: Iván & Nilson)*.
  * **17 de Ene 2027:** Cierre oficial del ciclo de desarrollo inicial y evaluación de resultados del primer piloto comercial *(Asignado a: Isaac & Equipo)*.

---

## ⚠️ Gestión de Riesgos y Dependencias Críticas
1. **Falsos positivos en PII:** Riesgo de que las expresiones regulares bloqueen información legítima corporativa. *Mitigación:* Pruebas unitarias estrictas en el Sprint 2 y umbrales de sensibilidad configurables.
2. **Latencia en streaming:** El proxy no debe superar los 50ms de sobrecarga en respuestas por streaming. *Mitigación:* Pruebas de estrés rigurosas durante el Sprint 3 y Sprint 6.
3. **Dependencia de APIs de terceros:** Caídas en los proveedores de modelos externos. *Mitigación:* Implementación de la lógica de *fallback* automático en el Sprint 4.

## 📈 Métricas de Éxito del Proyecto
* **Disponibilidad del Proxy (Uptime):** $\ge 99.9\%$.
* **Efectividad de Bloqueo de PII:** $100\%$ en documentos normados (RUT y Cédula/NIT).
* **Sobrecarga de Red (Latencia Promedio):** $< 45\text{ms}$ por petición procesada.