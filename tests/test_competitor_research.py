"""Research-matrix integrity only; no competitor testing."""
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from tools.validate_competitor_research import SOURCE, validate


class CompetitorResearchTests(unittest.TestCase):
    def setUp(self):
        self.d = json.loads(SOURCE.read_text(encoding="utf-8"))

    def run_manifest(self, data):
        with tempfile.TemporaryDirectory() as root:
            p = Path(root) / "matrix.json"
            p.write_text(json.dumps(data), encoding="utf-8")
            return validate(p)

    def test_valid_research(self):
        x = self.run_manifest(self.d)
        self.assertEqual(x["competitors"], 22)
        self.assertFalse(x["superiority_proven"])
        self.assertEqual(x["benchmarks_executed"], 0)

    def test_no_fake_benchmark(self):
        data = deepcopy(self.d)
        data["competitors"][0]["independent_benchmark"] = "PASSED"
        with self.assertRaises(ValueError):
            self.run_manifest(data)

    def test_no_fake_superiority(self):
        data = deepcopy(self.d)
        data["competitors"][0]["delia_superiority_proven"] = True
        with self.assertRaises(ValueError):
            self.run_manifest(data)

    def test_no_undocumented_production_claim(self):
        data = deepcopy(self.d)
        data["claims_status"] = "FULLY_VERIFIED"
        with self.assertRaises(ValueError):
            self.run_manifest(data)

    def test_cannot_mark_market_proof_complete(self):
        data = deepcopy(self.d)
        data["proof_required"][0]["status"] = "DONE"
        with self.assertRaises(ValueError):
            self.run_manifest(data)

    def test_no_duplicate_competitor(self):
        data = deepcopy(self.d)
        data["competitors"].append(deepcopy(data["competitors"][0]))
        with self.assertRaises(ValueError):
            self.run_manifest(data)

    def test_https_required(self):
        data = deepcopy(self.d)
        data["competitors"][0]["source"] = "http://unsafe"
        with self.assertRaises(ValueError):
            self.run_manifest(data)

    def test_hypothesis_label_required(self):
        data = deepcopy(self.d)
        data["proposed_wedge"] = "Unique and ready product"
        with self.assertRaises(ValueError):
            self.run_manifest(data)


if __name__ == "__main__":
    unittest.main()
