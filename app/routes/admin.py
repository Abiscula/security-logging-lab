from fastapi import APIRouter, Request
from app.DTO import ActionRequest
from app.events import log_sensitive_action

router = APIRouter(
  prefix="/admin",
  tags=["Admin"]
)

@router.post("/action")
def admin_action(data: ActionRequest, request: Request):
  ip = request.state.ip
  agent = request.state.user_agent

  log_sensitive_action(data.action, ip, agent)
  return {"status": "Ação registrada"}