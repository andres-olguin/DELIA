# 40 objeciones y respuestas responsables para DELIA

Edición de práctica. Plantilla: **validar preocupación → evidencia concreta → limitación → pregunta siguiente**. Se permiten respuestas breves y naturales; no memorizar literalmente. Estado 2026-11-09: no producto de seguridad certificado, no pilotos pagos confirmados.

## A. Comparación de productos (01–10)
1. **«PrivAiTe ya protege PII»**. Sí, y su trabajo es relevante. DELIA explora políticas de herramientas y evidencia vinculada a identidad junto con detectores regionales; esa combinación empresarial todavía debe validarse. ¿Qué parte de su solución actual les resulta insuficiente?
2. **«LiteLLM ya tiene gateway»**. Correcto: no pretendemos superar su routing por cantidad de proveedores. Nuestra hipótesis es actuar como control plane de decisiones y aprobaciones integrable. ¿Qué tool-calls ejecuta hoy su aplicación?
3. **«Cloudflare tiene DLP»**. Coincido; conviene comparar precisión regional, falsos positivos, costo y experiencia de operación con la misma batería de pruebas. No hemos ejecutado esa comparación aún.
4. **«Strathon ya hace Agent Firewall»**. Sí; es una razón para no afirmar novedad mundial. Nuestro posible valor está en integración de clientes latinoamericanos y pruebas regionales. Antes de comprar, comparen los dos productos.
5. **«Soup Wall también tiene gateway»**. Exactamente. Podemos aprender de su enfoque e incluso evaluar coexistencia; necesitamos identificar un dolor que no satisfaga.
6. **«Microsoft Presidio hace anonimización»**. Presidio es una opción real. No queremos reemplazar un detector suficiente; el foco adicional serían las políticas de acción, evidencia y despliegue por integradores.
7. **«Un regex bastaría»**. Para formatos controlados, quizá sí. Lo que estamos validando es el costo de fallas, límites de contexto, cambios de versión, comprobación independiente y acciones de agentes; si regex cubre su problema, úselo.
8. **«Ya usamos IAM corporativo»**. Bien. Lo adecuado es integrarse con ese IAM; no inventar otro. Falta construir identidad verificable en DELIA y comprobar scopes para herramientas.
9. **«Podemos desarrollar nuestra herramienta»**. Puede ser la mejor alternativa. Compare horas, revisión de seguridad, mantenimiento por países, pruebas y costo de propiedad; no asumamos que DELIA gana.
10. **«No veo una diferencia real»**. Es una observación válida. Si su infraestructura ya resuelve identidad, tool approval, DLP regional y evidencia, hoy no hay argumento suficiente para migrar.

## B. Seguridad y exactitud (11–20)
11. **«¿Qué porcentaje de datos sensibles atrapa?»**. El benchmark histórico de `main` fue insuficiente; PR #20 informa 55/55 en un corpus sintético de desarrollo de 96 casos, no precisión general. Falta corpus independiente.
12. **«¿Pueden garantizar cero fugas?»**. No. Ningún ensayo limitado permite garantizarlo. Diseñamos controles fail-closed, pruebas adversariales y medición, y admitimos riesgos residuales.
13. **«¿Tienen una certificación ISO/SOC?»**. No está acreditada ninguna certificación DELIA. Podemos mostrar políticas, pruebas y plan de hardening cuando estén disponibles.
14. **«¿Dónde almacenan mis prompts?»**. En este prototipo no se envían prompts a nadie; los recibos de simulación no incluyen argumentos crudos. El diseño de almacenamiento productivo aún no está aprobado.
15. **«¿Qué pasa si el detector falla?»**. La arquitectura objetivo exige bloqueo o política explícita de error. El flujo real de proxy todavía requiere correcciones P0.
16. **«¿Un hacker puede modificar el rol?»**. En el simulador, los roles se declaran, por tanto no es autenticación real. No recomiendo usarlo con datos o acciones reales hasta implementar identidad confiable.
17. **«¿Puede un agente saltarse DELIA?»**. Sí si puede ejecutar herramientas por canales fuera del enforcement. La beta deberá obligar a pasar por un adapter y probar ese límite.
18. **«¿Y si se reutiliza una aprobación?»**. El prototipo demuestra consumo de un solo uso en memoria. El escenario multiproceso requiere persistencia transaccional e idempotencia antes de producción.
19. **«¿Su firma HMAC demuestra que nunca se filtró información?»**. No. Solo acredita la integridad de ciertos metadatos con una clave. La ausencia de fuga requiere trazas y pruebas en el punto de salida.
20. **«¿Usan datos reales para probar?»**. No en este trabajo. Corpus y demo son sintéticos; un piloto autorizado requerirá condiciones legales, técnicas y contractuales especiales.

## C. Producto y roadmap (21–30)
21. **«¿Cuándo está listo?»**. Meta interna: beta avanzada el 15-01-2027, condicionada al cierre de controles P0. Es planificación, no garantía de despliegue productivo.
22. **«¿Las veinte ideas funcionan?»**. No. El catálogo distingue simulación, PR externo y plan; vendemos solo capacidades acreditadas por versión.
23. **«¿Puedo usarlo mañana?»**. Únicamente en laboratorio sintético en esta fase. No recomendamos tráfico productivo.
24. **«¿Tienen dashboard?»**. Está planificado y priorizado; no se debe presentar un mock o diseño como consola operativa.
25. **«¿Soportan PDF y audio?»**. Multimodal está en el roadmap, no implementado integralmente.
26. **«¿Tienen soporte en Brasil?»**. El catálogo considera expansión regional, sin afirmar detector LGPD o atención comercial brasileña ya validada.
27. **«¿Trabaja con agentes MCP?»**. Se propone un adapter con políticas de herramienta, pero no hay gateway MCP productivo. Podemos diseñar un contrato de prueba.
28. **«¿Puede instalarse self-hosted?»**. El prototipo Python corre localmente; un paquete enterprise autoinstalable con hardening y soporte aún está pendiente.
29. **«¿Y el fallback de proveedores?»**. Está en la arquitectura objetivo; no afirmar soporte operativo sin tests e2e, timeouts y consistencia de políticas.
30. **«¿Qué pasa si cae DELIA?»**. La opción segura para operaciones sensibles es fallar cerrados. Disponibilidad, recuperación y SLO se deberán medir con carga y runbooks.

## D. Precio, compras y confianza (31–40)
31. **«¿Cuánto cuesta?»**. Hay hipótesis de US$149/499/1499 por segmentos, no lista oficial. Primero definamos problemas, usuarios, integraciones y costo real.
32. **«¿Cuál es el ROI garantizado?»**. Ninguno. Podemos calcularlo con su baseline y medirlo en piloto; multas evitadas no equivalen a ahorro cierto.
33. **«¿Por qué pagar si hay software libre?»**. Solo pagaría por funciones adicionales, soporte, integración y responsabilidad que el software libre no cubra para su caso. Si no aporta valor, no comprar.
34. **«¿Qué ocurre con mis datos si dejan de operar?»**. Debemos diseñar exportación, retención y borrado contractual; no hay políticas productivas vigentes que prometer.
35. **«¿Son una empresa grande?»**. MasterTech es un emprendimiento en etapa inicial. No exageramos personal, experiencia corporativa ni ingresos.
36. **«¿Qué clientes tienen?»**. No hay clientes pagadores de DELIA confirmados. No atribuir a MasterTech los trabajos freelance personales de su fundador.
37. **«¿Pueden firmar SLA 99,9 %?»**. No sin mediciones, respaldo operativo y contrato que podamos cumplir.
38. **«¿Tenemos que decidir ahora?»**. No. Una decisión de seguridad requiere revisión técnica; acordemos una prueba de alcance claro y un calendario realista.
39. **«¿Qué pasa si un auditor externo encuentra un fallo?»**. Registraremos severidad, mitigación, responsables y evidencia. Un hallazgo crítico bloquearía producción.
40. **«¿Por qué debería confiar en ustedes?»**. No pedimos fe. Mostramos código, pruebas con SHA, limitaciones y un método de aceptación verificable; si no lo superamos, no recomendamos desplegar.

## Prácticas cronometradas
- Nivel A: responder 1–10 en 20 segundos cada una.
- Nivel B: responder 11–20 en 35 segundos, incluyendo un límite explícito.
- Nivel C: responder 21–30 en 30 segundos con fecha objetiva o NO VERIFICADO.
- Nivel D: responder 31–40 en 45 segundos con siguiente acción y sin presión.
- Una persona debe responder la objeción contraria («Si otro producto sí lo hace, ¿por qué DELIA?»). Calificación separada de persuasión, exactitud y ética.

## Errores eliminatorios
Inventar clientes, resultados, certificaciones, compatibilidad productiva, cumplimiento legal, soporte regional o disponibilidad; ocultar P0 #9; confundir benchmarks; utilizar datos personales reales en demo. En caso de error crítico, reiniciar el roleplay.
