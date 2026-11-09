"""Escenarios de ingresos exploratorios: no pronósticos financieros."""
from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class RevenueScenario:
    accounts: int
    monthly_price_usd: Decimal
    contribution_margin: Decimal
    monthly_fixed_cost_usd: Decimal

    def calculate(self) -> dict[str, str]:
        if type(self.accounts) is not int or self.accounts < 0:
            raise ValueError("accounts debe ser un entero >=0")
        if (self.monthly_price_usd < 0 or self.monthly_fixed_cost_usd < 0
                or not Decimal(0) <= self.contribution_margin <= Decimal(1)):
            raise ValueError("Precio, costos o margen fuera de rango")
        mrr = self.monthly_price_usd * self.accounts
        contribution = mrr * self.contribution_margin
        return {
            "label": "HIPÓTESIS, NO INGRESO REAL",
            "mrr_usd": str(mrr),
            "annualized_run_rate_usd": str(mrr * 12),
            "monthly_contribution_before_fixed_usd": str(contribution),
            "monthly_result_before_tax_and_other_costs_usd": str(contribution - self.monthly_fixed_cost_usd),
        }
