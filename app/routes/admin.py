from fastapi import APIRouter, Request, Query
from typing import Optional

from app.schemas.admin import ActionRequest
from app.services.security_events import SecurityEvents
from app.services.aws.s3_log_reader import list_logs


security_events = SecurityEvents()

router = APIRouter(
  prefix="/admin",
  tags=["Admin"]
)

@router.post("/action")
def admin_action(data: ActionRequest, request: Request):
  ip = request.state.ip
  agent = request.state.user_agent

  security_events.log_sensitive_action(data.action, ip, agent)
  return {"status": "Ação registrada"}


@router.get("/logs")
def get_logs(
    limit: int = Query(100, le=500),
    cursor: Optional[str] = None
):
    result = list_logs(limit=limit, cursor=cursor)

    return {
        "count": len(result["logs"]),
        "next_cursor": result["next_cursor"],
        "logs": result["logs"]
    }