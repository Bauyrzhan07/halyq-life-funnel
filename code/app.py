import asyncio
import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from fastapi_admin.app import app as admin_app
from fastapi_admin.exceptions import (
    forbidden_error_exception,
    not_found_error_exception,
    server_error_exception,
    unauthorized_error_exception,
)
from redis import asyncio as aioredis
from tortoise import Tortoise

from code.api import setup_routers
from code.config import settings, TORTOISE_CONFIG
from code.constants import BASE_DIR
from code.models import Admin
from code.providers import LoginProvider
from code.utils import setup_logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        redis = await aioredis.from_url(
            settings.redis_url,
            decode_responses=True,
            encoding="utf-8",
        )
        await asyncio.gather(
            admin_app.configure(
                logo_url=settings.admin_logo_url,
                template_folders=[os.path.join(BASE_DIR, "templates")],
                providers=[
                    LoginProvider(
                        login_logo_url=settings.login_logo_url,
                        admin_model=Admin,
                    ),
                ],
                favicon_url=settings.favicon_url,
                redis=redis,
            ),
            Tortoise.init(config=TORTOISE_CONFIG),
        )
        yield
    finally:
        await Tortoise.close_connections()


app = FastAPI(
    title="Halyq Life Funnel API",
    lifespan=lifespan,
    openapi_url="/openapi.json/",
)


@app.get("/")
async def index():
    return RedirectResponse(url="/admin")


admin_app.add_exception_handler(
    status.HTTP_500_INTERNAL_SERVER_ERROR,
    server_error_exception,
)
admin_app.add_exception_handler(status.HTTP_404_NOT_FOUND, not_found_error_exception)
admin_app.add_exception_handler(status.HTTP_403_FORBIDDEN, forbidden_error_exception)
admin_app.add_exception_handler(
    status.HTTP_401_UNAUTHORIZED,
    unauthorized_error_exception,
)

setup_routers(app)
setup_logger(settings.debug)

app.mount("/admin", admin_app)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("code.app:app", host="0.0.0.0", reload=settings.debug)
