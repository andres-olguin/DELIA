from uuid import uuid4
from dataclasses import dataclass
from app.models.chat import ChatRequest

@dataclass
class AuditResult:
    allowed: bool
    request_id: str
    reason: str | None = None

async def audit_prompt(request: ChatRequest) -> AuditResult:
    # Generar ID único para la trazabilidad de la solicitud
    req_id = str(uuid4())
    
    for message in request.messages:
        if message.role == "user":
            prompt = message.content
            # Regla de prueba para verificar el bloqueo de políticas de TALIA
            if "PROMPT_BLOCK_TEST" in prompt:
                return AuditResult(
                    allowed=False,
                    request_id=req_id,
                    reason="Test policy triggered"
                )
                
    return AuditResult(allowed=True, request_id=req_id)