# Investigación competitiva: cómo evitar ser otro proxy

Corte editorial 2026-11-09. Verificar licencias, versiones y claims antes de citar. **No se ha ejecutado comparativa DELIA vs. competidores con benchmarks homogéneos.**

## Punto de partida
Detectar PII, rate limiting, fallback y auditoría son capacidades ya existentes en gateways y repositorios abiertos. DELIA solo podría diferenciarse si ofrece integración superior, precisión regional medida, enforcement de herramientas y evidencia mínima con operación sencilla. «Primero del mundo» y «único en LATAM» no están sustentados.

## Familias de competencia
| Categoría | Referencias | Qué debemos aprender | Diferencia a validar |
|---|---|---|---|
| Gateway multi-LLM | LiteLLM, Cloudflare AI Gateway, Portkey | API, routing, presupuesto, fallback, observabilidad, DLP | Control de acciones/tenants integrado sin lock-in |
| PII/anonymization | Microsoft Presidio, PrivAiTe | Reconocedores, reversibilidad, precisión, política de tokens | Corpus local revisado, despliegue simple, límites explicados |
| Agent firewall/MCP | Strathon, Soup Wall, otros | Tool policies, aprobaciones, telemetría, aislamiento | Flujos empresariales y paquetes sectoriales CL/MX/CO/BO |
| Runtime / postura | Agent security platforms | Identidad, inventario, incidentes y gestión de riesgos | Implementación modular transparente y replicable |
| Compliance/GRC | suites GRC/privacidad | Evidencia, controles, documentación | Vincular decisiones concretas de agentes a registros mínimamente invasivos |

## Fuentes consultadas
1. OWASP Top 10 Agentic Applications 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
2. OWASP Agent Control Standard y materiales de seguridad: https://genai.owasp.org/initiatives/agentic-security-initiative/
3. OWASP LLM Top 10 2026: https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/
4. Strathon (autodeclaraciones de producto): https://getstrathon.com/
5. Soup Wall (documentación de su proyecto): https://github.com/SoupTeam/soup-wall
6. PrivAiTe: https://github.com/crp4222/PrivAiTe
7. Grepture Proxy: https://github.com/grepture/proxy
8. LLM Shield Proxy: https://github.com/ninadphalak/LLM-Shield-Proxy
9. Agent Security Index, directorio de herramientas (verificar fichas): https://agentsecurityindex.com/
10. Biblioteca del Congreso Nacional de Chile, Ley 21.719, versión verificada: https://www.bcn.cl/leychile/navegar?i=1209272&f=2026-12-01
11. Propuesta del Gobierno de Chile de postergación a 2027 (propuesta, no cambio vigente probado): https://www.economia.gob.cl/2026/09/01/gobierno-propone-ampliar-plazo-para-implementar-nueva-ley-de-proteccion-de-datos-y-institucionalidad.htm

## Hallazgos para decisiones
- Herramientas como Strathon ya publicitan deny-by-default, aprobaciones humanas, agentes con identidad y registros de integridad. Estas ideas NO son inexploradas.
- Diferenciación defensible: **evidencia de comportamiento + corpus regional independiente + tiempo de integración + integrador multicliente con soporte**.
- Testear un caso end-to-end comparable: «agente propone pago, política lo bloquea, requiere aprobación independiente, no filtra PII, produce recibo verificable».
- Validar costos, facilidad de onboarding, acciones bloqueadas y falsos positivos frente a soluciones reales con permisos legales, nunca fabricar un ganador.

## Legalidad
La ley 21.719 figura en la Biblioteca del Congreso Nacional con vigencia diferida 01-DIC-2026 al momento de la consulta; el Ejecutivo propuso su postergación un año. Confirmar estado legislativo en la fecha efectiva de uso; DELIA no ofrece certificación ni asesoría jurídica.
