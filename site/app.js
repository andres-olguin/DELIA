'use strict';
/*
 * Public DELIA demo: predetermined fictional examples. No backend, tracking,
 * external requests or user-supplied data. Not a security enforcement engine.
 */
const scenarios = Object.freeze({
  allowed: {
    agent: '"crm_assistant_demo"',
    action: '"crm.read_synthetic"',
    policy: '"read_only_demo"',
    evidence: '"synthetic_record_exists"',
    badge: 'PERMITIDO / MOCK',
    title: 'Consulta ilustrativa autorizada',
    description: 'Una política ficticia permite leer un registro de prueba. No se consulta ningún CRM real.'
  },
  denied: {
    agent: '"crm_assistant_demo"',
    action: '"crm.delete_contact"',
    policy: '"deny_destructive_demo"',
    evidence: '"no_operation_executed"',
    badge: 'DENEGADO / MOCK',
    title: 'Acción de prueba denegada',
    description: 'La regla simulada no autoriza eliminar un contacto. Esta pantalla no ejecuta acciones y no acredita bloqueo técnico real.'
  },
  unknown: {
    agent: '"support_agent_demo"',
    action: '"ticket.update_status"',
    policy: '"requires_verification_demo"',
    evidence: '"authoritative_result_missing"',
    badge: 'SIN VERIFICAR / MOCK',
    title: 'Resultado no comprobado',
    description: 'El ejemplo carece de evidencia fiable del estado final. No debería presentarse como éxito aunque el agente diga haber terminado.'
  }
});

const fields = {
  agent: document.getElementById('example-agent'),
  action: document.getElementById('example-action'),
  policy: document.getElementById('example-policy'),
  evidence: document.getElementById('example-evidence'),
  badge: document.getElementById('decision-badge'),
  title: document.getElementById('decision-title'),
  description: document.getElementById('decision-description')
};
const scenarioButtons = [...document.querySelectorAll('[data-scenario]')];
function selectScenario(id) {
  const data = scenarios[id];
  if (!data) return;
  for (const key of ['agent','action','policy','evidence']) fields[key].textContent = data[key];
  fields.badge.textContent = data.badge;
  fields.badge.className = 'decision-badge ' + id;
  fields.title.textContent = data.title;
  fields.description.textContent = data.description;
  scenarioButtons.forEach(button => button.setAttribute('aria-pressed', String(button.dataset.scenario === id)));
}
scenarioButtons.forEach(button => button.addEventListener('click', () => selectScenario(button.dataset.scenario)));

const toggle = document.getElementById('nav-toggle');
const mobileNav = document.getElementById('mobile-nav');
function closeNav() {
  toggle.setAttribute('aria-expanded', 'false');
  mobileNav.hidden = true;
}
toggle.addEventListener('click', () => {
  const open = toggle.getAttribute('aria-expanded') !== 'true';
  toggle.setAttribute('aria-expanded', String(open));
  mobileNav.hidden = !open;
});
mobileNav.querySelectorAll('a').forEach(link => link.addEventListener('click', closeNav));
document.addEventListener('keydown', event => {
  if (event.key === 'Escape') closeNav();
});
