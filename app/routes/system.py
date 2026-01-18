from fastapi import APIRouter, Request
from app.events import log_system_error

router = APIRouter(
  prefix="/system",
  tags=["System"]
)

@router.get("/error")
def system_error(request: Request):
  ip = request.client.host
  agent = request.headers.get("user-agent")

  try:
    1 / 0
  except Exception as e:
    log_system_error(str(e), ip, agent)
    return {"error": "Falha no sistema"}