from app.logging_config import logger

# Registra uma tentativa de login (sucesso ou falha)
def log_auth_attempt(username, ip, user_agent, success):
  result = "SUCCESS" if success else "FAIL"
  logger.info(
    f"EVENT=AUTH_ATTEMPT user={username} ip={ip} agent='{user_agent}' result={result}"
  )

# Registra uma ação sensível executada no sistema (auditoria)
def log_sensitive_action(action, ip, user_agent):
  logger.warning(
    f"EVENT=SENSITIVE_ACTION action={action} ip={ip} agent='{user_agent}'"
  )

# Registra um erro de sistema (incidente/falha)
def log_system_error(error, ip, user_agent):
  logger.error(
    f"EVENT=SYSTEM_ERROR error='{error}' ip={ip} agent='{user_agent}'"
  )