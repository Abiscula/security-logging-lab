import json
from app.logging_config import logger

# Registra uma tentativa de login (sucesso ou falha)
def log_auth_attempt(username, ip, user_agent, success):
  logger.info(json.dumps({
    "type": "EVENT",
    "event": "AUTH_ATTEMPT",
    "user": username,
    "ip": ip,
    "user_agent": user_agent,
    "result": "SUCCESS" if success else "FAIL"
  }))

# Registra uma ação sensível executada no sistema (auditoria)
def log_sensitive_action(action, ip, user_agent):
  logger.warning(json.dumps({
    "type": "EVENT",
    "event": "SENSITIVE_ACTION",
    "action": action,
    "ip": ip,
    "user_agent": user_agent
  }))

# Registra um erro de sistema (incidente/falha)
def log_system_error(error, ip, user_agent):
  logger.error(json.dumps({
    "type": "EVENT",
    "event": "SYSTEM_ERROR",
    "error": error,
    "ip": ip,
    "user_agent": user_agent
  }))