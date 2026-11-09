"""DELIA early sales scenario arithmetic: NO inferred conversion probabilities.

Reads synthetic assumptions only, no CRM, no network and no PII. It does not
predict customers or authorize services, spend, billing or production pilots.
"""
from __future__ import annotations

import json
from collections import defaultdict
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/growth/launch-2026-2027/forecast-scenarios.json"
SCENARIOS = {"Conservador", "Base", "Expansion"}
MONTHS = {"2026-12", "2027-01"}


def as_dec(x) -> Decimal:
    if isinstance(x, bool) or not isinstance(x, (int, float, str, Decimal)):
        raise ValueError("Expected nonnegative finite numeric value")
    val = Decimal(str(x))
    if not val.is_finite() or val < 0:
        raise ValueError("Expected nonnegative finite numeric value")
    return val


def evaluate(path: Path = SOURCE) -> dict:
    x = json.loads(Path(path).read_text(encoding="utf-8"))
    if x.get("schema_version") != "1.0" or x.get("currency") != "CLP":
        raise ValueError("Invalid forecasting schema")
    if x.get("status") != "SCENARIOS_NOT_STATISTICAL_FORECAST":
        raise ValueError("Scenarios may never claim calibrated sales certainty")
    if x.get("saas_mrr_included") != 0:
        raise ValueError("No SaaS MRR forecast before production security")
    if x.get("revenue_basis") != "NET_OF_IVA_IF_APPLICABLE":
        raise ValueError("Revenue must indicate its tax basis")
    p = x.get("assumptions", {})
    dprice = as_dec(p["diagnostic_price_clp"])
    lprice = as_dec(p["sandbox_lab_price_clp"])
    dcost = as_dec(p["diagnostic_direct_cost_fraction"])
    lcost = as_dec(p["sandbox_lab_direct_cost_fraction"])
    if any(not (Decimal("0") < value < Decimal("1")) for value in (dcost, lcost)):
        raise ValueError("Direct cost fractions must be (0,1)")
    if dprice == 0 or lprice == 0:
        raise ValueError("Package prices must be positive")
    if len(x.get("rows", [])) != 6:
        raise ValueError("Expected three scenarios x two months")
    seen = set()
    totals = defaultdict(lambda: {"gross_clp": Decimal(0),
                                  "direct_cost_clp": Decimal(0),
                                  "marketing_clp": Decimal(0),
                                  "contribution_clp": Decimal(0)})
    periods = []
    by_key = {}
    for row in x["rows"]:
        scenario, month = row.get("scenario"), row.get("month")
        key = (scenario, month)
        if scenario not in SCENARIOS or month not in MONTHS or key in seen:
            raise ValueError("Invalid or duplicate scenario/month")
        seen.add(key)
        by_key[key] = row
        for column in ("accounts_contacted_or_researched", "meetings", "proposals",
                       "diagnostic_sales", "lab_sales", "marketing_spend_clp"):
            if type(row.get(column)) is not int or row[column] < 0:
                raise ValueError(f"{column} must be nonnegative integer")
        if not (row["diagnostic_sales"] <= row["proposals"] <=
                row["meetings"] <= row["accounts_contacted_or_researched"]):
            raise ValueError("Inconsistent funnel")
        if month == "2026-12" and row["lab_sales"]:
            raise ValueError("No labs forecast before technical assessment")
        gross = dprice * row["diagnostic_sales"] + lprice * row["lab_sales"]
        direct_cost = dprice * row["diagnostic_sales"] * dcost + lprice * row["lab_sales"] * lcost
        marketing = Decimal(row["marketing_spend_clp"])
        contribution = gross - direct_cost - marketing
        record = {"scenario": scenario, "month": month,
                  "gross_clp": int(gross), "direct_cost_clp": int(direct_cost),
                  "marketing_clp": int(marketing), "contribution_clp": int(contribution)}
        periods.append(record)
        t = totals[scenario]
        for metric in ("gross_clp", "direct_cost_clp", "marketing_clp", "contribution_clp"):
            t[metric] += Decimal(record[metric])
    if seen != {(a,b) for a in SCENARIOS for b in MONTHS}:
        raise ValueError("Missing scenario/month")
    for scenario in SCENARIOS:
        dec = by_key[(scenario, "2026-12")]["diagnostic_sales"]
        jan = by_key[(scenario, "2027-01")]["lab_sales"]
        if jan > dec:
            raise ValueError("January lab contracts cannot exceed December diagnostics in this funnel")
    return {"label": "ILLUSTRATIVE_NO_SALES_VERIFIED", "periods": periods,
            "totals": {k:{m:int(v) for m,v in value.items()} for k,value in totals.items()},
            "saas_mrr_clp": 0, "real_customers_verified_by_model": 0}


if __name__ == "__main__":
    print(json.dumps(evaluate(), indent=2, ensure_ascii=False))
