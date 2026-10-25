from fastapi import APIRouter, HTTPException, Header, Depends
from sqlalchemy.orm import Session
from app.models.chat import ChatRequest
from app.services.audit import audit_prompt
from app.services.proxy import forward_request
from app.database import get_db
from app.models import AuditLog

router = APIRouter(prefix="/proxy/v1", tags=["Proxy"])

@router.post("/chat")
async def chat_proxy(
    request: ChatRequest, 
    authorization: str | None = Header(default=None),
    db: Session = Depends(get_db)
):
    # 1. Ejecutar auditoría y generar request_id único
    audit_result = await audit_prompt(request)
    
    # Determinar el estado o razón
    action = "ALLOWED"
    reason = None
    status_code_to_log = 200

    if not audit_result.allowed:
        action = "BLOCKED"
        reason = audit_result.reason
        
        # Guardar log de bloqueo en la base de datos antes de rechazar
        db_log = AuditLog(
            request_id=audit_result.request_id,
            model=request.model,
            prompt_preview=request.messages[-1].content[:255] if request.messages else "",
            action=action,
            reason=reason
        )
        db.add(db_log)
        db.commit()

        raise HTTPException(
            status_code=403,
            detail={
                "error": "Request blocked by TALIA policy",
                "request_id": audit_result.request_id,
                "reason": audit_result.reason
            }
        )
    
    # Extraer el token si viene en los headers del cliente
    api_key = None
    if authorization and authorization.startswith("Bearer "):
        api_key = authorization.split(" ")[1]

    # 2. Reenviar al proveedor upstream
    response_data = await forward_request(request, api_key=api_key)
    
    # Guardar log de éxito en la base de datos
    db_log = AuditLog(
        request_id=audit_result.request_id,
        model=request.model,
        prompt_preview=request.messages[-1].content[:255] if request.messages else "",
        action="ALLOWED",
        reason=None
    )
    db.add(db_log)
    db.commit()

    # Inyectar el request_id en la respuesta para trazabilidad completa
    if isinstance(response_data, dict):
        response_data["talia_request_id"] = audit_result.request_id

    # 3. Devolver la respuesta al cliente
    return response_data