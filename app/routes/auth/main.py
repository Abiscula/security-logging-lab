from fastapi import APIRouter, Request
from app.schemas.auth import LoginRequest
from app.services.login_attempts import LoginAttemptService
from app.routes.auth.handlers import (
    handle_blocked_login,
    handle_invalid_credentials,
    handle_successful_login
)

loginAttemptService = LoginAttemptService()

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(data: LoginRequest, request: Request):
    ip = request.state.ip
    user_agent = request.state.user_agent
    attempt_key = f"{data.username}:{ip}"

    if loginAttemptService.is_blocked(attempt_key):
        return handle_blocked_login(data.username, ip, user_agent)

    password_matches = data.password == "123456"

    if not password_matches:
        return handle_invalid_credentials(
            data.username,
            ip,
            user_agent,
            attempt_key
        )

    return handle_successful_login(
        data.username,
        ip,
        user_agent
    )