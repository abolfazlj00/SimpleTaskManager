from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import Task
from schemas import TaskCreate, TaskUpdate
from typing import Optional, List

async def get_tasks(db: AsyncSession) -> List[Task]:
    tasks = await db.execute(
        select(Task)
    )
    return tasks.scalars().all()

async def create_task(db: AsyncSession, new_task: TaskCreate) -> Task:
    task = Task(**new_task.model_dump())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def read_task_by_id(db: AsyncSession, task_id: int) -> Task | None:
    result = await db.execute(
        select(Task).where(Task.id == task_id)
    )
    return result.scalar()

async def update_task(db: AsyncSession, task_id: int, updaetd_task: TaskUpdate) -> Optional[Task]:
    result = await db.execute(
        select(Task).where(Task.id == task_id)
    )
    task = result.scalars().first()

    if task:
        update_data = updaetd_task.model_dump(
            exclude_unset=True
        )
        if len(update_data) > 0:
            for field, value in update_data.items():
                setattr(task, field, value)

            await db.commit()
            await db.refresh(task)
        return task

async def delete_task(db: AsyncSession, task_id: int) -> bool:
    result = await db.execute(
        select(Task).where(Task.id == task_id)
    )
    task = result.scalars().first()

    if not task:
        return False

    await db.delete(task)
    await db.commit()
    return True