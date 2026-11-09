"""Fail-closed placeholder for the old direct forwarding helper.

The old implementation emitted request.model_dump() and potentially forwarded
a caller-supplied Bearer token. No live forwarding is allowed here until an
authenticated provider adapter + mandatory policy enforcement is developed.
"""
from fastapi import HTTPException
from models.chat import ChatRequest


async def forward_request(request: ChatRequest, api_key: str | None = None):
    # Prevent bypass from code paths importing this helper directly.
    raise HTTPException(status_code=503, detail="Upstream forwarding is disabled")
