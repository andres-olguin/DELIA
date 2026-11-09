"""Ensayos sintéticos y métricas de decisión; no pentesting real."""
from __future__ import annotations
from dataclasses import dataclass

from .policy import Action, PolicyEngine


@dataclass(frozen=True)
class Scenario:
    name: str
    action: Action
    expected: str


def evaluate_scenarios(engine: PolicyEngine, scenarios: tuple[Scenario, ...]) -> dict:
    outcomes = []
    for scenario in scenarios:
        decision = engine.decide(scenario.action)
        outcomes.append({
            "name": scenario.name,
            "expected": scenario.expected,
            "observed": decision.outcome,
            "passed": decision.outcome == scenario.expected,
        })
    passed = sum(item["passed"] for item in outcomes)
    return {
        "mode": "SYNTHETIC_POLICY_TEST",
        "cases": len(outcomes),
        "passed": passed,
        "failed": len(outcomes) - passed,
        "outcomes": outcomes,
    }
