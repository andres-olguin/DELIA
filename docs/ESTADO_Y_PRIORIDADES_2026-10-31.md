# DELIA — Estado observado y prioridades abiertas

**Fecha de revisión documental:** 31 de octubre de 2026  
**Tipo:** observación del repositorio y propuesta de próximos pasos; **no** acta de aprobación, certificación de seguridad ni resultado de pruebas ejecutadas.  
**Alcance:** rama `main`, inspección de archivos publicados. No se ejecutaron dependencias, tests, despliegues ni un análisis de seguridad completo.

## Qué puede verificarse desde el repositorio

- Hay un [README](../README.md) con la visión de producto, arquitectura objetivo, stack, criterios de aceptación y roadmap.
- El [roadmap](roadmap.md) identifica un **Sprint 2** sobre sanitización de información personal, con hito objetivo al **8 de noviembre de 2026**.
- Existe código de detección/sanitización en `backend/dlp/pii.py` y pruebas asociadas en `tests/test_pii.py`.
- Hay componentes de API y proxy en `app/`, `backend/` y `services/`, además de archivos de Docker Compose y configuración de entorno.
- La carpeta `docs/` contiene un estudio de viabilidad y notas sobre demostración, seguridad y propuesta de valor.
- Persisten referencias a la identidad anterior **TALIA** en al menos `app/main.py` y `app/api/proxy.py`. Cualquier cambio de nombres expuestos por una API debe evaluar compatibilidad antes de aplicarse.

**Esto demuestra presencia de archivos y trabajo previo, no que las funcionalidades estén integradas, probadas o listas para producción.** Un estado de \"completado\" en el roadmap requiere comprobar resultados y criterios de aceptación.

## Prioridades técnicas propuestas — Sprint 2

1. **Reproducibilidad:** documentar cómo levantar el entorno desde un clon limpio y ejecutar las pruebas existentes; registrar errores y evidencias sin datos reales.
2. **Calidad de sanitización:** ampliar y validar casos positivos, negativos y de borde de RUT, cédula/NIT, correos, teléfonos y otras categorías admitidas; medir límites de detección.
3. **Tratamiento de datos sensibles:** revisar que auditoría, errores y trazas no divulguen prompts, credenciales ni valores personales innecesarios.
4. **Integración:** definir criterios verificables para invocar la sanitización antes de cualquier salida hacia proveedores externos y documentar qué ocurre ante fallos.
5. **Identidad:** revisar referencias TALIA/DELIA sin romper contratos de API o integraciones existentes.

Los responsables y las fechas deben confirmarse con las personas que acepten cada tarea; esta nota no asigna trabajo a nadie.

## Validación comercial — trabajo paralelo, no prueba de demanda

La hipótesis de DELIA es que equipos que integran LLM necesitan controlar el envío de datos sensibles, el uso de proveedores y la trazabilidad. **No hay evidencia suficiente aquí para afirmar que esa demanda esté validada o que existan clientes de DELIA.**

Propuesta de investigación antes de fijar precios o prometer capacidades:

- Delimitar segmentos iniciales (por ejemplo, empresas de software B2B que integran APIs de modelos y tratan información reservada).
- Preparar entrevistas de descubrimiento centradas en problemas actuales, soluciones existentes, costos, requisitos regulatorios y decisiones de compra; no usar entrevistas como preventa ficticia.
- Registrar respuestas anónimas o consentidas; separar observaciones, hipótesis y conclusiones.
- Comparar alternativas y evaluar la disposición a realizar un piloto **solo cuando exista una demostración verificable y límites documentados**.
- Decidir si mantener, ajustar o reducir el alcance del MVP usando evidencia obtenida.

## Propuesta de criterios para una demostración honesta

- Un caso de entrada **sintética** reproduce el tratamiento PII previsto.
- El resultado es verificable mediante comando/prueba o una simulación **marcada expresamente como tal**.
- Se documentan límites, detecciones fallidas, dependencias y comportamiento ante errores.
- No se exponen secretos ni materiales privados ni se garantiza seguridad/cumplimiento normativo.
- Cualquier despliegue público se revisa separadamente por riesgos, costos y autorización.

## Organización

Se propone usar **GitHub Issues y PRs** para tareas técnicas, criterios de aceptación y evidencia; la selección definitiva entre GitHub Projects/Trello corresponde al equipo. Una futura integración con MasterTech OS es una intención de planificación, **no una herramienta operativa actual**.

Para participar, consulta [CONTRIBUTING.md](../CONTRIBUTING.md). Los aportes deben respetar licencias, acuerdos, propiedad intelectual y acceso mínimo.

---

**Próxima actualización:** cuando se ejecuten pruebas, se validen resultados o se tomen decisiones explícitas sobre responsables y prioridades. No marcar como terminado lo que solo está documentado o propuesto.
