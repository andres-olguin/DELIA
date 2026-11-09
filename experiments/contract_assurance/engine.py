"""DELIA Outcome Assurance — *LABORATORIO SIN EFECTOS EXTERNOS*.

Evalúa invariantes de negocio y reconcilia una respuesta simulada, separando:
- validación previa de estado de negocio,
- autorización real (NO implementada aquí),
- ejecución por proveedor (NO implementada aquí),
- confirmación independiente del resultado (NO implementada; se simula).

NO es un control de producción: todos los estados son declarados por el llamante;
no hay verificación de identidad, locks de DB, idempotencia durable, ni acceso al
libro mayor del proveedor. Nunca usar con dinero, personas o datos reales.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from typing import Any


class ContractError(ValueError):
    """Entrada o definición de contrato inválida; no continuar."""


def _integer_amount(value: Any) -> bool:
    return type(value) is int and value >= 0


def _key(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip() or len(value) > 128:
        raise ContractError(f"{field}: texto no vacío hasta 128 caracteres")
    return value


def _digest(value: dict) -> str:
    try:
        payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                             allow_nan=False).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ContractError("La estructura debe ser JSON válido") from exc
    if len(payload) > 65536:
        raise ContractError("Tamaño excesivo para el laboratorio")
    return hashlib.sha256(payload).hexdigest()


@dataclass(frozen=True)
class RefundContract:
    contract_id: str
    version: int
    currency: str
    max_amount_minor: int
    require_customer_verification: bool = True
    require_paid_order: bool = True

    def __post_init__(self) -> None:
        _key(self.contract_id, "contract_id")
        if type(self.version) is not int or self.version <= 0:
            raise ContractError("La versión debe ser entero positivo")
        if self.currency not in {"CLP", "MXN", "COP", "PEN", "BRL"}:
            raise ContractError("Moneda regional no autorizada por este laboratorio")
        if not _integer_amount(self.max_amount_minor) or self.max_amount_minor == 0:
            raise ContractError("max_amount_minor debe ser entero positivo")
        if type(self.require_customer_verification) is not bool or type(self.require_paid_order) is not bool:
            raise ContractError("Los flags deben ser booleanos")

    @property
    def digest(self) -> str:
        return _digest(self.__dict__)


@dataclass(frozen=True)
class RefundProposal:
    tenant_id: str
    order_id: str
    operation_id: str
    amount_minor: int
    currency: str
    observed_state_version: int

    def __post_init__(self) -> None:
        for field in ("tenant_id", "order_id", "operation_id"):
            _key(getattr(self, field), field)
        if not _integer_amount(self.amount_minor) or self.amount_minor == 0:
            raise ContractError("amount_minor debe ser entero positivo")
        if type(self.observed_state_version) is not int or self.observed_state_version < 0:
            raise ContractError("observed_state_version inválida")

    @property
    def digest(self) -> str:
        return _digest(self.__dict__)


@dataclass(frozen=True)
class OrderSnapshot:
    tenant_id: str
    order_id: str
    state_version: int
    order_status: str
    paid_minor: int
    refunded_minor: int
    customer_verified: bool
    known_operations: frozenset[str]

    def __post_init__(self) -> None:
        _key(self.tenant_id, "tenant_id")
        _key(self.order_id, "order_id")
        if type(self.state_version) is not int or self.state_version < 0:
            raise ContractError("state_version inválida")
        if not all(_integer_amount(v) for v in (self.paid_minor, self.refunded_minor)):
            raise ContractError("Montos de snapshot inválidos")
        if self.refunded_minor > self.paid_minor:
            raise ContractError("Snapshot inconsistente: reembolsado supera pagado")
        if type(self.customer_verified) is not bool:
            raise ContractError("customer_verified inválido")
        if not isinstance(self.known_operations, frozenset):
            raise ContractError("known_operations debe ser conjunto congelado")
        for value in self.known_operations:
            _key(value, "known_operation")


@dataclass(frozen=True)
class GateResult:
    outcome: str  # ELIGIBLE_FOR_AUTHORIZATION o DENY (nunca ejecuta)
    reasons: tuple[str, ...]
    contract_hash: str
    proposal_hash: str

    @property
    def is_authorized(self) -> bool:
        """Siempre falso: la verificación del negocio no autentica ni autoriza."""
        return False


def preflight(contract: RefundContract, proposal: RefundProposal, snapshot: OrderSnapshot) -> GateResult:
    """Deny si fallan invariantes. Caso positivo SOLO puede ir a autorización externa."""
    reasons: list[str] = []
    if proposal.tenant_id != snapshot.tenant_id:
        reasons.append("TENANT_MISMATCH")
    if proposal.order_id != snapshot.order_id:
        reasons.append("ORDER_MISMATCH")
    if proposal.observed_state_version != snapshot.state_version:
        reasons.append("STATE_STALE")
    if proposal.currency != contract.currency:
        reasons.append("CURRENCY_MISMATCH")
    if proposal.amount_minor > contract.max_amount_minor:
        reasons.append("CONTRACT_LIMIT")
    if contract.require_paid_order and snapshot.order_status != "paid":
        reasons.append("ORDER_NOT_PAID")
    if contract.require_customer_verification and not snapshot.customer_verified:
        reasons.append("CUSTOMER_NOT_VERIFIED")
    if proposal.operation_id in snapshot.known_operations:
        reasons.append("OPERATION_ALREADY_SEEN")
    if proposal.amount_minor > snapshot.paid_minor - snapshot.refunded_minor:
        reasons.append("REFUND_EXCEEDS_BALANCE")
    return GateResult("DENY" if reasons else "ELIGIBLE_FOR_AUTHORIZATION",
                      tuple(sorted(reasons)), contract.digest, proposal.digest)


@dataclass(frozen=True)
class SettlementObservation:
    """Observación sintética. No representa respuesta autenticada de un proveedor."""
    tenant_id: str
    operation_id: str
    proposal_hash: str
    provider_state: str  # confirmed, rejected, pending, unknown
    observed_amount_minor: int | None

    def __post_init__(self) -> None:
        _key(self.tenant_id, "tenant_id")
        _key(self.operation_id, "operation_id")
        if self.provider_state not in {"confirmed", "rejected", "pending", "unknown"}:
            raise ContractError("provider_state inválido")
        if self.observed_amount_minor is not None and not _integer_amount(self.observed_amount_minor):
            raise ContractError("observed_amount_minor inválido")


@dataclass(frozen=True)
class Reconciliation:
    outcome: str  # VERIFIED_SIMULATED / REJECTED / HOLD / MISMATCH
    reason: str


def reconcile(proposal: RefundProposal, observation: SettlementObservation) -> Reconciliation:
    """Solo comparar dos estructuras sintéticas: no inferir ejecución real."""
    if observation.tenant_id != proposal.tenant_id or observation.operation_id != proposal.operation_id:
        return Reconciliation("MISMATCH", "Identidad de operación/tenant divergente")
    if observation.proposal_hash != proposal.digest:
        return Reconciliation("MISMATCH", "Hash de operación divergente")
    if observation.provider_state in {"unknown", "pending"}:
        return Reconciliation("HOLD", "Resultado no confirmado: requiere consultar fuente autorizada")
    if observation.provider_state == "rejected":
        return Reconciliation("REJECTED", "Operación simulada rechazada")
    if observation.observed_amount_minor != proposal.amount_minor:
        return Reconciliation("MISMATCH", "Importe observado no coincide")
    return Reconciliation("VERIFIED_SIMULATED", "Coincidencia de reporte sintético; NO verificación real")


def load_refund_contract(path) -> RefundContract:
    """Carga manifiesto de un archivo local explícitamente seleccionado por el operador."""
    from pathlib import Path
    p = Path(path)
    data = json.loads(p.read_text(encoding="utf-8"))
    allowed = {"contract_id", "version", "currency", "max_amount_minor",
               "require_customer_verification", "require_paid_order",
               "status", "disclaimer"}
    if not isinstance(data, dict) or set(data) - allowed or data.get("status") != "LAB":
        raise ContractError("Contrato no permitido o campos no reconocidos")
    if not {"contract_id", "version", "currency", "max_amount_minor"}.issubset(data):
        raise ContractError("Faltan campos obligatorios")
    return RefundContract(**{k: v for k, v in data.items() if k not in {"status", "disclaimer"}})
