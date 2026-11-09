"""Agregación local de recibos sin incluir argumentos ni agentes en salida."""
from collections import Counter
from typing import Iterable

from .policy import Receipt


def aggregate_receipts(receipts: Iterable[Receipt]) -> dict:
    counts = Counter()
    tools = Counter()
    for receipt in receipts:
        counts[receipt.outcome] += 1
        tools[receipt.tool] += 1
    return {
        "mode": "LOCAL_LAB_ONLY",
        "total_decisions": sum(counts.values()),
        "by_outcome": dict(sorted(counts.items())),
        "by_tool": dict(sorted(tools.items())),
    }
