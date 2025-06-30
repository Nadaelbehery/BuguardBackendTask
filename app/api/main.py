from fastapi import APIRouter
from app.api.routes import task, monitoring

api_router = APIRouter()

api_router.include_router(task.router)
api_router.include_router(monitoring.router)

