from botocore.exceptions import ClientError

from app.services.aws.s3_client import get_s3_client

BUCKET_NAME = "security-logs"


# Garante que o bucket de logs exista no S3 (LocalStack).
# Se não existir, cria automaticamente na inicialização da aplicação.
def ensure_bucket():
    s3 = get_s3_client()
    try:
        s3.head_bucket(Bucket=BUCKET_NAME)
    except ClientError:
        s3.create_bucket(Bucket=BUCKET_NAME)
