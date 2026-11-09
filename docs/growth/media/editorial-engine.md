# DELIA Evidence Media Engine — estrategia de visibilidad con demanda medible

**Ventana inicial:** 09/11/2026–08/01/2027. **Sin posts publicados ni programados por este documento.** Todo contenido es original y debe pasar revisión de evidencias, técnica, privacidad, propiedad intelectual y disponibilidad de producto.

## Posicionamiento editorial

**Categoría propuesta:** Enterprise AI Operations Assurance. **Promesa periodística:** explicar qué pueden hacer los agentes, qué pruebas independientes pueden limitar acciones y dónde quedan incertidumbres. **Promesa comercial acotada:** evaluación reproducible de un flujo concreto, no seguridad universal.

**Tono:** técnico pero comprensible, sobrio, sin miedo artificial. Conclusión práctica en cada publicación; enlaces a evidencia/experimento y corrección visible si cambia la fuente.

## Cinco pilares de contenido

1. **Prueba DELIA:** código reproducible, escenario bloqueado, SHA, entorno y lo que NO protege.
2. **Radar de seguridad de agentes:** analizar un incidente verificado, los límites del reporte y el control concreto a probar.
3. **Negocio y operaciones:** costo de revisión de un agente, onboarding de integradoras, contratación, ROI bien definido.
4. **Educación responsable:** sycophancy, prompt injection, tool hijacking, idempotencia, `unknown`, diagnóstico equivocado y divulgación científica.
5. **Construcción abierta:** ingeniería, decisiones de no construir, benchmarks contra alternativas y contribuciones del equipo con atribución y consentimiento.

## Canal, audiencia y CTA

| Canal | Audiencia | Cadencia base propuesta | Contenido/CTA |
|---|---|---|---|
| LinkedIn fundador y/o MasterTech | CTO, consultoras, CISO, operaciones | 2 posts/semana, sujetos a revisión | Problema + prueba + «conversemos de un flujo de CRM» |
| GitHub DELIA | Developers, security engineers, investigadores | 1 actualización técnica por semana | Tests, issues y reproducibilidad |
| YouTube Shorts/TikTok | Público tech y descubrimiento | 1 video ORIGINAL de 30–60 s/semana | «Ver prueba y límites en GitHub», no vender diagnóstico como producto |
| Artículo técnico/blog | Compradores que necesitan justificar inversión | 2 artículos/mes | Diagrama de operación y guía para evaluarla |
| Comunidad técnica/meetup | Integradoras y colaboradores | 1 demo abierta cada 4–6 semanas si hay capacidad | Reproducir 10 casos sintéticos |
| Email B2B individual | Prospectos profesionales pertinentes | Solo contacto legítimo según contexto | Una pregunta sobre su proceso y costo |
| Portugués / inglés | Partners regionales/globales | Inglés en fuentes y resumen; PT solo tras revisión nativa | Misma evidencia, jamás traducir claims sin verificar |

**No abrir todas las redes a la vez:** si el equipo dispone de menos de 6 h/sem para contenido, elegir LinkedIn + GitHub y reutilizar una demo corta quincenal.

## Embudo medible

Impresión → visita atribuible a investigación/README → descarga o ejecución de demo → pregunta técnica → discovery consentido → posible workshop E1 → design partner con contrato → Partner SaaS solo tras seguridad.

**KPI principal:** conversaciones calificadas con compradores que ya tienen agentes conectados a tools. **KPIs secundarios:** installs verificadas, retención del demo, feedback de no-fit, citas de fuentes, tasa de error/corrección. Vistas/likes = señales de distribución, no dinero.

**Atribución:** usar enlaces UTM cuando sea compatible y consentimiento de analytics; evitar tracking de terceros no autorizado. No publicar emails, capturas de chats privados ni cuentas de compradores.

## Calendario de ocho semanas

| Semana | Tema editorial | Activo demostrable | CTA medible |
|---|---|---|---|
| 09–15 nov | «Qué significa controlar una tool y qué no» | README + matriz de 14 riesgos | Visitar inventario / feedback técnico |
| 16–22 nov | «Una herramienta denegada no debe ejecutarse» | Mock o explicar que test aún está pendiente | Revisar issue P0 / solicitar entrevista |
| 23–29 nov | «Chile: de IA piloto a gobernanza» | ITD-IA 2026, 740 empresas | Conversación con integradora |
| 30 nov–06 dic | «No basta un DENY escrito por el LLM» | Demo de adapter solo cuando exista | Comparar con stack del comprador |
| 07–13 dic | «Los 4 resultados de una tool: confirmed/rejected/unknown/mismatch» | Contratos de laboratorio y límites | Descargar script de demo |
| 14–20 dic | «Cómo evalúas un agente que puede modificar un CRM» | Batería de pruebas con alcance | Proponer workshop sintético |
| 21–27 dic | «Lo que falló en DELIA y cómo lo comprobamos» | Reporte verdadero de QA, nunca inventado | Issue o contribución |
| 28 dic–03 ene | «Qué debe exigir un CTO antes de dar permisos» | Checklist reproducible de amenazas | Pedir revisión de un flujo |
| 04–08 ene | «Estado real de beta: logros, no-go y limitaciones» | SHA, resultados de CI y lista de gates | Solicitar demo solo si producto apto |

Una pieza solo se publica si el elemento «activo demostrable» existe. Si no, publicar una explicación transparente del test planeado, sin fingir que ya pasó.

## Cadena de producción

1. Investigación: un editor registra claim ID y fuente primaria con fecha.
2. Técnico: revisor confirma que el claim de producto corresponde a SHA/CI real.
3. Legal/ética: autorización de imágenes, citas, datos personales, salud/menores y publicidad.
4. Producción: guion, visuales **originales**, subtítulos precisos, CTA y accesibilidad.
5. Revisión final de lenguaje en ES/EN/PT según corresponda.
6. Publicación humana autorizada por canal; guardar URL y fecha solo cuando exista.
7. Seguimiento: visitas, errores, preguntas calificadas, correcciones y conversiones en CRM privado.

**Nunca:** usar extractos de TikTok de terceros sin permiso, deepfake de expertos, logos implicando colaboración, testimonios inventados, noticia de muerte como anzuelo para pagar DELIA, ni «certificado por OWASP».

## Experimentos A/B sin manipulación

A = «Cómo probar que un agente no ejecutó una acción prohibida»; B = «Por qué los permisos del LLM no bastan». Misma CTA técnica, ventana comparable, tamaño de muestra, sin ocultar contenido a compradores. Contenido no convierte automáticamente en ventas; aprender qué preguntas generan conversaciones útiles.

## Reputación y respuesta ante errores

Publicar corrección visible con fecha si una fuente se desmiente o la prueba falla. Archivar versión anterior en GitHub cuando sea seguro. En temas clínicos/legal, atribuir alegaciones y no discutir identidades de personas vulnerables innecesariamente. Ver [kit de prensa](press-trust-kit.md).
