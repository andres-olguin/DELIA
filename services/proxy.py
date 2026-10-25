import httpx
from fastapi import HTTPException
from app.models.chat import ChatRequest

# URL temporal o de prueba del proveedor de IA upstream (puedes ajustarla según el proveedor que utilices)
UPSTREAM_URL = "https://api.openai.com/v1/chat/completions"

async def forward_request(request: ChatRequest, api_key: str | None = None):
    payload = request.model_dump(exclude_none=True)
    
    headers = {
        "Content-Type": "application/json",
    }
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"

    try:
        async with httpx.AsyncClient(timeout=30.0) as client:
            response = await client.post(
                UPSTREAM_URL,
                json=payload,
                headers=headers
            )
            response.raise_for_status()
            return response.json()
            
    except httpx.TimeoutException:
        raise HTTPException(
            status_code=504,
            detail="Upstream provider timeout"
        )
    except httpx.HTTPStatusError as exc:
        raise HTTPException(
            status_code=502,
            detail=f"Upstream provider error: {exc.response.status_code}"
        )
    except httpx.RequestError:
        raise HTTPException(
            status_code=502,
            detail="Unable to reach upstream provider"
        )