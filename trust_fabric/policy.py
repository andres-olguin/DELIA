"""Políticas deny-by-default, aprobación de acciones y evidencia mínima en memoria.

Seguridad: este módulo es un PROTOTIPO DE LABORATORIO.
- Las identidades y el tenant proceden del llamante (no hay autenticación).
- No ejecuta herramientas ni redirige tráfico, solo evalúa solicitudes.
- Los tickets y eventos viven en memoria; reiniciar borra su estado.
- El HMAC acredita integridad de UN recibo con clave mantenida fuera del artefacto,
  no certifica que un sistema externo haya obedecido la decisión.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import secrets
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta, timezone
from typing import Any, Callable, Mapping


class PolicyError(ValueError):
    """Política malformada: no continuar ni permitir por defecto."""


def _canonical(value: Any) -> bytes:
    try:
        data = json.dumps(
            value, ensure_ascii=False, sort_keys=True, separators=(",", ":"),
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError, OverflowError) as exc:
        raise PolicyError("Los argumentos deben ser JSON finito") from exc
    if len(data) > 65536:
        raise PolicyError("Argumentos demasiado grandes para el simulador")
    return data


def _sha(value: Any) -> str:
    return hashlib.sha256(_canonical(value)).hexdigest()


def _required(label: str, value: str) -> None:
    if not isinstance(value, str) or not value.strip() or len(value) > 256:
        raise PolicyError(f"{label} debe ser texto no vacío de hasta 256 caracteres")


@dataclass(frozen=True)
class Action:
    tenant_id: str
    agent_id: str
    role: str
    tool: str
    arguments: Mapping[str, Any]

    def __post_init__(self) -> None:
        for key in ("tenant_id", "agent_id", "role", "tool"):
            _required(key, getattr(self, key))
        if not isinstance(self.arguments, Mapping):
            raise PolicyError("arguments debe ser un mapa JSON")
        _canonical(self.arguments)

    @property
    def fingerprint(self) -> str:
        return _sha({
            "tenant_id": self.tenant_id,
            "agent_id": self.agent_id,
            "role": self.role,
            "tool": self.tool,
            "arguments": self.arguments,
        })


@dataclass(frozen=True)
class Rule:
    id: str
    tool: str
    effect: str  # allow, deny, approve
    role: str
    min_amount_minor: int | None = None
    max_amount_minor: int | None = None

    def __post_init__(self) -> None:
        _required("rule.id", self.id)
        _required("rule.tool", self.tool)
        _required("rule.role", self.role)
        if self.effect not in {"allow", "deny", "approve"}:
            raise PolicyError("effect debe ser allow, deny o approve")
        for amount in (self.min_amount_minor, self.max_amount_minor):
            if amount is not None and (type(amount) is not int or amount < 0):
                raise PolicyError("Montos en unidades menores deben ser enteros >= 0")
        if (self.min_amount_minor is not None and self.max_amount_minor is not None
                and self.min_amount_minor > self.max_amount_minor):
            raise PolicyError("Rango de montos invertido")

    def matches(self, action: Action) -> bool:
        if self.tool != action.tool or self.role != action.role:
            return False
        if self.min_amount_minor is None and self.max_amount_minor is None:
            return True
        amount = action.arguments.get("amount_minor")
        if type(amount) is not int or amount < 0:
            return False
        return ((self.min_amount_minor is None or amount >= self.min_amount_minor)
                and (self.max_amount_minor is None or amount <= self.max_amount_minor))


@dataclass(frozen=True)
class Policy:
    tenant_id: str
    version: int
    rules: tuple[Rule, ...]
    default_effect: str = "deny"

    def __post_init__(self) -> None:
        _required("policy.tenant_id", self.tenant_id)
        if type(self.version) is not int or self.version < 1:
            raise PolicyError("version debe ser entero >= 1")
        if self.default_effect != "deny":
            raise PolicyError("El motor solo admite política por defecto DENY")
        if len({r.id for r in self.rules}) != len(self.rules):
            raise PolicyError("IDs de reglas duplicados")

    @property
    def digest(self) -> str:
        return _sha({
            "tenant_id": self.tenant_id,
            "version": self.version,
            "default_effect": self.default_effect,
            "rules": [asdict(r) for r in self.rules],
        })


@dataclass(frozen=True)
class Receipt:
    event_id: str
    tenant_hash: str
    agent_hash: str
    tool: str
    outcome: str
    action_hash: str
    policy_hash: str
    timestamp: str
    signature: str


@dataclass(frozen=True)
class Decision:
    outcome: str  # ALLOW / DENY / PENDING_APPROVAL
    reason: str
    receipt: Receipt
    approval_id: str | None = None

    @property
    def may_execute(self) -> bool:
        return self.outcome == "ALLOW"


@dataclass
class _Approval:
    tenant_id: str
    agent_id: str
    action_hash: str
    policy_hash: str
    expires_at: datetime
    approved_by: str | None = None
    used: bool = False


class PolicyEngine:
    """Controlador experimental SIN conexiones externas ni autenticación web."""

    def __init__(
        self, secret: bytes, *, approver_roles: frozenset[str],
        clock: Callable[[], datetime] | None = None, approval_ttl_seconds: int = 300,
    ) -> None:
        if not isinstance(secret, bytes) or len(secret) < 32:
            raise PolicyError("Usar una clave aleatoria de >= 32 bytes, nunca en repositorio")
        if not approver_roles or not all(isinstance(v, str) and v for v in approver_roles):
            raise PolicyError("Configurar roles de aprobadores explícitos")
        if type(approval_ttl_seconds) is not int or not 1 <= approval_ttl_seconds <= 3600:
            raise PolicyError("approval_ttl_seconds fuera de 1..3600")
        self._secret = secret
        self._roles = frozenset(approver_roles)
        self._clock = clock or (lambda: datetime.now(timezone.utc))
        self._ttl = approval_ttl_seconds
        self._policies: dict[str, Policy] = {}
        self._approvals: dict[str, _Approval] = {}
        self._receipts: list[Receipt] = []

    def _now(self) -> datetime:
        now = self._clock()
        if now.tzinfo is None or now.utcoffset() is None:
            raise PolicyError("El reloj debe utilizar zona horaria")
        return now.astimezone(timezone.utc)

    def register(self, policy: Policy) -> None:
        previous = self._policies.get(policy.tenant_id)
        if previous and policy.version <= previous.version:
            raise PolicyError("Una nueva política requiere versión estrictamente superior")
        self._policies[policy.tenant_id] = policy

    @property
    def receipts(self) -> tuple[Receipt, ...]:
        """Solo metadatos minimizados; nunca argumentos ni prompt original."""
        return tuple(self._receipts)

    def _receipt(self, action: Action, policy_hash: str, outcome: str) -> Receipt:
        fields = {
            "event_id": secrets.token_hex(16),
            "tenant_hash": _sha(action.tenant_id),
            "agent_hash": _sha(action.agent_id),
            "tool": action.tool,
            "outcome": outcome,
            "action_hash": action.fingerprint,
            "policy_hash": policy_hash,
            "timestamp": self._now().isoformat(),
        }
        signature = hmac.new(self._secret, _canonical(fields), hashlib.sha256).hexdigest()
        receipt = Receipt(**fields, signature=signature)
        self._receipts.append(receipt)
        return receipt

    def verify(self, receipt: Receipt) -> bool:
        try:
            fields = asdict(receipt)
            signed = fields.pop("signature")
            expected = hmac.new(self._secret, _canonical(fields), hashlib.sha256).hexdigest()
            return hmac.compare_digest(expected, signed)
        except (PolicyError, TypeError):
            return False

    def decide(self, action: Action, *, approval_id: str | None = None) -> Decision:
        policy = self._policies.get(action.tenant_id)
        policy_hash = policy.digest if policy else "none"
        if policy is None:
            return Decision("DENY", "Tenant sin política registrada", self._receipt(action, policy_hash, "DENY"))
        matches = [r for r in policy.rules if r.matches(action)]
        # En conflictos, prevalece deny > approve > allow, independientemente del orden.
        if any(r.effect == "deny" for r in matches):
            effect = "deny"
        elif any(r.effect == "approve" for r in matches):
            effect = "approve"
        elif any(r.effect == "allow" for r in matches):
            effect = "allow"
        else:
            effect = policy.default_effect

        if effect == "deny":
            return Decision("DENY", "Política deniega o no permite la operación", self._receipt(action, policy_hash, "DENY"))
        if effect == "allow":
            return Decision("ALLOW", "Regla explícita permite la operación", self._receipt(action, policy_hash, "ALLOW"))
        if approval_id:
            request = self._approvals.get(approval_id)
            if (request and not request.used and request.approved_by
                and request.tenant_id == action.tenant_id
                and request.agent_id == action.agent_id
                and hmac.compare_digest(request.action_hash, action.fingerprint)
                and hmac.compare_digest(request.policy_hash, policy_hash)
                and self._now() < request.expires_at):
                request.used = True
                return Decision("ALLOW", "Aprobación válida consumida una sola vez", self._receipt(action, policy_hash, "ALLOW"))
            return Decision("DENY", "Aprobación ausente, vencida, usada o no vinculada", self._receipt(action, policy_hash, "DENY"))

        identifier = secrets.token_urlsafe(24)
        self._approvals[identifier] = _Approval(
            tenant_id=action.tenant_id,
            agent_id=action.agent_id,
            action_hash=action.fingerprint,
            policy_hash=policy_hash,
            expires_at=self._now() + timedelta(seconds=self._ttl),
        )
        return Decision("PENDING_APPROVAL", "Requiere aprobación humana independiente",
                        self._receipt(action, policy_hash, "PENDING_APPROVAL"), identifier)

    def approve(self, approval_id: str, *, tenant_id: str, approver_id: str, approver_role: str) -> bool:
        """Confirma aprobación en memoria; nunca ejecuta herramientas."""
        _required("approver_id", approver_id)
        _required("tenant_id", tenant_id)
        request = self._approvals.get(approval_id)
        if (not request or request.used or request.approved_by
            or tenant_id != request.tenant_id
            or approver_role not in self._roles
            or approver_id == request.agent_id
            or self._now() >= request.expires_at):
            return False
        current = self._policies.get(tenant_id)
        if not current or not hmac.compare_digest(current.digest, request.policy_hash):
            return False
        request.approved_by = approver_id
        return True
