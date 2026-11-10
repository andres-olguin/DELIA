"""Synthetic audit experiment; NOT a production authorization decision."""
from dataclasses import dataclass
from uuid import uuid4

from models.chat import ChatRequest


@dataclass(frozen=True)
class AuditResult:
    allowed: bool
    request_id: str
    reason: str | None = None


async def audit_prompt(request: ChatRequest) -> AuditResult:
    request_id = str(uuid4())
    # This is a synthetic regression sentinel, not a data protection policy.
    for message in request.messages:
        if message.role == "user" and "PROMPT_BLOCK_TEST" in message.content:
            return AuditResult(False, request_id, "Synthetic test sentinel")
    return AuditResult(True, request_id)
