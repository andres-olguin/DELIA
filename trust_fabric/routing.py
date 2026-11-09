"""Planeador de rutas por sensibilidad y región, sin llamadas de red."""
from dataclasses import dataclass


LEVELS = {"PUBLIC": 0, "INTERNAL": 1, "CONFIDENTIAL": 2, "RESTRICTED": 3}


@dataclass(frozen=True)
class Destination:
    name: str
    region: str
    max_level: str
    approved: bool

    def __post_init__(self) -> None:
        if not self.name or not self.region or self.max_level not in LEVELS:
            raise ValueError("Destino inválido")


@dataclass(frozen=True)
class RoutePlan:
    outcome: str
    destination: str | None
    reason: str


def select_route(*, requested_region: str, sensitivity: str,
                 destinations: tuple[Destination, ...]) -> RoutePlan:
    if sensitivity not in LEVELS or not requested_region:
        return RoutePlan("DENY", None, "Sensibilidad o región no reconocida")
    eligible = [d for d in destinations if d.approved and d.region == requested_region
                and LEVELS[d.max_level] >= LEVELS[sensitivity]]
    if not eligible:
        return RoutePlan("DENY", None, "Sin destino permitido para región y sensibilidad")
    candidate = sorted(eligible, key=lambda d: (LEVELS[d.max_level], d.name))[0]
    return RoutePlan("PLAN_ONLY", candidate.name, "Ruta candidata, sin verificación legal ni egress")
