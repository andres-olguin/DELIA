"""Pruebas deterministas de contratos empresariales de laboratorio."""
import unittest
from pathlib import Path

from experiments.contract_assurance.engine import (
    ContractError, OrderSnapshot, RefundContract, RefundProposal,
    SettlementObservation, preflight, reconcile, load_refund_contract,
)
from experiments.contract_assurance.demo import run_demo


class OutcomeContractTests(unittest.TestCase):
    def setUp(self):
        self.c = RefundContract("demo", 1, "MXN", 2000000)
        self.p = RefundProposal("tenant-A", "order-01", "op-01", 1500000, "MXN", 7)
        self.s = OrderSnapshot("tenant-A", "order-01", 7, "paid", 2000000, 0,
                               True, frozenset())

    def check_denied(self, s=None, p=None, reason=None):
        r = preflight(self.c, p or self.p, s or self.s)
        self.assertEqual(r.outcome, "DENY")
        if reason:
            self.assertIn(reason, r.reasons)

    def test_valid_preflight_does_not_authorize(self):
        r = preflight(self.c, self.p, self.s)
        self.assertEqual(r.outcome, "ELIGIBLE_FOR_AUTHORIZATION")
        self.assertFalse(r.is_authorized)

    def test_wrong_tenant(self):
        self.check_denied(s=OrderSnapshot("tenant-B","order-01",7,"paid",2000000,0,True,frozenset()),
                          reason="TENANT_MISMATCH")

    def test_wrong_order(self):
        self.check_denied(s=OrderSnapshot("tenant-A","order-02",7,"paid",2000000,0,True,frozenset()),
                          reason="ORDER_MISMATCH")

    def test_stale_snapshot(self):
        self.check_denied(s=OrderSnapshot("tenant-A","order-01",8,"paid",2000000,0,True,frozenset()),
                          reason="STATE_STALE")

    def test_wrong_currency(self):
        self.check_denied(p=RefundProposal("tenant-A","order-01","op-01",1500000,"CLP",7),
                          reason="CURRENCY_MISMATCH")

    def test_contract_limit(self):
        self.check_denied(p=RefundProposal("tenant-A","order-01","op-01",2500000,"MXN",7),
                          reason="CONTRACT_LIMIT")

    def test_order_not_paid(self):
        self.check_denied(s=OrderSnapshot("tenant-A","order-01",7,"cancelled",2000000,0,True,frozenset()),
                          reason="ORDER_NOT_PAID")

    def test_customer_unverified(self):
        self.check_denied(s=OrderSnapshot("tenant-A","order-01",7,"paid",2000000,0,False,frozenset()),
                          reason="CUSTOMER_NOT_VERIFIED")

    def test_duplicate_operation(self):
        self.check_denied(s=OrderSnapshot("tenant-A","order-01",7,"paid",2000000,0,True,
                                           frozenset({"op-01"})), reason="OPERATION_ALREADY_SEEN")

    def test_refund_exceeds_remaining_balance(self):
        self.check_denied(s=OrderSnapshot("tenant-A","order-01",7,"paid",2000000,700000,True,
                                           frozenset()), reason="REFUND_EXCEEDS_BALANCE")

    def test_exact_remaining_balance_is_eligible(self):
        s = OrderSnapshot("tenant-A","order-01",7,"paid",2000000,500000,True,frozenset())
        self.assertEqual(preflight(self.c,self.p,s).outcome,"ELIGIBLE_FOR_AUTHORIZATION")

    def test_amount_bool_is_invalid(self):
        with self.assertRaises(ContractError):
            RefundProposal("tenant-A","order-01","op-01",True,"MXN",7)

    def test_refunded_greater_than_paid_is_invalid(self):
        with self.assertRaises(ContractError):
            OrderSnapshot("tenant-A","order-01",7,"paid",100,200,True,frozenset())

    def test_invalid_currency(self):
        with self.assertRaises(ContractError):
            RefundContract("demo",1,"XXX",2000000)

    def test_invalid_contract_limit(self):
        with self.assertRaises(ContractError):
            RefundContract("demo",1,"MXN",0)

    def observation(self, state="confirmed", amount=1500000, hash=None, tenant="tenant-A", op="op-01"):
        return SettlementObservation(tenant,op,hash or self.p.digest,state,amount)

    def test_reconciliation_synthetic_confirmation(self):
        self.assertEqual(reconcile(self.p,self.observation()).outcome,"VERIFIED_SIMULATED")

    def test_reconciliation_pending_holds(self):
        self.assertEqual(reconcile(self.p,self.observation("pending")).outcome,"HOLD")

    def test_reconciliation_unknown_holds(self):
        self.assertEqual(reconcile(self.p,self.observation("unknown")).outcome,"HOLD")

    def test_reconciliation_rejected(self):
        self.assertEqual(reconcile(self.p,self.observation("rejected",None)).outcome,"REJECTED")

    def test_reconciliation_amount_mismatch(self):
        self.assertEqual(reconcile(self.p,self.observation("confirmed",1)).outcome,"MISMATCH")

    def test_reconciliation_hash_mismatch(self):
        self.assertEqual(reconcile(self.p,self.observation(hash="wrong")).outcome,"MISMATCH")

    def test_reconciliation_wrong_tenant(self):
        self.assertEqual(reconcile(self.p,self.observation(tenant="tenant-B")).outcome,"MISMATCH")

    def test_reconciliation_wrong_op(self):
        self.assertEqual(reconcile(self.p,self.observation(op="op-02")).outcome,"MISMATCH")

    def test_load_manifest(self):
        path=Path("experiments/contract_assurance/contracts/commerce_refund_mx_v1.json")
        self.assertEqual(load_refund_contract(path).currency,"MXN")

    def test_demo_never_claims_real_execution(self):
        data=run_demo()
        self.assertFalse(data["real_transaction_executed"])
        self.assertTrue(data["requires_independent_authorization"])

if __name__=="__main__":
    unittest.main()
