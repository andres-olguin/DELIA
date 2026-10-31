# Política de seguridad — DELIA

**Versión:** 31 de octubre de 2026 · **Estado:** desarrollo y laboratorio, **no aprobado para producción ni para datos personales de clientes**.

## Reportar una vulnerabilidad

No publiques credenciales, tokens, documentos de identidad, prompts reales, registros, pruebas con información de terceros, payloads de explotación o detalles de exposición en GitHub Issues públicos. Comunica el hallazgo de forma privada mediante **contacto@mastertechg.com** con asunto `DELIA — reporte privado de seguridad` y una descripción mínima del componente, impacto, entorno de prueba, forma segura de reproducirlo con datos sintéticos y método seguro para recibir pruebas adicionales. El canal no implica garantía de respuesta en un plazo específico.

**Nunca envíes** secretos, tokens de proveedores, contraseñas ni datos reales en el primer mensaje. No se autoriza la explotación de sistemas ajenos, producción, pentesting contra clientes o pruebas de alto impacto. No hay programa de recompensas por fallos comprometido.

## Alcance y limitaciones actuales

- `main` contiene código experimental de sanitización. La API tiene inconsistencias de importación/esquemas, autenticación insuficiente de auditoría y persistencia potencial de prompts; el detector no se inserta en el reenvío HTTPX.
- No se ha publicado auditoría de seguridad completa ni certificación de cumplimiento; funciones planificadas no equivalen a controles operativos.
- Las demostraciones aceptables usan solo datos sintéticos y un entorno controlado. **No introducir clientes ni proveedores productivos.**
- La documentación comercial no puede describir el producto como un gateway seguro ya desplegable.

## Manejo responsable del hallazgo

1. Se acusa recibo cuando una persona responsable esté disponible; no existe SLA público de triaje.
2. Se registra de forma privada, evalúa criticidad y acceso mínimo, se prepara mitigación con revisión humana y pruebas reproducibles.
3. Si afecta datos, se preserva evidencia sin copiarlos a repositorios públicos y se analiza el deber de notificación por jurisdicción con asesoría profesional.
4. Se coordina divulgación posterior y actualizaciones documentadas sin revelar datos personales ni caminos de explotación innecesarios.

## Referencias

- [Auditoría de riesgos P0/P1](docs/RIESGOS_VALIDACION_PLAN_90_DIAS_RONDA2.md)
- [Issues de seguridad y arranque](https://github.com/andres-olguin/DELIA/issues)
- [Política de contribución](CONTRIBUTING.md)

**No confundir esta política con una certificación, soporte 24/7 o seguro de responsabilidad.**
