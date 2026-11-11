# Claude Code — DELIA

Antes de ejecutar tareas, leer `AGENTS.md`, `README.md`, el sprint activo y la [norma transversal MTS-ENG-001](https://github.com/andres-olguin/mastertech-corporate-governance/blob/main/docs/engineering/MULTIAGENT_WORKTREES.md).

**Worktree objetivo:** `MasterTech/<nombre-del-repo>/claude/`, como hermano de `main/`, `codex/` y `antigravity/`; un único repositorio Git con ramas independientes. Este es un **diseño futuro** hasta que los paths locales estén verificados; no crear/mover/borrar worktrees existentes a ciegas.

Claude Code prioriza arquitectura, QA, seguridad y revisión cruzada, pero la asignación por issue/sprint tiene preferencia. Acordar contratos y archivos bajo control antes de programar, compartir handoff (SHA, archivos, pruebas, riesgos, pendientes) y crear PR revisable; no integrar/desplegar automáticamente.

**Reglas particulares:** No afirmar que el proxy, DLP, autenticación o aislamiento multi-tenant son productivos sin pruebas reproducibles. No exponer credenciales, datos reales de clientes o prompts privados. Tratar cambios de autorización y seguridad como críticos.

La existencia de este archivo no implica que Claude esté instalado, autenticado o ejecutándose, ni que la norma central esté ya fusionada con `main`.
