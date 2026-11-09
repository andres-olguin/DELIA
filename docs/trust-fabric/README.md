# DELIA Trust Fabric — centro de documentación (propuesta 2026-11-09)

> Estado: arquitectura objetivo y prototipo local de políticas; **NO listo para producción, NO certificado, NO demuestra cumplimiento normativo, no autoriza uso de datos personales reales**.
> Rama de desarrollo: `feat/trust-fabric-2027-01`. Esta línea evoluciona DELIA, no cambia la marca ni fusiona PR #19/#20.

## Posicionamiento
DELIA aspira a ser una **capa de confianza para aplicaciones y agentes empresariales de IA**: decide qué datos pueden salir, qué herramientas puede invocar un agente, cuándo debe intervenir una persona y qué evidencia mínima acredita la evaluación de una política. Se integra con gateways existentes cuando sea viable, sin reinventar cada función de red.

## Qué existe hoy
- `trust_fabric/policy.py`: prototipo local en Python estándar, denegación por defecto, reglas por tenant y rol declarados por llamante, escalado a aprobación humana, token de aprobación de un solo uso vinculado a los argumentos, recibos minimizados con HMAC y separación lógica de políticas.
- `trust_fabric/demo.py`: simulación sin transacciones, sin red y sin información real.
- `tests/test_trust_fabric.py`: pruebas independientes; CI en Python 3.11 y 3.13.
- El motor **NO** verifica identidad real, no persiste aprobaciones, no intercepta tráfico HTTP, no ejecuta herramientas ni se integra con el proxy existente.
- Las reglas regionales MX/BO y el benchmark de Benjamín están en **PR #20**, no en `main`. No atribuir al prototipo integración de ese PR.
- La cobertura PII histórica en `main` es insuficiente para producción. El benchmark histórico de 172 casos informó 71 TP, 3 FP, 79 FN (47,33 % recall).
- Ningún piloto comercial, cliente de pago, ahorro, certificación o SLO ha sido acreditado.

## Índice de ejecución
1. [Catálogo completo de veinte capacidades](20-capacidades.md), con estado y Definition of Done individual.
2. [Arquitectura y límites de confianza](arquitectura.md).
3. [Plan acelerado: 67 días hasta 2027-01-15](plan-67-dias.md).
4. [Modelo de amenazas y controles por diseño](modelo-amenazas.md).
5. [Plan de pruebas, criterios de beta y métricas](pruebas-y-release.md).
6. [Matriz de dependencias y contratos de módulos](integraciones-y-contratos.md).
7. [Modelo económico, escenarios y crecimiento B2B2B](modelo-economico.md).
8. [Investigación competitiva y posicionamiento honesto](competencia-y-fuentes.md).
9. [Registro de decisiones técnicas](decisiones-adr.md).
10. [Manual operativo y adopción de contribuciones](gobernanza.md).
11. [Academia de ventas y presentaciones](../ventas/ACADEMIA_DELIA/README.md).

## Demostración local
Desde la raíz del repositorio, con Python 3.11+:
```bash
python -m unittest discover -s tests -p test_trust_fabric.py -v
python -m trust_fabric.demo
```
El ejemplo usa **una clave fija solo de demostración**, contiene nombres e importes sintéticos y **no llama a proveedores ni efectúa reembolsos**. Prohibido reutilizarla en producción.

## Condiciones de salida
- Todo cambio de comportamiento sensible: PR + dos ojos independientes + pruebas negativas + amenaza correspondiente.
- Una métrica solo se anuncia si existe artefacto ejecutado con versión, conjunto, fecha, entorno y resultados.
- El bloque comercial no sustituye asesoría jurídica ni auditoría de seguridad.
- Fecha objetivo de beta avanzada: **15 de enero de 2027** como meta condicionada a equipo/capacidad, no promesa de funcionalidad garantizada.

## Canales
Repositorio público: https://github.com/andres-olguin/DELIA ; asuntos de seguridad: ver `SECURITY.md`. Para contexto de producto: MasterTech SpA, diferenciando expresamente portafolio personal del fundador y casos propios de la sociedad.
