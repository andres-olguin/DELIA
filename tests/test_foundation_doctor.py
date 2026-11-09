"""Read-only foundation gate tests; no external network or production execution."""
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

from tools.foundation_doctor import ROOT, MANIFEST, evaluate, static_signals, main


class FoundationDoctorTests(unittest.TestCase):
    def setUp(self):
        self.doc = json.loads(MANIFEST.read_text(encoding="utf-8"))

    def check(self, doc):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "ledger.json"
            path.write_text(json.dumps(doc), encoding="utf-8")
            return evaluate(ROOT, path)

    def test_baseline_is_blocked_not_ready(self):
        report = evaluate()
        self.assertEqual(report["production_gateway"], "BLOCKED")
        self.assertFalse(report["production_release_authorized"])
        self.assertEqual(report["partner_saas"], "BLOCKED")
        self.assertEqual(report["controls_total"], 13)

    def test_static_flags_known_current_risks(self):
        signals = {x["id"] for x in static_signals()}
        for required in ("RAW_UPSTREAM_PAYLOAD",
                         "UNSANITIZED_FORWARD_CALL", "AUDIT_AUTH_ABSENT",
                         "RAW_PROMPT_LOG", "AUDIT_SCHEMA_MISMATCH",
                         "UPSTREAM_TOKEN_PASSTHROUGH",
                         "HARDCODED_DATABASE_PASSWORD", "MIGRATION_BYPASS"):
            self.assertIn(required, signals)

    def test_static_flags_broken_import_until_module_exists(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            route = root / "app/api/proxy.py"
            route.parent.mkdir(parents=True)
            route.write_text("from app.models.chat import ChatRequest\n", encoding="utf-8")

            broken_imports = [signal["path"] for signal in static_signals(root)
                              if signal["id"] == "BROKEN_IMPORT"]
            self.assertEqual(broken_imports, ["app/api/proxy.py"])

            module = root / "app/models/chat.py"
            module.parent.mkdir(parents=True)
            module.write_text("class ChatRequest:\n    pass\n", encoding="utf-8")
            self.assertNotIn("BROKEN_IMPORT", {signal["id"] for signal in static_signals(root)})

    def test_no_customer_claim_from_lab(self):
        self.assertEqual(evaluate()["research_demo"], "SYNTHETIC_ONLY")
        self.assertEqual(evaluate()["professional_diagnostic"],
                         "CONDITIONAL_ON_CAPACITY_AND_CONTRACT")

    def test_release_flag_cannot_certify(self):
        d = deepcopy(self.doc)
        d["release_claims"]["certified_security"] = True
        with self.assertRaises(ValueError):
            self.check(d)

    def test_schema_version_rejected(self):
        d = deepcopy(self.doc)
        d["schema_version"] = "3.0"
        with self.assertRaises(ValueError):
            self.check(d)

    def test_duplicate_control_rejected(self):
        d = deepcopy(self.doc)
        d["controls"].append(deepcopy(d["controls"][0]))
        with self.assertRaises(ValueError):
            self.check(d)

    def test_removed_p0_rejected(self):
        d = deepcopy(self.doc)
        d["controls"] = [c for c in d["controls"] if c["id"] != "SEC-001"]
        with self.assertRaises(ValueError):
            self.check(d)

    def test_verified_without_evidence_rejected(self):
        d = deepcopy(self.doc)
        d["controls"][0]["status"] = "VERIFIED"
        with self.assertRaises(ValueError):
            self.check(d)

    def test_verified_without_owner_rejected(self):
        d = deepcopy(self.doc)
        d["controls"][0]["status"] = "VERIFIED"
        d["controls"][0]["evidence_url"] = "https://github.com/example/example/actions/1"
        with self.assertRaises(ValueError):
            self.check(d)

    def test_unknown_control_state_rejected(self):
        d = deepcopy(self.doc)
        d["controls"][0]["status"] = "ALL_SECURE"
        with self.assertRaises(ValueError):
            self.check(d)

    def test_missing_acceptance_rejected(self):
        d = deepcopy(self.doc)
        d["controls"][0]["acceptance"] = "works"
        with self.assertRaises(ValueError):
            self.check(d)

    def test_artificial_verified_manifest_does_not_unlock_prod(self):
        d = deepcopy(self.doc)
        for c in d["controls"]:
            c["status"] = "VERIFIED"
            c["owner"] = "independent-reviewer"
            c["evidence_url"] = "https://github.com/example/example/actions/1"
        d["release_claims"]["production_gateway"] = True
        report = self.check(d)
        self.assertFalse(report["production_release_authorized"])
        self.assertEqual(report["production_gateway"], "BLOCKED")

    def test_missing_source_files_are_not_clean(self):
        with tempfile.TemporaryDirectory() as folder:
            x = static_signals(Path(folder))
            self.assertIn("SRC_MISSING", {z["id"] for z in x})

    def test_strict_mode_returns_nonzero(self):
        with patch("builtins.print"):
            self.assertEqual(main(["--require-production-ready"]), 2)

    def test_reporting_mode_does_not_break_ci(self):
        with patch("builtins.print"):
            self.assertEqual(main([]), 0)


if __name__ == "__main__":
    unittest.main()
