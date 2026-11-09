# DELIA — Riesgos de producto, ventas y afirmaciones permitidas

**Versión 2026-11-09.** Documento de autocontrol editorial y técnico. El estado de las funciones se determina por SHA y evidencia, no por la cantidad de documentación.

## Riesgos estratégicos

| Riesgo | Severidad | Control / decisión |
|---|---|---|
| «20 productos» sin recursos y sin mercado | Alta | Núcleo modular + 4 ICP prioritarios + resto backlog |
| Competencia de grandes clouds y gateways | Alta | Integración coexistente, diferenciación medible |
| Fuga de PII en el proxy existente | Crítica | #9 y test upstream mock antes de cualquier piloto real |
| Cliente invoca herramienta fuera del control | Crítica | Adapter único con enforce y test E2E, fail-closed |
| Aprobador falso o replay | Crítica | Identidad verificada, vínculo con acción, TTL y consumo transaccional |
| Mezcla de datos entre organizaciones | Crítica | Tenant derivado de identidad y pruebas cross-tenant |
| Logs con prompts/secretos | Crítica | Minimización, retención, RBAC, cifrado de almacenamiento y pruebas sentinel |
| Falta de datos independientes para PII | Alta | Dataset revisado separado de autores de reglas |
| Sobrecosto de SaaS/servicios | Alta | Metering, límites, margen y presupuesto aprobado |
| Promesas legales y comerciales falsas | Alta | Claims versionados, revisión contractual y criterio No-Go |
| Marca y PI sin evaluar | Alta | INAPI/IMPI, contribuciones, MIT, acuerdos privados |
| Dependencia de tiempo de colaboradores | Alta | Capacidad comprometida, priorizar P0 y bajar alcance |
| Proliferación de conectores vulnerables | Alta | Paquetes firmados, allowlist y escaneo antes de distribución |
| Reembolsos/pagos sin controles | Crítica | Demo ficticia y nunca operación real antes de gates |

## Afirmaciones: permitidas y prohibidas

| Afirmación | ¿Se puede usar hoy? | Forma correcta |
|---|---|---|
| «DELIA está en desarrollo» | Sí | Estado exacto |
| «Motor local de política probado en GitHub» | Sí, con SHA de PR #21 | Demo sintética, no seguridad productiva |
| «170 pruebas del trabajo regional» | Sí, atribuidas a PR #20 | Solo suite/revisión documentada y fecha |
| «Detecta el 100 % de datos personales» | No | 55/55 en corpus sintético de desarrollo; falta evaluación externa |
| «Firewall de agentes enterprise operacional» | No | Objetivo, adapter real y auth pendientes |
| «Aprobación humana inviolable» | No | Aprobación simulada, sin identidad real |
| «HMAC prueba que no hubo fuga» | No | HMAC prueba integridad de campos firmados, no toda la ejecución |
| «Somos únicos o primeros del mundo» | No | Competidores ya ofrecen gobierno de agentes |
| «Certificados por OWASP/NIST/ISO» | No | Se usan marcos como referencia |
| «Cumplimos Ley 21.719/LGPD/GDPR» | No | Controles a evaluar legalmente por jurisdicción |
| «Tenemos clientes y MRR DELIA» | No verificado | No atribuir facturación de otra actividad |
| «El SaaS estará listo el 15/01» | No como garantía | Meta de beta avanzada sujeta a Go/No-Go |
| «La plataforma permite 18 verticales» | No como hecho | Mapa de oportunidades y diseños sectoriales |
| «Ofrecemos Cloud/Partner/Enterprise» | Aún no | Portafolio comercial propuesto, no disponible |

## Nota regulatoria

El AI Act europeo y la ley chilena de datos personales tienen calendarios y obligaciones que deben comprobarse en la fuente oficial antes de citarse; una norma no impone contratar a DELIA. Fuentes: https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai y https://www.bcn.cl/leychile/.

## Políticas de release

No-Go obligatorio frente a fallo de auth, bypass, cross-tenant, egress PII, replay aprobado, registros inseguros, control sin pruebas de carga adecuadas o falta de contratos. Una demo sintética nunca autoriza usar datos sensibles, pagos o infraestructura crítica.

## Protección jurídica y comercial

- Verificar licencias MIT, derechos de colaboradores, marcas e imagen empresarial.
- Separar portafolio freelance personal del fundador de activos/casos facturados por MasterTech.
- Contratos de servicios, tratamiento de datos y licencias adaptados a país, bajo asesoría pertinente.
- No publicar prospectos identificables ni comunicaciones privadas en GitHub.
- No sugerir que un partner o prospecto usa DELIA hasta evidencia/acuerdo.

## Pregunta de control editorial obligatoria
«¿Este mensaje describe algo que funciona en un commit verificable, una función de laboratorio, una intención futura o una oportunidad de mercado?» Si no está claro, reescribir con estado, fuente, limitación y fecha.

## Nuevos límites de comunicación comercial (investigación global 09/11)

- **No decir:** «primera plataforma que autoriza tool calls», «primer sistema que reconcilia resultados de agentes» o «único con presupuestos cruzados». Helio, AgentTrustOps, Temporal y otros ya declaran esas capacidades.
- **Sí decir:** «DELIA investiga contratos de operación por industria con protección regional, evidencia de resultado y un canal de integradoras». Es hipótesis de producto, no ventaja medida.
- **Nunca equiparar** `ELIGIBLE_FOR_AUTHORIZATION` con autorización real ni `VERIFIED_SIMULATED` con operación bancaria confirmada.
- Los informes de comparación deben citar fuente, fecha y versión, y declarar que no se ejecutó un benchmark competitivo hasta que exista.
- Toda política con datos reales requiere controles S1–S4 y consentimiento contractual pertinente. Un laboratorio local es exclusivamente S0.

