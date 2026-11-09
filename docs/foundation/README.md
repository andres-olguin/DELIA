# DELIA — Foundation 2026: guía corta, verdad de producto y límites de lanzamiento

**Revisión:** 09/11/2026. **Estado real:** investigación y laboratorios sintéticos. La publicación de esta guía **NO convierte DELIA en SaaS, gateway productivo, herramienta certificada ni servicio que deba procesar datos reales**.

## 1. Qué estamos construyendo

**Visión:** DELIA estudia cómo controlar y comprobar operaciones de agentes IA conectados a sistemas empresariales.

**Primer mercado que probaremos:** integradoras B2B en Chile y México que implementan agentes en CRM/ticketing para más de un cliente.

**Diferenciador por validar:** un **kit de aseguramiento operacional por proceso** que se superpone a la infraestructura existente, expresa reglas, prueba fallos con datos ficticios, mide conformidad entre stacks y entrega un informe reutilizable con costo real por cliente. **Las piezas ya tienen competencia** (Helio, Pruvz, ACPT, AgentTrustOps, OpenShell, LangSmith, etc.). La combinación debe ganar su valor mediante pruebas con compradores. No decir «único» ni «primero».

**Posible negocio hoy, condicionado:** un **diagnóstico profesional de un proceso** con límites de confidencialidad, entrega y precio pactados; **no** prometer un gateway certificado. El precio CLP $290.000 de los escenarios es exploratorio, no tarifa validada.

**Negocio futuro:** kit de conformidad, SDK, Partner SaaS, enterprise/self-hosted y nuevas verticales **solo cuando existan controles, demanda y margen**.

## 2. Qué hay realmente en main

- DLP regional experimental y tests sintéticos, **pero el proxy HTTPX no tiene protección comprobada en egreso**.
- Laboratorio de contratos de resultados y comparador de dos adaptadores ficticios; **no** es un ensayo con dos gateways reales.
- Investigación de 40 referencias internacionales, riesgos de agent control y plan de captación.
- Simulador de ventas diciembre–enero y borradores de publicaciones; **no** son ingresos/clientes ni publicaciones programadas.
- Rama PR #21 de Trust Fabric abierta como DRAFT; no se debe presentar como integrado a main.

## 3. Estado real de seguridad — advertencia P0

[Libro de 13 controles](readiness-controls.json) y [evaluación de código](../../tools/foundation_doctor.py) registran problemas visibles de importaciones, reenvío de mensajes, autenticación, credenciales, logs, modelo DB y enforcement. Son señales verificables de código, **no evidencias de ataque real**. Su lista no es completa, y no sustituye auditoría independiente.

### Comandos

```bash
python -m unittest tests.test_foundation_doctor -v
python -m tools.foundation_doctor
# Un pipeline de release DEBERÍA bloquearse mientras existan P0:
python -m tools.foundation_doctor --require-production-ready
```

El último comando devuelve un código distinto de cero **a propósito**, porque este programa no concede autorización de producción automáticamente. El reporte usa heurísticas estáticas y evidencia declarada; aun con todos los checks limpios se requiere revisión técnica, legal y aprobación humana externa a este código.

### Tres niveles que nunca deben confundirse

1. **Investigación/demo sintética:** solo fixtures falsos, sin credenciales ni sistemas productivos; rotular `LAB/TEST ONLY`.
2. **Diagnóstico profesional de proceso:** depende de un contrato, permisos, privacidad y capacidad; el cliente puede terminar eligiendo una alternativa comercial distinta a DELIA.
3. **Software de control/piloto real:** **bloqueado** hasta resolver P0 y ensayar enforcement E2E, identidades, revocación y fuente autoritativa. Ni una venta ni un CI verde levantan el veto.

## 4. Prioridades de desarrollo para los próximos 10 días

1. **Arquitectura:** corregir arranque/imports y definir un esquema de auditoría con migraciones; eliminar bypass en salida. Ver [plan focalizado](PLAN_10_SEMANAS.md).
2. **Privacidad/identidad:** autorización de clientes y aislamiento, sanitización antes de egreso, logs minimizados, secretos fuera del código.
3. **Una demo CRM real de laboratorio:** una herramienta de prueba permitida, una denegada con **cero efectos observados** y un caso `unknown` que no se reporta como éxito.
4. **Una venta que se pueda entregar:** diagnóstico de un proceso, con entregables, exclusiones, precio por cotización y costos/hora.
5. **Una sola campaña de presencia orgánica:** LinkedIn + GitHub y clip original si existe prueba; registrar enlaces y conversaciones reales.

No iniciar salud, finanzas, pagos, marketplace, SOC, cloud enterprise o 18 verticales hasta tener seguridad y compradores.

## 5. Indicadores de cierre de esta etapa

| Evidencia | Estado |
|---|---|
| Instalar y arrancar en entorno limpio con una fuente de BD aislada | PENDIENTE |
| Negar e impedir ejecución E2E de una herramienta no autorizada | PENDIENTE |
| Demostrar token/canary sintético bloqueado antes de salida upstream | PENDIENTE |
| Autenticación real, tenant isolation y auditoría minimizada | PENDIENTE |
| Contrato CRM comparable en dos stacks reales | PENDIENTE |
| Una persona externa reproduce demo sin ayuda del equipo | PENDIENTE |
| Una conversación real con presupuesto y problema repetitivo | PENDIENTE |
| Primer post LinkedIn publicado con URL y fecha | PENDIENTE |
| Métricas de margen y pago real de primera oferta | PENDIENTE |

La tarea no es declarar esas filas completas hoy, sino diseñar pruebas que las hagan inequívocas.

## 6. Lecturas rápidas

- [Secuencia de producto y seguridad hasta enero](PLAN_10_SEMANAS.md).
- [Posicionamiento y criterios para abandonar nuevas ideas](UNICA_APUESTA_Y_KILL_RULES.md).
- [Oferta de diagnóstico profesional y delivery](SERVICIO_DIAGNOSTICO.md).
- [Competidores internacionales](../estrategia/red-team-competitivo-2026-11-09.md) y [18 referencias adicionales](../growth/launch-2026-2027/competencia-adicional.md).
- [Campaña social y ventas](../growth/launch-2026-2027/plan-redes-y-captacion.md).
- [Seguridad y divulgación responsable](../../SECURITY.md).

**Regla de cierre:** la base está preparada para **seguir desarrollando y probar**, no para declarar a DELIA listo para producción.
