# Campos internos do LogRecord que NÃO devem ir para o log final
LOG_RECORD_INTERNAL_FIELDS = {
  "msg",
  "args",
  "levelname",
  "levelno",
  "name",
  "pathname",
  "filename",
  "module",
  "exc_info",
  "exc_text",
  "stack_info",
  "lineno",
  "funcName",
  "created",
  "msecs",
  "relativeCreated",
  "thread",
  "threadName",
  "processName",
  "process"
}