from fastapi import APIRouter, Request, HTTPException
from app.schemas.auth import LoginRequest
from app.services.security_events import log_auth_attempt
from app.enums.login_errors import LoginErrors

router = APIRouter(
  prefix="/auth",
  tags=["Auth"]
)


@router.post("/login")
def login(data: LoginRequest, request: Request):
  ip = request.state.ip
  user_agent = request.state.user_agent

  password_matches = data.password == "123456"

  log_auth_attempt(
    username=data.username,
    ip=ip,
    user_agent=user_agent,
    success=password_matches,
    reason=None if password_matches else LoginErrors.INVALID_CREDENTIALS
  )

  if not password_matches:
    raise HTTPException(
      status_code=400,
      detail="Dados inválidos"
    )

  return {"success": True}