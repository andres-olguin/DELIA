# Playbook de implementación de las veinte capacidades

## Plantilla de cada ticket
ID TF-XX; usuario y problema confirmado; ejemplo positivo; tres negativos; threat model; contrato API/objeto; dependencia; DRI voluntariamente aceptado; revisor; estado; evidencia CI (SHA/run); presupuesto; riesgo residual y documentación de despliegue. No declarar Done por crear un stub.

## Definition of Ready
- Alcance y límites definidos, sin ambigüedad de quién lo usa.
- Historial de 1–2 soluciones alternativas contrastadas.
- Mocks sintéticos, escenarios de fallo y tests definidos.
- Acceso y capacidad del colaborador confirmados.
- Impacto en datos de clientes y jurisdicción evaluado.

## Definition of Done
- Código probado y aprobado por otra persona cuando afecte seguridad.
- Tests con datos sintéticos, negativos, regresión y versiones; métricas sin maquillaje.
- Una ruta E2E de ejecución sin bypass cuando la capacidad permita acciones externas.
- Control de secretos, registros, retención, rollback y evidencia de despliegue.
- Usuario/comprador prueba utilidad, no solo equipo técnico declara «terminado».
- Documento versionado y capacitación de soporte.

## Camino crítico de enero
#6 arranque → #7 auth/tenant → #8 secretos/logs → #9 sanitización previa al upstream → #11 CI → TF-06 firewall/adapter → TF-07 aprobación durable → TF-11 recibos → TF-12 policy studio → TF-14 observability. Los módulos exploratorios quedan desacoplados.

## Decisiones por prioridad
P0: protege contra fugas/acciones sin permiso. P1: beta avanzada requerida. P2: amplía mercado o madurez sin bloquear beta. P3: investigación especulativa, no requisito de lanzamiento.

## Protocolo de venta
El presentador debe mencionar el ID y estado (LAB, PR, PLAN) de la capacidad antes de demostrarla. Cualquier afirmación de que está operativa necesita pruebas reales del punto de ejecución, no solo resultados de un mock. Todo posible cliente debe recibir exclusiones y limitaciones.

## Cierre del 15-01-2027
Acta Go/No-Go por versión, CI, P0, amenazas, retención, costos, compradores entrevistados y soporte. **La fecha no obliga a lanzar una beta insegura.**
