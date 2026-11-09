# Manual maestro de ventas consultivas de DELIA — edición para formación intensiva

**Uso interno de entrenamiento.** No prometer capacidades que no estén verificadas por repositorio, CI, demo o contrato. Estado 2026-11-09: Trust Fabric dispone de un motor local experimental de decisiones y no es producto enterprise certificado.

## 1. El rol del vendedor técnico
No es «persuadir a cualquiera». Es diagnosticar si un integrador tiene un problema caro, frecuente y verificable de permisos, protección de datos o gobernanza al conectar agentes con sistemas empresariales, y proponer una validación limitada. Éxito puede significar **descartar un lead incompatible** con razones documentadas.

La conversación tiene tres planos:
- **Problema**: qué sucede, quién lo observa, cuál es el efecto cuantificable.
- **Solución existente**: qué controles tienen con su stack actual y qué huecos reales quedan.
- **Compra**: quién decide, quién integra, quién asume riesgo, presupuesto, plazo y criterios de éxito.

Una propuesta solo se presenta después de conocer esos tres planos. Evitar un monólogo con las veinte funciones.

## 2. Problema de negocio y costo del riesgo
Ejemplos hipotéticos: un agente de facturación envía PII por API; un agente de cobranza puede borrar registros; un chatbot con herramienta CRM usa permisos globales; un integrador mantiene múltiples políticas divergentes entre clientes. No afirmar que el prospecto hace eso sin verificarlo.

Explorar **frecuencia** («¿Cuántas veces al mes se invoca esa herramienta?»), **severidad** («¿Qué consecuencias tendría una transferencia incorrecta?»), **esfuerzo actual** («¿Cómo revisan cada despliegue?») y **propietario** («¿Quién recibe la alerta?»). Cuantificar si hay datos; si no, registrar «NO MEDIDO».

## 3. Mapa de compradores
### Fundador / CEO de integradora
Interés: vender soluciones con riesgos acotados, reducir trabajo replicado, diferenciar propuestas, crecer sin soporte inmanejable. Pregunta: «¿Cuánto tiempo les cuesta adaptar políticas a un cliente nuevo?» Métricas: coste de onboarding, margen por proyecto, incidencia de fallos y retención.

### CTO / arquitectura
Interés: API, middleware, límites de latencia, compatibilidad, fail-closed, testabilidad y lock-in. Pregunta: «¿En qué punto de su flujo puede imponerse una decisión sin bypass?» Mostrar diagrama, no logos de seguridad.

### CISO / seguridad
Interés: amenazas, identidad, least privilege, incidentes y trazabilidad. Pregunta: «¿Qué operación crítica no pueden bloquear hoy de forma uniforme?» Responder con límites del prototipo, pruebas, impacto y decisión de No-Go.

### Jurídico / privacidad
Interés: fundamento para tratamiento, transferencias, encargados, retención, datos sensibles, contratos y auditoría. Pregunta: «¿Qué datos salen hoy y con qué propósito?» No afirmar certificación, obligación de contratar DELIA o asesoría legal.

### Finanzas / procurement
Interés: gasto total, márgenes, riesgo de proveedor y contrato. Pregunta: «¿Qué costo quieren evitar y cuánto les cuesta resolverlo de otra manera?» No ofrecer ROI sin baseline ni confundir ARR con facturación.

### Desarrollador integrador
Interés: instalar rápido, ejemplos funcionales, debugging, CLI/SDK y control granular. Pregunta: «¿Qué prueba reproducible les haría confiar en un gateway nuevo?» Mostrar `pytest`, SHA y un caso exacto.

## 4. Técnica de descubrimiento: veinte preguntas útiles
1. ¿Qué agentes tienen en producción o piloto? 
2. ¿Qué herramientas invocan y con qué permisos?
3. ¿Qué información llega a proveedores externos?
4. ¿Quién conoce la lista de herramientas?
5. ¿Cómo detectan y corrigen un bypass?
6. ¿Qué política rige para datos fiscales e identificadores?
7. ¿Qué pasa si un proveedor falla?
8. ¿Qué pasa si su detector falla?
9. ¿Existe aprobación humana para acciones con dinero?
10. ¿Cómo auditan una aprobación y evitan replay?
11. ¿Qué proveedor/gateway utilizan hoy?
12. ¿Qué hacen bien esas herramientas?
13. ¿Qué limitación observada no han podido resolver?
14. ¿Cuánto cuesta su proceso manual?
15. ¿Quién recibe reportes de seguridad?
16. ¿Qué incidentes o casi-incidentes han medido?
17. ¿Cuál es su política de residencia de datos?
18. ¿Quién aprobaría una prueba técnica?
19. ¿Qué resultados objetivos definirían un piloto exitoso?
20. ¿Qué les haría decir que DELIA no tiene valor para ustedes?

Usar 5–8 preguntas, no interrogar con una lista completa. Tras cada respuesta, reformular la información confirmada y una pregunta de profundidad.

## 5. Técnica de explicación «qué → por qué → prueba»
La disciplina evita divagar:
- **Qué**: «El motor decide si una acción se permite, deniega o queda pendiente de aprobación».
- **Por qué**: «Un agente no debería poder emitir un reembolso arbitrario solo porque lo solicitó un modelo».
- **Prueba**: «Esta demo sintética verifica expiración, rechazo de cambios de importe y reutilización de la aprobación. No ejecuta dinero real».

Evitar «cumplimos todas las leyes», «100 % seguro» y «somos únicos». Reemplazar por resultados específicos con alcance.

## 6. Presentaciones por duración
**30 segundos:** segmento + problema + enfoque + estado + invitación.
**2 minutos:** historia operacional → riesgo → 3 controles → evidencia → pregunta.
**10 minutos:** descubrimiento 2, problema 1, arquitectura 2, demo 2, límites 1, validación 2.
**25 minutos:** agenda 2, diagnóstico 5, comparación 3, demo 5, threat model 3, economía 3, próximos pasos 4.
**45 minutos:** workshop interactivo con diagrama de cliente; no lo convertir en discurso de 45 minutos.

El guion nunca debe imponer una demo si el comprador pide discutir arquitectura o privacidad.

## 7. Diseño de historias de venta
Estructura SITUACIÓN → DECISIÓN → CONSECUENCIA → CONTROL → PRUEBA. Ejemplo ficticio:
«Un integrador construye un agente que propone reembolsos. Si usa permisos globales, una instrucción defectuosa podría iniciar una operación sensible. DELIA apunta a interponer una política: debajo de cierto umbral permite; por encima solicita aprobación vinculada al importe exacto; luego produce evidencia mínima. Hoy podemos simular ese comportamiento local, pero no está desplegado como protección empresarial».

No atribuir historia ficticia a un banco o cliente real.

## 8. Demostración técnicamente honesta
1. Anunciar entorno, versión y limitaciones.
2. Mostrar comando sin credenciales y sin Internet.
3. Invocar caso permitido, denegado, pendiente, aprobado y replay.
4. Comprobar que el recibo HMAC cambia si se altera la decisión.
5. Mostrar qué NO prueba: la autenticación real, upstream egress, persistencia, eficacia ante datos reales.
6. Solicitar al interlocutor que proponga un caso negativo adicional.
7. Cerrar con siguiente prueba acordada y dueño.

Si falla, no editar resultados: registrar error exacto, versión y plan de corrección.

## 9. Competencia sin ataques
Si mencionan PrivAiTe, LiteLLM, Cloudflare, Strathon o Soup Wall: «Sí, hay soluciones reales y varias capacidades similares. ¿Cuál usan? ¿Qué problema no resuelve?» Comparar por costo total, seguridad probada, soporte, integración, regiones y claridad de evidencia. No afirmar superioridad sin ejecutar benchmark homogéneo.

Una ventaja plausible de DELIA es combinar enfoque latinoamericano + políticas consistentes para agentes + evidencias verificables + soporte de integradores; cada pieza requiere prueba comercial.

## 10. Calificación de oportunidades
Propuesta de variables 0–2 (sin falsificar):
- **Dolor**: no hay brecha=0; sospecha=1; evidencia de problema=2.
- **Proyecto**: exploración=0; piloto definido=1; agente activo=2.
- **Acceso**: sin interlocutor=0; técnico=1; técnico y comprador=2.
- **Tiempo**: sin plazo=0; trimestre=1; evento/urgencia verificable=2.
- **Disposición a validar**: no=0; conversación=1; piloto bajo protocolo=2.
Total 0–10: 0–3 aprender, 4–6 profundizar, 7–10 preparar propuesta condicionada. No equivale a probabilidad estadística de venta. Registrar origen y fecha de cada puntuación.

## 11. ROI y solución alternativa
Calcular costo interno de revisión manual = horas×costo/hora + incidentes observados×costo atribuible + costo operativo de herramientas. Evitar contar multa evitada como ahorro seguro. Separar coste de licencia DELIA, implementación, migración, revisión legal, seguridad, soporte y consumo proveedor. Si el sistema existente resulta más económico y seguro, recomendar no cambiar.

## 12. Estructura de propuesta consultiva
1. Resumen de contexto **confirmado por cliente**.
2. Riesgo/oportunidad observado y costo de no resolver.
3. Solución actual y brecha no cubierta.
4. Alcance exacto DELIA en etapa correspondiente.
5. Exclusiones; dependencia de P0; riesgos y uso solo sintético hasta autorización.
6. Plan de prueba, tiempo y dueños (acordados, no inventados).
7. Métricas de aceptación y método de medición.
8. Precio hipótesis o cotización bajo costos.
9. Protección de datos, confidencialidad, IP y permisos.
10. Go/No-Go y próximo contacto.

## 13. Gestión de objeciones: fórmula ESCUCHA
**E**scuchar completa; **S**intetizar la objeción; **C**onfirmar significado; **U**bicar evidencia existente; **C**omparar alternativas; **H**onrar lo no verificado; **A**cordar siguiente prueba. No responder una objeción técnica con promesas futuras ni presión.

Ejemplo: «¿Por qué no usar LiteLLM?» → «Es válido; puede resolver buena parte del gateway. ¿Dónde están hoy los controles de aprobación de herramienta y auditoría por cliente? Si ya cumplen, no propongo cambiar. Si hay brecha, evaluemos un adapter pequeño con una prueba comparable».

## 14. Escucha activa y comunicación sin redundancia
Hablar como persona: frases de 10–18 palabras cuando sea posible; una idea por respiración; pausas para preguntas; sin muletillas repetidas ni lectura de todo el deck. Responder primero la pregunta. Ante silencio, dejar tiempo para pensar. Si no entiende, cambiar ejemplo, no elevar volumen.

Corrección de tres errores:
- «Tenemos seguridad completa» → «Tenemos un simulador de políticas y una hoja de ruta para enforcement completo».
- «El detector tiene precisión del 100 %» → «En 96 casos sintéticos de desarrollo obtuvo 55 TP y ningún error; falta dataset independiente».
- «Nuestra herramienta cumple la ley» → «Diseñamos controles relevantes y revisaremos obligaciones con profesionales por país».

## 15. Negociación profesional
No descontar antes de definir alcance y coste. Intercambiar concesiones por compromisos equivalentes: precio menor por menos integraciones, plazo de contrato, volumen o horario de soporte; no prometer función ausente. Mantener piso de margen y gastos de seguridad. Los pilotos pueden ser de alcance acotado y sin PII real si no pasan gates.

Preguntas: «¿Qué presupuesto se autorizó?», «¿Qué entregable hace que el comité apruebe?», «¿Qué alternativa usarían si no avanzamos?», «¿Quién firma la aceptación?».

## 16. Cierre sin presión
Tres cierres legítimos: 
- **Descubrimiento:** «¿Quién puede acompañar una reunión técnica de 30 minutos para mapear una herramienta y su política?».
- **Prueba:** «¿Les parece definir dos casos permitidos y dos bloqueados, con datos sintéticos, y compararlos con su solución actual?».
- **No-fit:** «Por sus respuestas, su control actual parece suficiente; no recomendaría integrar otra capa ahora».

## 17. Seguimiento
Enviar resumen con dolor confirmado, medida, propuesta, límites, responsables y fecha acordada. Si no responden, realizar seguimiento respetuoso según canal y consentimiento. Registrar «sin respuesta», no inventar decisión.

## 18. Ética y seguridad comercial
- No publicar nombres de personas entrevistadas, correos o números en repo público.
- No solicitar contratos o pantallazos sensibles para convencer.
- No tratar una empresa de un CSV como cliente.
- No usar regulaciones como amenazas comerciales.
- No prometer disponibilidad, precisión, ahorro, monitoreo 24/7 o compliance sin prueba y contrato.
- En discusiones de riesgos críticos, elevar a equipo técnico y jurídico, no improvisar.

## 19. Entrenamiento de preguntas hostiles
Una persona del equipo hace preguntas: «¿Qué hacen diferente?», «¿Por qué debería creerles?», «¿Puede un atacante saltarse su motor?», «¿Qué dato real procesaron?», «¿Tienen auditoría?». El vendedor debe responder en menos de 40 segundos, incluir evidencia si existe y una limitación honesta.

## 20. Modelo de reflexión post-reunión
Completar: objetivo inicial, información aprendida, términos mal explicados, afirmación no verificada detectada, objeciones, evidencia prometida, próximo paso y responsable. Puntuar técnicamente y comunicacionalmente por separado con `evaluacion-y-rubricas.md`.

## 21. Glosario rápido para hablar correctamente
- PII: información que puede identificar a alguien, según contexto.
- DLP: medidas para prevenir pérdida/exposición de información.
- Gateway: intermediario de solicitudes.
- Agent: software que usa modelo y herramientas para realizar tareas.
- Policy enforcement point: componente que obliga a aplicar la decisión, no simple recomendación.
- Tenant: organización aislada lógicamente en un servicio.
- RBAC/ABAC: permisos por rol/atributos.
- Fail closed: al fallar un control, denegar la operación.
- False negative: dato sensible que no fue detectado.
- Precision/Recall: métricas condicionadas al corpus y método.
- HMAC: verificación de integridad y autenticidad con clave secreta compartida, no certificación externa.
- SLA/SLO: compromisos contractuales/objetivos medidos, no sinónimos de «prometemos alta disponibilidad».
- ARR/MRR: run-rate de ingresos recurrentes solo sobre contratos reales, no escenarios hipotéticos.

## 22. Ejercicios de cierre de capítulo
A. Explica DELIA sin decir «IA» más de tres veces (90 segundos).
B. Diferencia caso sintético de caso real en 20 segundos.
C. Da un ejemplo de un competidor que haga mejor una función actual.
D. Formula 5 preguntas sin vender nada.
E. Declara el principal riesgo técnico en un solo párrafo.
F. Calcula un ROI con números inventados **marcados hipotéticos** y explica cómo lo medirías.
G. Simula un no-fit: di respetuosamente que el producto no añade valor.
H. Defiende por qué no fusionar un PR sin revisión, aun con 170 pruebas aprobadas.

## 23. Criterio de graduación interna
Un vendedor de DELIA se considera listo para conversaciones de **descubrimiento**, no para prometer producción, cuando obtiene >=80/100 en comunicación, >=85/100 en precisión técnica, cero afirmaciones falsas críticas y demuestra que sabe detener una venta insegura. Un líder técnico debe aprobar las demos que involucren PII o acciones.
