
# To-Do Reminder App

## Overview

This To-Do Reminder App provides a simple way to manage tasks. It exposes RESTful APIs to create, view, update, delete individual tasks, and delete all tasks. The app uses FastAPI for the backend, PostgreSQL for the database, and a simple HTML, CSS, and JavaScript frontend for interaction.

## Features

- **Add a New To-Do Task**
- **View List of To-Do Tasks**
- **Edit or Delete a Specific To-Do Task**
- **Delete All To-Do Tasks**

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript

## Setup

### Requirements

Make sure you have the following installed:

- Python 3.7+  
- PostgreSQL (or you can use MongoDB if preferred)
- pip (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/todo-reminder-app.git
    cd todo-reminder-app
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up PostgreSQL database:

    Create a new database called `todo_db` in your PostgreSQL instance:

    ```bash
    CREATE DATABASE todo_db;
    ```

4. Update the `DATABASE_URL` in `app/database.py` with your PostgreSQL credentials:

    ```python
    DATABASE_URL = "postgresql://postgres:password@localhost:5432/todo_db"
    ```

5. Run the app:

    ```bash
    uvicorn app.main:app --reload
    ```

    This will start the FastAPI app on `http://127.0.0.1:8000`.

6. Open `index.html` in your browser to interact with the app.

### Testing

The application is equipped with test cases for each API endpoint. To run tests, make sure the app is running and execute:

```bash
pytest
```

The tests will check the functionality of all the CRUD operations (create, read, update, delete) for To-Do tasks.

## API Endpoints

### 1. Create a To-Do Task

- **POST** `/todos`
- Request body: 
  ```json
  {
    "title": "Task Title",
    "description": "Task Description"
  }
  ```
- Response: 
  ```json
  {
    "id": 1,
    "title": "Task Title",
    "description": "Task Description",
    "status": "Pending",
    "created_at": "2024-12-15T10:00:00"
  }
  ```

### 2. Get All To-Do Tasks

- **GET** `/todos`
- Response: 
  ```json
  [
    {
      "id": 1,
      "title": "Task Title",
      "description": "Task Description",
      "status": "Pending",
      "created_at": "2024-12-15T10:00:00"
    }
  ]
  ```

### 3. Edit a To-Do Task

- **PUT** `/todos/{id}`
- Request body:
  ```json
  {
    "title": "Updated Title",
    "description": "Updated Description"
  }
  ```
- Response: 
  ```json
  {
    "id": 1,
    "title": "Updated Title",
    "description": "Updated Description",
    "status": "Pending",
    "created_at": "2024-12-15T10:00:00"
  }
  ```

### 4. Delete a To-Do Task

- **DELETE** `/todos/{id}`
- Response: No content (200 OK)

### 5. Delete All To-Do Tasks

- **DELETE** `/todos`
- Response: No content (200 OK)

## Hosting

The app can be hosted on any free hosting platform. For example:
- Render

Make sure to deploy the backend and frontend correctly by updating API URLs if necessary.


