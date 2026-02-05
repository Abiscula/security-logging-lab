import json
import logging

from app.logging.constants import LOG_RECORD_INTERNAL_FIELDS


class JsonFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            "timestamp": self.formatTime(record, "%Y-%m-%d %H:%M:%S"),
            "level": record.levelname,
            "logger": record.name,
            "message": record.getMessage(),
        }

        # Campos adicionais enviados via 'extra'
        for key, value in record.__dict__.items():
            if key not in LOG_RECORD_INTERNAL_FIELDS:
                log_record[key] = value

        return json.dumps(log_record)
