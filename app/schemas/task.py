from typing import Optional
from datetime import datetime, timezone
from pydantic import BaseModel, Field, field_validator
from app.models.task import TaskStatus, TaskPriority

class TaskCreate(BaseModel):
    title: str = Field(max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TaskStatus] = TaskStatus.pending
    priority: Optional[TaskPriority] = TaskPriority.medium
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = Field(None, max_length=100)

    @field_validator("title")
    @classmethod
    def title_must_not_be_blank(cls, v: str) -> str:
        v = v.strip()
        if not v:
            raise ValueError("Title cannot be empty or whitespace.")
        return v

    @field_validator("due_date")
    @classmethod
    def due_date_must_be_future(cls, v: Optional[datetime]) -> Optional[datetime]:
        if v and v <= datetime.now(timezone.utc):
            raise ValueError("Due date must be in the future.")
        return v

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    status: Optional[TaskStatus] = None
    priority: Optional[TaskPriority] = None
    due_date: Optional[datetime] = None
    assigned_to: Optional[str] = Field(None, max_length=100)

    @field_validator("title")
    @classmethod
    def title_not_blank(cls, v: Optional[str]) -> Optional[str]:
        if v is not None and not v.strip():
            raise ValueError("Title cannot be empty or whitespace.")
        return v

    @field_validator("due_date")
    @classmethod
    def due_date_in_future(cls, v: Optional[datetime]) -> Optional[datetime]:
        if v and v <= datetime.now(timezone.utc):
            raise ValueError("Due date must be in the future.")
        return v

class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime
    updated_at: Optional[datetime]
    due_date: Optional[datetime]
    assigned_to: Optional[str]

    class Config:
        from_attributes = True
