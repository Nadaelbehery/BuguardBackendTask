# Task Management API - FastAPI Intern Assessment

## Overview

This project is a Task Management API built with FastAPI, SQLModel, and SQLite, following RESTful principles. It supports full CRUD functionality with data validation, pagination, filtering, and auto-generated API documentation.

## Features

- FastAPI + SQLModel + SQLite
- Asynchronous database operations
- Pydantic-based validation
- Enum fields for task status and priority
- Filtering by status/priority
- Pagination with `skip` and `limit`
- Auto-created SQLite DB on startup
- Dockerized setup

## Installation

```bash
# Clone the repository
git clone https://github.com/Nadaelbehery/BuguardBackendTask.git
cd BuguardBackendTask

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate  # on Windows 

# Install dependencies
pip install -r requirements.txt

# Set database url
You can either:

### ➤ Create a `.env` file in the project root and include:
DATABASE_URL=sqlite+aiosqlite:///./sqlite.db

### ➤ Or set it manually:
Windows (Command Prompt):
set DATABASE_URL=sqlite+aiosqlite:///./sqlite.db


# Start the API
python main.py
```
# Access the API documentation at:

Swagger UI: http://localhost:8001/docs

Redoc: http://localhost:8001/redoc

---

### 5. Docker 

```bash
# Build Docker image
docker-compose up --build
```
# Access the API documentation at:

Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc


---

## API Endpoints

### General
- `GET /` — Endpoint info
- `GET /health` — Health check

### Tasks
- `POST /tasks` — Create a new task
- `GET /tasks` — List all tasks (supports `skip` and `limit` for pagination)
- `GET /tasks/{task_id}` — Retrieve a task by its ID
- `PUT /tasks/{task_id}` — Update a task
- `DELETE /tasks/{task_id}` — Delete a task

### Filtering
- `GET /tasks/status/{status}` — Filter tasks by status (`pending`, `in_progress`, `completed`, `cancelled`)
- `GET /tasks/priority/{priority}` — Filter tasks by priority (`low`, `medium`, `high`, `urgent`)
