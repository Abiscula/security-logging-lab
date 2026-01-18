from fastapi import APIRouter, Request, HTTPException
from app.schemas.auth import LoginRequest
from app.services.security_events import log_auth_attempt

router = APIRouter(
  prefix="/auth",
  tags=["Auth"]
)

@router.post("/login")
def login(data: LoginRequest, request: Request):
  ip = request.state.ip
  agent = request.state.user_agent

  success = data.password == "123456"
  log_auth_attempt(data.username, ip, agent, success)

  if not success:
    raise HTTPException(status_code=400, detail="Dados inválidos")

  return {"success": True}