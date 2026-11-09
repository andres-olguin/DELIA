import assert from 'node:assert/strict';
import { readFileSync, existsSync } from 'node:fs';
import { resolve } from 'node:path';

const root = resolve(import.meta.dirname, '..');
const read = (path) => readFileSync(resolve(root, path), 'utf8');
const required = ['site/index.html', 'site/styles.css', 'site/app.js', 'site/favicon.svg'];
for (const path of required) assert.ok(existsSync(resolve(root, path)), 'Missing: ' + path);
const html = read('site/index.html');
const js = read('site/app.js');
const css = read('site/styles.css');
assert.match(html, /<html lang="es-CL">/);
assert.match(html, /<meta name="viewport"/);
assert.match(html, /<main id="contenido">/);
assert.match(html, /href="\.\/styles\.css"/);
assert.match(html, /src="\.\/app\.js"/);
assert.match(html, /PROYECTO EN INVESTIGACIÓN Y DESARROLLO/);
assert.match(html, /Simulación educativa/);
assert.match(html, /no está certificado ni listo/);
assert.match(html, /mailto:contact@mastertechg\.com/);
assert.ok(!/<form[\s>]/i.test(html), 'No dead form or falsely implied collection');
for (const id of ['enfoque', 'laboratorio', 'roadmap', 'preguntas', 'inicio']) {
  assert.ok(html.includes('id="' + id + '"'), 'Missing anchor: ' + id);
}
for (const scenario of ['allowed', 'denied', 'unknown']) {
  assert.ok(html.includes('data-scenario="' + scenario + '"'), 'Missing tab ' + scenario);
  assert.ok(js.includes(scenario + ': {'), 'Missing example ' + scenario);
}
assert.ok(!/\b(fetch|XMLHttpRequest|WebSocket|sendBeacon|localStorage|sessionStorage)\b/.test(js), 'Public demo must not call networks or store data');
assert.match(css, /prefers-reduced-motion/);
assert.match(css, /focus-visible/);
console.log('PASS: DELIA public site, three mocked scenarios, route anchors, basic accessibility and isolation');
