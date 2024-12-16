from fastapi.testclient import TestClient
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.database import get_db

import os

# Set up a test database (in-memory SQLite database for testing)
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

# Create a new engine and session for testing
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables in the test database
Base.metadata.create_all(bind=engine)

# Initialize the FastAPI TestClient
client = TestClient(app)

# Dependency to override the get_db function to use the test database
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Override the dependency in the FastAPI app
app.dependency_overrides[get_db] = override_get_db

# Test Case 1: Create a new To-Do
def test_create_todo():
    response = client.post("/todos/", json={"title": "Test Task", "description": "Test description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["status"] == "Pending"
    assert "id" in response.json()

# Test Case 2: List all To-Dos
def test_list_todos():
    # First create a task
    client.post("/todos/", json={"title": "Test Task 1", "description": "Test description"})
    client.post("/todos/", json={"title": "Test Task 2", "description": "Test description"})
    
    response = client.get("/todos/")
    assert response.status_code == 200
    assert len(response.json()) >= 2  # Ensure there are at least 2 tasks

# Test Case 3: Get a single To-Do by ID
def test_get_todo():
    # Create a task
    response_create = client.post("/todos/", json={"title": "Test Task", "description": "Test description"})
    todo_id = response_create.json()["id"]
    
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
    assert response.json()["description"] == "Test description"

# Test Case 4: Edit a To-Do task
def test_edit_todo():
    # Create a task
    response_create = client.post("/todos/", json={"title": "Test Task", "description": "Test description"})
    todo_id = response_create.json()["id"]
    
    # Update the task
    response = client.put(f"/todos/{todo_id}", json={"title": "Updated Task", "description": "Updated description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"
    assert response.json()["description"] == "Updated description"

# Test Case 5: Delete a To-Do task
def test_delete_todo():
    # Create a task
    response_create = client.post("/todos/", json={"title": "Test Task", "description": "Test description"})
    todo_id = response_create.json()["id"]
    
    # Delete the task
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "ToDo deleted"
    
    # Verify that the task no longer exists
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404

# Test Case 6: Delete all To-Do tasks
def test_delete_all_todos():
    # Create some tasks
    client.post("/todos/", json={"title": "Test Task 1", "description": "Test description"})
    client.post("/todos/", json={"title": "Test Task 2", "description": "Test description"})
    
    # Delete all tasks
    response = client.delete("/todos/")
    assert response.status_code == 200
    assert response.json()["message"] == "All ToDos deleted"
    
    # Verify there are no tasks
    response = client.get("/todos/")
    assert len(response.json()) == 0
