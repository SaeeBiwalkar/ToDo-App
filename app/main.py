from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware
from fastapi.staticfiles import StaticFiles  # Import StaticFiles to serve static files
from app.database import engine
from app.models import Base
from app.routes.todos import router as todo_router

# Create the FastAPI app
app = FastAPI()

# Add CORS middleware to allow cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for local development, update for production security
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)

# Serve static files (HTML, CSS, JS) from the 'ui' folder
app.mount("/", StaticFiles(directory="ui", html=True), name="static")

from app.database import SessionLocal
from sqlalchemy.orm import Session

# Dependency to get the DB session
def get_db():
    db = SessionLocal()  # Creates a new database session
    try:
        yield db  # Makes the session available to the route function
    finally:
        db.close()  # Closes the session after the route finishes

# Create database tables (if not already created)
Base.metadata.create_all(bind=engine)

# Include the To-Do routes
app.include_router(todo_router, prefix="/todos", tags=["ToDos"])

# Root endpoint - This will serve your index.html file
@app.get("/")
async def root():
    return {"message": "Welcome to the To-Do Reminder App"}
