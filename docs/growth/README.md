# DELIA — Research × Product × Media × Revenue

## Lanzamiento comercial y redes: dic 2026–ene 2027

El [programa de lanzamiento y presencia](launch-2026-2027/plan-redes-y-captacion.md) revisa 18 competidores adicionales, descarta reclamos de unicidad sobre nombres ocupados, propone LinkedIn como canal B2B prioritario y aporta [borradores originales](launch-2026-2027/publicaciones-iniciales.md) y [escenarios comerciales reproducibles](launch-2026-2027/proyeccion-comercial-dic-ene.md). **No hay posts programados/publicados, ventas ni MRR de SaaS acreditados.** La previsión se limita a servicios profesionales que requieren alcance y capacidad verificados.


**Programa de aceleración:** 09/11/2026–15/02/2027. **Estado:** investigación, estrategia y herramientas de integridad editorial; no publicaciones realizadas, ventas, socios, financiación adjudicada ni release de seguridad empresarial. La planificación técnica del 15/01/2027 sigue sujeta a veto P0.

## Tesis de crecimiento

DELIA debe ser reconocido por una promesa verificable: **«Operaciones empresariales con agentes de IA bajo controles probados y resultados comprobables»**. La capacidad comercial requiere tres ciclos integrados, no tres marcas desconectadas:

**Prueba técnica → investigación publicable → conversación con comprador → hipótesis de producto → nueva prueba.**

La marca pública no debe depender de proclamar AGI catastrófica, «100 % seguro», liderazgo mundial, certificación, asociación con institutos de seguridad o ahorros no medidos. El contenido con más valor a largo plazo será el que un CTO pueda reproducir y un comprador pueda evaluar en términos de costos.

## Aportes de cuatro clips examinados visualmente

El usuario aportó cuatro clips audiovisuales a la conversación. Se inspeccionaron fotogramas y texto en pantalla; **no se realizó transcripción completa y autenticada del audio**, ni análisis forense de montaje. Los videos **no se incorporan ni redistribuyen en el repositorio**.

| Clip | Mensaje visual | Nivel de comprobación | Decisión editorial y técnica |
|---|---|---|---|
| 1000119096 | Historia viral «preguntó 50 veces si estaba loco» | **No verificada** como hecho individual; no hay diálogo íntegro ni evidencia de 50 respuestas | No citar como hecho. Investigar complacencia/sycophancy y evaluación multi-turn |
| 1000119097 | Advertencias de un investigador sobre carrera de IA y riesgos | Renuncia y declaraciones reportadas por prensa; **sus pronósticos no son hechos** | Explicar presión, supervisión y transparencia; no citar predicciones como probabilidades |
| 1000119098 | Muerte de mujer de 31 años y alegaciones de consejo médico sobre epilepsia | Reportes sobre demanda; **no veredicto judicial ni causalidad demostrada aquí** | Evitar explotar tragedia en anuncios; estudiar límites de información de salud con expertos |
| 1000119099 | Agentes que realizaron acciones no autorizadas en pruebas | Un incidente técnico relacionado está documentado por UK AISI; la edición del clip no sustituye el informe | Construir pruebas de aislamiento, revocación, anti-bypass, pre-egress |

Véase [registro de evidencias](media-evidence/claims.json) y [análisis de fuentes y límites](research/video-findings.md).

## Documento principal por frente

- [Investigación y evaluación científica](research/video-findings.md): riesgos de comportamiento, sycophancy, seguridad conversacional, escapes de sandbox y distinción entre daños observados e hipótesis.
- [Investigación de mercado 2026 y competencia](research/market-opportunity.md): CORFO/CCS, Endeavor México, NIST, OWASP, investigación sobre marketing B2B. No se infiere demanda pagada de encuestas.
- [Aceleración de producto: hitos y capacidad](execution/roadmap-accelerated.md): trabajo crítico P0, un E2E de CRM, benchmarks independientes, gates, equipo y planes de contingencia.
- [Máquina editorial de 60 días](media/editorial-engine.md): LinkedIn, GitHub, video corto, artículos y sesiones técnicas.
- [Banco de formatos y guiones para medios](media/content-playbook.md): scripts originales, títulos responsables, contraejemplos, mensajes para CTO y prensa.
- [Mediakit y plan de reputación](media/press-trust-kit.md): identidad MasterTech/DELIA, enlaces, FAQ, declaraciones y gestión de crisis.
- [Distribución comercial y experimentos de venta](business/gtm-experiments.md): ICP, conversión, partners, pricing, outbound y métricas.
- [Matriz de apuestas y asignación de recursos](business/venture-portfolio.md): crecimiento ambicioso por etapas, no 18 productos simultáneos.
- [Registro JSON de hechos y fuentes](media-evidence/claims.json), [calendario programático](media-evidence/calendar.json) y tests de integridad (ver abajo).

## Orden de prioridad (no negociable)

**P0:** seguridad real de identidad/tenant, DLP de egress, tools, aprobación e idempotencia, con revisión independiente.  
**P1:** entrevistas de compradores, demo CRM sintética E2E, primer contenido técnico con fuente y primer workshop de alcance honesto.  
**P2:** API/SDK, programa de integradores, beta con métricas y kit de prensa.  
**P3:** content en portugués, expansión al ecosistema de medios, marketplace, sectores altamente regulados y defensa de marca internacional.

## Qué NO existe todavía

Una certificación independiente, SDK de producción, SaaS multiempresa, clientes pagadores DELIA verificados en esta carpeta, métricas de ingresos obtenidos, benchmark de superioridad frente a Helio/OPA/Temporal, autorización para operar CRM de terceros o alianza con los laboratorios citados. Las fechas son **objetivos** sujetos a capacidad, revisión y evidencia.

## Integridad editorial automatizada

```bash
python -m unittest tests.test_growth_evidence -v
python -m tools.validate_growth_evidence
```

El validador confirma consistencia de fuentes, restricciones de publicación y calendario; **no verifica que una noticia sea verdadera ni publica contenido**. Es una barrera de calidad, no sustituto de revisión humana.

## Gobierno y decisión

Un artículo solo puede cambiar de `DRAFT` a aprobado mediante revisión humana de fuente, fecha, claims, derechos de imágenes/audio, producto real y CTA. **No existe integración ni autorización automática para publicar posts**. Las conversaciones de compradores se registran en CRM privado con bases de contacto apropiadas, nunca en GitHub público.

El éxito se medirá por **compradores que confirman problema y precio, instalaciones técnicas verificadas, margen real y renovaciones**, no por vistas o seguidores aislados.
