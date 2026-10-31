# DELIA para integradores de agentes de IA — ficha de descubrimiento

**MasterTech SpA — 31/10/2026.** Investigación y prototipo, no producto de seguridad aprobado para producción.

## Pregunta de negocio
Cuando una consultora desarrolla agentes para distintos clientes, ¿cuántas veces vuelve a configurar filtros de identificadores, controles de acceso y trazabilidad, y qué tan bien compara su solución con alternativas que ya paga o puede autoalojar?

## Propuesta de valor por validar
**DELIA busca reducir el trabajo repetido de comprobar y controlar qué información personal latinoamericana sale a proveedores de modelos de IA**, usando pruebas reproducibles por país y una futura capa de políticas por aplicación.

### Qué podemos mostrar hoy
- Detector parcial de RUT y NIT/cédula colombianos, correos, tarjetas y teléfonos, sin integración funcional con el proxy de producción.
- Corpus sintético etiquetado disponible para ejecutar un benchmark honesto.
- Resultados locales del detector actual con **recall total 47,33 % en 150 entidades sintéticas**, insuficiente para garantizar protección; [metodología](../../benchmarks/README.md).
- Comparaciones contra Presidio, Cloudflare y Google **pendientes**, por lo que no sostenemos ventaja competitiva.

### Qué no ofrecemos hoy
- Garantía de que PII no llegará al proveedor, protección multitenant, certificación, auditoría productiva, SLA, ni cumplimiento automático.
- Soporte CURP/RFC México y CI/NIT Bolivia verificado.
- Precios comerciales aprobados, casos de clientes DELIA o ahorro demostrado.

## ¿Qué buscamos de un integrador?
Entrevista técnica de 20–30 minutos. Conocer un flujo genérico sin prompts reales, alternativa que usa y costo de repetir controles. Si resulta relevante, benchmark en laboratorio y, **solo tras cerrar P0**, eventual piloto de alcance limitado y términos escritos.

**Pregunta inicial:** «Si ya usas LiteLLM, Presidio o las políticas de Cloudflare, ¿qué tarea concreta de privacidad tienes que repetir de un cliente a otro y cuánto cuesta?».

**Contacto:** [mastertechg.com](https://mastertechg.com) · contacto@mastertechg.com. No envíes contraseñas, datos de clientes ni prompts reales.

**Fuentes competitivas:** [LiteLLM](https://www.litellm.ai/pricing), [Presidio](https://microsoft.github.io/presidio/supported_entities/), [Cloudflare AI Gateway](https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/). Estado de compra: **no verificado**.
