from typing import Optional

from app.logging_config import logger
from app.enums.log_type import LogType
from app.enums.log_event import LogEvent
from app.enums.login_errors import LoginErrors

class SecurityEvents:

  # Registra uma tentativa de login (sucesso ou falha)
  def log_auth_attempt(
    self,
    username: str,
    ip: str,
    user_agent: str,
    success: bool,
    reason: Optional[LoginErrors] = None
  ):
    payload = {
      "type": LogType.EVENT,
      "event": LogEvent.AUTH_ATTEMPT,
      "user": username,
      "result": "SUCCESS" if success else "FAIL",
      "ip": ip,
      "user_agent": user_agent
    }

    if not success and reason is not None:
      payload["reason"] = reason

    logger.info("auth attempt", extra=payload)

  # Registra uma ação sensível executada no sistema (auditoria)
  def log_sensitive_action(self, action, ip, user_agent):
    logger.warning(
      "sensitive action",
      extra={
        "type": LogType.EVENT,
        "event": LogEvent.SENSITIVE_ACTION,
        "action": action,
        "ip": ip,
        "user_agent": user_agent
      }
    )

  # Registra um erro de sistema (incidente/falha)
  def log_system_error(self, error, ip, user_agent):
    logger.error(
      "system error",
      extra={
        "type": LogType.EVENT,
        "event": LogEvent.SYSTEM_ERROR,
        "error": error,
        "ip": ip,
        "user_agent": user_agent
      }
    )