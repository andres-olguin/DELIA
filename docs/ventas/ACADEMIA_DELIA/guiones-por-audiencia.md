# Guiones por audiencia y duración — DELIA Trust Fabric

Todas las versiones son **borradores para práctica**. Ajustar según descubrimiento y estado técnico; no asumir vínculos comerciales ni necesidad. La condición de prototipo debe quedar clara.

## Pitch de 20 segundos — integrador
«Si conectas agentes de IA a facturación o CRM, sabes que ocultar datos no basta: también hay que controlar qué operaciones pueden ejecutar. DELIA está desarrollando una capa de políticas, aprobaciones y evidencia para esos flujos, con pruebas regionales para Latinoamérica. ¿Cómo controlan esas operaciones hoy?».

## Pitch de 40 segundos — CTO
«DELIA se está construyendo como plano de control para agentes y aplicaciones de IA. El motor local ya permite probar reglas con denegación por defecto, aprobación de un solo uso y recibos verificables por HMAC. Todavía nos falta identidad real, integración en el proxy y aprobación durable. Nos gustaría entender su arquitectura y comparar una regla específica contra lo que ya utilizan».

## Pitch de 60 segundos — CISO
«El riesgo más delicado aparece cuando una IA deja de responder preguntas y comienza a ejecutar acciones. DELIA busca conectar autenticación, políticas por organización, filtros de datos, autorización de herramientas y evidencia mínima. Hoy podemos demostrar el algoritmo en laboratorio y ejecutar pruebas reproducibles. Antes de tratar datos de clientes necesitamos cerrar controles de identidad, egreso, persistencia y una revisión independiente. ¿Qué acción crítica necesita gobernar su empresa?».

## Pitch de 90 segundos — CEO de integradora
«Una integradora que despliega asistentes para muchos clientes repite controles de datos, permisos y trazabilidad. Eso consume horas y crea inconsistencias. DELIA busca ofrecer políticas reutilizables por cliente y por agente, con autorizaciones para acciones sensibles y evidencia sin almacenar el mensaje completo por defecto. Estamos probando un motor local, y la meta interna es una beta avanzada a mediados de enero, supeditada a calidad y seguridad. Si el problema existe para ustedes, podemos construir juntos una matriz de dos o tres herramientas y comparar costo, facilidad de integración y seguridad frente a su stack actual. ¿Cuánto les ocupa hoy mantener esos controles?».

## Pitch de 2 minutos — presentación en red
«Soy parte del equipo que desarrolla DELIA, una plataforma experimental de seguridad de agentes de IA. La mayoría de empresas piensa en qué responde el chatbot, pero a medida que conecta herramientas la pregunta cambia: ¿qué puede hacer? Imagina un agente que solicita emitir un reembolso de 18.000 pesos mexicanos. Nuestra demo ficticia consulta una política: si supera un umbral, necesita autorización independiente vinculada al importe; si alguien intenta reutilizar el ticket, se rechaza. Ese motor está probado en laboratorio con Python, pero no está conectado a operaciones reales ni listo para datos de clientes. También investigamos detección regional de identificadores y evidencia auditable. La propuesta comercial sería entregar ese control a integradoras y SaaS que ya usan agentes. Hoy buscamos entender problemas y probar hipótesis de producto. Me gustaría hacerte dos preguntas: ¿qué herramientas conectas a tus agentes?, ¿qué ocurre cuando una acción requiere permisos especiales?».

## Reunión 10 minutos — guion de hilo
1. «Antes de mostrar nada, quiero entender el flujo».
2. «¿Quién autoriza operaciones sensibles hoy?».
3. «Resumiré lo que entendí; corrígeme si algo está mal».
4. «Lo que estamos construyendo es un control de herramienta, no un sustituto mágico de su IAM».
5. «Podemos demostrar una simulación y enseñar los límites».
6. «Si no hay brecha con lo que usan, probablemente no necesiten otra plataforma».
7. «Si existe, acordemos un test limitado con casos sintéticos».

## Preguntas de cierre por rol
- CTO: «¿Cuál es la llamada que podríamos someter a pruebas comparativas?».
- CISO: «¿Qué política de aprobación sería un indicador claro de reducción de riesgo?».
- CFO: «¿Podemos estimar el costo actual del control manual antes de hablar de retorno?».
- Jurídico: «¿Qué datos y transferencias habría que mapear con su equipo?».
- CEO integrador: «¿Qué cliente piloto ficticio y sin datos reales representa mejor su mercado?».
- Desarrollador: «¿Qué ejemplo runnable o SDK les resultaría útil para evaluar?».

## Negativa profesional
«Por lo que describes, su solución actual resuelve estas necesidades y DELIA todavía no agregaría suficiente valor. Prefiero dejarlo registrado y revisar nuevamente si aparecen limitaciones específicas».

## Diferenciar a MasterTech
Explicar que DELIA es un desarrollo impulsado en el ecosistema MasterTech SpA. No atribuir a la sociedad proyectos del portafolio personal freelance ni afirmar facturación/productos desplegados que no estén registrados. Evitar cargos, nombres del equipo y compromisos comerciales no aceptados expresamente.

## Práctica de estilo
El mismo pitch en versiones: técnica, ejecutiva, coloquial, muy breve. Identificar y reducir «la idea», «por otro lado», redundancia y tecnicismos innecesarios. Responder primero la pregunta; usar ejemplos solo si son útiles.
