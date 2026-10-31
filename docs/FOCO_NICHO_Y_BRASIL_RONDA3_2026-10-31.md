# DELIA — Decisión de foco de validación y Brasil fase dos

**Corte 31-10-2026.** Análisis de hipótesis, no TAM observado ni decisión de clientes.

## Recomendación única: integradores B2B de agentes y aplicaciones LLM

**Valor en una frase:** «Ayudamos a los integradores que construyen agentes de IA para empresas a evaluar, con pruebas reproducibles, qué identificadores latinoamericanos podrían salir en sus llamadas a modelos y qué controles faltan frente a su solución actual». **Hoy es proyecto en desarrollo y benchmark**, no servicio de protección listo para producción.

| Nicho | Tamaño verificable del segmento comprador | Dolor hipotético | Alternativas | Esfuerzo DELIA | Dictamen |
|---|---|---|---|---|---|
| **Integradores de agentes (elegido)** | No verificado como número de integradores con 2+ clientes LLM. [25 firmas investigables](ALIANZAS_CANAL_25_RONDA2_2026-10-31.csv) no son TAM | Configurar repetidamente PII, permisos, logging y costos por cliente | LiteLLM, Presidio, Cloudflare, AWS/Google, herramientas propias | P0 + corpus, después SDK o plugin multicliente | **Probar primero**, por acceso a interlocutores técnicos y posibilidad de comparar trabajo repetido |
| **Fintech / SaaS financiero** | No hay conteo de entidades con llamadas LLM a datos confidenciales; **NV** | Reducción de exposición, gobierno de conectores financieros y auditoría | Purview, Bedrock, Model Armor, plataformas internas | Alto: seguridad, auditoría, identidades, DPA, SLA, sector financiero | Mantener investigación, no vender aún |
| **Cumplimiento de datos personales** | No hay denominador de organizaciones compradoras de un gateway y tampoco obligación de comprar DELIA | Procesos documentados, minimización, derechos, transferencia | DLP corporativos, asesorías jurídicas y controles internos | Muy alto: responsabilidad, regulación y reportes por país; no reemplaza bases legales | Descartar claims de compliance total |

## Evidencia comercial favorable y contraria

- **Buk** informa que ya utiliza APIs OpenAI/Gemini y cuenta con enmascaramiento, Langfuse y separación entre clientes; [fuente corporativa de septiembre 2026](https://supportcenter.buk.cl/hc/es-419/articles/53619330726043-Buk-AI-Seguridad-Privacidad-y-Tratamiento-de-Datos). **Objeción fuerte para DELIA**: la necesidad podría estar satisfecha.
- **Siigo** documenta MCP conectado a Claude y ChatGPT para facturas y clientes ([documentación](https://developers.siigo.com/docs/siigoapi/MCP/1-documentation/)). No se sabe si necesita controles adicionales.
- **Belvo** publicó su conector oficial de Claude en octubre de 2026 ([artículo técnico](https://belvo.com/es/blog/claude-belvo-conector-oficial/)); es ejemplo de diseño con permisos, no comprador DELIA.
- **Presidio** es extensible sin costo de licencia OSS ([documentación](https://microsoft.github.io/presidio/supported_entities/)). Por ello, «soporta RUT» no es diferenciador defendible por sí solo.

**Umbral propuesto HP:** realizar 12 entrevistas de integradores dentro de una meta total de 24, obtener al menos 4 relatos cuantificados de trabajo repetido y 2 equipos dispuestos a facilitar un benchmark de solo datos sintéticos, siempre sin compromiso de compra ficticio.

## Brasil — mercado de segunda fase, no equipo activo

**Marco:** Ley General de Protección de Datos Personales **13.709/2018 (LGPD)**, con [ANPD](https://www.gov.br/anpd/pt-br) y [Resolución CD/ANPD 19 de 23 agosto 2024](https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024) sobre transferencias internacionales y cláusulas contractuales. Esta normativa **no exige comprar DELIA**.

**Cambios necesarios para investigar:** (a) texto y soporte portugués brasileño; (b) validación contextual de CPF/CNPJ y teléfonos BR con corpus sintético; (c) modelado de roles controlador/operador, transferencias y transparencia con asesoría local; (d) precios/soporte BRL, fiscalidad y pasarela de cobro; (e) pruebas contra controles que ofrecen nativamente proveedores globales; (f) interlocutores e integradores brasileños corroborados. Ninguna de esas capacidades está validada en `main`.

**Decisión:** Brasil se mantiene **fase dos condicional**: no abrir prospección pagada ni prometer soporte portugués o ley LGPD antes de 2 pilotos medidos del nicho principal y al menos una investigación de precio/ingeniería en Brasil. El tamaño monetario del mercado específico es **NV**.

## Métricas que refutarían la tesis

- Entrevistados usan Presidio/Cloudflare/LiteLLM sin problemas pendientes medibles.
- Incapacidad técnica de DELIA para obtener recall sin falsos positivos destructivos.
- Costos de integración y soporte superiores a implementar un recognizer sencillo.
- Compradores rechazan añadir middleware o carecen de presupuesto.
- El producto se vuelve «servicio de desarrollo a medida», pero no SaaS escalable.

**Próximo paso:** entrevistas, benchmark comparativo y un caso pagado realmente cobrado antes de declarar validación.
