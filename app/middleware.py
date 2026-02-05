import time
from fastapi import Request
from app.services.aws.s3_log_writter import save_log
from app.enums.log_type import LogType

IGNORED_PATHS = [
  "/admin/logs",
]

async def request_context_middleware(request: Request, call_next):
  pre_request(request)

  response = await call_next(request)

  post_request(request, response)

  return response


# Ocorre antes da request
def pre_request(request: Request):
  request.state.ip = request.client.host if request.client else None
  request.state.user_agent = request.headers.get("user-agent")
  request.state.start_time = time.time()


#Ocorre após a request
def post_request(request: Request, response):
  if request.url.path in IGNORED_PATHS:
    return
  
  duration_ms = int((time.time() - request.state.start_time) * 1000)

  payload = {
    "type": LogType.REQUEST,
    "method": request.method,
    "path": request.url.path,
    "status": response.status_code,
    "duration_ms": duration_ms,
    "ip": request.state.ip,
    "user_agent": request.state.user_agent
  }

  save_log(payload)