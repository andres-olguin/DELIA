# DELIA — Encuesta de disposición de pago (Van Westendorp)

**Corte 31/10/2026.** Instrumento propuesto, **NO aplicado**. No existe evidencia de willingness to pay. Aplicarlo solo después de que el entrevistado haya entendido un **concepto preciso y hipotético** de servicio y sus límites.

## Definición idéntica presentada a cada persona

«Imagine una herramienta para un equipo integrador de aplicaciones LLM capaz de comparar y aplicar reglas verificadas de minimización de identificadores CL/CO/MX/BO, con auditoría minimizada, autenticación por tenant y soporte técnico. Estas capacidades se **consideran hipotéticas y no están disponibles hoy en DELIA**. Suponga una suscripción por organización, sin impuestos y con un volumen [definir] de solicitudes mensuales. El uso de APIs/modelos de terceros se factura aparte. El piloto inicial requeriría un acuerdo separado».

No mezclar precio por integrador, por aplicación, por cliente final y por millón de tokens sin especificarlo.

## Cuatro preguntas centrales

1. ¿A partir de qué **precio mensual USD** considerarías el servicio **tan barato** que dudarías de su calidad/soporte?
2. ¿A qué precio mensual USD te parecería **barato pero creíble** y una buena compra?
3. ¿A partir de qué precio mensual USD empezaría a resultar **caro pero todavía contemplable**?
4. ¿A partir de qué precio mensual USD sería **demasiado caro** y definitivamente no lo comprarías?

**Chequeo de consistencia:** `demasiado barato ≤ barato ≤ caro ≤ demasiado caro`. Si hay respuestas invertidas, preguntar por confusión y no inventar valores. Registrar país/moneda, cargo funcional, alternativa actual, volumen y base presupuestaria.

## Otras preguntas de evidencia real (no sustituyen el método)

- ¿Cuánto pagan **hoy** por control DLP/gateway/observabilidad, incluyendo hosting e ingeniería? Puede decir NV.
- ¿Cuál fue la última compra similar y quién la aprobó?
- ¿Qué proveedor existente sustituiría esta herramienta y cuál sería el costo de migración?
- ¿Quién tendría presupuesto, en qué fecha y con qué condición?
- ¿Qué respuesta indicaría que nunca comprarías un middleware adicional?

## Tratamiento estadístico

Van Westendorp genera curvas acumuladas de percepción y puntos de cruce (PMC/OPP/IPP/PME) a partir de **respuestas reales**, con n y sesgo de muestra explícitos. **Hoy todos esos puntos son NO CALCULADOS/NO VERIFICADOS.** Evitar sugerir que el punto «óptimo» implica transacciones pagadas. Con muestras pequeñas, reportar distribución sin conclusiones representativas.

Recoger solo identificador de encuesta anónimo y consentimientos para uso agregado, en archivo privado. Nunca subir nombres ni correos a GitHub.
