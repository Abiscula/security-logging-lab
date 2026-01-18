from fastapi import FastAPI, Request

from app.DTO import LoginRequest, ActionRequest
from app.events import (
  log_auth_attempt,
  log_sensitive_action,
  log_system_error
)

app = FastAPI()


@app.post("/auth/login")
def login(data: LoginRequest, request: Request):
  ip = request.client.host
  agent = request.headers.get("user-agent")

  success = data.password == "123456"
  log_auth_attempt(data.username, ip, agent, success)

  return {"success": success}


@app.post("/admin/action")
def admin_action(data: ActionRequest, request: Request):
  ip = request.client.host
  agent = request.headers.get("user-agent")

  log_sensitive_action(data.action, ip, agent)
  return {"status": "action registered"}


@app.get("/system/error")
def system_error(request: Request):
  ip = request.client.host
  agent = request.headers.get("user-agent")

  try:
    1 / 0
  except Exception as e:
    log_system_error(str(e), ip, agent)
    return {"error": "system failure simulated"}