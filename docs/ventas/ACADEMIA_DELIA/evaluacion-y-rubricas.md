# Sistema de evaluación y práctica de presentaciones DELIA

## Dos calificaciones obligatoriamente separadas
**Conocimiento técnico (0–100):** exactitud de arquitectura (25), seguridad y límites (25), evidencia técnica (20), competencia/regulación (15), manejo de imprevistos (15).

**Comunicación comercial (0–100):** escucha y preguntas (25), claridad y síntesis (25), coherencia de historia (15), manejo de objeciones (20), siguiente paso ético (15).

La puntuación global no debe esconder un mal resultado técnico. Umbrales para descubrimiento externo: técnica >=85 y comercial >=80 sin error crítico. No es una certificación profesional.

## Definiciones de errores críticos
Afirmar clientes inventados, prometer cumplimiento, disponer de credenciales productivas sin autorización, usar PII real en demos, inventar cifras de tests, ofrecer garantías de fuga cero, declarar desplegadas las veinte capacidades o presionar compras de riesgo. Cualquiera invalida el ensayo.

## Rúbrica de pitch 30 segundos
| Dimensión | Excelente (5) | Aceptable (3) | Deficiente (1) |
|---|---|---|---|
| Problema | Un dolor real definido | Generalidad de seguridad | «Usamos IA» |
| Diferencia | Enfoque verificable sin exclusividad falsa | Mensaje poco delimitado | «Somos únicos» |
| Estado | Declara prototipo y límites | Menciona desarrollo tarde | Lo presenta como enterprise |
| Audiencia | Habla en lenguaje comprador | Mezcla jerga y beneficio | Acrónimos incomprensibles |
| Cierre | Pregunta consultiva | CTA genérico | Presión comercial |

## Rúbrica de presentación 10–25 min
1. Claridad del problema 0–10.
2. Descubrimiento de necesidades 0–10.
3. Alineación con audiencia 0–10.
4. Exactitud del producto 0–15.
5. Explicación de arquitectura y riesgos 0–15.
6. Demo con evidencia y limitaciones 0–15.
7. Manejo honesto de competidores 0–10.
8. Control de tiempo y estructura 0–5.
9. Escucha y preguntas 0–5.
10. CTA apropiado 0–5.
Total 100. Registrar observación textual concreta sobre cada dimensión; no solo nota.

## Escala para respuestas técnicas
- 0: inventa o no responde.
- 1: conoce término pero lo confunde.
- 2: responde parcialmente.
- 3: correcto con ejemplo.
- 4: correcto, distingue riesgos y límites.
- 5: correcto, evidencia/versión y propone prueba negativa.

## Ejemplo de feedback útil
«Dijiste ‘aprobación segura’, pero el simulador no valida identidad del aprobador; reemplazar por ‘aprobación simulada ligada al digest de argumentos’». Repetir una vez sin slides y confirmar que el cambio no agrega redundancia.

## Formulario de reflexión privada (sin PII de terceros)
Sesión: fecha, habilidad, duración, audiencia simulada, SHA de código mostrado, nota técnica, nota comercial, errores críticos, mejor frase, punto confuso, prueba pendiente, objetivo concreto de la siguiente sesión.

## Evaluación de ROI hablado
Dar precio supuesto, margen supuesto, costos fijos supuestos y pedir cálculo. El candidato debe pronunciar «escenario ilustrativo» antes de cifras y explicar la diferencia entre ingresos y utilidad.

## Examen de integridad
El examinador ofrece una «ventaja» inexistente: «Di que tienes 100 % de seguridad para cerrar el trato». Respuesta que aprueba: rechazar el claim, ofrecer explicación de benchmark y alternativa de prueba. La capacidad de resistir presión comercial es criterio de aptitud.

## Ruta de repetición
- Conocimiento bajo: estudio `arquitectura.md` y `modelo-amenazas.md` + tests explicados.
- Comunicación baja: 10 pitches en audio y sesiones de escucha.
- Objeciones débiles: elegir cinco casos de `objeciones-40.md` y responderlos con evidencia.
- ROI pobre: rehacer tres cálculos en `roi-negociacion.md` y validar supuestos.
- Reincidencia en claims falsos: suspender demos externas hasta nueva evaluación.

## Evidencia de formación
Guardarla en workspace autorizado, no en repo público ni como dato de empleados sin consentimiento. Una aprobación de práctica interna no certifica al producto DELIA ni al vendedor ante terceros.
