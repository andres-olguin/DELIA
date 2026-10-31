# DELIA — Guion de demo de 10 minutos con datos sintéticos

**Fecha:** 31/10/2026 · **Permitido:** presentación de patrones y pruebas **solo localmente y con datos de prueba inventados**. No usar datos de personas reales, ni integrar este demo con cuentas productivas o proveedores externos sin aprobación.

## Preparación obligatoria

- Usar un clon local aislado, entorno controlado y salida a internet deshabilitada cuando se prueban reglas.
- Ejecutar la suite y dejar evidencia real; **hasta realizarla, el estado de resultados es NO VERIFICADO**.
- El API FastAPI presenta imports/esquemas incompatibles, y el proxy no invoca `redact`. **No mostrar el sistema completo como funcionando.**
- Las reglas de `backend/dlp/pii.py` pueden ser probadas por Python local si la instalación se verifica; documentar los resultados, errores y dependencias reales.

## Minuto 0–1 — problema
«Esta es una **demostración técnica de hipótesis, no un producto comercial listo**. Estamos intentando reducir datos innecesarios que se envían a proveedores LLM». Mostrar una secuencia descriptiva de solicitud.

## Minuto 1–3 — casos sintéticos CL/CO presentes en código
Demostrar en ambiente local cómo patrones **podrían** detectar `12.345.678-5` (ejemplo numérico de test RUT), `800.197.268-4` (ejemplo NIT de test), `C.C. 52.123.456` (ejemplo sintético), `ejemplo@empresa.invalid`, `+56 9 8765 4321`. Registrar salida verdadera de ejecución; no inventar que el test pasa si no se ejecutó.

## Minuto 3–4 — falsos positivos y negativos
- RUT `12.345.678-9` debe ser rechazado por dígito verificador (según test escrito).
- En texto «pedido 52123456» la cédula sin contexto no debe detectarse.
- Número en formato raro, fragmentos OCR, entidades en inglés/portugués, variantes sin guiones: rendimiento **no validado**.

## Minuto 4–5 — México y Bolivia (FUTURO)
Mostrar solo ejemplos de **especificación de pruebas**, no de resultado:
- México: RFC de prueba enmascarado `XXXX000000XXX` y CURP ilustrativa `XXXX000000XXXXXXXX` (marcadores, **no validadores reales**).
- Bolivia: «CI: 0000000-X» y «NIT: 0000000000» como strings ilustrativas sin validación boliviana.
**No implementados en `pii.py`**. No pretender cobertura ni precisión.

## Minuto 5–7 — integración y sus límites
Describir (pizarra) `app → detección → decisión → gateway → proveedor`, señalando que **el paso de detección a reenvío HTTPX todavía no está conectado**. La autenticación, los logs y los secretos presentan riesgos P0; no conectar a un proveedor real.

## Minuto 7–9 — benchmark que necesitamos hacer
Explicar precision (TP/(TP+FP)), recall (TP/(TP+FN)), tasa de falsos positivos, p50/p95 latencia, protección de outputs y fallos del intermediario. Comparación con Presidio/Cloudflare/Model Armor aún no ejecutada. Solicitar solo comentarios de casuística y requerimientos técnicos, **sin compartir prompts reales**.

## Minuto 9–10 — decisión
«¿Existe un problema real para probar esto? ¿Qué control tiene hoy y qué métricas exigiría?». Ofrecer entrevista técnica, no instalar en producción.

### Matriz de casos a ejecutar, no resultados

| País | Cadena sintética / de prueba | Intención de prueba | Estado del código |
|---|---|---|---|
| Chile | `12.345.678-5` | RUT válido ejemplo; redactar | Regla escrita, ejecución de auditoría NV |
| Chile | `12.345.678-9` | Dígito incorrecto, no tratar como RUT | Regla escrita |
| Chile | `+56 9 8765 4321` | Teléfono | Regla escrita |
| Colombia | `800.197.268-4` | NIT validación | Regla escrita |
| Colombia | `C.C. 52.123.456` | Cédula con contexto | Regla escrita |
| Colombia | `pedido 52123456` | Negativo contextual | Regla escrita |
| México | `CURP: XXXX000000XXXXXXXX` | Detector a diseñar | NO implementado |
| México | `RFC: XXXX000000XXX` | Detector a diseñar | NO implementado |
| Bolivia | `CI: 0000000-X` | Detector a diseñar | NO implementado |
| Bolivia | `NIT: 0000000000` | Detector a diseñar | NO implementado |

**Importante:** una cadena numérica inventada podría coincidir con un identificador real por azar. No se utilizará en mensajes externos ni pruebas productivas; el demo es local, sintético y de laboratorio. Las cadenas con sufijo `.invalid` evitan direcciones de correo activas.

## Evidencia exigida antes de mostrar «funciona»
Guardar versión del commit, entorno, comandos, outputs, tasa de errores y limitaciones. No guardar datos de terceros en repositorio público.
