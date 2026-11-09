# Registro de decisiones de arquitectura — ADR

## ADR-001 (propuesto) — Plataforma en lugar de gateway exclusivamente PII
Motivo: la inspección de texto es commodity. Decisión: desarrollar Trust Fabric con un plano de políticas y controles de herramientas, manteniendo la especialización regional como módulo. Tradeoff: superficie de seguridad mayor; adopción incremental. Estado: PROPUESTA, requiere validación con compradores.

## ADR-002 (aceptada para laboratorio) — Negación por defecto
El prototipo `trust_fabric/policy.py` no permite acciones sin política, regla y rol coincidentes; ante conflicto prevalece DENY. Restricción: un adaptador real debe hacer enforcement; nunca confiar en el cliente.

## ADR-003 (aceptada para laboratorio) — Aprobaciones ligadas a argumentos
Se usan fingerprints y tickets en memoria de un solo uso, con TTL y aprobador separado en la simulación. Producción requiere identidad criptográfica, transacciones atómicas y almacenamiento de duración finita.

## ADR-004 (aceptada para laboratorio) — Evidencia mínima
El recibo HMAC registra hash del actor y argumentos, no sus valores. Producción requiere KMS/clave por ambiente, cadena/almacén durable, firma verificable y retención.

## ADR-005 (propuesto) — Monolito modular, no veinte microservicios
Hasta disponer de carga real, separar módulos por contrato y gates, no por palabra de marketing. Preferir adapters existentes bajo licencias evaluadas.

## ADR-006 (propuesto) — Beta avanzada al 15 de enero
Plazo ambicioso condicionado a capacidad y seguridad. Si los P0 no cierran, demo sintética y no piloto con información sensible. Garantías y lanzamientos comerciales solo con pruebas y contratos.

## ADR-007 (propuesto) — Ventas a integradores B2B2B
Hipótesis de distribución rentable; se probará con entrevistas reales, piloto consentido y unit economics. Sin inferir clientes interesados desde directorios.
