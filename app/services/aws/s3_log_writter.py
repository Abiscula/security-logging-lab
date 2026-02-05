import json
import uuid
from datetime import datetime, timezone

from app.services.aws.s3_client import get_s3_client

BUCKET_NAME = "security-logs"

s3 = get_s3_client()


# Persiste um log no S3 (LocalStack)
def save_log(entry: dict):
    try:
        key = f"logs/{datetime.now(timezone.utc).strftime('%Y/%m/%d')}/{uuid.uuid4()}.json"

        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=key,
            Body=json.dumps(entry),
            ContentType="application/json",
        )

        return key
    except Exception as e:
        # Nunca derruba a aplicação por causa de log
        print("Erro ao salvar log no S3:", e)
        return None
