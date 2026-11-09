"""Valida el catálogo exploratorio DELIA sin conexión, paquetes de terceros ni secretos."""
from __future__ import annotations
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs" / "estrategia" / "catalogo-productos.json"
ALLOWED_TYPES = {"sdk","saas","oem_partner","self_hosted","api","assurance_service","training","industry_module"}
ALLOWED_STATES = {"planned","lab","beta","available","retired"}
VALID_GATES = ["S0","S1","S2","S3","S4"]


def load_and_validate(path: Path = CATALOG) -> dict:
    catalog = json.loads(path.read_text(encoding="utf-8"))
    if catalog.get("schema_version") != "1.0":
        raise ValueError("unsupported schema_version")
    dt.date.fromisoformat(catalog["review_date"])
    brand = catalog["brand"]
    if brand.get("name") != "DELIA" or brand.get("alternate_official") is not False:
        raise ValueError("No cambiar identidad oficial por hipótesis sin aprobación")
    products = catalog.get("products")
    if not isinstance(products, list) or len(products) < 1:
        raise ValueError("Debe haber productos declarados")
    ids = set()
    for p in products:
        if not isinstance(p, dict) or not p.get("id") or p["id"] in ids:
            raise ValueError("ID duplicado o producto inválido")
        ids.add(p["id"])
        if p.get("type") not in ALLOWED_TYPES or p.get("state") not in ALLOWED_STATES:
            raise ValueError("Tipo o estado no permitido")
        dt.date.fromisoformat(p["first_target"])
        if not p.get("name", "").startswith("DELIA "):
            raise ValueError("Product naming debe mantener DELIA")
        if not p.get("pricing_model") or not p.get("evidence"):
            raise ValueError("Modelo e indicación de evidencia obligatorios")
    if catalog.get("security_gates") != VALID_GATES:
        raise ValueError("Secuencia S0..S4 incorrecta")
    if catalog.get("production_ready") is not False or catalog.get("security_certified") is not False:
        raise ValueError("Estado productivo/certificación no acreditado")
    if catalog.get("sales_verified") is not False or catalog.get("pricing_verified") is not False:
        raise ValueError("No existen ventas ni pricing verificados en esta revisión")
    for doc in catalog.get("source_docs", []):
        target = (ROOT / doc).resolve()
        if not target.is_relative_to(ROOT.resolve()) or not target.is_file():
            raise ValueError(f"Documento de respaldo inexistente o fuera del repo: {doc}")
    return catalog


if __name__ == "__main__":
    data = load_and_validate()
    print(f"DELIA strategy catalog OK: {len(data['products'])} editions; no available claims")
