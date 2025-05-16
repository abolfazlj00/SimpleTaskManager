# Python Task Management API

This project is a simple Python-based API for managing tasks. It uses a modular architecture with separate files for configuration, database operations, routing, and data models.

## 🛠 Tech Stack

* FastAPI
* SqlAlchemy

## 🚀 Features

- Task CRUD operations (Create, Read, Update, Delete)
- SQLAlchemy for ORM-based database access
- Pydantic models for data validation

## Project Structure
```bash
.
├── app/
│ ├── config.py # Configuration settings
│ ├── crud.py # CRUD operations
│ ├── database.py # Database connection and setup
│ ├── main.py # Entry point of the app
│ ├── models.py # SQLAlchemy models
│ ├── schemas.py # Pydantic schemas
│ └── routers
│     └── tasks.py # Task-related API routes
├── .gitignore
├── .sample.env # Example environment configuration
├── LICENSE
├── README.md # Project documentation
```

## Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/abolfazlj00/SimpleTaskManager.git
cd SimpleTaskManager
python -m venv venv
```

2. **Create a virtual environment**
```bash
Linux: source venv/bin/activate  
Windows: venv\\Scripts\\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
    * Copy .sample.env to .env and fill in the required values.

5. **Run the application**
```bash
uvicorn app.main:app --reload
```

6. **Access the API docs**
    * Navigate to http://localhost:8000/docs
