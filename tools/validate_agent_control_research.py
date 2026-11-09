"""Validador estático de integridad de investigación, NO prueba de seguridad.

Nunca accede a red, datos reales, ejecutores ni agentes. Los resultados de esta
validación solo demuestran estructura y comunicación prudente del manifiesto.
"""
from __future__ import annotations
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/research/agent-control/controls-research-matrix.json"
EVIDENCE_STATES = {"PLANNED", "LAB_SYNTHETIC", "RESEARCH", "E2E_VERIFIED", "EXTERNALLY_REVIEWED"}
PRIORITIES = {"P0", "P1", "P2", "P3"}
_ID = re.compile(r"^AC-\d{2}$")


def validate(path: Path = SOURCE) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema_version") != "1.0":
        raise ValueError("Schema desconocido")
    date.fromisoformat(data["reviewed_at"])
    if data.get("assessment_type") != "THREAT_MODEL_AND_TEST_PLAN":
        raise ValueError("No es un plan de investigación válido")
    for k in ("product_ready", "mitigates_extinction", "security_certified"):
        if data.get(k) is not False:
            raise ValueError(f"Claim no acreditado: {k}")
    if not isinstance(data.get("frameworks"), list) or len(data["frameworks"]) < 5:
        raise ValueError("Sin fuentes primarias suficientes")
    urls = set()
    for x in data["frameworks"]:
        url = x.get("uri", "")
        if not url.startswith("https://") or url in urls:
            raise ValueError("Fuente insegura o duplicada")
        urls.add(url)
        if not x.get("name"):
            raise ValueError("Fuente sin nombre")
    risks = data.get("risks")
    if not isinstance(risks, list) or len(risks) < 10:
        raise ValueError("Matriz insuficiente")
    ids = set()
    for x in risks:
        i = x.get("id", "")
        if not _ID.fullmatch(i) or i in ids:
            raise ValueError("ID de riesgo inválido o duplicado")
        ids.add(i)
        for k in ("name", "attack_or_failure", "control_hypothesis", "test_design", "business_domain"):
            if not isinstance(x.get(k), str) or len(x[k].strip()) < 12:
                raise ValueError(f"{i} sin campo obligatorio {k}")
        if x.get("priority") not in PRIORITIES or x.get("evidence_state") not in EVIDENCE_STATES:
            raise ValueError(f"{i} prioridad/estado incorrecto")
        if x.get("claim") != "PLANNED_OR_LAB_ONLY":
            raise ValueError("Claim de producción no permitido en esta versión")
        if x.get("owner") != "UNASSIGNED":
            raise ValueError("El plan no puede asignar personas sin consentimiento")
    dates = [date.fromisoformat(m["date"]) for m in data.get("milestones", [])]
    if not dates or dates != sorted(dates):
        raise ValueError("Hitos sin fechas válidas o desordenados")
    return {"risk_scenarios": len(risks), "sources": len(urls),
            "p0_planned": sum(1 for x in risks if x["priority"] == "P0"
                              and x["evidence_state"] != "E2E_VERIFIED"),
            "production_claims_valid": True}


if __name__ == "__main__":
    print(json.dumps({"mode": "STRUCTURE_ONLY_NOT_SECURITY_ASSURANCE", **validate()},
                     indent=2))
