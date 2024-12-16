
# To-Do Reminder App

## Overview

 To-Do Reminder App allows users to manage tasks with functionalities to create, view, update, and delete individual tasks, as well as delete all tasks at once. The app exposes RESTful APIs for these operations and is built with FastAPI for the backend, PostgreSQL for the database, and a simple HTML, CSS, and JavaScript frontend for interaction.

## Features

- **Add a New To-Do Task**
- **View List of To-Do Tasks**
- **Edit or Delete a Specific To-Do Task**
- **Delete All To-Do Tasks**

## Tech Stack

- **Backend:** Python, FastAPI
- **Database:** PostgreSQL
- **Frontend:** HTML, CSS, JavaScript

## Setup Guide

 The steps required to set up and run the To-Do Reminder App locally.

### Requirements

Main softwares required ffor the application:

- Python 3.7+
- PostgreSQL (or MongoDB if preferred)
- pip (Python package installer)

### Installation

1. **Clone the repository:**

    Clone the GitHub repository to local machine:

    ```bash
    git clone https://github.com/SaeeBiwalkar/ToDo-App.git
    cd ToDo-App
    ```

2. **Install dependencies:**

    Install all required Python packages using the `requirements.txt` file:

    ```bash
    pip install -r requirements.txt
    ```

3. **Set up PostgreSQL Database:**

    Create a new PostgreSQL database called `todo_db` (if you are using PostgreSQL):

    ```bash
    CREATE DATABASE todo_db;
    ```

4. **Configure Database URL:**

    Update the `DATABASE_URL` in `app/database.py` with PostgreSQL credentials. It should look like this:

    ```python
    DATABASE_URL = "postgresql://postgres:password@localhost:5432/todo_db"
    ```

5. **Run the application:**

    Start the FastAPI app locally using Uvicorn:

    ```bash
    uvicorn app.main:app --reload
    ```

    The app will run on `http://127.0.0.1:8000`.

6. **Frontend Interaction:**

    Open `ui/index.html` in browser to interact with the app's frontend.

### Testing

The app comes with test cases for each of the API endpoints to ensure the functionality of all CRUD operations (Create, Read, Update, Delete). To run the tests, follow these steps:

1. Run the app first.

2. Run the test cases using `pytest`:

    ```bash
    pytest
    ```

    This will execute all the test cases and check that the app's functionality is working as expected.

## API Endpoints

Here is the list of available API endpoints in the app:

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

### 3. Get a Single To-Do Task by ID

- **GET** `/todos/{todo_id}`
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

### 4. Edit a To-Do Task

- **PUT** `/todos/{todo_id}`
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

### 5. Delete a To-Do Task

- **DELETE** `/todos/{todo_id}`
- Response: No content (200 OK)

### 6. Delete All To-Do Tasks

- **DELETE** `/todos`
- Response: No content (200 OK)

## Hosting

The app has been deployed to Render and can be accessed at the following URL: [Render App](https://todo-app-si20.onrender.com/).


## File Structure

Here’s a breakdown of the project’s file structure:

```
ToDo-App/
│
├── app/
│   ├── __init__.py
│   ├── crud.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   ├── routes/
│   │   └── todos.py
│   ├── schemas.py
│   └── tests/
│       └── test_todos.py
│
├── ui/
│   |── index.html
|   |── style.css
|   └── scrip.js
│
├── requirements.txt
└── README.md
```

## Notes

- **Database Design:** The database uses PostgreSQL with a simple `todos` table that holds tasks with columns such as `id`, `title`, `description`, `status`, and `created_at`.
- **Modularization:** The app is organized in modules to separate CRUD operations, database interactions, and route definitions for better maintainability.
- **Security:** Ensure that sensitive information (like database credentials) is handled securely, especially in production environments. For this project, it's handled via the `DATABASE_URL` in the `database.py` file.

