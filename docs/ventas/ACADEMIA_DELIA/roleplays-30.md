# Laboratorio de 30 roleplays comerciales y técnicos

## Metodología
Dos participantes: comprador escéptico y representante DELIA. Cada sesión 8 minutos: 2 diagnóstico, 3 objeciones, 2 propuesta, 1 resumen. Observador mide exactitud y claridad por separado. No memorizar frases, practicar estructuras. Puntuar con `evaluacion-y-rubricas.md`.

## Nivel 1 — explicaciones fundamentales (1–10)
1. **CEO curioso:** «¿En una frase qué hace DELIA?». Meta: qué/para quién/estado; no recitar acrónimo. Contraataque: «¿Y si no uso IA?». Salida: no-fit.
2. **Desarrollador junior:** «¿Qué es un gateway?». Meta: diagrama con aplicación, control y proveedor. Repregunta: «¿Intercepta todo mi navegador?». Salida: no, solo integraciones configuradas.
3. **Comprador latinoamericano:** «¿Qué es RUT y por qué importa?». Meta: patrón local y precisión, no inventar reglamentos. Repregunta: «¿Y México?». Salida: estado PR #20.
4. **CTO:** «¿Qué significa deny-by-default?». Meta: operar solo reglas explícitas; sin policy DENY. Repregunta: «¿Puedo modificar el role?». Salida: hoy demo lo recibe del llamante, auth pendiente.
5. **Analista:** «¿Cuál es la diferencia entre precisión y recall?». Meta: TP/FP/FN y sesgo del corpus. Repregunta: «Entonces 100 % real?». Salida: NO.
6. **Especialista en privacidad:** «¿Qué retienen sus recibos?». Meta: metadatos y hashes, no prompt; HMAC no implica cifrado de datos.
7. **Operaciones:** «¿Por qué necesita un supervisor?». Meta: acciones sensibles sobre umbral; aprobación exacta y de un uso en demo.
8. **Fundador integrador:** «¿Cuánto tiempo toma instalar?». Meta: demo offline inmediata; tiempo de integración empresarial NO MEDIDO.
9. **Contabilidad:** «¿Qué ventaja económica tiene?». Meta: describir método ROI, no ahorro garantizado.
10. **Periodista:** «¿Es el primer firewall de agentes de la región?». Meta: NO verificado; competidores existentes; diferenciación por demostrar.

## Nivel 2 — compradores informados (11–20)
11. **CTO con LiteLLM:** «Ya tengo routing, budgets y logs». Meta: reconocerlo y preguntar por tool enforcement, no inventar lagunas del producto.
12. **CTO con Cloudflare:** «También tengo DLP». Meta: benchmark pareado y compras basadas en brechas concretas, no vender detección simple.
13. **Ingeniero con PrivAiTe:** «Ya anonimiza y restaura». Meta: conocer su modelo, discutir eventual valor de approvals por agente.
14. **CISO con Strathon:** «Ya tengo firewall de herramientas». Meta: reconocer capacidades publicadas y proponer evaluación real, no «somos únicos».
15. **Jefe de RR.HH.:** «Mis datos son sensibles». Meta: rechazar demo con PII real, ofrecer datos sintéticos y gate legal.
16. **Líder de producto:** «¿Qué habrá el 15 de enero?». Meta: beta condicionada, ruta P0 y potencial recorte de alcance.
17. **Arquitecto:** «¿Se puede saltar el engine por otra ruta?». Meta: sí, en demo; enforcement endpoint real pendiente.
18. **Proveedor enterprise:** «¿Tienen ISO 27001 o SOC 2?». Meta: no presentar certificación no obtenida; facilitar controles y proceso.
19. **Finanzas:** «¿Puedo transferir $100.000 sin aprobación?». Meta: no inferir umbral comercial; policy configurable, demo no ejecuta dinero.
20. **Procurement:** «¿Dónde alojan datos y quién responde?». Meta: no hay productivo actual; contrato/hosting/residencia deben definirse.

## Nivel 3 — confrontación y negociación (21–30)
21. **CISO hostil:** «Un agente fabricó una aprobación». Meta: identidad criptográfica y antifraude no implementados, bloquear producción.
22. **Red teamer:** «Cambio el importe tras aprobar». Meta: hash exacto de argumentos y replay test, pero persistencia atómica pendiente.
23. **CTO escéptico:** «Solo son regex y más burocracia». Meta: reconocer componentes base, demostrar control de herramientas, cuantificar fricción.
24. **Comprador enfadado:** «Una falsa alarma detuvo ventas». Meta: tasas reales, opt-in por riesgo, revisión, no prometer ausencia de falsos positivos.
25. **Integrador con poco presupuesto:** «Puedo hacerlo en dos días». Meta: quizá sí; comparar costo total y responsabilidad, no atacar.
26. **Abogado:** «La Ley 21.719 exige usar DELIA?». Meta: NO; el estado legislativo debe verificarse por fecha; controles no equivalen a cumplimiento.
27. **Inversionista:** «¿Cuánto ARR tienen?». Meta: ARR no demostrado; hipótesis y fórmula, compradores no contactados.
28. **Directivo:** «Quiero instalarlo mañana con datos reales». Meta: negarse, explicar P0 y proponer entorno sintético.
29. **Cliente hipotético con incidente:** «¿DELIA causó una fuga?». Meta: no inventar investigación, canal seguro y plan de preservación de evidencia.
30. **Comité de inversión:** «¿Cómo construirán un negocio grande si otros tienen todo esto?». Meta: nicho, benchmarks, canal integradores, coste de integración, pruebas y riesgos, sin números inventados.

## Rúbrica individual por sesión
Por cada caso: 0–5 en comprensión, 0–5 exactitud técnica, 0–5 capacidad de contraste, 0–5 honestidad de límites, 0–5 siguiente paso apropiado. Máximo 25. Descalificación del ensayo si afirma certificación, producto desplegado, tasa de éxito universal o clientes inexistentes.

## Ejercicios de contrainterrogatorio
El comprador debe hacer «¿Dónde está la prueba?» dos veces; una sobre código y otra sobre retorno económico. El expositor no puede contestar con una hipótesis como si fuera dato. Pedir que enlace PR, workflow, dataset y un contrato piloto real si existe.

## Examen final
Elegir 3 casos al azar: 1 de cada nivel. Exponer 3 minutos sin slides y contestar 4 preguntas duras por caso. Aprobación de práctica interna: >=60/75, cero afirmaciones falsas críticas, capacidad de explicar arquitectura con precisión. Registrar aprendizajes solo en espacio privado del equipo cuando involucren personas o negociaciones.
