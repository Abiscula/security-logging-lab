from fastapi import APIRouter, Request, HTTPException

from app.schemas.auth import LoginRequest
from app.services.security_events import log_auth_attempt
from app.enums.login_errors import LoginErrors
from app.services.login_attempts import (
  register_failed_attempt,
  is_blocked
)

router = APIRouter(
  prefix="/auth",
  tags=["Auth"]
)

@router.post("/login")
def login(data: LoginRequest, request: Request):
    ip = request.state.ip
    user_agent = request.state.user_agent

    attempt_key = f"{data.username}:{ip}"

    # verifica se já está bloqueado
    if is_blocked(attempt_key):
        log_auth_attempt(
            username=data.username,
            ip=ip,
            user_agent=user_agent,
            success=False,
            reason=LoginErrors.TOO_MANY_ATTEMPTS
        )
        raise HTTPException(
            status_code=429,
            detail="Muitas tentativas de login. Tente novamente mais tarde."
        )

    # 2valida credenciais
    password_matches = data.password == "123456"

    if not password_matches:
        register_failed_attempt(attempt_key)

        log_auth_attempt(
            username=data.username,
            ip=ip,
            user_agent=user_agent,
            success=False,
            reason=LoginErrors.INVALID_CREDENTIALS
        )

        raise HTTPException(
            status_code=400,
            detail="Dados inválidos"
        )

    # sucesso
    log_auth_attempt(
        username=data.username,
        ip=ip,
        user_agent=user_agent,
        success=True
    )

    return {"success": True}