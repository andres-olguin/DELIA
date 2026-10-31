# DELIA — Comparadores administrados: protocolo de ejecución y hoja de resultados
**Corte:** 2026-10-31. **Estado:** Cloudflare DLP y Google Model Armor **NO EJECUTADOS**. Referencia de corpus: [synthetic_pii_r3.jsonl](../../benchmarks/synthetic_pii_r3.jsonl). Usar datos sintéticos exclusivamente.

## Cloudflare AI Gateway DLP (cuenta gratuita)
**Hecho, fuente oficial (2026-10-15):** [Pricing](https://developers.cloudflare.com/ai-gateway/reference/pricing/) afirma que DLP scanning de AI Gateway es gratis en todos los planes; sin suscripción Zero Trust se limitan a perfiles **Financial Information** y **Social / Insurance / National Identifier Numbers**. No asumir que reconocen RUT/CURP/NIT localmente. El uso de proveedores upstream y logs puede implicar otros cobros y riesgos.

1. Crear una cuenta gratuita Cloudflare sin enviar PII real.
2. Entrar en **AI → AI Gateway** y crear un gateway de prueba.
3. Abrir **Firewall → Data Loss Prevention → On**; **Add Policy**.
4. Elegir los dos perfiles disponibles, con acción **Block** y **Check Request**. Crear otra política **Flag** para contar detecciones sin bloquear cuando se evalúe capacidad. Documentar qué perfiles permite realmente la cuenta.
5. Conectar un proveedor o mecanismo de prueba autorizado. Desactivar/limitar logs de contenido según controles de la cuenta, fijar límites y presupuesto de consumo. **No colocar credenciales en GitHub**.
6. Inyectar por un cliente controlado los 172 textos sintéticos identificados por `id`. Registrar para cada ID si existe match de DLP, si es en solicitud/respuesta, si hubo bloqueo y categoría reportada. Sin respuesta estructurada que identifique *spans*, **no calcular F1 por spans**: medir detección binaria por caso aparte, NO compararla con el F1 de DELIA.
7. Exportar resultados sin secretos ni prompts completos y conservar fecha, perfil/plan, configuración, ubicación/endpoint y costo real.

**Procedimiento oficial (2026-09-25):** [Set up DLP](https://developers.cloudflare.com/ai-gateway/features/dlp/set-up-dlp/).

## Google Cloud Model Armor (nivel gratuito documentado)
**Hecho, fuente corporativa consultada 2026-10-31:** [Google Model Armor](https://cloud.google.com/security/products/model-armor) muestra **2 millones de tokens/mes gratuitos** para Model Armor y US$0,10/millón adicional bajo la modalidad documentada. No afirma que toda cuenta tenga sin condiciones acceso de facturación/API ni que detecte todos los tipos regionales.

1. Crear o seleccionar proyecto Google Cloud autorizado; comprobar elegibilidad, términos, región, cuota y si exige cuenta de facturación. Fijar alertas y límites.
2. Habilitar Model Armor API siguiendo la [documentación oficial](https://cloud.google.com/security/products/model-armor). Crear template con detección de datos sensibles y política de respuesta documentada.
3. Usar credenciales de mínimo privilegio almacenadas fuera del repositorio. No subir ID secretos ni token.
4. Enviar sólo las entradas sintéticas y guardar por `id` etiquetas/tipos, *spans* cuando realmente los devuelva la API, y costos/tokens. Registrar controles bloqueados o categorías no soportadas.
5. Si la API retorna un indicador de PII sin ubicaciones, elaborar **métrica por caso**, separada de match tipo+span; no convertir indicadores generales a TP/FN por entidad.
6. Desactivar recursos de prueba y revisar facturación; documentar `NO EJECUTADO` si no se habilita proyecto o permisos.

## Microsoft Presidio: comparación pendiente
Instalación oficial: https://microsoft.github.io/presidio/installation/ . Capturar versiones (`python -V`, `pip show presidio-analyzer spacy` y `python -m spacy validate`), idiomas/modelos instalados, recognizers activos, thresholds y mapeo de categorías. El dataset está mayormente en español; no usar un modelo inglés para afirmar cobertura equivalente. Crear mapeo explícito de entidades (RUT, NIT, CEDULA, CURP, RFC, CI/NIT BO) con categorías **NO SOPORTADA** si no hay reconocedor nativo; registrar la mejora por reconocedores personalizados como experimento separado.

## Plantilla por registro
`id_caso,fecha_utc,motor,version,plan,region,config_sha,perfil_o_template,tipo_esperado,spans_esperados,tipo_detectado,spans_detectados,resultado_bloqueo,latencia_ms,tokens,costo_usd,fuente_registro,estado,observacion`

Usar estado `EJECUTADO`, `NO EJECUTADO` o `INCOMPARABLE SIN SPANS`. Ningún valor de TP, FP, FN, precision, recall o F1 se inventa. Un evaluador independiente debe comprobar etiquetas y errores del corpus antes de adoptar conclusiones.

## Interpretación comercial obligatoria
DELIA previamente registró recall **47,33 %** (79 FN de 150 positivos). Por ello, no se debe presentar como alternativa de seguridad equivalente ni ganar en detección regional sin repetir los ensayos. Hipótesis de mejora: CURP/RFC México, CI/NIT Bolivia, direcciones, negativos difíciles y integración efectiva del egress. Pruebas productivas, seguridad multitenant, precio y soporte: **NO VERIFICADOS**.

## Runner Presidio preparado fuera de main (NO EJECUTADO)
Se preparó `DELIA_evaluate_presidio_r4.py` y su patch `DELIA_presidio_runner_r4_NO_EJECUTADO.patch` como archivos de entrega local. **No se subió código al repositorio**, por el [bloqueo OPS-01](https://github.com/andres-olguin/DELIA/issues/18). El script pasó `python -m py_compile` y el .patch pasó `git apply --check` en snapshot local; **no se ejecutó Presidio** ni hay resultados.

Tras corrección del ruleset y creación de rama nueva, en entorno de laboratorio sin datos reales:
```bash
git apply --check DELIA_presidio_runner_r4_NO_EJECUTADO.patch
git apply DELIA_presidio_runner_r4_NO_EJECUTADO.patch
python -m venv .venv
# activar .venv según sistema
python -m pip install presidio-analyzer spacy
python -m spacy download es_core_news_sm
python -m pip freeze > benchmarks/presidio_r4_pip_freeze.txt
python benchmarks/evaluate_presidio_r4.py --dataset benchmarks/synthetic_pii_r3.jsonl --output benchmarks/presidio_r4_resultados.json
```
**NO EJECUTADOS** los comandos anteriores; precios, versiones efectivas y métricas no están fijados todavía. El runner registra versiones de Presidio/spaCy, modelo ES, etiquetas exactas de tipo+span y las métricas por país/entidad. Reconocedores locales personalizados **no incluidos**, para no convertir una comparación del baseline nativo en versión ajustada sin atribuirlo.
