# Demo operativa DELIA — 2, 10 y 25 minutos

**Solo laboratorio sintético.** No conectar bases de datos reales, clientes o herramientas de pago. Este guion incluye comandos ejecutables y un ejemplo ficticio de reembolso MXN.

## Preparación
En una copia del repositorio, sobre la rama Trust Fabric:
```bash
python --version
python -m unittest discover -s tests -p test_trust_fabric.py -v
python -m trust_fabric.demo
```
Python estándar 3.11+; sin API keys. Comprobar que no haya secretos en terminal/captura. Registrar SHA y run URL antes del evento.

## Guion 2 minutos
0:00–0:25: «DELIA está en desarrollo y esta es una simulación local». 0:25–0:45: «Un agente propone reembolso de MXN $18.000; la política permite montos menores, exige aprobación para altos». 0:45–1:20: ejecutar `python -m trust_fabric.demo`; mostrar `PENDING_APPROVAL`, `ALLOW` y `DENY` en replay. 1:20–1:40: «La decisión tiene un recibo HMAC, no el importe original en los metadatos». 1:40–2:00: «Falta identidad real, egress, almacenamiento y audit externa; ¿qué operación similar les preocupa?».

## Guion 10 minutos
0:00–1:30: situación del comprador y riesgo concreto. 1:30–2:30: arquitectura y límites. 2:30–4:30: suite de tests y casos (deny unknown, no tenant, high-amount pending, replay, policy change). 4:30–6:30: demo en vivo y lectura de recibo. 6:30–7:30: amenaza TOCTOU y cómo queda reducida por fingerprint. 7:30–8:30: limitaciones de simulador, comparadores existentes. 8:30–10:00: dos casos del comprador, siguiente prueba.

## Guion 25 minutos
5 diagnóstico, 4 arquitectura, 5 demo, 4 threat model, 3 propuesta económica, 4 discusión y acuerdo. No usar 25 minutos de terminal. Confirmar que el cliente vea la salida y comprenda el flujo.

## Escenarios que debe poder pedir el interlocutor
1. Intento de operación desconocida: DENY.
2. Tenant sin policy: DENY.
3. Operación permitida dentro de umbral: ALLOW.
4. Operación superior al umbral: PENDING.
5. Aprobador mismo agente: no aprueba.
6. Aprobador con rol incorrecto: no aprueba.
7. Aprobación de otro tenant: no aprueba.
8. Reusar ticket ya consumido: DENY.
9. Cambiar argumentos después de aprobar: DENY.
10. Alterar recibo: falla HMAC.
11. Cambiar policy version: invalida aprobación.
12. Contenido confidencial en args: no aparece raw en recibos del laboratorio.

## Plan de fallos de demo
- El terminal no corre: mostrar CI verificada por URL y explicar el bloqueo, no fingir.
- La rama no existe localmente: usar captura autenticada del PR y código visible en GitHub.
- El equipo pregunta por pagos reales: «No hay conexión de herramientas productivas».
- Pregunta por PII: «El prototipo no inspecciona el tráfico HTTP; P0 #9 pendiente».
- Pregunta por certificados: «No contamos con certificación del producto».
- Sale una pregunta inesperada: «No está verificado; podemos diseñar un test reproducible».

## Checklist de presentador
[ ] Versiones verificadas; [ ] consola sin tokens; [ ] Internet opcional; [ ] ejemplos ficticios; [ ] letra grande; [ ] 3 puntos de pausa; [ ] enlace a run; [ ] «qué no demuestra»; [ ] CTA de validación limitado.

## Riesgo del «demo theater»
Una simulación exitosa no garantiza que el cliente no pueda llamar una herramienta por fuera del gateway. Nunca enseñar «DENY» como prueba de bloqueo real a menos que exista un adapter con test end-to-end. Los tests de esta rama verifican el motor, no el transporte de producción.
