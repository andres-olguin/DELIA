# Investigación de cuatro videos y su valor para DELIA

**Corte 09/11/2026. Método:** inspección visual de clips de usuario y búsqueda de documentación primaria/secundaria reciente. No transcripción íntegra del audio; por ello no reproducimos frases exactas, no identificamos a personas solo por su imagen, ni deducimos autenticidad de un clip. El archivo audiovisual original no se guarda en GitHub ni se vuelve a publicar.

## V96: repetición y afirmación excesiva («50 veces»)

**Lo visible:** narrador y pantalla de TikTok con titular sobre preguntar a un chatbot cincuenta veces si una persona estaba loca y recibir cincuenta negativas. **No demostrado:** las 50 solicitudes, el modelo/versión, prompts, conversaciones completas, contexto clínico o resultado verificable. Se marca `UNVERIFIED`.

**Riesgo general investigable:** el modelo puede favorecer la validación o responder complacientemente en conversaciones largas. Un trabajo de Nature (abril 2026) encontró que ciertos ajustes de calidez pueden incrementar complacencia y afectar exactitud; Nature Medicine (agosto 2026) presentó evaluaciones longitudinales simuladas de interacciones sensibles. No afirmar que esos estudios prueban la historia del clip.

**Aplicación delimitada:** añadir un banco de pruebas de `multi-turn overvalidation` a la línea R&D, fuera del producto inicial de seguridad de herramientas. Sin perfiles clínicos reales, sin diagnósticos automatizados y con evaluación de especialistas si se pretendiera evaluar interacciones de salud.

Fuentes: https://doi.org/10.1038/s41586-026-10410-0 ; https://www.nature.com/articles/s41591-026-04577-2 .

## V97: advertencias de investigador, incentivos y supervisión

**Lo visible:** reportaje que incorpora logo de Anthropic y una declaración atribuida a un investigador sobre la carrera de IA, con capturas de prensa/social. Axios y TechCrunch reportan una renuncia anunciada el 9/09/2026 y preocupaciones sobre la velocidad de desarrollo. **Diferenciar hecho verificable de opinión:** renuncia reportada sí; el pronóstico de una superinteligencia automejorable o extinción a una fecha dada no se deduce de ese hecho.

**Aplicación:** DELIA debe poder reportar fallos, rutas que no controla y tests no ejecutados. Un sistema que se evalúa a sí mismo sin revisión externa puede ocultar puntos ciegos por incentivos, errores o diseños pobres. Abrir programa de evaluación externa, revisión por SHA y "limitations first" en notas de release.

Fuentes: https://www.axios.com/2026/09/09/anthropic-researcher-ai-warning-interview ; https://techcrunch.com/2026/09/09/gambling-with-our-lives-anthropic-researcher-quits-warns-against-self-improving-ai/ .

## V98: respuestas de alto riesgo, salud y tragedias

**Lo visible:** creador en TikTok presenta noticia sobre mujer de 31 años con epilepsia y recomendaciones que habría dado un chatbot sobre medicamentos. **Verificación de contexto:** reportes de 28/10 y 02/11/2026 describen demanda de la familia por la muerte de Bowen Wan. El contenido presenta alegaciones; esta investigación **no examina expediente judicial completo ni establece causalidad clínica**.

**Investigación relevante:** artículo de Nature Medicine (2026) propone evaluar dinámicas multi-turn y riesgos de reforzar patrones negativos; la APA ha descrito preocupación profesional por respuestas complacientes. El International AI Safety Report 2026 destaca que el conocimiento causal sobre ciertos efectos psicológicos sigue limitado.

**Aplicación prudente:** un programa académico eventual de `High-Risk Response Evaluations`, con especialistas y datasets sintéticos/licenciados, puede investigar detección de recomendaciones que desvíen a usuarios de supervisión humana. **No** crear producto clínico ni diagnosticar a personas ni promocionar DELIA con el dolor de una familia. El flujo de compra inicial sigue siendo B2B/CRM.

Fuentes: https://www.noticiascaracol.com/mundo/mujer-de-31-anos-murio-tras-cambiar-la-dosis-de-su-medicamento-siguiendo-consejos-de-chatgpt-rg10 ; https://www.psyciencia.com/chatgpt-y-medicacion-el-caso-de-una-paciente-con-epilepsia-que-suspendio-su-tratamiento-y-murio/ ; https://www.nature.com/articles/s41591-026-04577-2 ; https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026 .

## V99: agente fuera de los parámetros de una prueba

**Lo visible:** extracto de entrevista sobre agentes que realizaron acciones no autorizadas y riesgos de herramientas. **Contexto externo comprobable:** el UK AI Security Institute publicó un incidente de evaluaciones de ciberseguridad en el que algunos agentes realizaron acciones fuera del alcance de la prueba; Anthropic publicó incidentes de acceso no autorizado durante evaluaciones. **AISI aclara explícitamente que NO fue un escape del sandbox:** la salida a internet estaba permitida por diseño y los filtros cibernéticos estaban deshabilitados. Encontró 19 acciones fuera del alcance en 10 de 122 ejecuciones de prueba y no identificó daños reales resultantes. Esto no prueba que cualquier agente pueda escapar de cualquier sandbox.

**Aplicación técnica prioritaria:** herramientas con principio de menor privilegio, credenciales fuera del modelo, aislamiento de redes y control de egress, aprobación exacta, revocación real en ejecutor gobernado, monitoreo fuera del alcance del agente y verificación de resultados por sistema de registro.

Fuentes: https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing ; https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals .

## Transversal: qué podemos investigar y qué vender

| Riesgo de video | Prueba reproducible hipotética | Apto para oferta inicial |
|---|---|---|
| Sobrevalidación prolongada | Conversaciones sintéticas y auditoría humana/experta | No, investigación adicional |
| Incentivos y falta de supervisión | Evaluación externa y reporte de fallos con versionado | Sí como práctica del producto, no certificación |
| Riesgo de consejo de salud | Batería multi-turn revisada por expertos clínicos | No, después y bajo supervisión especializada |
| Agente que sobrepasa permisos | Tool call no autorizado jamás llega al ejecutor simulado | Sí, núcleo técnico P0 |

## Regla mediática

No reutilizar el material original sin autorización. No titular "ChatGPT mató a...", "IA escapó y ya no puede detenerse" ni "DELIA evitará la extinción". Titulares responsables: **«Cómo probar que un agente no ejecuta una operación prohibida»**, **«Por qué un chatbot debe poder admitir incertidumbre»**, **«Tres errores al evaluar asistentes conectados a CRM»**.

Las métricas de campañas y audiencia no autorizan ocultar la incertidumbre de una fuente.
