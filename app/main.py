from fastapi import FastAPI
from routers.tasks import router as task_manager_router
from models import Base
from database import engine

app = FastAPI()

app.include_router(
    router=task_manager_router
)

@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)