# ¿Qué información personal puede escapar en una solicitud a un modelo de IA?

**Artículo técnico para revisión editorial, 31 de octubre de 2026.** Autor institucional propuesto: MasterTech SpA. Se usa información sintética. No contiene incidentes reales de clientes ni resultados de protección productiva.

## El problema no es que exista un prompt: es quién recibe sus datos

Un asistente empresarial puede responder preguntas sobre facturación, recursos humanos y atención al cliente. En cada caso, la aplicación suele reunir contexto: órdenes, mensajes, notas, resultados de herramientas y, potencialmente, identificadores personales. El equipo de ingeniería debe definir por qué cada campo es necesario para la inferencia, qué proveedor externo recibe el texto, si existe transferencia internacional y quién puede inspeccionar la traza.

No hay que asumir que todo proveedor LLM use automáticamente los datos para entrenamiento. El tratamiento depende del contrato, el producto, el plan y las opciones de retención de cada proveedor; se deben revisar políticas vigentes y acuerdos firmados. Por ejemplo, [Buk informó en septiembre de 2026](https://supportcenter.buk.cl/hc/es-419/articles/53619330726043-Buk-AI-Seguridad-Privacidad-y-Tratamiento-de-Datos) que utiliza APIs empresariales de OpenAI/Gemini y que aplica minimización y controles de registro.

## Cinco puntos donde se puede escapar contenido

1. **Construcción del contexto:** el agente agrega una ficha completa cuando solo necesitaba una categoría de producto.
2. **Resultados de herramientas:** consultas a ERP o CRM incorporan correos, facturas, RUT/NIT o identificadores de terceros. [Siigo](https://developers.siigo.com/docs/siigoapi/MCP/1-documentation/) documenta un conector MCP con acciones sobre datos contables, ejemplo del tipo de flujo que requiere revisión.
3. **Observabilidad:** guardar íntegros prompts/respuestas en logs añade una superficie de exposición. La observabilidad útil no exige retener siempre los textos completos.
4. **Errores y reintentos:** fallbacks pueden reenviar contexto a proveedores secundarios; sin una política por destino es difícil auditar qué salió.
5. **Entradas no textuales:** documentos OCR, imágenes y metadatos pueden escapar a un filtro regex que solo revisa texto UTF-8.

## Qué es —y qué no es— una protección DLP

Una capa DLP puede detectar y enmascarar categorías conocidas, bloquear solicitudes o registrar decisiones. Sin embargo, **ningún patrón asegura 100 % de detección**: hay errores de formato, entidades sin validación, nombres propios, información contextual y falsos positivos.

**Ejemplo completamente ficticio:**

Entrada: `Cliente de prueba: RUT 12.345.678-5; escríbele a persona@empresa.invalid`.

Salida deseada para una política que permite ambos tipos: `Cliente de prueba: RUT [[RUT]]; escríbele a [[EMAIL]]`.

Esta es una *ilustración*, no prueba de que un gateway completo de DELIA lo garantice. El detector `backend/dlp/pii.py` existe pero no está integrado en el reenvío real del proxy `services/proxy.py`.

## Cinco salvaguardas complementarias

- Minimizar datos **antes** de construir contexto, no solo después.
- Enmascarar o bloquear por **tipo de entidad y finalidad**; probar formatos difíciles y contextuales.
- Autorización por usuario/tenant, claves de servicio gestionadas, separación entre aplicaciones.
- Logs de metadatos mínimos sin secretos ni texto completo por defecto; retención controlada.
- Pruebas de integración que verifiquen realmente lo enviado al upstream, no solo el resultado de una función aislada.

Como referencias de controles y amenazas, pueden consultarse la documentación oficial de [Cloudflare AI Gateway DLP](https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/), [Presidio](https://microsoft.github.io/presidio/supported_entities/), [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications/) y [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).

## ¿Qué revela DELIA como caso de estudio?

En una evaluación local de **172 textos sintéticos y 150 entidades**, el detector de DELIA acertó exactamente 71, produjo 3 falsos positivos y omitió 79: recall **47,33 %**, un resultado insuficiente para garantizar que no escape PII. [Método y límites](../../benchmarks/README.md). El componente tampoco se ejecuta automáticamente antes de llamar al proveedor LLM. **Estas deficiencias deben contarse, no esconderse.**

## Conclusión

Una política útil no se anuncia mediante «detectamos datos», sino que demuestra **qué categorías cubre, cuántas pierde, cómo reacciona al error y quién puede comprobar la salida real**. Para una organización que ya paga Cloudflare, Azure o Bedrock, la opción más segura podría ser completar la configuración existente en lugar de instalar un proxy adicional.

*Fuentes consultadas y edición: 31-10-2026. Proyecto DELIA: investigación, no sistema comercial certificado.*
