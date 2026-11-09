# Manual operativo de ingeniería — entregas, responsables y gates

## Responsabilidad
Todo issue tiene una persona DRI que aceptó la tarea, un revisor técnico y un aprobador si aplica. Andrés puede programar, Isaac también puede aportar código, Iván puede llevar integración, Benjamín puede extender CI/benchmark, Nilson solo si confirma capacidad y Emmanuel solo si formaliza colaboración. **No asignación automática**, no exclusividad, no remuneración o relación laboral implícita.

## Definición de Done
1. Rama desde versión conocida, sin incluir secretos.
2. Descripción de problema, amenaza, criterios y alcance negativo.
3. Tests locales o CI con versión, SHA y resultados.
4. Aprobación de revisor no autor de la implementación para cambios sensibles.
5. PR fusionado tras gates, monitoreo y rollback preparado; recién entonces tarjeta Done.
6. Si se rechaza, registrar evidencia y plan de reparación, no maquillar resultados.

## Asignaciones propuestas por frente, no órdenes
- Base P0: arquitecto + revisor independiente.
- DLP regional/benchmarks: mantenedor actual del motor, con responsable del corpus independiente distinto.
- Agent Firewall y Policy Studio: pareja de backend y seguridad, roles aceptados.
- Dashboard y ventas: frontend + comercial, evitando inventar testimonios.
- Seguridad/QA: auditor designado, separado de autor cuando sea posible.

## Cadencia rápida pero sostenible
Planificación por entregable y riesgo, no reuniones largas por costumbre. Registro asíncrono: commit/PR, evidencia, bloqueo y siguiente paso. Una sesión de integración 2 veces por semana y una demo de 10 minutos cada viernes cuando haya avance sustantivo.

## Gestión de cambios
- Mantener `main` protegida y PR #19/#20 intactos hasta revisión.
- No activar auto-merge, no rebases forzados en ramas ajenas, no tocar credenciales/producción.
- Archivos de documentación públicos sin datos financieros o clientes identificables salvo fuentes públicas contextualizadas.
- No convertir exploración comercial en promesas de seguridad o resultados de negocios.

## Ingreso de colaboradores
Invitación y permisos mínimos, claridad de licencia del repositorio y propiedad intelectual, acuerdos adecuados para materiales confidenciales, verificación de acceso a GitHub/Trello, protocolo de revisión y disposición de trabajo real.
