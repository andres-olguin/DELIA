"""Demo determinista con contrato de resultado (sin API, sin dinero)."""
from __future__ import annotations

import json
from pathlib import Path
from .engine import (
    load_refund_contract, RefundProposal, OrderSnapshot, preflight,
    SettlementObservation, reconcile,
)


def run_demo() -> dict:
    contract = load_refund_contract(Path(__file__).parent / "contracts/commerce_refund_mx_v1.json")
    proposal = RefundProposal("empresa-ficticia", "pedido-001", "refund-001", 1800000, "MXN", 3)
    snapshot = OrderSnapshot("empresa-ficticia", "pedido-001", 3, "paid", 2000000, 0,
                             True, frozenset())
    pre = preflight(contract, proposal, snapshot)
    # Esta observación NO sale de una API, de un medio de pago ni de una base de datos.
    observation = SettlementObservation("empresa-ficticia", "refund-001", proposal.digest,
                                        "confirmed", 1800000)
    post = reconcile(proposal, observation)
    return {
        "mode": "SYNTHETIC_LOCAL_LAB",
        "preflight": pre.outcome,
        "requires_independent_authorization": not pre.is_authorized,
        "reconciliation": post.outcome,
        "real_transaction_executed": False,
        "provider_or_bank_contacted": False,
        "warning": "No garantiza autorización ni verificación reales",
    }


if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2, ensure_ascii=False))
