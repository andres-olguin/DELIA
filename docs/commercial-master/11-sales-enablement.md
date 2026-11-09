# 11 — Academia de preventa DELIA: mensajes, presentaciones y objeciones

**Uso para entrenamiento de equipo**, no testimonios ni afirmaciones de implementación empresarial. El laboratorio de contratos está en `main`, y Trust Fabric en PR #21 DRAFT. Cualquier demo requiere esta advertencia.

## Propuesta de 10 palabras

«DELIA busca verificar y controlar operaciones empresariales realizadas por agentes de IA».

No decir «garantiza» ni «sin riesgo». En su etapa actual solo demuestra precondiciones y reconciliación sobre datos ficticios.

## Pitch 30 segundos — CTO de integradora

«Cuando despliegas agentes para varios clientes, el riesgo ya no es solo qué responde el modelo, sino qué puede modificar y cómo sabes que el resultado fue correcto. DELIA está desarrollando contratos de operación que especifican permisos, límites, aprobación y comprobación posterior, con especialización latinoamericana. Hoy tenemos un laboratorio reproducible, no un gateway productivo. Me interesa saber cómo resuelves eso hoy y qué parte te cuesta mantener».

## Pitch 90 segundos — founder/COO de integradora

«Imagina entregar un agente a un segundo cliente que usa un CRM distinto. Hay que repetir reglas, autorizaciones, manejo de errores y evidencia de cada cambio. A medida que agregas cuentas, esa repetición consume margen. DELIA busca empaquetar contratos operativos verificables por cliente. Un contrato incluye qué herramienta puede invocarse, cuáles son sus límites y cómo verificar el resultado. Ya tenemos un laboratorio sintético que detecta condiciones incompatibles y resultados desconocidos, aunque aún faltan identidad, ejecución segura y conectores de producción. Estamos probando si esta especialización reduce horas de integración frente a lo que ya se usa, incluyendo gateways abiertos. Si tu solución actual lo hace mejor, es preferible conservarla. ¿Cómo manejan hoy la aprobación y comprobación de cambios en un CRM?».

## Pitch 20 segundos — comprador de operaciones

«No queremos venderte otro chatbot. Buscamos que los procesos asistidos por IA tengan condiciones comprobables y excepciones gestionables. Estamos en fase de pruebas y queremos medir qué parte de tus revisiones manuales consume más tiempo».

## Presentación de 10 slides para una reunión de 15 minutos

| # | Título | Mensaje clave | Prueba o pregunta |
|---|---|---|---|
| 1 | Qué hace DELIA | Visión de operaciones verificables | Aclarar estado LAB |
| 2 | El problema actual | Tools permiten efectos fuera del texto | Preguntar qué modifica el agente |
| 3 | Coste oculto | Repetición de políticas/integración | Solicitar horas de proceso real |
| 4 | Qué usan hoy | Reconocer IAM/gateway existente | Preguntar qué hace bien |
| 5 | Contrato operacional | Precondiciones, permiso, efecto, resultado | Diagrama |
| 6 | Demo local | Reembolso ficticio, saldos, desconocidos | `python -m experiments.contract_assurance.demo` |
| 7 | Lo que NO hace | No IAM, no dinero, no upstream protegido | P0 y PR #21 |
| 8 | Diferenciación a medir | Reutilización, regional, instalación | Comparación justa |
| 9 | Posible paquete E1 | Workshop con entregables y exclusiones | Presupuesto a validar |
| 10 | Cierre | ¿Vale medir un flujo suyo con sandbox? | Próximo paso acordado |

## Demo de 2 minutos

0:00: «Esto es laboratorio. No accede a su CRM ni procesa pagos».
0:20: explicar contrato de devolución ficticia, tenant y pedido.
0:45: ejecutar `python -m experiments.contract_assurance.demo`.
1:10: mostrar que `ELIGIBLE_FOR_AUTHORIZATION` NO es permiso de ejecutar; `VERIFIED_SIMULATED` es coincidencia de datos falsos.
1:35: preguntar «¿qué regla de su CRM necesitaría algo similar?» y anotar alternativa actual.

**No mostrar una salida verde como prueba de seguridad de clientes.**

## Objeciones principales

**«¿Por qué no usar Temporal?»** Respuesta: «Temporal es válido para procesos durables. DELIA tendría valor si su contrato de negocio y su guía de seguridad ahorran configuración; aún debemos medirlo. No necesitamos reemplazar Temporal».

**«Helio ya tiene aprobación»**: «Sí. Nuestra hipótesis va más allá del estado de la tool-call y se concentra en verificar una regla de negocio y el resultado; reconozco que AgentTrustOps y Temporal resuelven partes similares».

**«Quiero conectarlo mañana a producción»**: «No sería responsable: faltan auth, egress y ejecución segura. Sí podemos hacer un estudio o sandbox aislado».

**«¿Cuánto cuesta?»**: «Estamos validando paquetes. Para un workshop de alcance limitado podemos cotizar horas y entregables; el SaaS aún no tiene precios oficiales ni está disponible».

**«Necesito certificación de cumplimiento»**: «No tenemos una certificación DELIA; podemos mapear controles y recomendar revisión por profesionales acreditados».

**«¿Cuánto ahorra?»**: «Solo podemos calcularlo si medimos su proceso actual, el nuestro y costos completos. No tenemos un porcentaje general probado».

**«¿De quién es la propiedad intelectual?»**: «La licencia del repositorio es MIT y debe respetarse; para una relación comercial hay que revisar titularidad, contribuciones y alcance contractual».

**«Ustedes son pequeños»**: «Es verdad que DELIA está en etapa temprana. No proponemos un despliegue crítico, sino un ejercicio técnico de alcance y evidencia, con condiciones claras».

**«No veo diferencia con mi stack»**: «Entonces no recomendaría reemplazarlo. Si desean contrastar costos para un proceso concreto, podemos hacerlo; de lo contrario podemos descartar esta oportunidad».

## Roleplays de ventas — cinco exámenes

1. CTO con stack Helio/OPA que resuelve el 90 % del flujo. Objetivo: detectar no-fit sin insistir.
2. CFO que pregunta por un ROI de 200 %. Objetivo: negar cifra inventada y diseñar medición.
3. Integrador con 5 clientes que exige descuentos y soporte 24/7. Objetivo: costo real y límites de capacidad.
4. Jefe BPO que insiste en cargar un CSV de clientes. Objetivo: rechazar PII y ofrecer casos sintéticos.
5. Inversionista que confunde 25 tests con 25 clientes. Objetivo: distinguir evidencia técnica y comercial.

## Evaluación

Separar exactitud técnica, comunicación, escucha, manejo de riesgo, claridad económica y cierre, cada una 0–5. Cero afirmaciones críticas falsas como requisito. No usar conversaciones reales de terceros para entrenamiento sin consentimiento.

## Seguimiento de reunión (estructura)

«Gracias por explicarme cómo trabajan con [flujo]. Entendí que actualmente utilizan [alternativa] y que el costo principal es [hecho confirmado]. Podemos evaluar [alcance limitado] con datos ficticios, sin tocar producción. Lo que DELIA todavía no resuelve es [limitación]. Si consideran que vale la pena, acordemos un caso, una métrica y quién debe revisarlo».

## Material relacionado

`docs/ventas/ACADEMIA_DELIA/` contiene el programa anterior en PR #21. Este documento lo aterriza al ICP de integradoras y la oferta E1 actual. No copiar números de ROI de ejemplos como si fueran resultados de clientes.
