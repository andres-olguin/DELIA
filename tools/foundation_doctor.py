"""DELIA foundation readiness doctor — read-only static signals and evidence ledger.

NO network, imports of application modules, secrets, database access, production
tests, customer data or live tool execution. This deliberately errs on the side
of NOT READY. Absence of a static signature is never proof of security.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/foundation/readiness-controls.json"
STATES = {"OPEN", "IN_PROGRESS", "IN_REVIEW", "VERIFIED"}
SEVERITIES = {"P0", "P1"}
PRODUCTION_REQUIRED = {"SEC-001", "SEC-002", "SEC-003", "SEC-004",
                       "SEC-005", "SEC-006", "SEC-007", "SEC-008"}


def _content(base: Path, path: str) -> str:
    file = base / path
    try:
        return file.read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        # Missing files are readiness failures; do not treat them as clean.
        return ""


def static_signals(base: Path = ROOT) -> list[dict[str, str]]:
    """Signals are grounded in specific file evidence, not proofs of exploitation."""
    proxy = _content(base, "services/proxy.py")
    route = _content(base, "app/api/proxy.py")
    audit = _content(base, "services/audit.py")
    main = _content(base, "app/main.py")
    models = _content(base, "app/models.py")
    compose = _content(base, "docker-compose.yml")
    db = _content(base, "app/database.py")
    findings: list[dict[str, str]] = []

    def issue(code: str, file: str, detail: str):
        findings.append({"id": code, "path": file, "evidence": detail,
                         "kind": "POTENTIAL_SECURITY_OR_INTEGRATION_BLOCKER"})

    # These are the imports literally found in the current codebase. The check
    # recognizes module.py and package/__init__.py without importing anything.
    for p, text in (("app/api/proxy.py", route),
                    ("services/audit.py", audit),
                    ("services/proxy.py", proxy)):
        if not text:
            issue("SRC_MISSING", p, "Required code path not readable")
            continue
        for dotted in ("app.models.chat", "app.services.audit", "app.services.proxy"):
            if re.search(r"(?m)^\s*from\s+" + re.escape(dotted) + r"\s+import\b", text):
                stem = dotted.replace(".", "/")
                if not (base / (stem + ".py")).is_file() and not (base / stem / "__init__.py").is_file():
                    issue("BROKEN_IMPORT", p, "Import path absent in source tree: " + dotted)
    if "request.model_dump" in proxy and re.search(r"json\s*=\s*payload", proxy):
        issue("RAW_UPSTREAM_PAYLOAD", "services/proxy.py",
              "Original serialized request used for provider JSON; DLP call not evidenced")
    if re.search(r"forward_request\(request\b", route):
        issue("UNSANITIZED_FORWARD_CALL", "app/api/proxy.py",
              "Forward call receives the original request object")
    if "prompt_preview=request.messages" in route:
        issue("RAW_PROMPT_LOG", "app/api/proxy.py",
              "Raw user-message preview used to populate audit record")
    if re.search(r"@app\.(?:get|post)\(\"/audit/\"", main):
        # This is a flag, not a security proof. No authenticated dependency is visible.
        if not any(s in main for s in ("require_authenticated_principal", "require_scoped_principal",
                                        "Security(require_", "Depends(require_")):
            issue("AUDIT_AUTH_ABSENT", "app/main.py",
                  "Audit routes appear without an authentication dependency")
    if "request_id=" in route and "class AuditLog" in models and not re.search(
        r"(?m)^\s*request_id\s*=\s*Column\(", models
    ):
        issue("AUDIT_SCHEMA_MISMATCH", "app/models.py",
              "AuditLog constructor uses request_id but mapped model lacks that column")
    if "api_key = authorization.split" in route and "forward_request(request, api_key=api_key)" in route:
        issue("UPSTREAM_TOKEN_PASSTHROUGH", "app/api/proxy.py",
              "Client Authorization is forwarded as upstream provider credential without validated identity")
    if (re.search(r"POSTGRES_PASSWORD\s*:\s*postgres\b", compose) or
            "postgres:postgres@" in db):
        issue("HARDCODED_DATABASE_PASSWORD", "docker-compose.yml; app/database.py",
              "Development password appears embedded in database configuration")
    if "models.Base.metadata.create_all(bind=engine)" in main:
        issue("MIGRATION_BYPASS", "app/main.py",
              "Tables are auto-created at import rather than managed by controlled migrations")
    return findings


def evaluate(base: Path = ROOT, manifest: Path | None = None) -> dict[str, Any]:
    path = manifest if manifest is not None else (base / "docs/foundation/readiness-controls.json")
    doc = json.loads(path.read_text(encoding="utf-8"))
    if doc.get("schema_version") != "1.0" or doc.get("product_stage") != "RESEARCH_AND_SYNTHETIC_LAB":
        raise ValueError("Unknown readiness manifest or invalid current stage")
    if doc.get("readiness_meaning") != "MANUAL_EVIDENCE_REQUIRED_STATIC_CODE_SIGNALS_ONLY":
        raise ValueError("Readiness cannot imply automatic external security validation")
    controls = doc.get("controls")
    if not isinstance(controls, list) or len(controls) < 12:
        raise ValueError("Missing gates")
    ids = set()
    for c in controls:
        cid = c.get("id")
        if not isinstance(cid, str) or not cid or cid in ids:
            raise ValueError("Missing/duplicate control ID")
        ids.add(cid)
        if c.get("severity") not in SEVERITIES or c.get("status") not in STATES:
            raise ValueError("Unknown severity or state")
        if not isinstance(c.get("acceptance"), str) or len(c["acceptance"]) < 28:
            raise ValueError("Control lacks testable acceptance statement")
        if not isinstance(c.get("issues"), list) or not c["issues"]:
            raise ValueError("Control must map to an issue")
        if c["status"] == "VERIFIED":
            evidence = c.get("evidence_url")
            if not isinstance(evidence, str) or not evidence.startswith("https://"):
                raise ValueError("A verified claim requires evidence link")
            if c.get("owner") in (None, "", "UNASSIGNED"):
                raise ValueError("A verified claim requires an accountable reviewer/owner")
    if not PRODUCTION_REQUIRED.issubset(ids):
        raise ValueError("A mandatory production gate is absent")
    claims = doc.get("release_claims", {})
    if not isinstance(claims, dict) or any(type(v) is not bool for v in claims.values()):
        raise ValueError("Claim flags must be explicit booleans")
    if not claims or claims.get("certified_security") is not False:
        raise ValueError("A certification must never be self-attested by this tool")

    signals = static_signals(base)
    missing = sorted(PRODUCTION_REQUIRED - {c["id"] for c in controls if c["status"] == "VERIFIED"})
    # A record may be marked VERIFIED by humans, but signal detection still
    # blocks. Even no signals and no missing controls is only a checklist; it
    # does not certify security. External review is always mandatory.
    production_gate_passed = (not missing and not signals and
                              claims.get("production_gateway") is True)
    return {
        "mode": "READ_ONLY_STATIC_RISK_SCREEN_NOT_A_SECURITY_AUDIT",
        "research_demo": "SYNTHETIC_ONLY",
        "professional_diagnostic": "CONDITIONAL_ON_CAPACITY_AND_CONTRACT",
        "production_gateway": "REVIEW_REQUIRED" if production_gate_passed else "BLOCKED",
        "partner_saas": "BLOCKED",
        "production_release_authorized": False,  # Explicit human + independent review always required.
        "controls_total": len(controls),
        "controls_verified": sum(c["status"] == "VERIFIED" for c in controls),
        "mandatory_controls_unverified": missing,
        "static_signals": signals,
        "limitations": (
            "Static signature checks are incomplete; absence of warnings does NOT "
            "establish security, privacy compliance, working CI, or market readiness."
        ),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="DELIA foundation readiness (non-authoritative)")
    parser.add_argument("--require-production-ready", action="store_true",
                        help="Exit nonzero unless independently authorized production readiness is recorded")
    args = parser.parse_args(argv)
    report = evaluate()
    print(json.dumps(report, ensure_ascii=False, indent=2))
    # Always fail closed: a human-independent review and later dedicated release
    # authorization system would be needed to lift this block.
    return 2 if args.require_production_ready and not report["production_release_authorized"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
