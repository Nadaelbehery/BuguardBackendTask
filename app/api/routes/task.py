from fastapi import APIRouter, Depends, HTTPException, status, Query
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.task import TaskCreate, TaskUpdate, TaskResponse
from app.db import get_session
from app.crud import task as crud_task
from app.models.task import TaskStatus, TaskPriority

router = APIRouter(prefix="/tasks", tags=["Tasks"])

# Create Task
@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED, summary="Create a new task")
async def create_task(task: TaskCreate, db: AsyncSession = Depends(get_session)):
    return await crud_task.create_task(db, task)

# List Tasks with Pagination
@router.get("/", response_model=List[TaskResponse], summary="List all tasks with pagination")
async def list_tasks(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    db: AsyncSession = Depends(get_session)
):
    return await crud_task.get_tasks(db, skip=skip, limit=limit)

# Get Task by ID
@router.get("/{task_id}", response_model=TaskResponse, summary="Retrieve a task by its ID")
async def get_task(task_id: int, db: AsyncSession = Depends(get_session)):
    task = await crud_task.get_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Update Task
@router.put("/{task_id}", response_model=TaskResponse, summary="Update an existing task")
async def update_task(task_id: int, updates: TaskUpdate, db: AsyncSession = Depends(get_session)):
    task = await crud_task.update_task(db, task_id, updates)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# Delete Task
@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT, summary="Delete a task by ID")
async def delete_task(task_id: int, db: AsyncSession = Depends(get_session)):
    success = await crud_task.delete_task(db, task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return

# Filter by Status
@router.get("/status/{status}",
    response_model=List[TaskResponse], summary="Filter tasks by status")
async def get_tasks_by_status(status: TaskStatus, db: AsyncSession = Depends(get_session)):
    return await crud_task.filter_tasks_by_status(db, status)

# Filter by Priority
@router.get("/priority/{priority}", response_model=List[TaskResponse], summary="Filter tasks by priority")
async def get_tasks_by_priority(priority: TaskPriority, db: AsyncSession = Depends(get_session)):
    return await crud_task.filter_tasks_by_priority(db, priority)
