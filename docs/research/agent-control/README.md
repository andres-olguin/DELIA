# DELIA Agent Control Research — seguridad y control humano de agentes

**Versión:** 09/11/2026. **Estado:** estudio y plan de evaluación. **No** es tecnología para controlar AGI, no está validado en producción y **no** afirma prevenir catástrofes ni pérdida global de control. Las evaluaciones y controles críticos descritos son futuros salvo el laboratorio sintético citado expresamente.

## Motivación y procedencia

Un video de recopilación periodística aportado para analizar EL PROYECTO DELIA reúne comentarios y advertencias sobre inteligencia artificial y pérdida de control, con extractos históricos de varias fechas. **Es un disparador para formular preguntas, no evidencia científica suficiente ni autorización para copiar o distribuir el video.** No almacenamos el material audiovisual en el repositorio, no atribuimos citas textuales sin transcripción y contexto verificables, y no deducimos que un riesgo extremo sea inevitable.

Fuentes primarias modernas: [International AI Safety Report 2026](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026), [panel científico de la ONU (septiembre 2026)](https://www.un.org/independent-international-scientific-panel-ai/en/thematic-briefs/ai-agents-misalignment-risks), [OWASP Agentic Top 10](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/), [OWASP Agent Control Standard](https://genai.owasp.org/resource/agent-control-standard-acs/), [NIST AI RMF GAI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence), [MITRE ATLAS](https://atlas.mitre.org/), [UK AISI ControlArena](https://control-arena.aisi.org.uk/) y [Monitorability Evals](https://alignment.openai.com/monitorability-evals).

El informe internacional distingue daños actuales observables de escenarios futuros de pérdida de control, cuya probabilidad y dinámica generan desacuerdo científico. No equiparar una simulación de evaluación con una catástrofe en el mundo real.

## Tesis técnica acotada

**DELIA investiga controles verificables de agentes de IA en procesos empresariales donde existen herramientas y permisos concretos.** Un agente puede solicitar, pero no debe tener autoridad para cambiar la política o ejecutar fuera del punto de control. Los mecanismos de revocación y límites deben pertenecer a infraestructura independiente del agente, y sus evidencias han de contrastarse con efectos del sistema real cuando sea seguro.

### Preguntas científicas y de ingeniería

1. ¿Qué comportamiento adversarial se observó realmente, en qué entorno y con qué capacidad?
2. ¿Qué actor controla el ejecutor, la red, la política, las credenciales y la auditoría?
3. ¿Podemos probar que una operación prohibida **no ocurrió** en un sandbox instrumentado?
4. ¿Qué ocurre al reiniciar, reintentar, delegar, revocar o modificar argumentos?
5. ¿Qué falla si el monitor, el modelo o el evaluador se equivoca?
6. ¿Qué evidencia necesitamos para afirmar una cobertura limitada y reproducible?

## Tres programas independientes

**A. Enterprise Agent Control (prioridad P0):** IAM por principal real, least privilege, límites de herramientas, bloqueo de salida de datos, aprobaciones exactas, revocación independiente, auditoría minimizada y reconciliación. Aplicación comercial al ICP de integradoras con CRM/BPO.

**B. Control Evaluation Lab (prioridad P1):** control evals, red teaming de prompt injection, poisoning y bypass, reportes sobre SHA, muestras holdout y explícita tasa de falsos negativos. Evaluación inspirada por ControlArena y MITRE ATLAS, no reproducida ni validada todavía.

**C. Frontier Control Research (exploratorio P3):** monitorabilidad, robustez ante agentes que se adaptan al evaluador, capacidad de sabotaje y limitaciones de supervisión. Investigación abierta y colaborativa, **no** afirmación de que DELIA protege contra IA superinteligente o extinción.

## Riesgos y pruebas

[Inventario JSON de 14 escenarios](controls-research-matrix.json), con hipótesis de control y test, prioridad y evidencia marcada `PLANNED`, `LAB_SYNTHETIC` o `RESEARCH`. El inventario **no** dice que esas pruebas ya pasaron. El preflight sintético de Outcome Assurance en `main` demuestra una comprobación local de condiciones, no control en un ejecutor externo.

[Protocolo experimental y requisitos de prueba](evaluation-protocol.md) · [Producto y economía responsable](product-opportunity.md) · [Plan y decisiones](roadmap.md).

## Distinción crítica

Un módulo DELIA no controla a un modelo remoto sin acceso o un agente que pueda usar otro ejecutor. La «parada de emergencia» solo puede impedir nuevas ejecuciones en interfaces bajo control de la organización, y requiere pruebas sobre esos puntos, no un botón decorativo. No prometer «control total» de sistemas avanzados.

## Integridad de investigación

- Fuente, fecha, versión y evidencia para cada afirmación externa.
- Separar amenaza observada, escenario hipotético, mitigación propuesta y prueba realmente ejecutada.
- Control y revisor independientes, entorno sandbox con datos ficticios, no investigación ofensiva en sistemas ajenos.
- Ningún puntaje de seguridad sin denominador, fixture y escenario reproducibles.
- No usar como referencia de certeza científica titulares o cortes de video sin contexto.

## Comando de validación del estudio

```bash
python -m unittest tests.test_agent_control_research -v
python -m tools.validate_agent_control_research
```

Valida la estructura y las precauciones del inventario; **no prueba controles de seguridad de producción**.
