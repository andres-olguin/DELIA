"""Demo sintética: python -m trust_fabric.demo (sin conexiones ni claves reales)."""
import json
from dataclasses import asdict

from .policy import Action, Policy, PolicyEngine, Rule


def run_demo() -> dict:
    engine = PolicyEngine(b"demo-only-never-use-in-production-32-byte-key", approver_roles=frozenset({"supervisor"}))
    engine.register(Policy("empresa_demo_mx", 1, (
        Rule("r1", "invoice.read", "allow", "operator"),
        Rule("r2", "refund.issue", "allow", "operator", max_amount_minor=1_000_000),
        Rule("r3", "refund.issue", "approve", "operator", min_amount_minor=1_000_001),
        Rule("r4", "invoice.delete", "deny", "operator"),
    )))
    action = Action("empresa_demo_mx", "agente_demo", "operator", "refund.issue",
                    {"amount_minor": 1_800_000, "currency": "MXN", "invoice": "FAKE-001"})
    pending = engine.decide(action)
    approved = engine.approve(pending.approval_id, tenant_id="empresa_demo_mx",
                              approver_id="supervisor_humano_demo", approver_role="supervisor")
    accepted = engine.decide(action, approval_id=pending.approval_id)
    replay = engine.decide(action, approval_id=pending.approval_id)
    return {
        "modo": "SIMULACION SIN TRANSACCIONES",
        "antes": pending.outcome,
        "aprobacion_humana_simulada": approved,
        "despues": accepted.outcome,
        "reutilizacion": replay.outcome,
        "integridad_recibo": engine.verify(accepted.receipt),
        "no_ejecuta_herramientas": True,
        "comprobante": asdict(accepted.receipt),
    }


if __name__ == "__main__":
    print(json.dumps(run_demo(), ensure_ascii=False, indent=2))
