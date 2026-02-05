from app.services.aws.s3_client import get_s3_client

BUCKET_NAME = "security-logs"

s3 = get_s3_client()

s3.create_bucket(Bucket=BUCKET_NAME)

print(f"Bucket '{BUCKET_NAME}' criado com sucesso")
