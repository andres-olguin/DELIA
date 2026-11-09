"""Pasaporte de datos como metadatos de simulación; no aplica permisos fuera del proceso."""
from dataclasses import dataclass
from datetime import datetime, timezone

from .routing import LEVELS


@dataclass(frozen=True)
class DataPassport:
    tenant_id: str
    classification: str
    allowed_purposes: frozenset[str]
    expires_at: datetime

    def __post_init__(self) -> None:
        if not self.tenant_id or self.classification not in LEVELS or not self.allowed_purposes:
            raise ValueError("Pasaporte sin tenant, clasificación o finalidad")
        if self.expires_at.tzinfo is None:
            raise ValueError("Expiración debe incluir zona horaria")

    def allows(self, *, tenant_id: str, purpose: str, now: datetime) -> bool:
        if now.tzinfo is None:
            return False
        return (tenant_id == self.tenant_id and purpose in self.allowed_purposes
                and now.astimezone(timezone.utc) < self.expires_at.astimezone(timezone.utc))

    def derive(self, *, purpose_subset: frozenset[str],
               classification: str, expires_at: datetime) -> "DataPassport":
        if not purpose_subset or not purpose_subset.issubset(self.allowed_purposes):
            raise ValueError("No se puede ampliar finalidades")
        if classification not in LEVELS or LEVELS[classification] < LEVELS[self.classification]:
            raise ValueError("No se puede rebajar la clasificación")
        if expires_at.tzinfo is None or expires_at > self.expires_at:
            raise ValueError("No se puede ampliar expiración")
        return DataPassport(self.tenant_id, classification, purpose_subset, expires_at)
