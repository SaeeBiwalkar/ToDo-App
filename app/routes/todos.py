from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.crud import *
from app.schemas import *
from app.database import SessionLocal
from typing import List


router = APIRouter()

# Dependency to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Add a new To-Do task
@router.post("/", response_model=ToDoResponse)
def add_todo(todo: ToDoCreate, db: Session = Depends(get_db)):
    return create_todo(db, todo)

# List all To-Do tasks
@router.get("/", response_model=List[ToDoResponse])
def list_todos(db: Session = Depends(get_db)):
    return get_all_todos(db)

# Get a single To-Do task by ID
@router.get("/{todo_id}", response_model=ToDoResponse)
def get_todo_item(todo_id: int, db: Session = Depends(get_db)):
    db_todo = get_todo_by_id(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return db_todo

# Edit an existing To-Do task
@router.put("/{todo_id}", response_model=ToDoResponse)
def edit_todo(todo_id: int, todo: ToDoUpdate, db: Session = Depends(get_db)):
    db_todo = update_todo(db, todo_id, todo)
    if not db_todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    return db_todo

# Delete a single To-Do task by ID
@router.delete("/{todo_id}")
def delete_todo_item(todo_id: int, db: Session = Depends(get_db)):
    db_todo = get_todo_by_id(db, todo_id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    delete_todo(db, todo_id)
    return {"message": "ToDo deleted"}

# Delete all To-Do tasks
@router.delete("/")
def delete_all_items(db: Session = Depends(get_db)):
    delete_all_todos(db)
    return {"message": "All ToDos deleted"}
