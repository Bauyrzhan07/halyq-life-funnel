from fastapi import FastAPI

from code.api.endpoints import attribution, health, recommendations


def setup_routers(app: FastAPI):
    app.include_router(attribution.router, tags=["attribution"])
    app.include_router(health.router, tags=["health"])
    app.include_router(recommendations.router, tags=["recommendations"])
