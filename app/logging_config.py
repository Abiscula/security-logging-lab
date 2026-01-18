import logging
import os
from app.logging.formatter import JsonFormatter

os.makedirs("logs", exist_ok=True)

handler = logging.FileHandler("logs/app.jsonl")
handler.setFormatter(JsonFormatter())

logger = logging.getLogger("security_lab")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
logger.propagate = False