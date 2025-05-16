# Python Task Management API

This project is a simple Python-based API for managing tasks. It uses a modular architecture with separate files for configuration, database operations, routing, and data models.

## 🛠 Tech Stack

* FastAPI
* SqlAlchemy
* Pydantic

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

## ⚙️ Setup Instructions

1. **Clone the repository**
```bash
git clone https://github.com/abolfazlj00/SimpleTaskManager.git
cd SimpleTaskManager
python -m venv venv
```

2. **Create a virtual environment**
#### On **Windows**:
```bash
venv/Scripts/activate
```
#### On **Linux/macOS**:
```bash
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
- Copy `.sample.env` to `.env` and update the necessary values.

5. **Run the application**
```bash
cd app
uvicorn main:app --reload
```

6. **Access the API docs**
    * Navigate to http://localhost:8000/docs


## 🚀 Deployment to Linux Server (Gunicorn + systemd)

This section describes how to deploy the FastAPI application on a Linux server using `gunicorn` with `uvicorn workers` and `systemd` to manage the process.

### ✅ 1. Install Required Packages

```bash
sudo apt update
sudo apt install python3-pip python3-venv -y
```

Clone the project and set up the environment:

```bash
git clone https://github.com/abolfazlj00/SimpleTaskManager.git
cd SimpleTaskManager
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### ✅ 2. Install Gunicorn with Uvicorn Worker

```bash
pip install gunicorn uvicorn
```

### ✅ 3. Create a systemd Service File

```bash
sudo nano /etc/systemd/system/simpletaskmanager.service
```

Paste the following content:

```ini
[Unit]
Description=SimpleTaskManager FastAPI App
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/SimpleTaskManager
ExecStart=/path/to/SimpleTaskManager/venv/bin/gunicorn -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:8000
Restart=always

[Install]
WantedBy=multi-user.target
```

📌 Replace `/path/to/SimpleTaskManager` with the actual project directory path.

### ✅ 4. Start and Enable the Service

```bash
sudo systemctl daemon-reexec
sudo systemctl daemon-reload
sudo systemctl enable simpletaskmanager
sudo systemctl start simpletaskmanager
```

To check the status:

```bash
sudo systemctl status simpletaskmanager
```

### ✅ 5. Access the API

Open your browser or use `curl`:

```
http://<your-server-ip>:8000/docs
```

## 📝 License

This project is licensed under the terms of the [MIT License](LICENSE).