# 08 — Tablero de dirección: métricas que sirven para tomar decisiones

## No inventar una «probabilidad» de éxito

El software no puede convertir 2 entrevistas y 25 tests en un porcentaje confiable de ventas. La herramienta `commercial_ops.decision_support` genera un **índice de prioridad de investigación 0–100**, que **NO es una probabilidad de conversión**. El éxito requiere resultados de mercado, retención, seguridad y margen observados.

## KPIs de cinco capas

| Capa | Indicador | Fórmula o evidencia | Qué indica |
|---|---|---|---|
| Problema | Entrevistas con dolor confirmado | Conteo con fecha, costo y alternativa documentados | Existencia de problema |
| Compra | Compradores con presupuesto/decisión identificados | Documento/confirmación de actor económico | Capacidad de contratar |
| Producto | Tiempo a primera política segura | Horas de instalación independiente bajo criterios fijos | Fricción de adopción |
| Seguridad | Ejecuciones no autorizadas en test E2E | Conteo con fixture SHA, entorno y versiones | Correctness limitada al conjunto |
| Negocio | Costo por workflow verificado | Costos operativos atribuibles / acciones externamente reconciliadas | Valor económico por uso |
| Comercial | Ofertas de pago aceptadas | Contratos, pago, fechas y alcance | Monetización demostrada |
| Retención | Renovaciones/uso mensual | Cuentas activas y cohortes | Adopción sostenible |
| Partner | Tenants activos y margen partner | Facturación y costos segmentados | Distribución que escala |

**Nunca usar conteo de acciones de un modelo como resultado empresarial**. Un agente puede gastar más tokens y ejecutar más pasos sin producir más valor.

## Scorecard heurístico (0 a 100, no chance)

Nueve dimensiones 0–4: gravedad, frecuencia, costo documentado, acceso al comprador económico, presupuesto, urgencia, facilidad de integración, brecha real frente a sustituto, capacidad interna. Los pesos son iguales por conveniencia inicial, **no están estadísticamente calibrados**.

**Reglas duras, independientemente del índice:**
- Sin consentimiento para discovery → no contactar.
- Sin evidencia verificada → solo investigación.
- Problema bajo o alternativa suficiente → no-fit.
- Sin comprador/presupuesto → descubrir, no proponer SaaS.
- Datos reales o herramientas con efectos → laboratorio o revisión independiente; **nunca autorización automática**.
- Reembolso → solo laboratorio mientras no haya gates financieros.

## Tres semáforos separados

1. **Comercial:** verde solo si hay dolor, comprador y avance registrado, no por número de mails.
2. **Producto:** verde por test E2E sobre SHA con revisión; sintético es ámbar para producción.
3. **Seguridad:** cualquier P0 abierto = rojo para piloto con datos reales; ningún contrato comercial puede saltar esto.

## Carta de decisiones quincenal

| Pregunta | Evidencia necesaria | Decisión posible |
|---|---|---|
| ¿Alguien paga por resolver este problema? | Oferta con precio y aceptación/cobro | Mantener oferta, ajustar o descartar |
| ¿Qué alternativa usa hoy? | Herramienta y versión, costo | Integrar, reemplazar o no-fit |
| ¿Tenemos un proceso repetible? | Dos instalaciones pareadas | Producto o consultoría |
| ¿El margen aguanta soporte? | Horas y COGS reales | Subir precio, automatizar o limitar |
| ¿Hay un riesgo de seguridad abierto? | P0/tests/reviewer | No-Go |
| ¿Vale desarrollar un segundo pack? | Uso y presupuesto del primero | Ampliar o aplazar |

## Gates de aprendizaje

**G0 20/11:** al menos 3 conversaciones genuinas + documentación de alternativa (meta).
**G1 18/12:** 5 entrevistas profundas con proceso; una demo comparativa segura (meta).
**G2 08/01:** dos instalaciones externas del laboratorio, tiempo y fallos medidos (meta).
**G3 15/01:** Go/No-Go técnico con matriz P0.
**G4 31/03:** decisión seguir, pivotar o reducir inversión con evidencia comercial.

### Criterios para pivot

Si 15 entrevistas del ICP no revelan dolor repetido con dueño económico o ninguna persona quiere siquiera explorar una evaluación de alcance acotado, detener construcción generalista y reconsiderar segmento/propuesta. Si las alternativas resuelven mejor y más barato el flujo, DELIA debe interoperar o limitarse a contratos/servicios. Son **reglas de gobierno propuestas**, no resultados históricos.

## Registro de decisión (ADR comercial)

```text
Fecha:
Hipótesis y segmento:
Evidencia a favor (fuente/fecha):
Evidencia en contra:
Tamaño de muestra:
Alternativa vigente:
Costos y riesgos:
Decisión: seguir / ajustar / pausar / abandonar
Responsable que acepta:
Fecha de próxima revisión:
```

## Scorecard semanal — tabla simple

| Semana | Prospectos investigados | Discovery consentido | Problemas confirmados | Ofertas pagadas | Pilotos seguros | MRR verificado | Incidentes P0 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 09/11 | No medido | No medido | No medido | No verificado | No verificado | No verificado | P0 abiertos |

No reemplazar `No medido` por cero sin consultar registros reales. No usar datos personales o contactos identificables en tablas públicas.

## Modelos de ingresos

Las cifras de MRR 2027 en los roadmaps previos son aspiracionales, no forecasts ni targets suficientes para contratar equipo. Revisarlas trimestralmente según cobros, churn y margen. Nunca anunciar valoración por multiplicador sobre ingresos hipotéticos.

## Indicadores a evitar

Estrellas de GitHub como demanda pagada, visualizaciones como compradores, cantidad de commits como tracción, tests unitarios como seguridad productiva, logos de prospectos como contratos, emails enviados como pipeline firme, reembolsos sintéticos como dinero ahorrado.
