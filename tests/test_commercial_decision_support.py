"""Garantiza que el scorecard no se confunda con probabilidad o autorización."""
from dataclasses import replace
from decimal import Decimal
import unittest

from commercial_ops.decision_support import (
    DIMENSIONS, Opportunity, PartnerEconomics, assess_opportunity, break_even_accounts,
)
from commercial_ops.demo import example


class QualificationTests(unittest.TestCase):
    def setUp(self):
        self.c = Opportunity(
            opportunity_id="SYN-001",
            wedge="bpo_crm_low_risk",
            scores={x: 4 for x in DIMENSIONS},
            buyer_consented_for_discovery=True,
            evidence_has_been_reviewed=True,
        )

    def test_perfect_score_is_not_conversion_probability(self):
        a = assess_opportunity(self.c)
        self.assertEqual(a.priority_index, 100)
        self.assertEqual(a.stage, "LAB_EVALUATION_CANDIDATE")
        self.assertFalse(a.real_world_pilot_authorized)

    def test_no_consent_means_no_contact(self):
        a = assess_opportunity(replace(self.c, buyer_consented_for_discovery=False))
        self.assertEqual(a.stage, "DO_NOT_CONTACT")

    def test_unverified_evidence(self):
        a = assess_opportunity(replace(self.c, evidence_has_been_reviewed=False))
        self.assertEqual(a.stage, "DISCOVERY_ONLY")

    def test_weak_problem_no_fit(self):
        scores = dict(self.c.scores); scores["problem_severity"] = 1
        self.assertEqual(assess_opportunity(replace(self.c, scores=scores)).stage,
                         "NO_FIT_OR_RESEARCH")

    def test_competitor_already_sufficient_no_fit(self):
        scores = dict(self.c.scores); scores["alternative_gap_evidence"] = 0
        self.assertEqual(assess_opportunity(replace(self.c, scores=scores)).stage,
                         "NO_FIT_OR_RESEARCH")

    def test_no_budget(self):
        scores = dict(self.c.scores); scores["budget_evidence"] = 0
        self.assertEqual(assess_opportunity(replace(self.c, scores=scores)).stage, "DISCOVERY_ONLY")

    def test_live_data_blocks_without_verified_gates(self):
        a = assess_opportunity(replace(self.c, requests_live_data=True))
        self.assertEqual(a.stage, "LAB_ONLY_NO_LIVE_PILOT")
        self.assertFalse(a.real_world_pilot_authorized)

    def test_external_side_effects_require_review(self):
        a = assess_opportunity(replace(
            self.c, requests_external_side_effects=True,
            identity_and_tenant_gates_verified=True,
            privacy_egress_gates_verified=True,
            contract_approved_for_pilot=True))
        self.assertEqual(a.stage, "SECURITY_REVIEW_REQUIRED")
        self.assertFalse(a.real_world_pilot_authorized)

    def test_refund_wedge_remains_lab(self):
        a = assess_opportunity(replace(self.c, wedge="commerce_refund_lab_only"))
        self.assertEqual(a.stage, "LAB_EVALUATION_CANDIDATE")
        self.assertFalse(a.real_world_pilot_authorized)

    def test_bad_wedge_rejected(self):
        with self.assertRaises(ValueError):
            replace(self.c, wedge="hospital_production")

    def test_reject_person_name_as_id(self):
        with self.assertRaises(ValueError):
            replace(self.c, opportunity_id="Empresa Juan Perez")

    def test_missing_score_dimension_rejected(self):
        scores = dict(self.c.scores); scores.pop("urgent_trigger")
        with self.assertRaises(ValueError):
            replace(self.c, scores=scores)

    def test_bool_is_not_score(self):
        scores = dict(self.c.scores); scores["urgent_trigger"] = True
        with self.assertRaises(ValueError):
            replace(self.c, scores=scores)

    def test_middle_score(self):
        scores = {x: 2 for x in DIMENSIONS}; scores["problem_severity"] = 3
        scores["alternative_gap_evidence"] = 3
        a = assess_opportunity(replace(self.c, scores=scores))
        self.assertEqual(a.stage, "VALIDATION_CANDIDATE")

    def test_no_automatic_authorization_even_high_score(self):
        for v in (0,1,2,3,4):
            scores={x:v for x in DIMENSIONS}
            o=replace(self.c,scores=scores)
            self.assertFalse(assess_opportunity(o).real_world_pilot_authorized)


class EconomicsTests(unittest.TestCase):
    def setUp(self):
        self.x=PartnerEconomics(
            active_tenants=3, platform_fee_usd=Decimal("199"),
            per_tenant_fee_usd=Decimal("79"), metered_operations=10000,
            per_operation_fee_usd=Decimal("0.005"),
            cloud_and_storage_usd=Decimal("80"), support_and_operations_usd=Decimal("180"),
            partner_commission_fraction=Decimal("0.15"),
            payment_processing_usd=Decimal("10"))

    def test_revenue_arithmetic(self):
        x=self.x.calculate()
        self.assertEqual(x["monthly_gross_revenue_usd"],"486.000")
        self.assertEqual(x["annualized_gross_run_rate_usd"],"5832.000")

    def test_contribution_arithmetic(self):
        x=self.x.calculate()
        self.assertEqual(x["monthly_partner_commission_usd"],"72.90000")
        self.assertEqual(x["monthly_contribution_usd"],"143.10000")

    def test_negative_revenue_rejected(self):
        with self.assertRaises(ValueError):
            replace(self.x,per_tenant_fee_usd=Decimal("-10")).calculate()

    def test_invalid_commission(self):
        with self.assertRaises(ValueError):
            replace(self.x,partner_commission_fraction=Decimal("1.1")).calculate()

    def test_nan_cost_rejected(self):
        with self.assertRaises(ValueError):
            replace(self.x, cloud_and_storage_usd=Decimal("NaN")).calculate()

    def test_break_even_22(self):
        self.assertEqual(break_even_accounts(
            fixed_monthly_cost_usd=Decimal("8000"),
            net_arpa_usd=Decimal("499"),
            contribution_margin=Decimal("0.75")),22)

    def test_break_even_zero_revenue(self):
        self.assertIsNone(break_even_accounts(
            fixed_monthly_cost_usd=Decimal("8000"),
            net_arpa_usd=Decimal("0"),
            contribution_margin=Decimal("0.75")))

    def test_break_even_zero_fixed(self):
        self.assertEqual(break_even_accounts(
            fixed_monthly_cost_usd=Decimal("0"),
            net_arpa_usd=Decimal("0"),
            contribution_margin=Decimal("0")),0)

    def test_demo_labels_not_real(self):
        d=example()
        self.assertFalse(d["opportunity"]["real_world_pilot_authorized"])
        self.assertIn("SIMULACION",d["mode"])


if __name__=="__main__":
    unittest.main()
