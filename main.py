from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.api.main import api_router
from app.db import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Run at startup
    await init_db()
    yield

app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

