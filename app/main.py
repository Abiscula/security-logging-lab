from fastapi import FastAPI

from app.middleware import request_context_middleware
from app.routes.auth import router as auth_router
from app.routes.admin import router as admin_router
from app.routes.system import router as system_router

app = FastAPI()

# registra o middleware
app.middleware("http")(request_context_middleware)

# registra os routers
app.include_router(auth_router)
app.include_router(admin_router)
app.include_router(system_router)