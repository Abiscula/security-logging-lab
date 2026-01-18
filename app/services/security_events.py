import json
from app.logging_config import logger

from app.logging_config import logger

# Registra uma tentativa de login (sucesso ou falha)
def log_auth_attempt(username, ip, user_agent, success):
  logger.info(
    "auth attempt",
    extra={
      "type": "EVENT",
      "event": "AUTH_ATTEMPT",
      "user": username,
      "result": "SUCCESS" if success else "FAIL",
      "ip": ip,
      "user_agent": user_agent
    }
  )

# Registra uma ação sensível executada no sistema (auditoria)
def log_sensitive_action(action, ip, user_agent):
  logger.warning(
    "sensitive action",
    extra={
      "type": "EVENT",
      "event": "SENSITIVE_ACTION",
      "action": action,
      "ip": ip,
      "user_agent": user_agent
    }
  )

# Registra um erro de sistema (incidente/falha)
def log_system_error(error, ip, user_agent):
  logger.error(
    "system error",
    extra={
      "type": "EVENT",
      "event": "SYSTEM_ERROR",
      "error": error,
      "ip": ip,
      "user_agent": user_agent
    }
  )