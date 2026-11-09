"""DELIA Evidence Media Studio — validates planning documents; it does not fact-check.

No posting, no network, no medical/legal assessment, no CRM access. A successful
run proves only schema and publication safeguards for these JSON manifests.
"""
from __future__ import annotations

import json
from datetime import date
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CLAIMS = ROOT / "docs/growth/media-evidence/claims.json"
CALENDAR = ROOT / "docs/growth/media-evidence/calendar.json"
STATUSES = {"UNVERIFIED", "REPORTED_EVENT", "REPORTED_ALLEGATION",
            "RESEARCH_FINDING", "LIMITED_PRODUCT_EVIDENCE", "HYPOTHESIS"}
PUBLIC_USES = {"NOT_AS_FACT", "CONTEXT_WITH_ATTRIBUTION", "RESEARCH_REPORT", "PROPOSAL_ONLY"}
CALENDAR_STATES = {"DRAFT", "APPROVED", "PUBLISHED"}
CHANNELS = {"linkedin", "github", "short_video", "technical_article", "webinar", "email"}
KNOWN_SOURCE_KINDS = {"primary_institution", "first_party_report", "reported_news",
                      "peer_reviewed_research", "professional_analysis",
                      "international_assessment", "standards_documentation",
                      "government_research", "market_study", "platform_perspective",
                      "repository_source"}


def _date(s: str, label: str) -> date:
    if not isinstance(s, str):
        raise ValueError(f"{label} debe ser YYYY-MM-DD")
    try:
        return date.fromisoformat(s)
    except ValueError as exc:
        raise ValueError(f"{label} fecha inválida") from exc


def validate(claims_path: Path = CLAIMS, calendar_path: Path = CALENDAR) -> dict:
    evidence = json.loads(Path(claims_path).read_text(encoding="utf-8"))
    plan = json.loads(Path(calendar_path).read_text(encoding="utf-8"))
    if evidence.get("schema_version") != "1.0" or plan.get("schema_version") != "1.0":
        raise ValueError("Versión de schema no soportada")
    review = _date(evidence.get("review_date"), "research_review")
    if _date(plan.get("review_date"), "calendar_review") != review:
        raise ValueError("Fecha de revisión del calendario no coincide")
    if not isinstance(evidence.get("sources"), list) or len(evidence["sources"]) < 5:
        raise ValueError("Sin fuentes externas documentadas")
    by_source = {}
    urls = set()
    for source in evidence["sources"]:
        key = source.get("id")
        url = source.get("url", "")
        parsed = urlsplit(url)
        if (not isinstance(key, str) or not key.startswith("S-") or key in by_source
                or not parsed.scheme == "https" or not parsed.netloc
                or parsed.username or parsed.password or url in urls):
            raise ValueError("Fuente duplicada o URL no segura")
        urls.add(url)
        if source.get("kind") not in KNOWN_SOURCE_KINDS or not source.get("publisher"):
            raise ValueError("Fuente sin clasificación")
        if _date(source.get("published"), key) > review:
            raise ValueError("Fuente posterior a la revisión")
        by_source[key] = source

    claims = {}
    for claim in evidence.get("claims", []):
        cid = claim.get("id")
        if not isinstance(cid, str) or not cid.startswith("C-") or cid in claims:
            raise ValueError("Claim ID inválido o duplicado")
        claims[cid] = claim
        status = claim.get("status")
        usage = claim.get("public_use")
        refs = claim.get("sources")
        if status not in STATUSES or usage not in PUBLIC_USES:
            raise ValueError(f"{cid} estado/uso inválido")
        if not isinstance(claim.get("statement"), str) or len(claim["statement"]) < 35:
            raise ValueError(f"{cid} sin afirmación clara")
        if not isinstance(claim.get("qualifier"), str) or len(claim["qualifier"]) < 40:
            raise ValueError(f"{cid} sin límite/contexto")
        if type(claim.get("product_claim")) is not bool:
            raise ValueError(f"{cid} product_claim debe ser booleano")
        if not isinstance(refs, list) or len(refs) != len(set(refs)):
            raise ValueError(f"{cid} referencias inválidas")
        if any(ref not in by_source for ref in refs):
            raise ValueError(f"{cid} referencia a fuente no registrada")
        if status == "UNVERIFIED" and (refs or usage != "NOT_AS_FACT"):
            raise ValueError(f"{cid} video no verificado usado como hecho")
        if status in {"REPORTED_EVENT", "REPORTED_ALLEGATION", "RESEARCH_FINDING",
                      "LIMITED_PRODUCT_EVIDENCE"} and not refs:
            raise ValueError(f"{cid} afirmación sin fuente")
        if status == "REPORTED_ALLEGATION" and usage != "CONTEXT_WITH_ATTRIBUTION":
            raise ValueError(f"{cid} acusación debe llevar atribución explícita")
        if status == "HYPOTHESIS" and usage != "PROPOSAL_ONLY":
            raise ValueError(f"{cid} hipótesis no puede presentarse como resultado")
        vid = claim.get("origin_video")
        if vid is not None and vid not in {"1000119096", "1000119097", "1000119098", "1000119099"}:
            raise ValueError(f"{cid} origen audiovisual desconocido")

    items = plan.get("items", [])
    if not isinstance(items, list) or not items:
        raise ValueError("No hay calendario editorial")
    ids = set()
    release_count = 0
    for item in items:
        uid = item.get("id")
        if not isinstance(uid, str) or not uid.startswith("M-") or uid in ids:
            raise ValueError("ID editorial inválido o duplicado")
        ids.add(uid)
        if item.get("channel") not in CHANNELS:
            raise ValueError(f"{uid} canal inválido")
        if item.get("status") not in CALENDAR_STATES:
            raise ValueError(f"{uid} estado editorial inválido")
        if type(item.get("approved")) is not bool:
            raise ValueError(f"{uid} aprobación debe ser booleana")
        if not item.get("audience") or not item.get("cta") or not item.get("topic"):
            raise ValueError(f"{uid} faltan audiencia, topic o CTA")
        d = _date(item.get("date"), f"{uid} publicación")
        if d < review:
            raise ValueError(f"{uid} fecha anterior a revisión")
        refs = item.get("claim_refs")
        if not isinstance(refs, list) or not refs:
            raise ValueError(f"{uid} post sin afirmaciones rastreables")
        if len(refs) != len(set(refs)) or any(x not in claims for x in refs):
            raise ValueError(f"{uid} evidencia desconocida o duplicada")
        if any(claims[x]["status"] == "UNVERIFIED" for x in refs):
            raise ValueError(f"{uid} contiene historia viral no verificada")
        # Even if it is a future post, treat dangerous sensational claims as unsafe titles.
        normalized = item["topic"].casefold()
        if any(x in normalized for x in ("chatgpt mató", "extinción garantizada",
                                         "100% seguro", "certificado por owasp")):
            raise ValueError(f"{uid} titular no respaldado o sensacionalista")
        if item["status"] == "DRAFT":
            if item["approved"] or item.get("publication_url") is not None:
                raise ValueError(f"{uid} borrador no puede decir aprobado o publicado")
        else:
            if not item["approved"]:
                raise ValueError(f"{uid} publicación sin revisión")
            if item["status"] == "PUBLISHED":
                u = item.get("publication_url") or ""
                parsed = urlsplit(u)
                if parsed.scheme != "https" or not parsed.netloc:
                    raise ValueError(f"{uid} publicado sin URL real")
                release_count += 1
            if item["status"] == "APPROVED" and item.get("publication_url") is not None:
                raise ValueError(f"{uid} contenido aún no publicado tiene URL")
    return {
        "mode": "SCHEMA_AND_CLAIM_GATES_ONLY_NOT_FACT_CHECKED",
        "source_count": len(by_source),
        "claim_count": len(claims),
        "calendar_items": len(items),
        "published": release_count,
        "unverified_blocked_from_calendar": sum(1 for x in claims.values()
                                                 if x["status"] == "UNVERIFIED"),
    }


if __name__ == "__main__":
    print(json.dumps(validate(), ensure_ascii=False, indent=2))
