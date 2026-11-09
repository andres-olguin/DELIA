"""Pruebas independientes de dependencias externas. Ejecutar: python -m unittest tests.test_trust_fabric -v"""
import dataclasses
import unittest
from datetime import datetime, timedelta, timezone

from trust_fabric import Action, Policy, PolicyEngine, PolicyError, Rule


class TrustFabricTests(unittest.TestCase):
    def setUp(self):
        self.t = datetime(2026, 11, 9, tzinfo=timezone.utc)
        self.engine = PolicyEngine(b"x" * 32, approver_roles=frozenset({"security_admin"}),
                                   clock=lambda: self.t, approval_ttl_seconds=120)
        self.policy = Policy("tenant_A", 1, (
            Rule("allow_low", "refund.issue", "allow", "operator", max_amount_minor=1000000),
            Rule("review_high", "refund.issue", "approve", "operator", min_amount_minor=1000001),
            Rule("deny_delete", "invoice.delete", "deny", "operator"),
            Rule("allow_read", "invoice.read", "allow", "operator"),
        ))
        self.engine.register(self.policy)

    def act(self, amount=1800000, tenant="tenant_A", agent="robot_A", tool="refund.issue"):
        return Action(tenant, agent, "operator", tool, {"amount_minor": amount, "currency": "MXN"})

    def test_default_deny_unlisted_tool(self):
        self.assertEqual(self.engine.decide(self.act(tool="payment.transfer")).outcome, "DENY")

    def test_missing_tenant_deny(self):
        self.assertEqual(self.engine.decide(self.act(tenant="tenant_B")).outcome, "DENY")

    def test_allow_low_value(self):
        self.assertTrue(self.engine.decide(self.act(1000000)).may_execute)

    def test_approval_high_value(self):
        decision = self.engine.decide(self.act(1000001))
        self.assertEqual(decision.outcome, "PENDING_APPROVAL")
        self.assertFalse(decision.may_execute)

    def test_same_agent_cannot_self_approve(self):
        ticket = self.engine.decide(self.act()).approval_id
        self.assertFalse(self.engine.approve(ticket, tenant_id="tenant_A", approver_id="robot_A",
                                             approver_role="security_admin"))

    def test_wrong_role_cannot_approve(self):
        ticket = self.engine.decide(self.act()).approval_id
        self.assertFalse(self.engine.approve(ticket, tenant_id="tenant_A", approver_id="human",
                                             approver_role="operator"))

    def test_cross_tenant_approval_denied(self):
        ticket = self.engine.decide(self.act()).approval_id
        self.assertFalse(self.engine.approve(ticket, tenant_id="tenant_B", approver_id="human",
                                             approver_role="security_admin"))

    def test_approval_bound_to_exact_arguments(self):
        ticket = self.engine.decide(self.act()).approval_id
        self.assertTrue(self.engine.approve(ticket, tenant_id="tenant_A",
                                            approver_id="human", approver_role="security_admin"))
        self.assertEqual(self.engine.decide(self.act(1800001), approval_id=ticket).outcome, "DENY")

    def test_approval_single_use(self):
        action = self.act()
        ticket = self.engine.decide(action).approval_id
        self.assertTrue(self.engine.approve(ticket, tenant_id="tenant_A",
                                            approver_id="human", approver_role="security_admin"))
        self.assertEqual(self.engine.decide(action, approval_id=ticket).outcome, "ALLOW")
        self.assertEqual(self.engine.decide(action, approval_id=ticket).outcome, "DENY")

    def test_expired_approval_denied(self):
        action = self.act()
        ticket = self.engine.decide(action).approval_id
        self.t = self.t + timedelta(minutes=3)
        self.assertFalse(self.engine.approve(ticket, tenant_id="tenant_A",
                                             approver_id="human", approver_role="security_admin"))

    def test_policy_change_invalidates_approval(self):
        action = self.act()
        ticket = self.engine.decide(action).approval_id
        self.engine.register(Policy("tenant_A", 2, self.policy.rules))
        self.assertFalse(self.engine.approve(ticket, tenant_id="tenant_A",
                                             approver_id="human", approver_role="security_admin"))

    def test_invalid_policy_versions(self):
        with self.assertRaises(PolicyError):
            self.engine.register(Policy("tenant_A", 1, self.policy.rules))

    def test_invalid_json_arguments(self):
        with self.assertRaises(PolicyError):
            Action("tenant_A", "robot_A", "operator", "tool", {"x": float("nan")})

    def test_denial_precedes_allow(self):
        engine = PolicyEngine(b"x"*32, approver_roles=frozenset({"security_admin"}))
        engine.register(Policy("tenant_A", 1, (Rule("one", "invoice.read", "allow", "operator"),
                                               Rule("two", "invoice.read", "deny", "operator"))))
        self.assertEqual(engine.decide(self.act(tool="invoice.read")).outcome, "DENY")

    def test_receipt_integrity(self):
        receipt = self.engine.decide(self.act()).receipt
        self.assertTrue(self.engine.verify(receipt))
        changed = dataclasses.replace(receipt, outcome="ALLOW")
        self.assertFalse(self.engine.verify(changed))

    def test_no_raw_arguments_in_receipts(self):
        action = Action("tenant_A", "robot_A", "operator", "invoice.read",
                        {"document": "SECRETO-PRUEBA-NO-ALMACENAR"})
        decision = self.engine.decide(action)
        self.assertNotIn("SECRETO-PRUEBA-NO-ALMACENAR", repr(decision.receipt))
        self.assertNotIn("SECRETO-PRUEBA-NO-ALMACENAR", repr(self.engine.receipts))

    def test_missing_amount_does_not_match_threshold(self):
        action = Action("tenant_A", "robot_A", "operator", "refund.issue", {"currency": "MXN"})
        self.assertEqual(self.engine.decide(action).outcome, "DENY")

    def test_wrong_tool_does_not_use_approval(self):
        action = self.act()
        ticket = self.engine.decide(action).approval_id
        self.assertTrue(self.engine.approve(ticket, tenant_id="tenant_A",
                                            approver_id="human", approver_role="security_admin"))
        self.assertEqual(self.engine.decide(self.act(tool="invoice.delete"), approval_id=ticket).outcome, "DENY")


if __name__ == "__main__":
    unittest.main()
