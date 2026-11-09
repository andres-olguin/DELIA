"""Test de inventario de investigación: NO valida controles en ejecución."""
import json
import tempfile
import unittest
from pathlib import Path
from tools.validate_agent_control_research import SOURCE, validate


class ResearchIntegrityTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(SOURCE.read_text(encoding="utf-8"))

    def with_manifest(self, data):
        with tempfile.TemporaryDirectory() as temp:
            file = Path(temp) / "manifest.json"
            file.write_text(json.dumps(data), encoding="utf-8")
            return validate(file)

    def test_original_is_structurally_valid(self):
        output = validate()
        self.assertGreaterEqual(output["risk_scenarios"], 14)
        self.assertTrue(output["production_claims_valid"])

    def test_cannot_claim_product_ready(self):
        self.data["product_ready"] = True
        with self.assertRaises(ValueError):
            self.with_manifest(self.data)

    def test_cannot_claim_certification(self):
        self.data["security_certified"] = True
        with self.assertRaises(ValueError):
            self.with_manifest(self.data)

    def test_cannot_claim_extinction_mitigation(self):
        self.data["mitigates_extinction"] = True
        with self.assertRaises(ValueError):
            self.with_manifest(self.data)

    def test_duplicate_risk_rejected(self):
        self.data["risks"].append(self.data["risks"][0])
        with self.assertRaises(ValueError):
            self.with_manifest(self.data)

    def test_no_fake_e2e_claim_in_this_version(self):
        self.data["risks"][0]["claim"] = "PRODUCTION_SAFE"
        with self.assertRaises(ValueError):
            self.with_manifest(self.data)

    def test_unapproved_ownership_rejected(self):
        self.data["risks"][0]["owner"] = "Person A"
        with self.assertRaises(ValueError):
            self.with_manifest(self.data)

    def test_empty_test_design_rejected(self):
        self.data["risks"][0]["test_design"] = ""
        with self.assertRaises(ValueError):
            self.with_manifest(self.data)

    def test_invalid_evidence_state_rejected(self):
        self.data["risks"][0]["evidence_state"] = "CERTIFIED"
        with self.assertRaises(ValueError):
            self.with_manifest(self.data)

    def test_duplicate_sources_rejected(self):
        self.data["frameworks"][1]["uri"] = self.data["frameworks"][0]["uri"]
        with self.assertRaises(ValueError):
            self.with_manifest(self.data)

    def test_unsorted_milestones_rejected(self):
        self.data["milestones"].reverse()
        with self.assertRaises(ValueError):
            self.with_manifest(self.data)

    def test_risk_p0_gaps_are_visible(self):
        report = validate()
        self.assertGreater(report["p0_planned"], 0)


if __name__ == "__main__":
    unittest.main()
