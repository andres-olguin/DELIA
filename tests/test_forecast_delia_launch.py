"""Tests are accounting/methodology checks; not statistical validation."""
import json
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from tools.forecast_delia_launch import evaluate, SOURCE


class LaunchForecastTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(SOURCE.read_text(encoding="utf-8"))

    def test_with(self, data):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "s.json"
            path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
            return evaluate(path)

    def test_three_scenario_totals(self):
        t=self.test_with(self.data)["totals"]
        self.assertEqual(t["Conservador"]["gross_clp"], 290000)
        self.assertEqual(t["Base"]["gross_clp"], 1660000)
        self.assertEqual(t["Expansion"]["gross_clp"], 3320000)

    def test_contributions(self):
        t=self.test_with(self.data)["totals"]
        self.assertEqual(t["Conservador"]["contribution_clp"], 128500)
        self.assertEqual(t["Base"]["contribution_clp"], 860500)
        self.assertEqual(t["Expansion"]["contribution_clp"], 1721000)

    def test_base_monthly_revenue(self):
        p=self.test_with(self.data)["periods"]
        self.assertEqual(next(x for x in p if x["scenario"]=="Base" and x["month"]=="2026-12")["gross_clp"],290000)
        self.assertEqual(next(x for x in p if x["scenario"]=="Base" and x["month"]=="2027-01")["gross_clp"],1370000)

    def test_not_saas_revenue(self):
        x=self.test_with(self.data)
        self.assertEqual(x["saas_mrr_clp"],0)
        self.assertEqual(x["real_customers_verified_by_model"],0)

    def test_reject_claimed_forecast_accuracy(self):
        d=deepcopy(self.data);d["status"]="95_PERCENT_CONFIDENT"
        with self.assertRaises(ValueError):self.test_with(d)

    def test_reject_prelaunch_saas(self):
        d=deepcopy(self.data);d["saas_mrr_included"]=1000000
        with self.assertRaises(ValueError):self.test_with(d)

    def test_reject_fake_negative_spend(self):
        d=deepcopy(self.data);d["rows"][0]["marketing_spend_clp"]=-1
        with self.assertRaises(ValueError):self.test_with(d)

    def test_reject_funnel_exceeds_replies(self):
        d=deepcopy(self.data);d["rows"][0]["meetings"]=200
        with self.assertRaises(ValueError):self.test_with(d)

    def test_reject_fake_extra_lab_december(self):
        d=deepcopy(self.data);d["rows"][0]["lab_sales"]=1
        with self.assertRaises(ValueError):self.test_with(d)

    def test_reject_january_lab_without_prior_diagnostics(self):
        d=deepcopy(self.data);d["rows"][1]["lab_sales"]=1
        with self.assertRaises(ValueError):self.test_with(d)

    def test_reject_duplicate_row(self):
        d=deepcopy(self.data);d["rows"][1]=deepcopy(d["rows"][0])
        with self.assertRaises(ValueError):self.test_with(d)

    def test_reject_unsafe_cost_fraction(self):
        d=deepcopy(self.data);d["assumptions"]["sandbox_lab_direct_cost_fraction"]=2
        with self.assertRaises(ValueError):self.test_with(d)

    def test_reject_undefined_tax_basis(self):
        d=deepcopy(self.data);d["revenue_basis"]="TOTAL"
        with self.assertRaises(ValueError):self.test_with(d)

    def test_decreasing_price_changes_projected_gross_not_actual_customers(self):
        d=deepcopy(self.data);d["assumptions"]["diagnostic_price_clp"]=200000
        x=self.test_with(d)
        self.assertEqual(x["totals"]["Base"]["gross_clp"],1390000)
        self.assertEqual(x["real_customers_verified_by_model"],0)

    def test_missing_month_rejected(self):
        d=deepcopy(self.data);d["rows"].pop()
        with self.assertRaises(ValueError):self.test_with(d)


if __name__=="__main__":unittest.main()
