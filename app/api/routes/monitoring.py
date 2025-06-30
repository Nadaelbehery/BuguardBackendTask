from fastapi import APIRouter, Depends, Request
from fastapi.routing import APIRoute
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from app.db import get_session

router = APIRouter(tags=["Monitoring"])

# Root Endpoint
@router.get("/", summary="API Root")
async def root(request: Request):
    routes_info = []

    for route in request.app.routes:
        if isinstance(route, APIRoute):
            routes_info.append({
                "path": route.path,
                "methods": list(route.methods),
                "summary": route.summary or "",
                "tags": route.tags or []
            })

    return {
        "message": "Welcome to the Task Management API",
        "version": "1.0.0",
        "available_endpoints": routes_info
    }

# Health check endpoint
@router.get("/health", summary="Health Check")
async def health_check(db: AsyncSession = Depends(get_session)):
    try:
        await db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "reachable"}
    except Exception as e:
        print("Health check error:", str(e))
        return {"status": "degraded", "database": "unreachable"}
