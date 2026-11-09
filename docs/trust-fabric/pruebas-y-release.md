# Estrategia de pruebas y puerta de entrega

## Criterio de evidencia
Para cada cambio guardar: commit SHA, dataset hash, versión Python, dependencia, comando exacto, resultado (pass/fail), limitaciones y revisor. «Prueba escrita» no equivale a «prueba ejecutada».

## Lo que ya se ejecuta
```bash
python -m unittest discover -s tests -p test_trust_fabric.py -v
python -m trust_fabric.demo
```
En el branch Trust Fabric estas pruebas cubren allow/deny, precedencia, expiración, un solo uso, vinculación de argumentos, rechazo cross-tenant en aprobación **lógica**, validación de entradas, política versionada y HMAC. Los roles siguen declarados por el llamante: no probar contra servidor real.

## Suite futura por capa
1. Policy: fuzz/property testing de configuraciones inválidas, conflictos, cambios de policy, modelos desconocidos y límites de importe.
2. Identidad: JWT inválido, issuer distinto, scopes caducados, tenant interpolado, key rotation, rol malicioso.
3. Agent: tool denied no se ejecuta, reintento/idempotencia, carrera de aprobaciones, cambios de argumentos y ejecución transaccional.
4. DLP: corpus independiente CL/MX/CO/BO con ground truth revisado por otra persona, casos negativos difíciles, unicode, JSON, archivos y streaming.
5. Egress: mock que captura todas las solicitudes, redacción obligatoria, stream partial chunk, proveedores caídos, redirect, SSRF y no secrets.
6. Auditoría: ausencia de PII raw, retención, hashing, verificación tampering, pérdida de DB, timezone, backup/restore.
7. E2E: onboarding tenant, política versionada, agente intenta reembolso, approval, adapter ejecuta una sola vez, auditoría sin datos reales.
8. Performance: 1/10/50 concurrencia, p50/p95/p99, CPU/memoria, costo por 1K requests y límites de recursos.
9. Secure SDLC: Dependabot/auditoría de dependencias, SBOM, secret scans, static analysis, licencias, revisión de PR por pares.
10. Usabilidad: lector de pantalla, móvil, tiempos de respuesta, claridad de copy, recuperación de errores y demo guiada.

## Hitos Go / No-Go
- **S0 listo:** simulador determinista y CI local; no autoriza público productivo.
- **S1 listo:** autenticación efectiva, aislamiento, autorizaciones, DLP egreso con mocks y CI por PR; sin pilotos sensibles.
- **S2 beta avanzada:** dashboard funcional, persistencia, métricas, runbooks y dos integraciones de prueba; corpus independiente; revisiones externas cuando sea viable.
- **S3 productivo:** revisión de seguridad y legal, SLA operativo, gestión de incidentes, infraestructura endurecida y acuerdo formal de cliente.

## Métricas y cómo reportarlas
- `TP` hallazgo exacto de tipo y tramo; `FP` hallazgo no anotado; `FN` omisión.
- `Precision = TP/(TP+FP)`, `Recall = TP/(TP+FN)`, `F1=2TP/(2TP+FP+FN)` cuando definido.
- Reportar por país y entidad, separando dataset entrenamiento/desarrollo, independiente y adversarial.
- Nunca mezclar el benchmark histórico 172 con el 96 MX/BO ni construir «100 % de seguridad» a partir de uno.
- Latencia del proxy = delta respecto a bypass comparable, no tiempo total de respuesta de proveedor.
- ROI y ahorro solo si medidos con clientes bajo acuerdo.

## Revisión de lanzamiento 15-01-2027
Acta: versión, módulos funcionando, módulos bloqueados, incidentes, riesgos asumidos, reviewer técnico, responsable comercial, asesoría jurídica consultada, contrato piloto, presupuesto y decisión Go/No-Go. Un resultado No-Go no es fracaso: protege la continuidad de DELIA.
