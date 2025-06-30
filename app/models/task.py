from sqlmodel import SQLModel, Field
from sqlalchemy import Column, DateTime
from typing import Optional
from datetime import datetime, timezone
from enum import Enum

class TaskStatus(Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    cancelled = "cancelled"

class TaskPriority(Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(..., max_length=200, description="Task title")
    description: Optional[str] = Field(default=None, max_length=200, description="Task Description")
    status: TaskStatus = Field(default=TaskStatus.pending, description="Task status")
    priority: TaskPriority = Field(default=TaskPriority.medium, description="Task priority")
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        sa_column=Column(DateTime(timezone=True), nullable=False), 
        description="Creation timestamp"
    )
    updated_at: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), nullable=True),
        description="Last update timestamp"
    )
    due_date: Optional[datetime] = Field(
        default=None,
        sa_column=Column(DateTime(timezone=True), nullable=True),
        description="Task deadline"
    )
    assigned_to: Optional[str] = Field(default=None, max_length=100, description="Assignee name")

