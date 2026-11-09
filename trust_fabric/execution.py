"""Simulador cerrado de tools: solo modifica un ledger ficticio en memoria.

NO es un adaptador de producción: no autentica el principal, no usa base de
datos, no garantiza atómicidad multiproceso y no ejecuta pagos o proveedores.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any

from .policy import Action, Decision, PolicyEngine


@dataclass(frozen=True)
class ExecutionResult:
    decision: Decision
    executed: bool
    synthetic_result: dict[str, Any] | None


class FakeToolEnvironment:
    """Un conjunto fijo de herramientas simuladas, sin callbacks arbitrarios."""

    def __init__(self, engine: PolicyEngine) -> None:
        self.engine = engine
        self._refunds: list[str] = []

    @property
    def synthetic_refunds(self) -> tuple[str, ...]:
        return tuple(self._refunds)

    def invoke(self, action: Action, *, approval_id: str | None = None) -> ExecutionResult:
        decision = self.engine.decide(action, approval_id=approval_id)
        if not decision.may_execute:
            return ExecutionResult(decision, False, None)
        if action.tool == "refund.issue":
            amount = action.arguments.get("amount_minor")
            currency = action.arguments.get("currency")
            if type(amount) is not int or amount <= 0 or currency != "MXN":
                # No se ejecuta aunque la política lo permita; entorno de test exige esquema.
                return ExecutionResult(decision, False, None)
            fake_id = f"FAKE-{len(self._refunds) + 1:04d}"
            self._refunds.append(fake_id)
            return ExecutionResult(decision, True, {"simulation_id": fake_id, "mode": "FAKE"})
        if action.tool == "invoice.read":
            return ExecutionResult(decision, True, {"invoice": "FAKE-001", "mode": "FAKE"})
        return ExecutionResult(decision, False, None)
