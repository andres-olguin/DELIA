# DELIA Outcome Contracts — Laboratorio local

**Estado: SIMULACIÓN.** No usar datos personales, cobros, pagos, facturas reales ni conectar sistemas productivos. El módulo no incluye autorización real, políticas, IAM, controles de concurrencia, persistencia, proveedores, auditoría duradera ni capacidad de detención de acciones externas.

## Propósito

Mostrar que un flujo de negocio debe separar:

1. **Preflight / invariant checks**: qué exige el contrato de proceso.
2. **Autorización externa**: quién está autorizado a operar (no implementada).
3. **Ejecución**: efecto real idempotente en sistema de registro (no implementada).
4. **Reconciliación**: lectura independiente de resultado real (solo objetos sintéticos).
5. **Evidencia**: resumen minimizado y durable (no implementada).

Si pasa la primera verificación se obtiene `ELIGIBLE_FOR_AUTHORIZATION`, **nunca ALLOW**. El caso `VERIFIED_SIMULATED` únicamente comprueba coherencia entre estructuras locales proporcionadas por el mismo programa, no un resultado bancario/ERP verificado.

## Ejecutar

```bash
python -m unittest tests.test_outcome_contracts -v
python -m experiments.contract_assurance.demo
```

Python 3.11+ sin dependencias externas. CI para Python 3.11 y 3.13. El archivo `contracts/commerce_refund_mx_v1.json` muestra un manifiesto mínimo de reembolso **ficticio** en MXN. La unidad `amount_minor` corresponde a unidades menores representadas por entero, no una regla de cambio de divisas.

## Invariantes de negocio cubiertos

Moneda, tenant lógico, pedido, versión de snapshot, importe máximo contractual, saldo de devolución, estado pagado, bandera declarada de cliente verificado y operación repetida. El laboratorio **no valida** la bandera de cliente contra un proveedor de identidad ni guarda los IDs de forma duradera. La aceptación de precondiciones puede quedar obsoleta antes de una operación real; el control contra TOCTOU requiere transacción o precondición atómica del sistema autoritativo.

## Resultados sintéticos

`VERIFIED_SIMULATED`: el reporte local coincide; **no prueba que dinero cambió de manos**.
`HOLD`: resultado desconocido o pendiente; no se puede marcar terminado ni reintentar sin comprobación.
`REJECTED`: el reporte local indica rechazo.
`MISMATCH`: tenant, operation ID, fingerprint o importe diferentes.

## Próxima versión

Separar identidad y política, autenticar el sistema fuente, implementar idempotencia duradera, workflow recovery y revisión independiente. Antes de conectores reales comparar con **Helio**, **AgentTrustOps**, **Temporal** y **Agentgateway**; preferir una integración cuando ahorre riesgos/horas.

## Relación con DELIA

Este experimento en `main` no modifica `backend/`, `services/`, `app/`, ni el PR #21. La documentación de estrategia se encuentra en `docs/estrategia/delia-outcome-assurance.md`. El interés comercial debe validarse mediante entrevistas, no por el resultado de los tests.
