import json
from app.services.aws.s3_client import get_s3_client

BUCKET_NAME = "security-logs"

s3 = get_s3_client()


def list_logs(limit: int = 100):
    response = s3.list_objects_v2(
        Bucket=BUCKET_NAME,
        Prefix="logs/"
    )

    objects = response.get("Contents", [])

    # ordena pelos mais recentes
    objects = sorted(objects, key=lambda x: x["LastModified"], reverse=True)

    logs = []

    for obj in objects[:limit]:
        data = s3.get_object(Bucket=BUCKET_NAME, Key=obj["Key"])
        body = data["Body"].read().decode("utf-8")
        logs.append(json.loads(body))

    return logs