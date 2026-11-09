# Academia comercial DELIA — Argumentos y entrenamientos sectoriales

**Versión:** 2026-11-09. Complementa la Academia existente en PR #21. Usar solo datos sintéticos, sin convertir una demostración en promesa de protección productiva. Cada vertical tiene una pregunta que detecta necesidad y una prueba que el equipo debe ejecutar antes de asegurar capacidad.

## Estructura de una presentación de 10 minutos
- Min 0–2: reconocer stack y riesgo real del comprador.
- Min 2–3: dibujar flujo actual del agente (identidad → tool → negocio).
- Min 3–5: enseñar la decisión del motor local, aclarando que no ejecuta sistemas reales.
- Min 5–7: límites de identidad, PII/egress, persistencia, competencia.
- Min 7–9: definir prueba comparativa con su solución actual.
- Min 9–10: siguiente paso con objetivos, fecha y responsable acordados.

## Pitches por industria

### Integrador / MSP
**Apertura:** «Si estás entregando agentes a distintos clientes, ¿cómo evitas que un mismo cambio de política afecte a organizaciones diferentes?». **Valor propuesto:** políticas/identidad reutilizables y evidencia por tenant. **Demo:** tenant A autorizado a leer, tenant B denegado. **Meta de venta:** reducir trabajo por nuevo cliente. **Objeción:** «Ya lo construimos» → pedir un caso concreto que les cueste mantener.

### SaaS B2B
**Apertura:** «¿Quién puede autorizar a su agente para modificar información que hoy solo consultaba?». **Valor:** punto de control previo a ejecutar herramientas. **Demo:** change-status sin permiso DENY. **Meta:** minimizar incidentes y retrasos de adopción. **Objeción:** «El modelo nunca lo haría» → los permisos deben verificarse fuera del modelo.

### Ecommerce / retail
**Apertura:** «¿Qué política gobierna una devolución de alto importe solicitada por un bot?». **Valor:** autorización humana ligada al monto y auditable. **Demo:** reembolso ficticio de MXN 18.000, PENDING, aprobación, rechazo replay. **Meta:** control sin paralizar operaciones legítimas. **Objeción:** «Nuestro ERP ya autoriza» → explorar si hay valor incremental; podría no haber.

### Contact center / BPO
**Apertura:** «¿Qué información del cliente se envía al modelo y quién puede cambiar su cuenta?». **Valor:** PII regional y permisos de CRM. **Demo:** redacción con datos sintéticos y acción de modificación bloqueada, solo tras integrar seguridad. **Meta:** medir FN/FP, p95 y coste por agente. **Objeción:** «Un filtro de palabras basta» → comparar en corpus independiente.

### Logística
**Apertura:** «¿Un agente puede cambiar una ruta o cancelar un despacho sin una persona?». **Valor:** autorizaciones por impacto económico. **Demo:** despacho ficticio con approval. **Meta:** prevenir cambios indebidos y revisar latencia. **Limitación:** no conexión real al WMS hasta pasar P0.

### Recursos Humanos
**Apertura:** «¿Qué datos de candidatos y nómina necesita de verdad el agente?». **Valor:** minimización y control de operaciones sobre registros. **Demo:** lectura limitada y bloqueo de alteración de nómina, con personas ficticias. **Riesgo:** no automatizar decisiones discriminatorias o contractuales sin evaluación legal.

### Legal
**Apertura:** «¿Se podrían resumir contratos sin exponer todos sus identificadores?». **Valor:** redacción contextual con control de acceso y evidencia. **Demo:** contrato completamente inventado. **Límite:** confidencialidad y privilegios profesionales requieren revisión.

### Fintech
**Apertura:** «¿Qué impide que un agente solicite transferir fondos fuera de su autorización?». **Valor:** acción bloqueada por política exacta y aprobación adicional. **Demo:** pago simulado sin dinero. **Riesgo:** jamás integrar pagos reales con el laboratorio.

### InsurTech
**Apertura:** «¿Quién autoriza un cambio de estado o importe en un siniestro?». **Valor:** trazabilidad y revisión de acciones. **Demo:** siniestro ficticio. **Meta:** separación rol/revisión.

### Salud
**Apertura:** «¿Cómo limitan el acceso a información de pacientes al mínimo requerido?». **Valor:** control de acceso por finalidad. **Demo:** expediente de paciente sintético. **Límite:** no decisiones médicas autónomas ni datos reales en PoC.

### Educación
**Apertura:** «¿Qué permisos tiene el tutor IA sobre registros de estudiantes?». **Valor:** accesos limitados a información, sin cambios de nota. **Demo:** ficha ficticia. **Límite:** datos de menores y reglas institucionales.

### Sector público
**Apertura:** «¿Cómo demuestran quién autorizó una operación ejecutada por un agente?». **Valor:** evidencia y políticas verificables. **Demo:** trámite sintético. **Límite:** procurement, soberanía y normativa requieren contratación y revisión.

## Guion extendido para CFO / comité de inversión (4 minutos)

«DELIA explora un mercado de software empresarial donde la IA deja de responder preguntas y comienza a modificar sistemas. Nuestra tesis económica no es cobrar por una regex: es proveer una misma plataforma de controles a integradoras que trabajan con múltiples clientes, luego monetizar por suscripción, uso y módulos por sector. El riesgo es claro: ya existen grandes competidores y no tenemos ingresos DELIA confirmados. Por eso proponemos tres pruebas sucesivas: primero seguridad de operaciones con un adapter sin bypass; segundo, demostrar un tiempo y costo de integración competitivo; tercero, conseguir compradores que paguen por esas diferencias. El escenario de ingresos del repositorio es solo matemático y no es una valoración. Si no hay valor incremental, reduciremos DELIA a un componente interoperable en vez de sostener un gateway innecesario».

## Guion extendido para CISO / comité técnico (4 minutos)

«Una decisión del modelo de IA no equivale a autorización corporativa. DELIA propone identificar al agente y su organización, inspeccionar contenido permitido, verificar una política versionada, exigir aprobación humana cuando corresponda e impedir que la herramienta se ejecute sin permiso. El estado actual incluye un laboratorio de reglas y aprobación sintética, no autenticación ni enforcement productivo. Para superar esa limitación necesitamos ejecutar pruebas de cross-tenant, replay, TOCTOU, no-egress, retención mínima y falla cerrada en el punto real de ejecución. Compartiremos versiones y fallos con claridad. No pedimos datos reales antes del cierre de P0».

## Comparaciones que el vendedor debe practicar
1. «LiteLLM ya lo hace»: separar gateway de tool enforcement y evaluar stack concreto.
2. «Cloudflare ya tiene DLP»: aceptar y ofrecer comparar casos regionales con métricas.
3. «Palo Alto tiene agent security»: reconocer madurez y recursos; hablar de integración y costo total.
4. «No necesito software nuevo»: no insistir, preguntar si hay una brecha.
5. «¿Puedo instalarlo hoy con clientes?»: no; solo laboratorio controlado.
6. «¿Cuánto ahorro?»: método de medición, no porcentaje inventado.
7. «¿Cumple ley chilena?» : no ofrecer certificación o dictamen legal.
8. «¿Por qué Latinoamérica?» : detectar formatos y flujos locales es hipótesis medible, no garantía de monopolio.

## Entrenamiento progresivo: 6 sesiones
- Sesión 1 (12/11): marca y pitch 30/90 segundos, claridad y honestidad.
- Sesión 2 (19/11): mapa de comprador y descubrimiento, 12 preguntas útiles.
- Sesión 3 (26/11): 4 simulaciones por sector prioritario, preguntas técnicas.
- Sesión 4 (03/12): confrontación con competidores y objeciones.
- Sesión 5 (10/12): modelado de ROI, pricing y decisión No-Go.
- Sesión 6 (17/12): presentación completa 20 minutos con CTO, CISO y CFO simulados.

**Fechas de entrenamiento sugeridas, no sesiones realizadas ni responsabilidades asignadas.**

## Rúbrica de evaluación
Puntuar por separado exactitud técnica (100), claridad oral (100), escucha y diagnóstico (100), manejo honesto de límites (100) y capacidad de acordar siguiente prueba (100). Un error crítico —clientes ficticios como reales, afirmación de 100 % de seguridad, certificación inexistente, prueba no ejecutada— invalida la práctica, aunque el discurso sea convincente.

El material de grabaciones y evaluaciones personales se conserva en una herramienta privada, con consentimiento; nunca en repositorio público.
