# Afirmaciones comerciales permitidas, prohibidas y comparativa

**Versión 09-11-2026.** Revisar este documento antes de toda presentación externa.

## Semáforo de afirmaciones
| Afirmación | Estado | Cómo reformular |
|---|---|---|
| «Trust Fabric es un proyecto en desarrollo» | VERIFICABLE | Exacto |
| «Existe un motor local de políticas deny-by-default» | VERIFICABLE en rama | Precisar que no está en main ni autentica usuarios remotos |
| «Las pruebas Trust Fabric corrieron en CI» | VERIFICABLE con SHA/run | Mostrar URL y versión probada |
| «Nuestro Agent Firewall protege herramientas reales» | NO DEMOSTRADO | «Simula decisiones; falta adapter productivo» |
| «Aprobación humana segura en la nube» | NO DEMOSTRADO | «Simulador con TTL y un solo uso; faltan IAM y almacenamiento» |
| «Auditoría inmutable» | NO DEMOSTRADO | «HMAC local sin log durable; tamper-evidence a evaluar» |
| «Cifrado reversible completo» | NO DEMOSTRADO | «Privacy Vault planificado» |
| «100 % de PII detectada» | FALSO GENERALIZAR | «Corpus sintético MX/BO propio: 55/55; no generaliza» |
| «Compatible con los agentes de cualquier proveedor» | NO DEMOSTRADO | «Adapters por construir y verificar» |
| «Cumplimos la Ley 21.719/LGPD» | NO DEMOSTRADO | «Diseñamos controles que podrían apoyar obligaciones, previa revisión legal» |
| «Ya vendemos a bancos / líderes» | NO VERIFICADO | «Segmentos de investigación, sin clientes de pago DELIA comprobados» |
| «En enero estará listo para producción» | PROMESA SIN BASE | «Meta de beta avanzada sujeta a seguridad y capacidad» |
| «Ahorra X % en costos o evita multas» | NO MEDIDO | «Modelo de retorno para validar en un piloto» |

## Quién compite
- **LiteLLM:** gateway de múltiples modelos con presupuestos, controles, observabilidad, etc.
- **Cloudflare AI Gateway:** intermediación, análisis y controles de datos según configuración.
- **Microsoft Presidio:** framework de detección/anónimización PII, útil para comparación.
- **PrivAiTe:** proxy self-hosted de protección de información, con funciones que deben revisarse en su versión.
- **Grepture Proxy y LLM-Shield-Proxy:** proyectos con enfoques parcialmente coincidentes.
- **Strathon y Soup Wall:** proyectos de seguridad de agentes y tráfico, control de herramientas.
Fuentes y URLs: `docs/trust-fabric/competencia-y-fuentes.md`.

## Matriz de comparabilidad para la reunión
| Eje | Pregunta | Evidencia necesaria |
|---|---|---|
| DLP | ¿Qué entidades/países cubre, con qué recall? | Dataset independiente mismo hardware/versión |
| Herramientas | ¿Bloquea ejecución real sin bypass? | E2E con adapters |
| Identidad | ¿Verifica roles y tenants? | Security tests + threat model |
| Aprobaciones | ¿Evita replay, TOCTOU y autoprobación? | Tests de concurrencia y expiración |
| Privacidad | ¿Conserva prompts completos? | Inspección de logs y retención |
| Operación | ¿Cuánto tarda instalar? | Cronómetro de onboarding reproducible |
| Economía | ¿Cuál es coste total por mes? | Tarifa + nube + soporte + personal |
| Compliance | ¿Qué control tiene evidencia legal? | Matriz jurídica por jurisdicción, no sellos inventados |

## Fuentes y verificación legal
OWASP Agentic 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
OWASP Agent Control Standard: https://genai.owasp.org/initiatives/agentic-security-initiative/
Ley chilena 21.719, BCN con fecha diferida: https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01
Propuesta de postergación del Ejecutivo (NO confundir con ley vigente): https://www.economia.gob.cl/2026/09/01/gobierno-propone-ampliar-plazo-para-implementar-nueva-ley-de-proteccion-de-datos-y-institucionalidad.htm

## Reglas de fuentes
No atribuir al producto resultados de benchmarks de terceros sin ejecutarlos. No usar logotipos de competidores o prospectos como prueba de alianza. Guardar fuente, fecha, estado «leído íntegramente / extracto / no verificado» y versión de la herramienta. Actualizar el material con cada release; retirar inmediatamente claims superados por regressions.
