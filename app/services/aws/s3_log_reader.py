from typing import Optional
import json
from app.services.aws.s3_client import get_s3_client

BUCKET_NAME = "security-logs"

s3 = get_s3_client()


def list_logs(limit: int = 100, cursor: Optional[str] = None):
    params = {
        "Bucket": BUCKET_NAME,
        "Prefix": "logs/",
        "MaxKeys": limit,
    }

    # se vier cursor, continua dali
    if cursor:
        params["ContinuationToken"] = cursor

    response = s3.list_objects_v2(**params)

    objects = response.get("Contents", [])

    logs = []
    for obj in objects:
        data = s3.get_object(Bucket=BUCKET_NAME, Key=obj["Key"])
        body = data["Body"].read().decode("utf-8")
        logs.append(json.loads(body))

    return {
        "logs": logs,
        "next_cursor": response.get("NextContinuationToken")
    }