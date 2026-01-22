from fastapi import APIRouter, Request
from app.schemas.admin import ActionRequest
from app.services.security_events import SecurityEvents

security_events = SecurityEvents()

router = APIRouter(
  prefix="/admin",
  tags=["Admin"]
)

@router.post("/action")
def admin_action(data: ActionRequest, request: Request):
  ip = request.state.ip
  agent = request.state.user_agent

  security_events.log_sensitive_action(data.action, ip, agent)
  return {"status": "Ação registrada"}