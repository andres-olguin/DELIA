# DELIA — Pitch y mensajes de entrevista al nicho integrador

**Estado:** solo entrevistas y validación, 31/10/2026.

## Elevator pitch (30 segundos)

«Los integradores que construyen agentes de IA para varias empresas tienen que decidir qué datos envía cada aplicación al modelo y cómo auditan esa decisión. Estamos desarrollando DELIA y probando reglas para identificadores latinoamericanos. Ya tenemos un corpus sintético y un detector parcial, pero todavía no un gateway de seguridad listo. Nos interesa conversar con equipos que usan LiteLLM, Presidio, Cloudflare u otras herramientas para saber qué trabajo repiten y si existe una mejora medible que realmente valga la pena desarrollar».

## CTO / arquitectura

«¿Qué parte de sus filtros de datos, permisos y telemetría implementan desde cero en cada cliente? Si ya tienen una solución suficiente, también nos sirve conocerla».

## Responsable de seguridad

«¿Cómo demuestran con tests que identificadores RUT/NIT de una solicitud no salen innecesariamente al proveedor LLM y qué brechas documentan? No pedimos logs ni datos reales».

## Socio / gerente general

«¿Cuántas horas de ingeniería consume cada nueva integración de políticas de datos? Solo nos interesa estudiar una alternativa si ese costo existe y es verificable».

## Objeciones que **debemos aceptar**

- «Ya usamos Presidio» → preguntar por costo de crear/sostener recognizers regionales; no alegar que Presidio carezca de ellos.
- «Ya tenemos Langfuse / Cloudflare» → reconocer controles existentes, pedir especificidad del vacío; no vender redundancia.
- «El middleware agrega un riesgo» → correcto hasta que se prueben auth, fail-safe, aislamiento, latencia y logs.
- «No tienen clientes DELIA» → correcto; estamos en descubrimiento y no pretendemos lo contrario.

## Llamado a la acción permitido

«¿Tendrían 20 minutos para una entrevista técnica sin información confidencial? Al terminar podemos compartirles un resumen anónimo de hallazgos y el benchmark sintético abierto, con sus limitaciones».

Se debe ofrecer el benchmark de forma **no exclusiva** y sin condicionar la entrevista a compra. Nunca afirmar certificaciones o beneficios no medidos.
