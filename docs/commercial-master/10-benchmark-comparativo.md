# 10 — Benchmark de compra: DELIA frente a hacer nada, construir y comprar

**No se ha realizado este benchmark instrumentado todavía.** La matriz define pruebas comunes y criterios de evaluación, no resultados ni ganadores.

## Las seis alternativas legítimas

0. **Hacer nada:** continuar manualmente o no automatizar; siempre debe tener costo y riesgos medidos.
1. **Construir internamente:** código propio con permisos de CRM y pruebas; comparar esfuerzo del equipo.
2. **Helio / gateways MCP:** approvals, presupuestos y políticas según documentación.
3. **Temporal + OPA/Cerbos:** workflow durable y autorización; calcular integración y costo de mantener.
4. **Agentgateway + política existente:** gateway/autoridad central sin DELIA, quizá suficiente.
5. **Suite Microsoft/Google/Palo Alto:** seguridad y gobierno como parte de ecosistema amplio, sujeto a ediciones.
6. **DELIA propuesta:** contrato sectorial + evidencia de resultado y guía de integración; nunca afirmar superioridad sin prueba.

## Caso universal: CRM de ticket sintético

- El cliente A autoriza lectura y etiquetado; B no puede leer A.
- El agente intenta exportar contactos o borrar: debe denegarse antes de la llamada.
- Una aprobación de modificación debe estar ligada a argumentos e identidad real.
- Un timeout produce estado UNKNOWN y no duplica efectos.
- Un resultado simulado diferente del estado real del mock produce MISMATCH.
- El reporte no debe incluir email/número original del ticket.
- Registrar tiempo y errores de instalación por un desarrollador externo.
- Validar si la solución requiere subsistemas que el equipo ya posee y si la integración es más simple sin DELIA.

## Batería de escenarios

| Prueba | Negativo | Medición |
|---|---|---|
| IAM | Tenant sin credencial, token vencido | 401/403 y cero tool calls |
| RBAC | Agente sin scope | Deny y no ejecución |
| Cross-tenant | Mezcla entre A/B | Deny |
| Policy | Falta regla/versión desconocida | Fail-closed |
| Approval | Replay o aprobador igual a agente | Deny |
| TOCTOU | Cambia valor tras aprobación | Deny |
| DLP | Identificador regional, chunking, formato no previsto | Captura real pre-egress |
| Tool calls | Ruta alternativa de ejecución | No bypass |
| Idempotencia | Doble request de mismo operation_id | Un efecto o ninguno, DB test |
| Recovery | Timeout/caída tras llamada | UNKNOWN/HOLD, no «success» fingido |
| Reconciliación | Resultado provider contradice request | Mismatch |
| Observabilidad | Prompt sensible en logs | 0 sentinels en prueba definida |
| TCO | Dos instalaciones por herramienta | Horas + nube + soporte |
| Latencia | 1/10/50 concurrencia | p50/p95/p99 en mismo equipo |
| Despliegue | Reinicio/rollback | Recuperación y reporte de gaps |

**Un caso no implementado se marca N/A/FAIL con explicación**, no se puntúa como 100 % correcto. Comparar versiones y configuraciones equivalentes; si un competidor requiere add-on con costo, incluirlo en el TCO.

## Formato de comparación por herramienta

```text
Nombre / URL:
Commit o versión:
Fecha:
Licencia / edición:
Entorno hardware:
Quién ejecutó:
Casos permitidos y fallados:
Casos no ejecutados:
Errores de integración:
Tiempo desde instalación a primera política:
Costo/mes comparable:
Hallazgos de seguridad y límites:
Conclusión seguir/no-fit/pivot:
```

## Buyer experiment

Al comprador mostrar dos diagramas: stack actual y propuesta DELIA. Preguntar por preferencias de integración, riesgos, costos y mantenimiento. No mostrar SOLO «nuestra» demo; explicar dónde la alternativa es superior. Si con OPA/Temporal se resuelve por un costo menor y sin fricción, **recomendar esa opción y reorientar DELIA a un pack compatible**.

## Métrica unificadora

**Cost per independently verified business outcome** = costo total atribuible / número de operaciones contrastadas con sistema autoritativo. Si no hay evidencia autoritativa, denominador no medido; no sustituir por llamadas del LLM.

## Sources

Investigación global previa: `docs/estrategia/investigacion-global-2026-11-09.md`.
Estudios mercado y enlaces oficiales: `14-fuentes-y-supuestos.md`.
No copiar código o funcionalidades de licencias incompatibles sin revisión.
