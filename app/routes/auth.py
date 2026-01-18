from fastapi import APIRouter, Request, HTTPException
from app.DTO import LoginRequest
from app.events import log_auth_attempt

router = APIRouter(
  prefix="/auth",
  tags=["Auth"]
)

@router.post("/login")
def login(data: LoginRequest, request: Request):
  ip = request.client.host
  agent = request.headers.get("user-agent")

  success = data.password == "123456"
  log_auth_attempt(data.username, ip, agent, success)

  if not success:
    raise HTTPException(status_code=400, detail="Dados inválidos")

  return {"success": True}