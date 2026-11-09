"""Asegura la integridad del registro de ediciones y sus límites comerciales."""
import json
import tempfile
import unittest
from pathlib import Path

from tools.validate_strategy_catalog import CATALOG, load_and_validate


class StrategyCatalogTests(unittest.TestCase):
    def test_catalog_real_is_valid(self):
        c = load_and_validate()
        self.assertGreaterEqual(len(c["products"]), 8)
        self.assertFalse(c["production_ready"])

    def test_no_duplicate_ids(self):
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        data["products"].append(data["products"][0])
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "manifest.json"
            p.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_and_validate(p)

    def test_no_fake_certification(self):
        data = json.loads(CATALOG.read_text(encoding="utf-8"))
        data["security_certified"] = True
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "manifest.json"
            p.write_text(json.dumps(data), encoding="utf-8")
            with self.assertRaises(ValueError):
                load_and_validate(p)

    def test_names_all_start_with_delia(self):
        c = load_and_validate()
        self.assertTrue(all(p["name"].startswith("DELIA ") for p in c["products"]))


if __name__ == "__main__":
    unittest.main()
