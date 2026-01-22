import logging
import os
from app.logging.formatter import JsonFormatter

class LoggingConfig:

    def __init__(self, name="security_lab", level=logging.INFO, path="logs/app.jsonl"):
        self.name = name
        self.level = level
        self.path = path

    # Garante que o diretório de logs exista
    def ensure_log_directory(self):
        os.makedirs("logs", exist_ok=True)

    # Cria o handler de arquivo
    def create_file_handler(self):
        handler = logging.FileHandler(self.path)
        handler.setFormatter(JsonFormatter())
        return handler

    # Cria e retorna o logger configurado
    def build_logger(self) -> logging.Logger:
        self.ensure_log_directory()

        logger = logging.getLogger(self.name)
        logger.setLevel(self.level)

        if not logger.handlers:
            logger.addHandler(self.create_file_handler())

        logger.propagate = False
        return logger
    
logging_config = LoggingConfig()
logger = logging_config.build_logger()