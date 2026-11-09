"""Herramientas deterministas de calificación y economía comercial para DELIA.

**Uso: planificación interna, no producción comercial ni seguridad de IA.**
No almacenan personas, empresas identificables, correos, teléfonos, ni datos
sensibles. Los indicadores son reglas heurísticas NO modelos probabilísticos
de conversión ni predicciones de éxito. Los resultados no autorizan pilotos.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, ROUND_CEILING
from typing import Mapping

DIMENSIONS = (
    "problem_severity",
    "problem_frequency",
    "current_cost_evidence",
    "economic_buyer_access",
    "budget_evidence",
    "urgent_trigger",
    "technical_integration_fit",
    "alternative_gap_evidence",
    "available_capacity",
)
ALLOWED_WEDGES = frozenset({
    "bpo_crm_low_risk",
    "b2b_saas_low_risk",
    "integrator_partner_lab",
    "commerce_refund_lab_only",
})
DECIMAL_ZERO = Decimal("0")
DECIMAL_ONE = Decimal("1")


def _money(value: Decimal, name: str) -> Decimal:
    if not isinstance(value, Decimal) or not value.is_finite() or value < DECIMAL_ZERO:
        raise ValueError(f"{name} debe ser Decimal finito no negativo")
    return value


@dataclass(frozen=True)
class Opportunity:
    """Sin datos personales ni nombres de clientes; ID sintético interno."""
    opportunity_id: str
    wedge: str
    scores: Mapping[str, int]
    buyer_consented_for_discovery: bool
    evidence_has_been_reviewed: bool
    requests_live_data: bool = False
    requests_external_side_effects: bool = False
    identity_and_tenant_gates_verified: bool = False
    privacy_egress_gates_verified: bool = False
    contract_approved_for_pilot: bool = False

    def __post_init__(self) -> None:
        if (not isinstance(self.opportunity_id, str)
                or not self.opportunity_id.startswith("SYN-")
                or len(self.opportunity_id) > 64):
            raise ValueError("Usar solo IDs de planificación SYN- sin nombres/PII")
        if self.wedge not in ALLOWED_WEDGES:
            raise ValueError("Caso no permitido en la estrategia inicial")
        if set(self.scores) != set(DIMENSIONS):
            raise ValueError("Faltan o sobran dimensiones")
        for v in self.scores.values():
            if type(v) is not int or not 0 <= v <= 4:
                raise ValueError("Cada puntuación debe ser entero entre 0 y 4")
        for key in (
            "buyer_consented_for_discovery",
            "evidence_has_been_reviewed",
            "requests_live_data",
            "requests_external_side_effects",
            "identity_and_tenant_gates_verified",
            "privacy_egress_gates_verified",
            "contract_approved_for_pilot",
        ):
            if type(getattr(self, key)) is not bool:
                raise ValueError(f"{key} debe ser booleano")


@dataclass(frozen=True)
class Assessment:
    priority_index: int  # Índice 0-100; NO porcentaje de conversión.
    stage: str
    reasons: tuple[str, ...]
    real_world_pilot_authorized: bool = False


def assess_opportunity(o: Opportunity) -> Assessment:
    """Clasifica prioridad de investigación, nunca da permiso de despliegue."""
    index = round(sum(o.scores.values()) * 100 / (4 * len(DIMENSIONS)))
    reasons: list[str] = []
    if not o.buyer_consented_for_discovery:
        reasons.append("NO_DISCOVERY_CONSENT")
        return Assessment(index, "DO_NOT_CONTACT", tuple(reasons))
    if not o.evidence_has_been_reviewed:
        reasons.append("EVIDENCE_UNREVIEWED")
        return Assessment(index, "DISCOVERY_ONLY", tuple(reasons))
    if o.scores["problem_severity"] <= 1 or o.scores["alternative_gap_evidence"] <= 1:
        reasons.append("WEAK_OR_NO_INCREMENTAL_VALUE")
        return Assessment(index, "NO_FIT_OR_RESEARCH", tuple(reasons))
    if o.scores["economic_buyer_access"] <= 1 or o.scores["budget_evidence"] <= 1:
        reasons.append("NO_BUYER_OR_BUDGET_VALIDATION")
        return Assessment(index, "DISCOVERY_ONLY", tuple(reasons))
    if o.requests_live_data or o.requests_external_side_effects:
        reasons.append("HIGHER_RISK_REQUEST")
        if not (o.identity_and_tenant_gates_verified and o.privacy_egress_gates_verified
                and o.contract_approved_for_pilot):
            reasons.append("SECURITY_OR_CONTRACT_GATES_OPEN")
            return Assessment(index, "LAB_ONLY_NO_LIVE_PILOT", tuple(reasons))
        # Los flags son autorreportados y NO sustituyen controles ni autorización.
        reasons.append("REQUIRES_INDEPENDENT_GATE_REVIEW")
        return Assessment(index, "SECURITY_REVIEW_REQUIRED", tuple(reasons))
    if o.wedge == "commerce_refund_lab_only":
        reasons.append("FINANCIAL_USE_CASE_LAB_ONLY")
        return Assessment(index, "LAB_EVALUATION_CANDIDATE", tuple(reasons))
    if index >= 75:
        return Assessment(index, "LAB_EVALUATION_CANDIDATE", tuple())
    if index >= 50:
        return Assessment(index, "VALIDATION_CANDIDATE", tuple())
    return Assessment(index, "DISCOVERY_ONLY", ("LOW_EVIDENCE_PRIORITY",))


@dataclass(frozen=True)
class PartnerEconomics:
    """Modelo de contribución ilustrativo, NO tarifa, valoración o predicción."""
    active_tenants: int
    platform_fee_usd: Decimal
    per_tenant_fee_usd: Decimal
    metered_operations: int
    per_operation_fee_usd: Decimal
    cloud_and_storage_usd: Decimal
    support_and_operations_usd: Decimal
    partner_commission_fraction: Decimal
    payment_processing_usd: Decimal

    def calculate(self) -> dict[str, str]:
        if type(self.active_tenants) is not int or self.active_tenants < 0:
            raise ValueError("active_tenants debe ser entero no negativo")
        if type(self.metered_operations) is not int or self.metered_operations < 0:
            raise ValueError("metered_operations debe ser entero no negativo")
        for name in (
            "platform_fee_usd", "per_tenant_fee_usd", "per_operation_fee_usd",
            "cloud_and_storage_usd", "support_and_operations_usd",
            "payment_processing_usd",
        ):
            _money(getattr(self, name), name)
        rate = self.partner_commission_fraction
        if (not isinstance(rate, Decimal) or not rate.is_finite()
                or not DECIMAL_ZERO <= rate <= DECIMAL_ONE):
            raise ValueError("partner_commission_fraction fuera de rango")
        gross = (
            self.platform_fee_usd +
            self.active_tenants * self.per_tenant_fee_usd +
            self.metered_operations * self.per_operation_fee_usd
        )
        commission = gross * rate
        variable_cost = (
            self.cloud_and_storage_usd + self.support_and_operations_usd +
            self.payment_processing_usd + commission
        )
        contribution = gross - variable_cost
        margin = contribution / gross if gross > DECIMAL_ZERO else None
        return {
            "label": "ESCENARIO_DE_PRACTICA_NO_INGRESOS_OBTENIDOS",
            "monthly_gross_revenue_usd": str(gross),
            "annualized_gross_run_rate_usd": str(gross * 12),
            "monthly_partner_commission_usd": str(commission),
            "monthly_attributable_costs_usd": str(variable_cost),
            "monthly_contribution_usd": str(contribution),
            "contribution_margin": str(margin) if margin is not None else "UNDEFINED",
        }


def break_even_accounts(*, fixed_monthly_cost_usd: Decimal,
                        net_arpa_usd: Decimal, contribution_margin: Decimal) -> int | None:
    """Punto de equilibrio simplificado; None si imposible/indefinido."""
    fixed = _money(fixed_monthly_cost_usd, "fixed_monthly_cost_usd")
    arpa = _money(net_arpa_usd, "net_arpa_usd")
    if (not isinstance(contribution_margin, Decimal) or not contribution_margin.is_finite()
            or not DECIMAL_ZERO <= contribution_margin <= DECIMAL_ONE):
        raise ValueError("contribution_margin debe ser Decimal en [0,1]")
    if fixed == 0:
        return 0
    monthly_contribution = arpa * contribution_margin
    if monthly_contribution <= 0:
        return None
    return int((fixed / monthly_contribution).to_integral_value(rounding=ROUND_CEILING))
