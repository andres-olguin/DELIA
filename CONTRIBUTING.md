# Guía de contribución — DELIA

DELIA es un proyecto en desarrollo activo. Este repositorio público contiene documentación y código en evolución; **no debe interpretarse como un producto listo para producción ni como una garantía de seguridad o cumplimiento normativo**.

Consulta primero el [README](README.md), el [roadmap](docs/roadmap.md) y el [estado técnico y prioridades](docs/ESTADO_Y_PRIORIDADES_2026-10-31.md).

## Cómo proponer una mejora

1. **Revisa los Issues abiertos** para evitar trabajo duplicado. Si no hay una tarea adecuada, abre una propuesta que explique el problema, el alcance y una forma verificable de comprobar la solución.
2. **Acuerda el alcance antes de implementar cambios grandes.** Los sprints del roadmap son orientativos; una asignación histórica no equivale a una tarea aceptada o completada.
3. **Trabaja en una rama separada** y presenta un pull request (PR). Evita comprometer directamente la rama principal sin coordinación.
4. **Incluye evidencia:** describe qué archivos cambiaste, cómo los probaste, qué resultados obtuviste y qué limitaciones quedan pendientes. Si no ejecutaste pruebas, indícalo expresamente.
5. **Pide revisión** antes de fusionar. Los cambios sensibles en autenticación, sanitización, auditoría o comunicación con proveedores necesitan especial atención.

### Convención sugerida de ramas y commits

- Rama: `docs/guia-contribucion`, `fix/pii-casos-borde`, `feat/control-cuotas`.
- Commit: `docs: aclarar criterios de contribución`, `test: ampliar casos RUT`.

Son convenciones propuestas, no una política formal aprobada.

## Calidad y seguridad

- Usa **datos sintéticos** en pruebas, ejemplos, capturas y tickets. No subas datos personales reales, conversaciones privadas, identificaciones, prompts sensibles ni información de clientes.
- Nunca publiques credenciales, tokens, claves API, archivos `.env` ni secretos de infraestructura.
- Comprueba casos positivos, negativos y límites; documenta falsos positivos/falsos negativos en las reglas PII.
- Minimiza registros: no incluyas valores originales sensibles en logs, mensajes de error o evidencia compartida.
- No declares una función como completada sin ejecución reproducible, pruebas pertinentes y revisión del comportamiento.
- Las dependencias externas, los servicios de IA y las integraciones deberán utilizarse con autorización cuando se maneje información reservada.

Si descubres una posible vulnerabilidad que pudiera exponer datos, **no publiques instrucciones de explotación ni datos sensibles en un Issue público**. Comunícalo de manera privada a **contacto@mastertechg.com** para coordinar su revisión.

## Pruebas

Para reproducir la suite en Linux, ejecuta estos comandos desde la raíz con
Python 3.14.4. Las dependencias directas e indirectas de prueba tienen versiones
fijas en [requirements-test.txt](requirements-test.txt).

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-test.txt
.venv/bin/python -m pip check
.venv/bin/python -m pytest -q --tb=short tests/
```

Las pruebas API usan SQLite en memoria y las pruebas del cliente HTTP usan
un adaptador en memoria. GitHub Actions ejecuta la misma suite y el benchmark
sintético en los PR hacia `main` y en los pushes a las ramas configuradas.
Si tu PR modifica código, añade las pruebas correspondientes y registra los
comandos usados y sus resultados. Consulta el
[informe del benchmark](docs/benchmarks/RESULTADOS_MX_BO.md) para reproducir
la comparación y conocer sus límites.

## Participación y condiciones

La colaboración debe ser **voluntaria, informada y acordada según el alcance concreto**. Abrir una conversación o contribuir a un Issue público no incorpora automáticamente a una persona al equipo, no crea un vínculo laboral ni implica remuneración o participación societaria. Actualmente MasterTech no tiene presupuesto confirmado para remunerar nuevas colaboraciones. Cualquier condición económica, de propiedad intelectual o de acceso reservado requiere un acuerdo separado antes de asumir compromisos.

El repositorio es público, pero **las credenciales, documentación interna, materiales de clientes y repositorios privados no lo son**; los accesos se otorgan exclusivamente de manera autorizada y según necesidad.

Agradecemos propuestas claras, críticas técnicas fundamentadas y revisiones que ayuden a comprobar el valor real de DELIA.
