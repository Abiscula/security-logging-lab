import logging
import os
import json

os.makedirs("logs", exist_ok=True)

class JsonFormatter(logging.Formatter):
  def format(self, record):
    log_record = {
      "timestamp": self.formatTime(record, "%Y-%m-%d %H:%M:%S"),
      "level": record.levelname,
      "logger": record.name,
      "message": record.getMessage(),
    }
    return json.dumps(log_record)

handler = logging.FileHandler("logs/app.jsonl")
handler.setFormatter(JsonFormatter())

logger = logging.getLogger("security_lab")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
logger.propagate = False