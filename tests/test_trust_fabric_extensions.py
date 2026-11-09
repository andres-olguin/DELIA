"""Pruebas sintéticas del segundo bloque funcional Trust Fabric."""
import unittest
from datetime import datetime, timedelta, timezone
from decimal import Decimal

from trust_fabric import Action, Policy, PolicyEngine, Rule
from trust_fabric.economics import RevenueScenario
from trust_fabric.evaluation import Scenario, evaluate_scenarios
from trust_fabric.execution import FakeToolEnvironment
from trust_fabric.observatory import aggregate_receipts
from trust_fabric.passport import DataPassport
from trust_fabric.routing import Destination, select_route


class ExtensionTests(unittest.TestCase):
    def setUp(self):
        self.engine = PolicyEngine(b"X"*32, approver_roles=frozenset({"supervisor"}))
        self.engine.register(Policy("t1", 1, (
            Rule("refund_low", "refund.issue", "allow", "worker", max_amount_minor=5000),
            Rule("refund_high", "refund.issue", "approve", "worker", min_amount_minor=5001),
            Rule("read", "invoice.read", "allow", "worker"),
        )))
        self.tools = FakeToolEnvironment(self.engine)

    def act(self, amount, tenant="t1"):
        return Action(tenant, "agent", "worker", "refund.issue",
                      {"amount_minor": amount, "currency": "MXN"})

    def test_no_execution_while_pending(self):
        result = self.tools.invoke(self.act(10000))
        self.assertFalse(result.executed)
        self.assertEqual(result.decision.outcome, "PENDING_APPROVAL")
        self.assertEqual(len(self.tools.synthetic_refunds), 0)

    def test_executed_once_with_approval(self):
        a = self.act(10000)
        pending = self.tools.invoke(a).decision
        self.assertTrue(self.engine.approve(pending.approval_id, tenant_id="t1",
                                            approver_id="human", approver_role="supervisor"))
        self.assertTrue(self.tools.invoke(a, approval_id=pending.approval_id).executed)
        self.assertFalse(self.tools.invoke(a, approval_id=pending.approval_id).executed)
        self.assertEqual(len(self.tools.synthetic_refunds), 1)

    def test_unregistered_tool_does_not_execute(self):
        result = self.tools.invoke(Action("t1", "agent", "worker", "system.delete", {}))
        self.assertFalse(result.executed)

    def test_schema_guard_on_fake_refund(self):
        # Política explícita de lectura, pero herramienta de pago rechaza moneda inválida
        a = Action("t1", "agent", "worker", "refund.issue",
                   {"amount_minor": 5000, "currency": "USD"})
        self.assertFalse(self.tools.invoke(a).executed)

    def test_routing_disallows_wrong_region_and_classification(self):
        endpoints = (Destination("mx_public", "MX", "PUBLIC", True),)
        self.assertEqual(select_route(requested_region="MX", sensitivity="RESTRICTED",
                                      destinations=endpoints).outcome, "DENY")
        self.assertEqual(select_route(requested_region="CL", sensitivity="PUBLIC",
                                      destinations=endpoints).outcome, "DENY")

    def test_routing_only_approved(self):
        e = (Destination("vendor", "MX", "RESTRICTED", False),)
        self.assertEqual(select_route(requested_region="MX", sensitivity="PUBLIC", destinations=e).outcome, "DENY")

    def test_routing_plans_without_network(self):
        e = (Destination("lab", "MX", "INTERNAL", True),)
        self.assertEqual(select_route(requested_region="MX", sensitivity="PUBLIC", destinations=e).outcome, "PLAN_ONLY")

    def test_passport_tenant_and_expiration(self):
        expiry = datetime(2027, 1, 1, tzinfo=timezone.utc)
        p = DataPassport("t1", "INTERNAL", frozenset({"support"}), expiry)
        self.assertTrue(p.allows(tenant_id="t1", purpose="support", now=expiry - timedelta(days=1)))
        self.assertFalse(p.allows(tenant_id="t2", purpose="support", now=expiry - timedelta(days=1)))
        self.assertFalse(p.allows(tenant_id="t1", purpose="support", now=expiry))

    def test_passport_cannot_expand_purpose(self):
        p = DataPassport("t1", "CONFIDENTIAL", frozenset({"support"}),
                         datetime(2027, 1, 1, tzinfo=timezone.utc))
        with self.assertRaises(ValueError):
            p.derive(purpose_subset=frozenset({"support","marketing"}),
                     classification="CONFIDENTIAL", expires_at=p.expires_at)

    def test_passport_cannot_reduce_classification(self):
        p = DataPassport("t1", "CONFIDENTIAL", frozenset({"support"}),
                         datetime(2027, 1, 1, tzinfo=timezone.utc))
        with self.assertRaises(ValueError):
            p.derive(purpose_subset=frozenset({"support"}),
                     classification="PUBLIC", expires_at=p.expires_at)

    def test_observatory_no_original_arguments(self):
        self.engine.decide(Action("t1", "agent", "worker", "invoice.read", {"secret": "VERY-SENSITIVE-STRING"}))
        report = aggregate_receipts(self.engine.receipts)
        self.assertNotIn("VERY-SENSITIVE-STRING", repr(report))
        self.assertEqual(report["total_decisions"], 1)

    def test_red_team_synthetic(self):
        cases = (
            Scenario("deny", Action("t1", "agent", "worker", "system.delete", {}), "DENY"),
            Scenario("allow", Action("t1", "agent", "worker", "invoice.read", {}), "ALLOW"),
        )
        result = evaluate_scenarios(self.engine, cases)
        self.assertEqual(result["passed"], 2)
        self.assertEqual(result["failed"], 0)

    def test_economic_scenario_is_hypothetical(self):
        p = RevenueScenario(30, Decimal("499"), Decimal("0.75"), Decimal("8000"))
        result = p.calculate()
        self.assertEqual(result["mrr_usd"], "14970")
        self.assertEqual(result["annualized_run_rate_usd"], "179640")
        self.assertIn("HIPÓTESIS", result["label"])

    def test_bad_economic_assumptions(self):
        with self.assertRaises(ValueError):
            RevenueScenario(-1, Decimal("499"), Decimal("0.75"), Decimal("0")).calculate()

    def test_unknown_classification_rejected(self):
        self.assertEqual(select_route(requested_region="MX", sensitivity="SECRET",
                                      destinations=()).outcome, "DENY")


if __name__ == "__main__":
    unittest.main()
