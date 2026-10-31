# DELIA — Registro de investigación y auditoría de evidencias, Ronda 2

**Fecha de corte:** 31 de octubre de 2026 · **Proyecto:** DELIA / MasterTech SpA · **Tipo:** investigación documental con límites explícitos. No se contactó a ninguna cuenta, ni se realizó entrevista, compra, test de producto o solicitud de fondos.

## 1. Objetivo y protocolo

Ampliar a cuatro países la prospección y crear materiales de venta sin confundir:
- **HV:** contenido de fuente primaria o sitio oficial examinado, describe lo que publica su titular.
- **EP:** estimación matemática/ingeniería con método, no predicción.
- **HP:** hipótesis comercial o de producto pendiente de entrevista y benchmark.
- **NV:** dato no verificado, incluyendo presupuesto de compra, LLM real usado por una empresa, dominios no accesibles, resultado de pruebas o fecha futura no anunciada.

Rondas: (A) lectura de main/estudios, (B) investigación de nuevas cuentas y fuentes, (C) competencia/expedientes/regulación, (D) precios/pilotos y mensajes, (E) validación/producto, (F) auditoría y verificación GitHub.

## 2. Recuento reproducible de referencias

**[Catálogo CSV de fuentes, fecha, estado y solapamiento](REFERENCIAS_Y_ESTADO_VERIFICACION_RONDA2.csv).**

| Medida | Conteo de inventario | Interpretación |
|---|---:|---|
| Bibliografía del estudio previo de cuatro países | **108** URLs numeradas | Punto de partida para comparación por URL normalizada (dominio sin `www`, ruta sin / final) |
| Catálogo adicional Ronda 2, URLs distintas | **232** | Compuesto por sitios de cuentas, documentos de proveedores, resoluciones, fondos, eventos y directorios |
| URLs no presentes entre las 108 anteriores | **199** | **Fuentes/enlaces adicionales identificados y examinados con intensidad variable; NO significa 199 sitios auditados íntegramente** |
| Referencias de páginas con contenido consultado/registrado | **138** | Incluye algunas URLs también presentes en bibliografía anterior |
| Sitios empresariales individuales con contenido web contrastado | **116 de 160** | Autodescripción en web pública, no comprobación de stack privado ni de compra |
| Sitios empresariales pendientes de corroboración individual | **44 de 160** | Figura empresa/sitio vía directorio o fuente inicial, pero no se verificó el contenido corporativo directamente |
| Otras fuentes solo consultadas mediante búsqueda, referencia parcial o lectura limitada | **50** | No equivalen a fuentes primarias verificadas integralmente |

**Resultado frente al requisito «150 fuentes adicionales»:** el inventario contiene **199 URLs distintas que no estaban en las 108 referencias anteriores**, por encima del umbral de **enlaces de investigación**. Sin embargo, **no se alcanzó la verificación integral, individual y de contenido de 150 de esas 199 páginas**; la cifra no debe presentarse como «150 fuentes primarias completamente auditadas». Se necesita revisión adicional de los sitios que fallaron, metadatos, fechas, LinkedIn y prensa antes de afirmar cumplimiento más estricto. La diferencia importa: contar enlaces no es equivalente a validar evidencia.

La normalización de URLs usada solo elimina prefijo `www.` y slash final; redirecciones, duplicados semánticos y enlaces a documentos idénticos podrían requerir reconciliación manual. Las categorías de fuente son heterogéneas: resolución oficial ≠ autodescripción comercial ≠ directorio de empresas.

## 3. Qué se revisó y con qué alcance

### Repositorio DELIA

Leídos los estudios previos, README, roadmap, documentación, código que implementa `app/api/proxy.py`, `app/main.py`, `app/models.py`, `backend/dlp/pii.py`, `backend/network_utils/replay_session.py`, `services/proxy.py` y `services/audit.py`, tests escritos y los commits anteriores. **No se ejecutó** pytest, Docker, benchmark PII ni revisión dinámica de seguridad. Existe disparidad de imports, modelos, auth y redaction-before-egress. No hay certificación ni producto terminado.

### Cuentas

Se partió de 60 empresas de la Ronda 1 y se añadieron 100 candidatas desde directorios especializados, contrastando **116 sitios individuales** a nivel de contenido público; no hay tres fuentes independientes por empresa, no todas tienen LinkedIn validado y no hay contacto con comprador. [Lista 160](PROSPECTOS_RONDA2_160_CL_CO_MX_BO_2026-10-31.csv), estado `no contactada`, 40 cada país y 10 ola 1 por país.

**No se verificó:** interés DELIA, presupuesto, stack LLM privado, identidad/domicilio legal de algunas marcas, tamaño de plantilla (fuente pública desigual), política técnica vigente y persona decisora. No scrapeamos teléfonos ni correos personales.

### Competencia

Se consultaron páginas oficiales de precios y características de Cloudflare, LiteLLM, Portkey, Lakera, Nightfall, Presidio, Purview, Azure, AWS, Google Model Armor, Langfuse, Helicone, Kong, Vercel y OpenRouter. Algunos precios son públicos (consultar fecha), otros **NV/cotización**. En particular, la lectura visible de Lakera no reveló tabla monetaria completa. Los competidores pueden extender reconocedores locales; ausencia de mención de RUT/CURP no prueba incapacidad. **No hay benchmark de DELIA** contra ellos.

### Riesgos/sanciones

Diez expedientes de autoridades de protección de datos y consumidor. **No todos son IA ni LLM**: varios son tratamiento de geolocalización, contraseñas, retención o reconocimiento facial. Son indicios de costos de prácticas incorrectas, no «multas que DELIA habría evitado».

**Corrección jurídica importante:** el Garante italiano publicó sanción anunciada a OpenAI en 2024, pero su nota oficial informa que la oposición fue acogida por sentencia del Tribunal de Roma publicada el **18/03/2026**. Se corrigió el [informe](ESTUDIO_RONDA2_PROFUNDIZACION_COMERCIAL_2026-10-31.md) para no presentar la sanción como definitiva. Fuente oficial: https://gpdp.it/web/guest/home/docweb/-/docweb-display/docweb/10085432.

### Regulación

Fuentes oficiales Chile BCN/Senado/CMF, México DOF/Cámara/TEPJF, Colombia SIC/DANE/DNP y Bolivia Cámara Diputados/AGETIC/ATT. Confirmar cambios antes de la venta. **Bolivia PL538 es proyecto**, Chile prórroga Ley 21.719 no estaba publicada como reforma definitiva al corte. El middleware no sustituye obligaciones jurídicas.

### Programas/eventos

Se consultaron programas CORFO, ProChile, iNNpulsa, Ruta del Emprendimiento, programas mexicanos y bolivianos con fechas verificadas de noviembre cuando constan. Algunas actividades de 2026 ya cerraron. **No se encontró calendario confirmado de futuros eventos relevantes para cada uno de los seis meses en los cuatro países**: mejor NV que fechas ficticias.

## 4. Ángulos explorados al fallar una búsqueda

- Sitio corporativo directo `https://...` → variante con `www.` o resultado indexado/búsqueda → si persiste error, `NV`.
- Datos empresariales IA generales → censos sectoriales (INEGI/DANE) → directorios; cuando el dato no medía API LLM, **no usar como adopción de gateway**.
- «Sanciones por IA generativa» → expedientes oficiales de IA y privacidad → clasificar causalidad (biometría/seguimiento no LLM).
- Fundraising «subsidios abiertos» → sitio oficial convocatoria → bases y cierre → si no hay elegibilidad de empresa chilena o producto comercializado, marcar NV/no elegible aparente.
- Competidor sin tarifa pública → revisión sitio de precios y docs → `cotización` o `NV`, nunca US$0 por defecto.

## 5. Hallazgos y falsadores que faltan

1. **Entrevistas reales con decisores (0 realizadas)**: al menos 20 conversaciones, 6 dolores verificables, 2 potenciales pilotos negociados como hitos HP.
2. **Costos propios medidos (0)**: hosting/retención/soporte/hora/despliegue antes de anunciar tarifa DELIA.
3. **Ejecución de tests de DELIA (0)** y benchmark para RUT/NIT/CURP/RFC/CI: cualquier ventaja competitiva sigue siendo HP.
4. **Ventas de DELIA (0 verificadas)**: otros ingresos de MasterTech **no** significan adopción de este producto.
5. **Identidad de compradores (0 verificados)**: la base indica solo roles, sin datos personales.
6. **Elegibilidad fondos/partner (NV)**: MasterTech es chilena y su presencia internacional no prueba cumplimiento de bases de México, Colombia o Bolivia.
7. **TAM nacional en USD (NV)**: sin población observada de compradores de gateway independiente; el [modelo editable](ESCENARIOS_TAM_SAM_SOM_RONDA2.csv) deliberadamente mantiene vacíos los denominadores.

## 6. Control de comunicaciones

La información de prospectos es una **lista de investigación**, no un CRM de marketing consentido. Usar únicamente canales públicos corporativos y respetar solicitudes de no contacto. No enviar secuencias WhatsApp frías o automatizadas a números privados. El [CRM vacío](ventas/CRM_ENTREVISTAS.csv) está diseñado para almacenar datos sensibles únicamente en infraestructura **privada**, no en GitHub público.

**Auditoría del próximo ciclo:** visitar los 44 sitios pendientes; comprobar identidad/fuente legal y duplicidades, ampliar fuentes LinkedIn+prensa para las 40 cuentas ola 1 y registrar 20 entrevistas verificadas o sus tasas reales de no respuesta. Todo avance debe estar respaldado por evidencia fechada, no por «número de documentos publicados».

---

## 7. Entregables producidos y trazabilidad

- [Estudio Ronda 2](ESTUDIO_RONDA2_PROFUNDIZACION_COMERCIAL_2026-10-31.md).
- [160 cuentas](PROSPECTOS_RONDA2_160_CL_CO_MX_BO_2026-10-31.csv) y [25 potenciales canales](ALIANZAS_CANAL_25_RONDA2_2026-10-31.csv).
- [Fuentes numeradas CSV](REFERENCIAS_Y_ESTADO_VERIFICACION_RONDA2.csv).
- [Costos de operación modelo](MODELO_FINANCIERO_EDITABLE_RONDA2.csv) y [TAM/SAM/SOM](ESCENARIOS_TAM_SAM_SOM_RONDA2.csv).
- [Fondos y eventos](FONDOS_EVENTOS_COMUNIDADES_RONDA2_2026-10-31.md).
- [Riesgos técnicos, puertas comerciales y 13 semanas](RIESGOS_VALIDACION_PLAN_90_DIAS_RONDA2.md).
- [Kit de ventas](ventas/ONE_PAGER_DELIA_ES.md) y archivos relacionados en `docs/ventas/`.

**Próxima versión:** después de entrevistas, benchmarks y revisión técnica, sin borrar las v1/v2 históricas.
