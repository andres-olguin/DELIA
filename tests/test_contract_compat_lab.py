"""Purely mocked conformance: never an assertion of production security."""
import unittest
from copy import deepcopy
from pathlib import Path
from tempfile import TemporaryDirectory
import json
from competitive_assurance.compat_lab import (
    SOURCE_MODE, load_contract, compare_mock, summarize_mock,
)
from competitive_assurance.demo import run_demo


class MockContractTests(unittest.TestCase):
    def setUp(self):
        self.contract = load_contract(
            Path("docs/competitive-assurance/contracts/ticketing_v1.json"))
        self.report = {
            "mode": SOURCE_MODE, "adapter_name": "mock-unit-test",
            "cases": [{
                "id": c["id"], "tenant_id": c["tenant_id"],
                "tool": c["tool"], "decision": c["expected_decision"],
                "observed_effect": False
            } for c in self.contract["cases"]],
        }

    def mutate(self, cid, **updates):
        report = deepcopy(self.report)
        item = next(x for x in report["cases"] if x["id"] == cid)
        item.update(updates)
        return report

    def status(self, report, cid):
        return next(x for x in compare_mock(self.contract, report)
                    if x.case_id == cid)

    def test_fixture_has_10_cases(self):
        self.assertEqual(len(self.contract["cases"]), 10)

    def test_all_matches_are_simulated_only(self):
        x = summarize_mock(self.contract, self.report)
        self.assertEqual(x["counts"]["MATCH_SIMULATED"], 10)
        self.assertTrue(x["all_observations_consistent_with_fixture"])
        self.assertFalse(x["real_vendor_tested"])
        self.assertFalse(x["external_effects_observed"])

    def test_deny_mismatch_is_violation(self):
        x = self.status(self.mutate("export_a", decision="ALLOW"), "export_a")
        self.assertEqual(x.status, "CONTRACT_VIOLATION")
        self.assertIn("DECISION_MISMATCH", x.reasons)

    def test_deny_with_effect_is_violation(self):
        x = self.status(self.mutate("export_a", observed_effect=True), "export_a")
        self.assertIn("UNAUTHORIZED_MOCK_EFFECT", x.reasons)

    def test_review_with_effect_is_violation(self):
        x = self.status(self.mutate("update_a", observed_effect=True), "update_a")
        self.assertEqual(x.status, "CONTRACT_VIOLATION")

    def test_cross_tenant_allow_is_violation(self):
        x = self.status(self.mutate("cross_tenant", decision="ALLOW"), "cross_tenant")
        self.assertEqual(x.status, "CONTRACT_VIOLATION")

    def test_wrong_tenant_context_is_violation(self):
        x = self.status(self.mutate("read_a", tenant_id="tenant-B"), "read_a")
        self.assertIn("CASE_CONTEXT_MISMATCH", x.reasons)

    def test_wrong_tool_context_is_violation(self):
        x = self.status(self.mutate("read_a", tool="contacts.export"), "read_a")
        self.assertEqual(x.status, "CONTRACT_VIOLATION")

    def test_unknown_decision_is_indeterminate(self):
        x = self.status(self.mutate("read_a", decision="UNKNOWN"), "read_a")
        self.assertEqual(x.status, "INDETERMINATE")

    def test_nonboolean_effect_is_indeterminate(self):
        x = self.status(self.mutate("read_a", observed_effect="not known"), "read_a")
        self.assertEqual(x.status, "INDETERMINATE")

    def test_missing_effect_is_indeterminate(self):
        report = deepcopy(self.report)
        report["cases"][0].pop("observed_effect")
        self.assertEqual(self.status(report, "read_a").status, "INDETERMINATE")

    def test_missing_case_is_indeterminate(self):
        report = deepcopy(self.report)
        report["cases"] = [x for x in report["cases"] if x["id"] != "cross_tenant"]
        self.assertEqual(self.status(report, "cross_tenant").status, "INDETERMINATE")

    def test_duplicate_response_fails(self):
        report = deepcopy(self.report)
        report["cases"].append(deepcopy(report["cases"][0]))
        with self.assertRaises(ValueError):
            compare_mock(self.contract, report)

    def test_unexpected_response_fails(self):
        report = deepcopy(self.report)
        report["cases"].append({"id":"new","tenant_id":"tenant-A","tool":"read",
                                "decision":"ALLOW","observed_effect":False})
        with self.assertRaises(ValueError):
            compare_mock(self.contract, report)

    def test_real_adapter_masquerading_rejected(self):
        report = deepcopy(self.report)
        report["mode"] = "PRODUCTION_ENFORCEMENT"
        with self.assertRaises(ValueError):
            compare_mock(self.contract, report)

    def test_duplicate_contract_case_rejected(self):
        contract = deepcopy(self.contract)
        contract["cases"].append(deepcopy(contract["cases"][0]))
        with TemporaryDirectory() as root:
            p = Path(root) / "contract.json"
            p.write_text(json.dumps(contract), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_contract(p)

    def test_contract_cannot_claim_production(self):
        contract = deepcopy(self.contract)
        contract["mode"] = "REAL_GATEWAY"
        with TemporaryDirectory() as root:
            p = Path(root) / "contract.json"
            p.write_text(json.dumps(contract), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_contract(p)

    def test_demo_detects_violation_and_gap(self):
        x = run_demo()
        a, b = x["mock_adapters"]
        self.assertFalse(x["real_vendor_tested"])
        self.assertEqual(a["counts"]["CONTRACT_VIOLATION"],1)
        self.assertEqual(b["counts"]["INDETERMINATE"],1)

    def test_no_real_call_guarantee(self):
        x = run_demo()
        self.assertFalse(x["real_external_tools_called"])
        self.assertEqual(x["mode"],SOURCE_MODE)


if __name__=="__main__":
    unittest.main()
