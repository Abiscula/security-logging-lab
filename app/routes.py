from fastapi import APIRouter, Request, HTTPException

from app.DTO import LoginRequest, ActionRequest
from app.events import (
  log_auth_attempt,
  log_sensitive_action,
  log_system_error
)

router = APIRouter()

@router.post("/auth/login")
def login(data: LoginRequest, request: Request):
  ip = request.client.host
  agent = request.headers.get("user-agent")

  success = data.password == "123456"
  log_auth_attempt(data.username, ip, agent, success)

  if not success:
    raise HTTPException(
      status_code=400,
      detail="Dados inválidos"
    )

  return {"success": True}


@router.post("/admin/action")
def admin_action(data: ActionRequest, request: Request):
  ip = request.client.host
  agent = request.headers.get("user-agent")

  log_sensitive_action(data.action, ip, agent)
  return {"status": "Ação registrada"}


@router.get("/system/error")
def system_error(request: Request):
  ip = request.client.host
  agent = request.headers.get("user-agent")

  try:
    1 / 0
  except Exception as e:
    log_system_error(str(e), ip, agent)
    return {"error": "Falha no sistema"}