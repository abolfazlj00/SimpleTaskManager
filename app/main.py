from fastapi import FastAPI
from routers.tasks import router as task_manager_router
from models import Base
from database import engine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create Tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield

app = FastAPI(
    lifespan=lifespan
)


app.include_router(
    router=task_manager_router
)
