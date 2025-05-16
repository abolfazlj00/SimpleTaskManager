
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from schemas import TaskCreate, TaskRead, TaskUpdate
from crud import get_tasks, create_task, read_task_by_id, update_task, delete_task
from typing import List

router = APIRouter(
    prefix=""
)

@router.get("/tasks", response_model=List[TaskRead])
async def get(db: AsyncSession = Depends(get_db)):
    return await get_tasks(
        db=db
    )

@router.post("/tasks", response_model=TaskRead)
async def create(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await create_task(
        db=db,
        new_task=task
    )

@router.get("/tasks/{task_id}", response_model=TaskRead)
async def read(task_id: int, db: AsyncSession = Depends(get_db)):
    return await read_task_by_id(
        db=db,
        task_id=task_id
    )

@router.put("tasks/{task_id}", response_model=TaskRead)
async def update(task_id: int, task: TaskUpdate, db: AsyncSession = Depends(get_db)):
    updated_task = await update_task(
        db=db,
        task_id=task_id,
        updaetd_task=task
    )
    if not updated_task:
        raise HTTPException(
            status_code=404, 
            detail="Task not found"
        )
    return task

@router.delete("tasks/{task_id}", response_model=bool)
async def delete(task_id: int, db: AsyncSession = Depends(get_db)):
    is_deleted = await delete_task(
        db=db,
        task_id=task_id
    )
    if not is_deleted:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )