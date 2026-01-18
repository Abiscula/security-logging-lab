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
    }

    # Campos extras (payload)
    for key, value in record.__dict__.items():
      if key not in ("msg", "args", "levelname", "levelno", "name", "pathname",
                     "filename", "module", "exc_info", "exc_text", "stack_info",
                     "lineno", "funcName", "created", "msecs", "relativeCreated",
                     "thread", "threadName", "processName", "process"):
        log_record[key] = value

    return json.dumps(log_record)

handler = logging.FileHandler("logs/app.jsonl")
handler.setFormatter(JsonFormatter())

logger = logging.getLogger("security_lab")
logger.setLevel(logging.INFO)
logger.addHandler(handler)
logger.propagate = False