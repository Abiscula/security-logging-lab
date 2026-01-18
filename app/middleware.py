import json
import time
from fastapi import Request
from app.logging_config import logger

async def request_context_middleware(request: Request, call_next):
  # ===== PRÉ-ROTA =====
  request.state.ip = request.client.host if request.client else None
  request.state.user_agent = request.headers.get("user-agent")

  start_time = time.time()

  # Executa a rota
  response = await call_next(request)

  # ===== PÓS-ROTA =====
  duration_ms = int((time.time() - start_time) * 1000)

  logger.info(json.dumps({
    "type": "REQUEST",
    "method": request.method,
    "path": request.url.path,
    "status": response.status_code,
    "duration_ms": duration_ms,
    "ip": request.state.ip,
    "user_agent": request.state.user_agent
  }))

  return response