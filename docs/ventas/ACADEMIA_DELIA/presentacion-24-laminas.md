# Guion completo: presentación DELIA Trust Fabric de 24 láminas

**Audiencia:** CTO/CISO/integrador B2B. **Duración:** 22–28 minutos + preguntas. **Estado:** narrativa objetivo y demo local, no lanzamiento comercial. Cada lámina incluye: mensaje, visual, notas, pregunta y evidencia.

## Acto I — contexto y necesidad (1–6)
### 01. Portada — Controlar la IA cuando ya puede actuar
**En pantalla:** DELIA Trust Fabric | MasterTech SpA | propuesta en desarrollo.
**Visual:** aplicación → política → agente/herramienta → evidencia.
**Decir:** «Las empresas están conectando modelos de IA con sistemas, clientes y operaciones. Nuestro desafío es mantener el control». **No decir:** «Somos la única plataforma». **Pregunta:** «¿Qué sistemas conecta actualmente su IA?». **Tiempo:** 45 s.

### 02. El cambio de riesgo: de texto a acciones
**Visual:** leer factura vs. emitir reembolso. **Decir:** «Ocultar datos es necesario, pero no basta si un agente también puede ejecutar operaciones». **Pregunta:** «¿Cuál es la operación con mayor impacto que un agente puede realizar?». **Tiempo:** 60 s.

### 03. Riesgos distintos
**Visual:** fuga, permisos, dependencia de proveedor, auditabilidad. **Decir:** «No todos los fallos se solucionan con un filtro de regex». **Evidencia:** referencia OWASP Agentic Top 10 2026, no incidencias de clientes DELIA. **Tiempo:** 60 s.

### 04. La solución actual del comprador
**Visual:** casillas para gateway, DLP, RBAC, revisión humana. **Decir:** «Su organización probablemente ya tiene controles; queremos saber qué falta». **Pregunta:** «¿Qué componente aplicaría una denegación de herramientas hoy?». **Tiempo:** 60 s.

### 05. Caso ilustrativo: reembolso de MXN 18.000
**Visual:** agente pide acción, umbral MXN 10.000. **Decir:** «El modelo recomienda, pero la política decide si la herramienta puede ejecutarse». **Aclarar:** ejemplo sintético. **Tiempo:** 60 s.

### 06. Qué significa confianza verificable
**Visual:** decisión, aprobación, evidencia sin payload. **Decir:** «Una operación crítica requiere saber qué se autorizó, por quién y bajo qué política». **Tiempo:** 45 s.

## Acto II — propuesta y diferenciación (7–12)
### 07. DELIA como control plane
**Visual:** capas: identidad, DLP, políticas, herramientas, auditoría. **Decir:** «Buscamos integrarnos con la infraestructura existente, no reemplazarla innecesariamente». **Tiempo:** 60 s.

### 08. Protect
**Visual:** RUT, NIT, CURP, RFC sin valores reales. **Decir:** «La cobertura regional debe medirse por identificador y país». **Límite:** PR #20 regional no fusionado y 100 % restringido al corpus propio. **Tiempo:** 60 s.

### 09. Agent Control
**Visual:** ALLOW / DENY / PENDING. **Decir:** «Hoy existe un motor local de políticas y prueba; falta un adapter de ejecución seguro». **Tiempo:** 50 s.

### 10. Human Approval
**Visual:** reembolso > umbral → supervisor → ticket de un uso. **Decir:** «La autorización exacta debe impedir cambios de importe después de aprobar». **Límite:** demo en memoria, identidad declarada. **Tiempo:** 60 s.

### 11. Verify
**Visual:** recibo HMAC sin prompt, dashboard futuro. **Decir:** «Comenzamos con evidencia mínima para proteger la privacidad». **Límite:** no hay ledger persistente ni KMS. **Tiempo:** 45 s.

### 12. ¿Qué hay frente a competidores?
**Visual:** capacidades comunes vs. diferenciación por demostrar. **Decir:** «LiteLLM, Cloudflare y soluciones de agent firewall ya resuelven partes del problema; exploramos una integración regional medible». **Pregunta:** «¿Cuál herramienta usan y qué no les resuelve?». **Tiempo:** 80 s.

## Acto III — demo y verdad técnica (13–18)
### 13. Antes de la demo
**Pantalla:** «Laboratorio sintético, sin datos reales, sin API externa». **Decir:** «Lo que van a ver prueba decisiones, no protección productiva completa». **Tiempo:** 20 s.

### 14. Política mínima
**Visual:** `refund.issue`, umbral bajo permitir, alto aprobar. **Decir:** «El motor niega todo lo que no tenga regla explícita». **Tiempo:** 45 s.

### 15. Acción retenida
**Visual:** `PENDING_APPROVAL`. **Decir:** «La operación propuesta de MXN 18.000 se retiene; no se ejecuta». **Tiempo:** 40 s.

### 16. Aprobación y no replay
**Visual:** aprobación → `ALLOW` → reuso `DENY`. **Decir:** «Se comprueba que el mismo ticket no puede autorizar dos operaciones». **Tiempo:** 50 s.

### 17. Recibo verificable
**Visual:** hash, HMAC, tipo de herramienta. **Decir:** «No almacenamos el argumento original en el recibo de esta demo». **Advertir:** sin identidad real, sin persistencia, sin prueba de que un upstream no haya filtrado datos. **Tiempo:** 45 s.

### 18. Qué falta
**Visual:** P0 en rojo discreto: identidad, sanitización de egress, API/E2E, retención y pruebas externas. **Decir:** «No pediremos datos sensibles hasta cerrar estos controles». **Tiempo:** 50 s.

## Acto IV — compra, riesgos y siguiente paso (19–24)
### 19. Dónde DELIA podría aportar valor
**Visual:** integrador que tiene múltiples agentes y clientes. **Decir:** «Una sola interfaz de políticas puede reducir divergencias, si la integración prueba ser útil». **Pregunta:** «¿Cuántas políticas replican entre proyectos?». **Tiempo:** 45 s.

### 20. Plan acelerado
**Visual:** 09/11→15/01 con gates. **Decir:** «Meta de beta avanzada para 15 enero; no prometemos saltarnos revisiones de seguridad». **Tiempo:** 50 s.

### 21. Criterios de piloto
**Visual:** casos permitidos, denegados, aprobados, p95, costo y fallos. **Decir:** «El piloto debe tener umbrales acordados y poder concluir que no encajamos». **Tiempo:** 55 s.

### 22. Modelo de compra posible
**Visual:** Team, Business, Integrator como hipótesis. **Decir:** «Estos precios solo orientan entrevistas; el alcance, costos y aceptación se definirán». **Tiempo:** 40 s.

### 23. Riesgos y responsabilidades
**Visual:** empresa / MasterTech / proveedor IA. **Decir:** «La protección compartida requiere permisos, configuración, monitoreo, un contrato de tratamiento y límites explícitos». **Tiempo:** 55 s.

### 24. Cierre con pregunta
**Visual:** «Identifiquemos una operación y midamos un control». **Decir:** «¿Podemos mapear una herramienta crítica y acordar cómo se probaría el bloqueo, con datos sintéticos?». **Siguiente paso:** reunión técnica, responsable y fecha acordados. **Tiempo:** 50 s.

## Ensayo y control del tiempo
Primera práctica: grabar 28 minutos; segunda práctica: 20 min; tercera: 12 min con solo 10 láminas clave (1,2,4,7,9,13,16,18,21,24). Evaluar en paralelo claridad y verdad técnica, sin esconder los no-GO.

## Materiales de apoyo permitidos
- Captura del workflow Trust Fabric CI, con URL y SHA comprobados.
- Terminal local `python -m trust_fabric.demo` con textos sintéticos.
- Código de `trust_fabric/policy.py` resaltando limitaciones.
- OWASP Agentic 2026 y fichas de competidores con fecha.
- Un diagrama general de arquitectura objetivo, claramente rotulado.

## Preguntas para interrumpir al presentador durante el ensayo
«¿Quién valida el rol en esa demo?», «¿Qué pasa con la aprobación si se reinicia el servidor?», «¿El motor puede ser saltado por el cliente?», «¿Se conserva el prompt?», «¿Quién paga por seguridad y soporte?», «¿Por qué no usar Strathon?», «¿Qué demostración tendrían en enero?». Una respuesta correcta reconoce limitaciones, ubica la evidencia y propone un gate, no un discurso evasivo.
