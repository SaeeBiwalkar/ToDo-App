from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Base class for creating and updating To-Do tasks
class ToDoBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "Pending"  # Default status
    due_date: Optional[datetime] = None  # Optional due date

# Schema for creating a new To-Do task (inherits from ToDoBase)
class ToDoCreate(ToDoBase):
    pass

# Schema for updating an existing To-Do task (inherits from ToDoBase)
class ToDoUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    due_date: Optional[datetime]

# Schema for returning a To-Do task (includes ID and created_at)
class ToDoResponse(ToDoBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True  # Tells Pydantic to treat ORM models as dictionaries
