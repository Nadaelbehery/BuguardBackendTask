from typing import List, Optional
from sqlmodel import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate
from datetime import datetime, timezone

async def create_task(db: AsyncSession, task_in: TaskCreate) -> Task:
    task = Task(**task_in.model_dump())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task

async def get_task(db: AsyncSession, task_id: int) -> Optional[Task]:
    return await db.get(Task, task_id)

async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 10) -> List[Task]:
    result = await db.execute(select(Task).offset(skip).limit(limit))
    return result.scalars().all()

async def update_task(db: AsyncSession, task_id: int, updates: TaskUpdate) -> Optional[Task]:
    task = await db.get(Task, task_id)
    if not task:
        return None

    task_data = updates.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(task, key, value)

    task.updated_at = datetime.now(timezone.utc)
    await db.commit()
    await db.refresh(task)
    return task

async def delete_task(db: AsyncSession, task_id: int) -> bool:
    task = await db.get(Task, task_id)
    if not task:
        return False
    await db.delete(task)
    await db.commit()
    return True

async def filter_tasks_by_status(db: AsyncSession, status: str) -> List[Task]:
    result = await db.execute(select(Task).where(Task.status == status))
    return result.scalars().all()

async def filter_tasks_by_priority(db: AsyncSession, priority: str) -> List[Task]:
    result = await db.execute(select(Task).where(Task.priority == priority))
    return result.scalars().all()
