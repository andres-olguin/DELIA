# DELIA — Secuencia ejecutable hasta la decisión de enero de 2027

**Inicio:** 09/11/2026. **Meta:** 15/01/2027. Los hitos son objetivos de ejecución **condicionados a disponibilidad real, contratos y puertas de seguridad**, no compromisos a clientes.

## Arquitectura mínima objetivo (no implementada completamente)

```text
Comprador / integrador (identidad comprobada, tenant real)
  -> DELIA Policy Front Door (fail closed, authn/authz por tool/actor)
  -> DLP & data policy before ANY egress
  -> Approval broker (actor humano, args exactos, expiración, idempotencia)
  -> Execution adapter con credenciales del servidor y allowlist
  -> CRM sandbox no productivo
  -> Outcome reconciler (lee fuente de verdad, no solo la respuesta del agente)
  -> Evidencia minimizada por organización y revisión humana
```

**Prohibición arquitectónica:** el agente no controla claves, políticas, logs, revocaciones ni tiene una ruta alternativa hacia el proveedor/herramienta. No se concede producción a partir de mocks.

## Semanas y criterios de salida

| Periodo | Hito principal | Entregable y prueba de no regresión | Si falla |
|---|---|---|---|
| **9–15 nov** | Reparar base reproducible | Imports, modelos, schemas y migraciones alineados. Test import/DB de CI sin credenciales reales | Corregir arranque, no añadir features |
| **16–22 nov** | Cerrar auth y privacidad en la ruta | Un identity test válido, un tenant ajeno denegado, canary sintético bloqueado antes de upstream | Deshabilitar egress en demo |
| **23–29 nov** | Eliminar rutas alternativas y secretos | Mock upstream y detector en ruta completa, logs minimizados, no claves de cliente reenviadas | Bloquear ruta vulnerable |
| **30 nov–6 dic** | Integrador E2E de herramienta ficticia | Tool fuera de permiso = cero efecto observado, pruebas adversariales de prompt/tool injection | Sin release |
| **7–13 dic** | Aprobaciones e idempotencia durables | Reutilización de aprobación y cambio de args no producen doble acción | No habilitar escrituras |
| **14–20 dic** | Resultado y recuperación | `UNKNOWN` nunca SUCCESS, sandbox source-of-truth y fallos de red/reintentos | Mostrar incertidumbre |
| **21–27 dic** | Benchmark de conformidad | Protocolo equivalente para 2 stacks reales si se consiguen integraciones y permisos | Registrar NOT_EXECUTED |
| **28 dic–3 ene** | Kit de instalación reproducible | Ejemplo Docker/configuración segura, diagnóstico y tests; sin credenciales en repos | Detener beta externa |
| **4–10 ene** | Revisión externa independiente | Otro implementador instala y corre fixtures, registra tiempos y false blocks | Mantener LAB |
| **11–15 ene** | Gate de beta avanzada | P0 firmados por responsables, informe de QA, versionado, SLA realista y decisión Go/No-Go | Posponer beta productiva |

**Gates obligatorios:** SEC-001 a SEC-008 en [readiness-controls.json](readiness-controls.json), reporte reproducible y revisión independiente. Ningún plazo, contrato potencial ni contenido mediático puede reemplazarlos.

## Paralelismo recomendado por capacidad, no por nombres

**Core/backend:** rutas, autenticación, DLP, herramientas, idempotencia, reconciliación.  
**QA/reviewer:** tests negativos, seguridad, no bypass, reproducibilidad.  
**Producto/entrega:** scripts demo, onboarding externo y costo real de implementación.  
**Comercial/editorial:** entrevistas consentidas, landing/github, contenido original y propuestas.  

Cada historia debe tener persona que **acepte el rol**, tiempo asignado, SHA, revisor y definición de completado. Cerrar PR #21 solo tras verificar cada integración, no por pasar tests unitarios de laboratorio.

## Si solo hay recursos para una semana

1. Reparar imports y base de datos local aislada.
2. Proteger auditoría y deshabilitar salida raw en una ruta de demo.
3. Ejecutar un test que pruebe que no hubo llamada al upstream cuando se deniega.
4. Preparar video propio con ese test y sus límites, no con promesas.
5. Investigar/contactar 5 integradoras con interés justificable para entrevistas.

**Criterio para invertir en nuevas capacidades:** tener al menos un workflow instrumentado, costo de implementación medido y al menos un comprador real que confirme el problema. Si no, mantener foco.

## Entregables de una beta avanzada honesta

- Entorno de prueba autoinstalable y documentación con SHA.
- Contratos y fixtures por tenant/sandbox con permisos explícitos.
- Una ruta de acciones permitidas y denegadas con evidencia externa real en sandbox.
- Política de secretos, retención, auditoría minimizada y revocación.
- Casos de abuso y límites publicados, no solo casos felices.
- Script demo de 3 minutos para prospectos técnicos y pitch de 90 segundos.
- Estimación de COGS y costo de soporte a partir de una instalación real.

No son evidencia de cumplimiento hasta que exista un informe ejecutado y revisado.
