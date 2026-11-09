# DELIA — Guiones audiovisuales y textos originales para validación humana

**Borradores, NO publicados.** Al grabar, demostrar solamente lo que existe en el SHA actual. La voz, imágenes, efectos, música y rostros de terceros necesitan derechos/consentimiento. No reproducir clips aportados para investigación.

## Tres guiones de video corto (35–60 segundos)

### Video A — «El agente dice que tiene permiso. ¿Lo tiene?»

**Gancho (0–5 s):** «Que una IA diga “puedo hacerlo” no significa que tenga autorización».  
**Problema (5–15 s):** «Un agente conectado a un CRM puede proponer leer, cambiar o borrar registros. El permiso debe verificarse fuera del modelo».  
**Prueba (15–35 s):** mostrar diagrama o un test **realmente disponible** en versión señalada; si solo está en laboratorio, rotularlo «SIMULACIÓN, sin conexión a CRM».  
**Límite (35–45 s):** «DELIA todavía está en desarrollo. Una prueba en sandbox no garantiza seguridad productiva».  
**CTA (45–60 s):** «Publicamos el diseño y las pruebas en GitHub. Qué controles usan hoy con sus agentes?».

**Claims asociados:** seguridad de agentes y OWASP ACS; nunca prometer enforcement actual no probado.

### Video B — «Una respuesta exitosa puede no ser una operación confirmada»

**Gancho:** «¿Y si un agente dice “listo”, pero el sistema jamás confirmó el cambio?».  
**Demostración:** mostrar el laboratorio local Outcome Assurance con estados `VERIFIED_SIMULATED`, `HOLD` y `MISMATCH`; explicar que la prueba es ficticia, sin dinero ni datos reales.  
**Resultado:** «Un proveedor puede fallar, demorar o responder de manera inconsistente. Los sistemas serios deben distinguir resultado reportado y resultado comprobado».  
**CTA:** «El código del ejercicio es público. Estamos buscando integradoras que quieran comparar este enfoque con su stack actual».

### Video C — «¿Puede un agente actuar fuera del alcance?»

**Gancho:** «En evaluaciones de seguridad se han documentado agentes actuando fuera de sus parámetros autorizados».  
**Contexto:** «El UK AI Security Institute publicó resultados de incidentes en evaluaciones. Eso no significa que todos los agentes puedan escapar de cualquier control».  
**Prueba futura:** diagrama de identidad, permisos, egress y revocación fuera del agente; no presentar una pantalla ficticia como test completado.  
**CTA:** «DELIA investiga cómo medir estos riesgos en CRM y otras herramientas, con pruebas que otros puedan reproducir».

Fuente: https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing .

## Tres borradores de LinkedIn (no publicar antes de revisión)

### Post 1 — calidad de evidencia

«Muchos debates sobre seguridad de IA se quedan en una pregunta: “qué tan peligrosa puede ser?”. En proyectos empresariales necesitamos otra: “qué operaciones concretas puede ejecutar este agente y cómo comprobamos sus límites?”. En DELIA estamos construyendo un programa de pruebas de herramientas, permisos y resultados. Todavía es investigación y laboratorio, no software productivo certificado. Documentamos lo que funciona y lo que falta. Repositorio y matriz de riesgos: [URL actual de GitHub]».

### Post 2 — negocio

«Un integrador que trabaja con agentes conectados a CRM puede resolver permisos de distintas formas: herramientas nativas, gateways, OPA, Temporal o código propio. Queremos comprobar si contratos de operación reutilizables pueden ahorrar trabajo real sin introducir otra plataforma costosa. No estamos asumiendo que DELIA es la mejor alternativa. Buscamos entender cuánto tarda hoy ese trabajo y qué errores se repiten. Qué cuesta más mantener al incorporar un segundo cliente?».

### Post 3 — Chile

«El ITD-IA 2026 de CORFO/CCS/PMG, realizado con 740 empresas, ubica la gobernanza en 27/100 puntos. No significa que esas empresas vayan a comprar DELIA. Sí es una razón para discutir procesos, responsables y pruebas antes de conectar agentes a sistemas reales. Estamos estudiando primero un caso de CRM de bajo riesgo: permisos verificables, negaciones y resultados inciertos. Fuente oficial y metodología en GitHub».

Fuente: https://www.ccs.cl/2026/09/04/chile-mide-primera-vez-madurez-ia-parte-34-100-puntos-oportunidad-escalamiento/ .

## Artículo técnico original: estructura reutilizable

**Título:** «Cómo evaluar un agente de IA conectado a un CRM sin poner datos reales en riesgo».  
**Resumen:** contexto y amenazas; alternativa actual; diagrama de control; 10 tests con fixtures falsos; resultados con SHA; cobertura y no ejecutados; costo de instalación y próximas decisiones.  
**Apéndice:** herramientas, versión, permisos, reproducibilidad, fuentes, notas de corrección.  
**CTA:** sesión técnica de 25 minutos de discovery cuando exista capacidad. No requiere correo masivo ni «acreditación» de seguridad.

## Webinar público de 20 minutos (solo cuando demo reproducible)

2 min quién es DELIA y estado; 4 min riesgo de una tool; 6 min demo sin PII; 4 min resultado desconocido; 2 min alternativa Helio/OPA/Temporal; 2 min preguntas y enlaces. Registrar dudas, no testimonios sin autorización.

## Escalera educativa para audiencia amplia

- **Nivel 1:** permisos, privacidad y por qué «la IA dijo» no es evidencia.
- **Nivel 2:** tool calls, scopes, políticas y separación modelo/ejecutor.
- **Nivel 3:** reproducibilidad, hash, logs y provider `unknown`.
- **Nivel 4:** contratos operacionales, idempotencia, sandbox, test independiente.
- **Nivel 5:** investigación de monitorabilidad y control adaptativo con incertidumbre.

## Lineamientos de marca

Usar siempre **DELIA**, mencionando *Data Encryption & Limiting Intelligence Agent* como expansión histórica cuando corresponda. La línea comercial propuesta es «Operaciones empresariales verificables con IA», no slogan de garantía. Identificar MasterTech SpA como organización impulsora del proyecto según derechos aplicables. Separar explícitamente experiencia freelance personal del fundador de proyectos facturados por la empresa. Ningún logo de instituto/cliente como endorsement sin permiso.

## Protocolo de lanzamiento de cualquier guion

Revisor de fuente → revisor técnico → permiso de imagen/voz → revisión de tono y claims → publicación por persona autorizada → capturar URL real → seguimiento de conversaciones y correcciones. El calendario JSON mantiene todo como `DRAFT` hasta completar revisión.
