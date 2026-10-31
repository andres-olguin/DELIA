# DELIA — Entrevista de descubrimiento B2B (30 minutos)

**Estado:** investigación, no propuesta vinculante. Objetivo: identificar problema real, alternativa y autoridad de compra, no pedir elogios del producto.

## 0–3 minutos · encuadre y consentimiento
«Gracias por conversar. Estamos investigando seguridad y gobernanza de integraciones con modelos de IA. No necesitamos datos personales, credenciales ni ejemplos reales de sus clientes. ¿Está bien tomar notas desidentificadas para nuestra investigación interna? Puede pedirnos detener la toma de notas».

## 3–8 minutos · mapa de producto y personas
1. ¿Qué producto suyo **ya opera** con APIs LLM? ¿Desde cuándo, con qué usuarios y volumen aproximado (si pueden revelarlo)?
2. ¿Quién es dueño de arquitectura, seguridad, operación y presupuesto?
3. ¿Qué herramientas ya usan: Cloudflare, LiteLLM, Azure, Bedrock, Model Armor, Presidio, otra?
4. ¿Dónde se transforman o revisan los datos antes de llamar al proveedor?

## 8–16 minutos · problema real y costo actual
5. Cuénteme el último caso en que una política de datos impidió un lanzamiento o provocó trabajo manual. ¿Qué ocurrió, cuándo y cuánto trabajo exigió?
6. ¿Qué identificadores locales llegan a sus flujos de prueba (RUT, NIT, CURP, RFC u otros) y cómo tratan falsos positivos?
7. ¿Cuánto tiempo/hora-persona invierten por mes en mantener controles por cliente/aplicación?
8. ¿Qué coste paga su organización por gateway, DLP, logs, hosting o consultoría? ¿Qué parte no conoce?
9. ¿Qué riesgo o brecha ha priorizado seguridad para este trimestre, si alguno?
10. ¿Por qué no sería suficiente mantener su solución actual?

## 16–22 minutos · compra y competencia
11. ¿Quién aprueba herramientas nuevas? ¿Qué requisitos de seguridad/legal hay para un nuevo intermediario?
12. ¿Se ha aprobado presupuesto para este problema? ¿De qué partida saldría y en qué ventana de compra?
13. ¿Qué 2–3 proveedores compararon y por qué ganó el actual?
14. ¿Qué costo tendría el cambio e integración, aparte del precio de licencia?
15. ¿Han pagado antes por un servicio comparable? ¿Qué métricas motivaron la decisión?

## 22–27 minutos · piloto y evidencia
16. Sin compartir datos reales, ¿qué conjunto de prueba sintético reflejaría los casos difíciles?
17. ¿Qué precisión/recall/latencia, retención y capacidad técnica serían exigibles?
18. ¿Qué criterios harían **inaceptable** un piloto?
19. Si el benchmark demostrara una brecha no cubierta, ¿quién lideraría un piloto, autorizaría la arquitectura y aprobaría un contrato **pagado**?
20. ¿Qué evento interno tendría que suceder para considerar una compra? (No preguntar simplemente «¿le gusta DELIA?»).

## 27–30 minutos · cierre responsable
«Resumiré sin datos sensibles los problemas que escuché, la solución actual y si tiene sentido una segunda conversación. Si no vemos un encaje claro, no vamos a insistir».

**Métricas/CRM privado:** fecha, país, sector, rol (no nombre público), actual stack verificado, problema reciente, costo conocido/NV, presupuesto conocido/NV, autoridad, siguiente acción consentida, criterios de privacidad, objeciones.  
**Salida:** clasificar I0–I5 de forma observada, no asignar intención de compra por cortesía.

**Entrevista rechazada o sin presupuesto:** cerrar agradeciendo; no crear un lead «caliente». Los riesgos P0 del software prohíben pilotos de datos reales hasta revisión técnica.
