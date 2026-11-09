"""Pruebas de los cuatro packs sintéticos; no constituye seguridad productiva."""
import unittest

from trust_fabric.policy import Action, PolicyEngine, PolicyError
from trust_fabric.sector_packs import PACK_IDS, load_pack, pack_metadata
from trust_fabric.packs_demo import run


class SectorPackTests(unittest.TestCase):
    def setUp(self):
        self.engine = PolicyEngine(b"X"*32, approver_roles=frozenset({"supervisor"}))
        for name in PACK_IDS:
            self.engine.register(load_pack(name))

    def action(self, pack, tool, role, data=None):
        return Action("demo_"+pack, "agent-demo", role, tool, data or {})

    def test_all_four_packs_present(self):
        self.assertEqual(PACK_IDS, frozenset({"commerce","contact_center","integrators","saas_b2b"}))

    def test_each_pack_has_deny_by_default(self):
        for name in PACK_IDS:
            self.assertEqual(load_pack(name).default_effect, "deny")
            self.assertEqual(self.engine.decide(self.action(name,"system.root","agent")).outcome,"DENY")

    def test_commerce_low_refund_allowed(self):
        a = self.action("commerce","refund.issue","support",{"amount_minor":1000000,"currency":"MXN"})
        self.assertEqual(self.engine.decide(a).outcome,"ALLOW")

    def test_commerce_high_refund_requires_approval(self):
        a = self.action("commerce","refund.issue","support",{"amount_minor":1000001,"currency":"MXN"})
        self.assertEqual(self.engine.decide(a).outcome,"PENDING_APPROVAL")

    def test_commerce_order_delete_denied(self):
        self.assertEqual(self.engine.decide(self.action("commerce","orders.delete","support")).outcome,"DENY")

    def test_bpo_ticket_read_allowed(self):
        self.assertEqual(self.engine.decide(self.action("contact_center","cases.read","agent")).outcome,"ALLOW")

    def test_bpo_contact_export_denied(self):
        self.assertEqual(self.engine.decide(self.action("contact_center","contact.export","agent")).outcome,"DENY")

    def test_bpo_contact_change_requires_approval(self):
        self.assertEqual(self.engine.decide(self.action("contact_center","customer.update","agent")).outcome,"PENDING_APPROVAL")

    def test_integrator_secrets_export_denied(self):
        self.assertEqual(self.engine.decide(self.action("integrators","secrets.export","consultant")).outcome,"DENY")

    def test_integrator_tenant_cannot_use_saas_policy(self):
        self.assertEqual(self.engine.decide(self.action("integrators","records.read","service_agent")).outcome,"DENY")

    def test_saas_b2b_read_allowed(self):
        self.assertEqual(self.engine.decide(self.action("saas_b2b","records.read","service_agent")).outcome,"ALLOW")

    def test_saas_b2b_keys_export_denied(self):
        self.assertEqual(self.engine.decide(self.action("saas_b2b","keys.export","service_agent")).outcome,"DENY")

    def test_unknown_pack_rejected(self):
        with self.assertRaises(PolicyError):
            load_pack("../../etc/passwd")

    def test_pack_metadata_not_shipped(self):
        self.assertTrue(all(pack_metadata(i)["not_production"] for i in PACK_IDS))

    def test_demo_has_no_external_execution(self):
        results = run()
        self.assertEqual(len(results["packs"]), 4)
        self.assertTrue(all(p["no_external_execution"] for p in results["packs"]))
        self.assertTrue(all(p["receipt_verified"] for p in results["packs"]))


if __name__ == "__main__":
    unittest.main()
