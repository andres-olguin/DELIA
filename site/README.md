# DELIA — Sitio público estático

**Estado:** código de frontend de investigación, no despliegue verificado. **Fecha de preparación:** 09/11/2026.

## Arquitectura
- `site/index.html`: landing pública con identidad visual, enfoque, roadmap, transparencia y CTA por mailto.
- `site/styles.css`: responsive sin bundler.
- `site/app.js`: tres escenarios ficticios definidos en el navegador (permitido, denegado, sin verificación). **No ejecuta DELIA ni llama a API alguna**.
- `.github/workflows/public-site-pages.yml`: valida en PR; tras integración en main publica **solo `site/`** a GitHub Pages.
- `tools/check-public-site.mjs`: comprobaciones estáticas sin dependencias.

## Habilitación por el propietario
1. Revisar PR, contenido, seguridad y derechos; integrar en `main`.
2. En GitHub > DELIA > **Settings > Pages > Build and deployment > Source**, elegir **GitHub Actions**.
3. Abrir **Actions > DELIA public site · GitHub Pages** y usar **Run workflow** en main si el cambio inicial no desencadenó despliegue.
4. Esperar el resultado **success** y verificar manualmente `https://andres-olguin.github.io/DELIA/` (PC/móvil), rutas, enlaces y consola. **No declarar el sitio publicado hasta comprobar HTTP 200**.
5. Enlazar desde la ficha existente de MasterTech `/proyectos/delia/`; su hosting Webuzo se publica por separado. No cambiar DNS ni sustituir `mastertechg.com` por un dominio de Pages.

### Pruebas locales
```sh
node --check site/app.js
node tools/check-public-site.mjs
python -m http.server 8000 --directory site
```
Abrir `http://localhost:8000/`. Comprobar teclado, 320/390/768/1280 px, móvil y enlace `mailto:`; el test automatizado **no sustituye pruebas de navegador**.

### Seguridad y limitaciones
- Prohibido publicar `backend/`, `docs/`, archivos `.env`, credenciales, informes privados o datos de clientes. El artefacto Pages apunta explícitamente a `site/`.
- No hay autenticación, persistencia, endpoint ni producto SaaS en esta interfaz.
- Los estados de la consola son **mock determinista**. Nada del frontend debe utilizarse como prueba de bloqueo de operaciones o protección de datos.
- Sin formulario de captación: contacto por el cliente de correo. No se afirma recepción.
- La beta enero 2027 es solo una **meta condicionada** a seguridad y validación.

### Reversión
Revertir la integración de este PR o deshabilitar Pages en Settings > Pages; retirar el enlace desde MasterTech por su flujo de despliegue independiente. Sin DNS ni backend afectado.
