"""DELIA Trust Fabric: motor local experimental de decisiones para agentes.

Este paquete no reenvía peticiones, no autentica usuarios remotos ni garantiza
seguridad de producción. Solo sirve para evaluación determinista y simulación.
"""
from .policy import (
    Action, Rule, Policy, Decision, Receipt, PolicyEngine, PolicyError,
)
__all__ = ["Action", "Rule", "Policy", "Decision", "Receipt", "PolicyEngine", "PolicyError"]
