"""Static contract-versus-mock-response comparison.

WARNING: This tests ONLY whether self-declared mock decisions agree with a
synthetic contract. It cannot enforce tools, authenticate actors, inspect a
network, verify provider actions, check legal compliance, or guarantee safety.
"""
from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

VALID_DECISIONS = {"ALLOW", "DENY", "REVIEW"}
SOURCE_MODE = "MOCK_ONLY_NO_ENFORCEMENT"


def _nonblank(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value or value.strip() != value or len(value) > 128:
        raise ValueError(f"{label}: invalid identifier")
    return value


def load_contract(path: str | Path) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        raise ValueError("Invalid contract schema")
    if data.get("mode") != SOURCE_MODE:
        raise ValueError("Production claims in mock contract are forbidden")
    _nonblank(data.get("contract_id"), "contract_id")
    if type(data.get("version")) is not int or data["version"] < 1:
        raise ValueError("Invalid contract version")
    if not isinstance(data.get("cases"), list) or len(data["cases"]) < 2:
        raise ValueError("Contract must have cases")
    ids: set[str] = set()
    for case in data["cases"]:
        if not isinstance(case, dict) or set(case) != {"id", "tenant_id", "tool", "expected_decision"}:
            raise ValueError("Case fields invalid")
        cid = _nonblank(case["id"], "case.id")
        _nonblank(case["tenant_id"], "case.tenant_id")
        _nonblank(case["tool"], "case.tool")
        if cid in ids:
            raise ValueError("Duplicate case")
        ids.add(cid)
        if case["expected_decision"] not in VALID_DECISIONS:
            raise ValueError("Bad decision")
    return data


@dataclass(frozen=True)
class CaseVerdict:
    case_id: str
    status: str   # MATCH_SIMULATED | CONTRACT_VIOLATION | INDETERMINATE
    reasons: tuple[str, ...]


def compare_mock(contract: dict, adapter_report: dict) -> list[CaseVerdict]:
    """Compare canonical expected decisions with simulated adapter observations.

    No vendor compatibility is inferred. An unknown report cannot be a pass.
    """
    if adapter_report.get("mode") != SOURCE_MODE:
        raise ValueError("Only simulated reports allowed")
    _nonblank(adapter_report.get("adapter_name"), "adapter_name")
    reported = adapter_report.get("cases")
    if not isinstance(reported, list):
        raise ValueError("No observation cases")
    by_id: dict[str, dict] = {}
    for entry in reported:
        if not isinstance(entry, dict):
            raise ValueError("Observation must be object")
        cid = _nonblank(entry.get("id"), "observation id")
        if cid in by_id:
            raise ValueError("Duplicate observation ID")
        by_id[cid] = entry
    expected_ids = {x["id"] for x in contract["cases"]}
    if set(by_id) - expected_ids:
        raise ValueError("Unexpected case IDs in mock adapter")
    results = []
    for case in contract["cases"]:
        cid = case["id"]
        entry = by_id.get(cid)
        if entry is None:
            results.append(CaseVerdict(cid, "INDETERMINATE", ("NO_OBSERVATION",)))
            continue
        if not {"tenant_id", "tool", "decision", "observed_effect"}.issubset(entry):
            results.append(CaseVerdict(cid, "INDETERMINATE", ("INCOMPLETE_OBSERVATION",)))
            continue
        if entry["tenant_id"] != case["tenant_id"] or entry["tool"] != case["tool"]:
            results.append(CaseVerdict(cid, "CONTRACT_VIOLATION", ("CASE_CONTEXT_MISMATCH",)))
            continue
        if entry["decision"] not in VALID_DECISIONS:
            results.append(CaseVerdict(cid, "INDETERMINATE", ("UNKNOWN_DECISION",)))
            continue
        if type(entry["observed_effect"]) is not bool:
            results.append(CaseVerdict(cid, "INDETERMINATE", ("UNKNOWN_EFFECT",)))
            continue
        reasons = []
        if entry["decision"] != case["expected_decision"]:
            reasons.append("DECISION_MISMATCH")
        # For DENY and REVIEW, no tool effect is acceptable in our mock fixture.
        if case["expected_decision"] in {"DENY", "REVIEW"} and entry["observed_effect"]:
            reasons.append("UNAUTHORIZED_MOCK_EFFECT")
        status = "CONTRACT_VIOLATION" if reasons else "MATCH_SIMULATED"
        results.append(CaseVerdict(cid, status, tuple(reasons)))
    return results


def summarize_mock(contract: dict, adapter_report: dict) -> dict[str, Any]:
    verdicts = compare_mock(contract, adapter_report)
    counts = {k: sum(v.status == k for v in verdicts)
              for k in ("MATCH_SIMULATED", "CONTRACT_VIOLATION", "INDETERMINATE")}
    return {
        "mode": SOURCE_MODE,
        "adapter": adapter_report["adapter_name"],
        "contract_id": contract["contract_id"],
        "counts": counts,
        "all_observations_consistent_with_fixture": (
            counts["CONTRACT_VIOLATION"] == 0 and counts["INDETERMINATE"] == 0),
        "real_vendor_tested": False,
        "external_effects_observed": False,
        "claims": "MOCK_FIXTURE_CONSISTENCY_ONLY",
        "findings": [{"id": v.case_id, "status": v.status, "reasons": list(v.reasons)}
                     for v in verdicts if v.status != "MATCH_SIMULATED"],
    }
