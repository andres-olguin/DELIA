"""Demo extendida de controles locales sin servicios ni datos reales."""
import json
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from .economics import RevenueScenario
from .evaluation import Scenario, evaluate_scenarios
from .execution import FakeToolEnvironment
from .observatory import aggregate_receipts
from .passport import DataPassport
from .policy import Action, Policy, PolicyEngine, Rule
from .routing import Destination, select_route


def run_lab() -> dict:
    engine = PolicyEngine(b"LAB-KEY-IS-NOT-A-PRODUCTION-SECRET-0001",
                          approver_roles=frozenset({"supervisor"}))
    engine.register(Policy("LAB_MX", 1, (
        Rule("read", "invoice.read", "allow", "operator"),
        Rule("refund_low", "refund.issue", "allow", "operator", max_amount_minor=1_000_000),
        Rule("refund_high", "refund.issue", "approve", "operator", min_amount_minor=1_000_001),
        Rule("delete", "invoice.delete", "deny", "operator"),
    )))
    tool_env = FakeToolEnvironment(engine)
    action = Action("LAB_MX", "robot", "operator", "refund.issue",
                    {"amount_minor": 1_800_000, "currency": "MXN"})
    pending = tool_env.invoke(action)
    no_execution_before_approval = len(tool_env.synthetic_refunds) == 0
    approved = engine.approve(pending.decision.approval_id, tenant_id="LAB_MX",
                              approver_id="human", approver_role="supervisor")
    executed = tool_env.invoke(action, approval_id=pending.decision.approval_id)
    replay = tool_env.invoke(action, approval_id=pending.decision.approval_id)
    scenarios = (
        Scenario("bloqueo desconocido", Action("LAB_MX", "robot", "operator", "system.delete", {}), "DENY"),
        Scenario("sin política", Action("OTHER", "robot", "operator", "invoice.read", {}), "DENY"),
        Scenario("lectura permitida", Action("LAB_MX", "robot", "operator", "invoice.read", {}), "ALLOW"),
    )
    p = DataPassport("LAB_MX", "CONFIDENTIAL", frozenset({"invoicing", "audit"}),
                     datetime(2027, 1, 1, tzinfo=timezone.utc))
    route = select_route(requested_region="mx-central", sensitivity="CONFIDENTIAL",
                         destinations=(Destination("externo_no_aprobado", "mx-central", "RESTRICTED", False),
                                       Destination("modelo_local_demo", "mx-central", "CONFIDENTIAL", True)))
    revenue = RevenueScenario(30, Decimal("499"), Decimal("0.75"), Decimal("8000")).calculate()
    return {
        "label": "DEMOSTRACIÓN DE LABORATORIO, SIN PROTECCIÓN REAL",
        "approval_human_simulated": approved,
        "blocked_before": no_execution_before_approval,
        "executed_fake": executed.executed,
        "replay_denied": not replay.executed,
        "refunds_fake": len(tool_env.synthetic_refunds),
        "policy_evaluation": evaluate_scenarios(engine, scenarios),
        "passports": {"purpose_allow": p.allows(tenant_id="LAB_MX", purpose="audit",
                      now=datetime(2026, 11, 9, tzinfo=timezone.utc))},
        "route": route.__dict__,
        "observatory": aggregate_receipts(engine.receipts),
        "revenue": revenue,
    }


if __name__ == "__main__":
    print(json.dumps(run_lab(), ensure_ascii=False, indent=2))
