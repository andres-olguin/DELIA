# DELIA — Master Commercial Operating System (MCOS)

**Revisión:** 09/11/2026. **Dueño comercial propuesto:** dirección de MasterTech SpA; DRI y capacidad deben confirmarse. **Estado:** estrategia y herramientas de planificación, no clientes, ventas, pilotos productivos ni producto certificado. Versionado en GitHub; no divulgar datos de prospectos.

## La decisión que cambia el plan

El crecimiento de DELIA no vendrá de añadir 30 funciones indiferenciadas. La oportunidad de aprendizaje y caja más cercana está en **un flujo de atención y CRM de bajo riesgo en integradoras tecnológicas que ya entregan agentes**.

**Posicionamiento paraguas:** DELIA — *Verified Enterprise AI Operations*. La propuesta es reducir incertidumbre al permitir que las operaciones de agentes cumplan reglas concretas y mostrar evidencia de los resultados. No se promete que el sistema actual ya pueda hacerlo en producción.

**Oferta inicial, no servicio existente:** *DELIA Workflow Readiness Lab* — diagnóstico pagado de un proceso, threat model ligero, matriz de permisos, casos sintéticos, contraste con gateway actual, informe y diseño de piloto. No es certificación de seguridad ni prueba de protección productiva.

**Producto núcleo posterior:** DELIA Outcome Assurance para integradores B2B2B; un contrato de proceso versionado + APIs/adapters de autorización y resultado, con política regional y métricas. Requiere cerrar #6/#7/#8/#9/#11, desarrollar ejecución segura y revisión externa antes de operaciones reales.

## Tres motores del negocio

1. **Learning engine:** entrevistas, pruebas negativas y exclusiones; registra también quién decide NO comprar y por qué.
2. **Revenue engine:** servicio de descubrimiento de alcance estrecho → piloto de laboratorio condicionado → Partner/Cloud/Enterprise cuando la seguridad esté lista.
3. **Proof engine:** resultados verificables de proceso y costos; CI, integración reproducible, métricas económicas y evidencia honesta, no una colección de logos.

## Orden estricto de prioridades

| Prioridad | Frente | Por qué |
|---|---|---|
| P0 | Identidad, egress, control de ejecución y secretos | Sin seguridad real no hay producto empresarial |
| P1 | 10 entrevistas de problema en segmento muy definido | Confirmar comprador, dolor y sustitutos |
| P1 | Una demo BPO/CRM de bajo riesgo en sandbox | Menor fricción que ejecutar reembolsos reales |
| P1 | Oferta Workflow Readiness Lab con entregables y precio testable | Camino ético a ingresos tempranos por valor humano real |
| P1 | Primer design partner que acepte medir integración | Poder demostrar adopción y valor incremental |
| P2 | Paquetes ecommerce y otros sectores | Después de comprobar repetibilidad |
| P3 | Marketplace, red federada, 18 sectores completos | Después de retención y distribución |

**Prohibido:** convertir tareas P0 en «Done» por pasar tests sintéticos, afirmar ingresos inexistentes, vender procesamiento de datos sensibles, usar contactos privados en GitHub o declarar éxito comercial por completar documentos.

## Índice operativo

1. [Segmento único, comprador y estrategia de posicionamiento](01-segmento-y-competencia.md)
2. [Escalera de ofertas y monetización con exclusiones](02-ofertas-y-precios.md)
3. [Manual detallado de descubrimiento, prospección y entrevistas](03-prospeccion-y-discovery.md)
4. [Programa de design partners y pruebas seguras](04-design-partners.md)
5. [Distribución B2B2B y programa de integradoras](05-canal-partner.md)
6. [Roadmap maestro 09/11/2026–31/03/2027](06-roadmap-ejecucion.md)
7. [Financiación y capital de operación, convocatoria BIG13](07-financiacion-y-capital.md)
8. [Sistema de KPI, experimentos y decisión de pivot](08-metricas-y-decisiones.md)
9. [Registro de riesgos y claims](09-riesgos-y-controles.md)
10. [Benchmark contra alternativa existente y prueba de valor](10-benchmark-comparativo.md)
11. [Mensajes, presentaciones, guiones y manejo de objeciones](11-sales-enablement.md)
12. [Árbol de productos y opciones estratégicas a 2028](12-expansion-y-opciones.md)
13. [Sprint comercial de 14 días listo para delegar](13-sprint-14-dias.md)
14. [Evidencia del mercado, estudios y fuentes oficiales](14-fuentes-y-supuestos.md)
15. [Ficha comercial de una página para compradores](15-onepager-para-compradores.md)
16. [Plantilla de alcance de design partner, NO contrato jurídico](16-ficha-piloto-y-mou.md)
17. [Programa de evidencia Product–Market Fit](17-programa-validacion-pmf.md)

## Herramienta ejecutable

```bash
python -m unittest tests.test_commercial_decision_support -v
python -m commercial_ops.demo
```

`commercial_ops/` evalúa **prioridad heurística**, no probabilidad matemática de venta. El índice de 0 a 100 no es forecast ni justifica contactar a alguien sin consentimiento. El simulador económico nunca representa facturación real.

## Estado verificado al corte

- El nuevo laboratorio de Outcome Assurance está en `main` (PR #30) y validado con tests sintéticos: no autentica ni ejecuta herramientas.
- Trust Fabric sigue en [PR #21](https://github.com/andres-olguin/DELIA/pull/21), borrador, con módulos de laboratorio y seguridad productiva pendiente.
- En `main` hay cobertura PII insuficiente según benchmark histórico y pendientes P0. PR #19 y #20 de colaboradores se revisan por separado.
- Las ediciones SaaS/Partner y 18 verticales son portafolio propuesto, no servicios disponibles.
- **No se han acreditado aquí clientes DELIA, ventas, entrevistas, certificaciones, contratos, fondos adjudicados ni métricas de retención.**

## Regla maestra

Cada semana responder: **¿qué riesgo de negocio importante hemos reducido con evidencia?** Si solo se generó documentación y no se validó una hipótesis con un comprador, el avance comercial de la semana es cero.

## Fuente de verdad

El backlog técnico está en GitHub; el estado de mercado y CRM debe vivir en sistema privado con consentimiento. GitHub público guarda únicamente estadísticas anonimizadas, hipótesis, casos sintéticos, metodología y resultados autorizados. Los contratos reales, grabaciones, datos de clientes y propuestas confidenciales nunca se publican.
