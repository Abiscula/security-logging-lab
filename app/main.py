from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.middleware import request_context_middleware
from app.routes.admin import router as admin_router
from app.routes.auth.main import router as auth_router
from app.routes.system import router as system_router
from app.services.aws.s3_bootstrap import ensure_bucket


# Executa tarefas de inicialização da aplicação.
# ensure_bucket - Garante que o bucket S3 de logs exista antes da API começar a aceitar requisições.
@asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_bucket()
    yield


app = FastAPI(lifespan=lifespan)

# registra o middleware
app.middleware("http")(request_context_middleware)

# registra os routers
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(system_router)
