from fastapi import HTTPException
from app.services.security_events import SecurityEvents
from app.services.login_attempts import LoginAttemptService
from app.enums.login_errors import LoginErrors

security_events = SecurityEvents()
login_attempt_service = LoginAttemptService()

# Trata tentativas de login quando o usuário já está bloqueado
def handle_blocked_login(username, ip, user_agent):
    security_events.log_auth_attempt(
        username=username,
        ip=ip,
        user_agent=user_agent,
        success=False,
        reason=LoginErrors.TOO_MANY_ATTEMPTS
    )

    raise HTTPException(
        status_code=429,
        detail="Muitas tentativas de login. Tente novamente mais tarde."
    )

# Trata falha de autenticação por credenciais inválidas
def handle_invalid_credentials(username, ip, user_agent, attempt_key):
    login_attempt_service.register_failed_attempt(attempt_key)

    security_events.log_auth_attempt(
        username=username,
        ip=ip,
        user_agent=user_agent,
        success=False,
        reason=LoginErrors.INVALID_CREDENTIALS
    )

    raise HTTPException(
        status_code=400,
        detail="Dados inválidos"
    )

# Fluxo de sucesso
def handle_successful_login(username, ip, user_agent):
    security_events.log_auth_attempt(
        username=username,
        ip=ip,
        user_agent=user_agent,
        success=True
    )

    return {"success": True}