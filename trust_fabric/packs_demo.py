"""Recorre cuatro packs sectoriales de DELIA sin herramientas ni conexión externa."""
import json

from .policy import Action, PolicyEngine
from .sector_packs import PACK_IDS, load_pack, pack_metadata


def run() -> dict:
    examples = {
        "commerce": ("support", "refund.issue", {"amount_minor": 1800000, "currency": "MXN"}),
        "contact_center": ("agent", "contact.export", {"sample": "FAKE-001"}),
        "integrators": ("consultant", "crm.write", {"record": "FAKE-001"}),
        "saas_b2b": ("service_agent", "records.read", {"record": "FAKE-001"}),
    }
    engine = PolicyEngine(b"sector-packs-LAB-only-never-use-this-key-for-prod", approver_roles=frozenset({"lab_supervisor"}))
    response = []
    for name in sorted(PACK_IDS):
        policy = load_pack(name)
        engine.register(policy)
        role, tool, args = examples[name]
        action = Action(policy.tenant_id, "demo_agent", role, tool, args)
        result = engine.decide(action)
        response.append({**pack_metadata(name), "example_tool": tool, "decision": result.outcome,
                         "receipt_verified": engine.verify(result.receipt),
                         "no_external_execution": True})
    return {"mode": "LAB_SIMULATION_ONLY", "packs": response}


if __name__ == "__main__":
    print(json.dumps(run(), ensure_ascii=False, indent=2))
