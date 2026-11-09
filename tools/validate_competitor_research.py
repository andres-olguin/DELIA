"""Check competitor research manifest consistency; NOT market proof or due diligence.

No web access, licensing interpretation, security certification, or benchmark.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/estrategia/competidores-directos-2026-11-09.json"
RELATIONSHIPS = {"DIRECT", "ADJACENT", "INCUMBENT", "STANDARD"}


def validate(path: Path = SOURCE) -> dict:
    obj = json.loads(Path(path).read_text(encoding="utf-8"))
    if obj.get("schema_version") != "1.0":
        raise ValueError("Invalid schema")
    date.fromisoformat(obj["as_of"])
    if obj.get("claims_status") != "EVIDENCE_IS_VENDOR_DOCS_NOT_TEST_RESULTS":
        raise ValueError("Unsupported evidence claim")
    if not isinstance(obj.get("competitors"), list) or len(obj["competitors"]) < 15:
        raise ValueError("Insufficient competitor landscape")
    names = set()
    for x in obj["competitors"]:
        name = x.get("name")
        if not isinstance(name, str) or not name.strip() or name in names:
            raise ValueError("Duplicate or missing competitor")
        names.add(name)
        parsed = urlsplit(x.get("source", ""))
        if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
            raise ValueError("No HTTPS source")
        if x.get("relationship") not in RELATIONSHIPS:
            raise ValueError("Invalid relationship")
        if x.get("evidence_type") != "VENDOR_OR_REPOSITORY_ASSERTION":
            raise ValueError("Vendor claims must be marked")
        if x.get("independent_benchmark") != "NOT_EXECUTED" or x.get("delia_superiority_proven") is not False:
            raise ValueError("False benchmark/superiority claim")
        date.fromisoformat(x["documentation_checked"])
        if len(x.get("documented_overlaps", "")) < 20 or len(x.get("commercial_consequence", "")) < 20:
            raise ValueError("Missing relevant competitor description")
    proofs = obj.get("proof_required", [])
    if len(proofs) < 4 or not all(p.get("status") == "PLANNED" for p in proofs):
        raise ValueError("Market experiments must not be premarked complete")
    for p in proofs:
        date.fromisoformat(p["gate"])
    if "HYPOTHESIS" not in obj.get("proposed_wedge", ""):
        raise ValueError("Untested differentiator must be labeled hypothesis")
    return {"competitors": len(names),
            "direct": sum(x["relationship"] == "DIRECT" for x in obj["competitors"]),
            "benchmarks_executed": 0, "superiority_proven": False,
            "mode": "RESEARCH_SCHEMA_ONLY_NOT_MARKET_VALIDATION"}


if __name__ == "__main__":
    print(json.dumps(validate(), indent=2))
