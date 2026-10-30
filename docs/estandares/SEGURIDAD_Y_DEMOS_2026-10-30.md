# Criterios transversales de seguridad y demostración — 2026-10-30

Propuesta documental para DELIA; no implica auditoría superada ni despliegue aprobado.

## Checklist previo a producción
- [ ] Inventariar rutas API, marcar cuáles son públicas y probar autorización por objeto y usuario.
- [ ] Validar entradas en servidor y probar datos malformados, límites e inyecciones.
- [ ] Aplicar rate limiting por cuenta/usuario/IP según amenazas; proteger login y operaciones costosas.
- [ ] Manejar errores sin revelar secretos, trazas o datos privados; proteger logs.
- [ ] Revisar tokens, cookies, caducidad, revocación, sesiones y CSRF cuando aplique.
- [ ] Revisar CORS por entorno; no sustituye autenticación.
- [ ] Auditar dependencias, secretos, permisos y exposición accidental en historial Git.
- [ ] Probar aislamiento de datos y RLS cuando corresponda.
- [ ] Probar flujos completos, regresión, backups, restauración y rollback.
- [ ] Documentar revisión de accesibilidad, identidad visual y diferenciación de frontend.
- [ ] Registrar evidencias, fecha, responsable, riesgos abiertos y aprobación de liberación.

## Demo visual
Investigar interfaz mínima de demostración, documentación API interactiva o sandbox con datos ficticios; usar GitHub Pages solo para sitios estáticos o servicio de hosting adecuado. Enlazar demo en README/About una vez desplegada y verificada. No exponer servicios privados, llaves ni datos reales.

## Registro diario
Registrar avances relevantes con fecha en issues, PR, commits y documentación. No crear commits vacíos ni publicar información confidencial.

## Estado
Propuesta pendiente de revisión por proyecto. Ninguna casilla se considera aprobada por defecto.
