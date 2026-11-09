"""Ejercicio de planificación: SIN llamadas, pagos, ventas, datos personales ni CRM."""
from decimal import Decimal
from .decision_support import DIMENSIONS, Opportunity, PartnerEconomics, assess_opportunity, break_even_accounts


def example() -> dict:
    candidate = Opportunity(
        opportunity_id="SYN-BPO-01",
        wedge="bpo_crm_low_risk",
        scores=dict(zip(DIMENSIONS, (4,3,3,3,3,3,4,3,3))),
        buyer_consented_for_discovery=True,
        evidence_has_been_reviewed=True,
    )
    economics = PartnerEconomics(
        active_tenants=3, platform_fee_usd=Decimal("199"),
        per_tenant_fee_usd=Decimal("79"), metered_operations=10000,
        per_operation_fee_usd=Decimal("0.005"),
        cloud_and_storage_usd=Decimal("80"),
        support_and_operations_usd=Decimal("180"),
        partner_commission_fraction=Decimal("0.15"),
        payment_processing_usd=Decimal("10"),
    )
    a = assess_opportunity(candidate)
    return {
        "mode": "SIMULACION_DE_GTM_NO_PROBABILIDAD",
        "opportunity": {"priority_index": a.priority_index, "stage": a.stage,
                        "real_world_pilot_authorized": a.real_world_pilot_authorized},
        "partner_economics": economics.calculate(),
        "break_even_accounts_example": break_even_accounts(
            fixed_monthly_cost_usd=Decimal("8000"),
            net_arpa_usd=Decimal("499"),
            contribution_margin=Decimal("0.75")),
        "status": "No hay compradores, contratos o ingresos verificados por este ejercicio",
    }


if __name__ == "__main__":
    import json
    print(json.dumps(example(), ensure_ascii=False, indent=2))
