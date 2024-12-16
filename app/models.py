from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class ToDo(Base):
    __tablename__ = "todos"

    # Define the columns for the ToDo table
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    status = Column(String, default="Pending")
    due_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

