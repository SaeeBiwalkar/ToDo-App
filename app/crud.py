from sqlalchemy.orm import Session
from app.models import ToDo
from app.schemas import ToDoCreate, ToDoUpdate

# Get all To-Do tasks
def get_all_todos(db: Session):
    return db.query(ToDo).all()

# Create a new To-Do task
def create_todo(db: Session, todo: ToDoCreate):
    db_todo = ToDo(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Get a To-Do task by its ID
def get_todo_by_id(db: Session, todo_id: int):
    return db.query(ToDo).filter(ToDo.id == todo_id).first()

# Update an existing To-Do task
def update_todo(db: Session, todo_id: int, todo: ToDoUpdate):
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        for key, value in todo.dict(exclude_unset=True).items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)
    return db_todo

# Delete a To-Do task
def delete_todo(db: Session, todo_id: int):
    db_todo = get_todo_by_id(db, todo_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()

# Delete all To-Do tasks
def delete_all_todos(db: Session):
    db.query(ToDo).delete()
    db.commit()
