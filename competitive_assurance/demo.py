"""Demonstrate mocked policy drift only, never connecting to external tools."""
from __future__ import annotations

import json
from pathlib import Path

from .compat_lab import SOURCE_MODE, load_contract, summarize_mock


def run_demo() -> dict:
    contract = load_contract(Path(__file__).resolve().parents[1] /
                             "docs/competitive-assurance/contracts/ticketing_v1.json")
    def mock(name: str) -> dict:
        return {
            "mode": SOURCE_MODE,
            "adapter_name": name,
            "cases": [{
                "id": case["id"],
                "tenant_id": case["tenant_id"],
                "tool": case["tool"],
                "decision": case["expected_decision"],
                "observed_effect": False,
            } for case in contract["cases"]],
        }
    a = mock("mock-A-not-a-real-vendor")
    b = mock("mock-B-not-a-real-vendor")
    for row in a["cases"]:
        if row["id"] == "export_a":
            row["decision"] = "ALLOW"
            row["observed_effect"] = True
    b["cases"] = [row for row in b["cases"] if row["id"] != "cross_tenant"]
    return {
        "mode": SOURCE_MODE, "real_vendor_tested": False,
        "real_external_tools_called": False,
        "mock_adapters": [summarize_mock(contract, a), summarize_mock(contract, b)],
    }


if __name__ == "__main__":
    print(json.dumps(run_demo(), indent=2, ensure_ascii=False))
