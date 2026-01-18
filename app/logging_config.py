import logging
import os
from app.logging.formatter import JsonFormatter

# Garante que o diretório de logs exista.
def ensure_log_directory(path: str = "logs") -> None:
  os.makedirs(path, exist_ok=True)


# Cria e configura o handler de arquivo com formatter JSON.
def create_file_handler(
  filepath: str = "logs/app.jsonl"
) -> logging.FileHandler:

  handler = logging.FileHandler(filepath)
  handler.setFormatter(JsonFormatter())
  return handler


# Configura e retorna o logger principal da aplicação.
def configure_logger(
  name: str = "security_lab",
  level: int = logging.INFO
) -> logging.Logger:
  
  ensure_log_directory()

  logger = logging.getLogger(name)
  logger.setLevel(level)

  if not logger.handlers:
    logger.addHandler(create_file_handler())

  logger.propagate = False
  return logger


logger = configure_logger()