"""Production proxy route is disabled until authentication + pre-egress DLP.

Do not replace this with a simple 'allowed' audit check: the old flow forwarded
the caller's raw messages and bearer credential to the upstream provider.
The public synthetic demonstration is independent of this endpoint.
"""
from fastapi import APIRouter, HTTPException
from models.chat import ChatRequest

router = APIRouter(prefix="/proxy/v1", tags=["Experimental proxy"])


@router.post("/chat")
async def chat_proxy(request: ChatRequest):
    # The request is intentionally not logged, persisted or forwarded.
    # Re-enable only after SEC-002/003/004 are independently verified.
    raise HTTPException(
        status_code=503,
        detail="Proxy disabled until identity, pre-egress DLP and audit gates pass",
    )
