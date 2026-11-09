# DELIA Sector Packs — primer catálogo ejecutable de laboratorio

Versión 09/11/2026. **Estado exclusivo LAB. No autentica a empresas, no ejecuta herramientas ni accede a datos reales.** Los packs son configuraciones JSON deterministas del motor de políticas, no nuevos productos SaaS.

## Cuatro packs implementados

| Pack | Tenant DEMO | Reglas de ejemplo | ¿Qué demuestra? |
|---|---|---|---|
| DELIA for Commerce | demo_commerce | pedidos.read ALLOW, refund.issue bajo umbral ALLOW y alto umbral APPROVAL, orders.delete DENY | Un umbral explícito puede transformar una intención en aprobación pendiente |
| DELIA for Contact Centers | demo_contact_center | cases.read ALLOW, customer.update APPROVAL, contact.export DENY | Una política de agente puede diferenciar lectura, cambio y exportación |
| DELIA for Integrators | demo_integrators | crm.read ALLOW, crm.write APPROVAL, secrets.export DENY | Una configuración por cliente ilustra separación lógica y roles |
| DELIA for SaaS B2B | demo_saas_b2b | records.read ALLOW, records.write APPROVAL, keys.export DENY | Una API de negocio puede declarar permisos por herramienta |

Los nombres de tools son puramente ficticios. Los tenants y roles son cadenas pasadas por el código y por tanto **no representan autenticación o aislamiento de producción**. Se rechazan packs desconocidos y campos extraños en las reglas; el default es siempre DENY. Las aprobaciones en laboratorio son en memoria y no ejecutan acciones.

## Comandos reproducibles
~~~bash
python -m unittest discover -s tests -p 'test_trust_fabric*.py' -v
python -m trust_fabric.packs_demo
~~~

La CI ejecuta ambos con Python 3.11 y 3.13. El JSON de salida informa decisión y verificación de recibo HMAC, no resultado real de herramientas.

## Evolución hacia paquetes vendibles (no implementada)
1. Confirmar un comprador y el costo de su problema.
2. Integrar identidad verificable, scopes y tenant derivado de credencial.
3. Construir adaptador con ejecución bloqueada sin bypass y prueba E2E.
4. Documentar política de datos, retención, consentimiento y permisos.
5. Implementar herramientas reales únicamente con autorización, entornos de prueba y contratos.
6. Medir instalación, p95, efectividad de controles y esfuerzo de soporte.
7. Versionar manifest firmado, migración, rollback y compatibilidad de API.
8. Revisar precio y margen por sector antes de anunciar disponibilidad.

## Relación comercial
Estos cuatro primeros packs corresponden a las oportunidades de la [estrategia de main](../../estrategia/verticales-y-casos-de-uso.md). El desarrollo técnico pertenece al PR #21 mientras permanezca en borrador. No publicar logotipos de prospectos ni prometer integraciones con CRM/Shopify/ERP todavía inexistentes.

## Seguridad
No se aceptan instrucciones generadas por el modelo como una política autorizada. Los manifests no contienen secretos ni datos de clientes; toda operación desconocida se deniega. El control real necesita obligar al ejecutor a consultar la política mediante un enforcement server-side; este paquete **todavía no lo implementa**.
