"""DELIA Sector Packs: manifests estáticos y simulaciones de políticas.

No autenticación, no endpoints, no herramientas reales ni certificación. Cada pack
usa una identidad demo declarada, exclusivamente para tests sintéticos.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .policy import Policy, PolicyError, Rule


ROOT = Path(__file__).resolve().parent / "packs"
PACK_IDS = frozenset({"commerce", "contact_center", "integrators", "saas_b2b"})
REQUIRED_RULE_FIELDS = {"id", "tool", "effect", "role"}
ALLOWED_RULE_FIELDS = REQUIRED_RULE_FIELDS | {"min_amount_minor", "max_amount_minor"}


def load_pack(pack_id: str) -> Policy:
    if pack_id not in PACK_IDS:
        raise PolicyError("Pack desconocido; solo se permiten manifiestos auditados")
    path = ROOT / f"{pack_id}.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or data.get("id") != pack_id or data.get("status") != "lab":
        raise PolicyError("Pack no válido o no autorizado para laboratorio")
    if data.get("default_effect") != "deny" or data.get("operates_real_tools") is not False:
        raise PolicyError("El pack no puede activar permisos por defecto ni herramientas reales")
    content = data.get("rules")
    if not isinstance(content, list) or not 1 <= len(content) <= 40:
        raise PolicyError("Número de reglas fuera de 1..40")
    rules = []
    for record in content:
        if not isinstance(record, dict):
            raise PolicyError("La regla debe ser un objeto")
        if not REQUIRED_RULE_FIELDS.issubset(record) or set(record) - ALLOWED_RULE_FIELDS:
            raise PolicyError("Campos obligatorios o prohibidos en la regla")
        rules.append(Rule(**record))
    return Policy(tenant_id=data["demo_tenant_id"], version=data["version"], rules=tuple(rules))


def pack_metadata(pack_id: str) -> dict[str, Any]:
    """Ficha comercial de laboratorio, sin información identificable de personas."""
    if pack_id not in PACK_IDS:
        raise PolicyError("Pack desconocido")
    data = json.loads((ROOT / f"{pack_id}.json").read_text(encoding="utf-8"))
    return {
        "id": pack_id,
        "name": data["name"],
        "status": data["status"],
        "demo_tenant_id": data["demo_tenant_id"],
        "description": data["description"],
        "not_production": True,
    }
