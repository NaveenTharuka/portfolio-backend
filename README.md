# ⚡ Personal Portfolio - Backend

A RESTful backend built with FastAPI that powers my personal portfolio. It provides secure APIs for managing projects, skills, certifications, interests, experience, and contact messages through an authenticated admin dashboard.

## ✨ Features

- RESTful API architecture
- JWT Authentication
- Secure admin endpoints
- CRUD operations
- PostgreSQL database
- UUID-based resources
- File/image support
- CORS configuration
- Environment-based configuration

## 🛠️ Tech Stack

- FastAPI
- Python
- SQLAlchemy
- PostgreSQL
- Supabase
- Pydantic
- Uvicorn

## 📂 Project Structure

```
app/
├── routes/
├── services/
├── models/
├── schemas/
├── config/
├── utils/
└── main.py
```

## 🚀 Getting Started

### Clone the repository

```bash
https://github.com/NaveenTharuka/portfolio-backend.git
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file.


### Run the server

```bash
uvicorn app.main:app --reload
```

Server runs on:

```
http://localhost:8000
```

Interactive API Documentation:

```
http://localhost:8000/docs
```

## 📌 API Modules

- Projects
- Skills
- Interests
- Certifications
- Contact Messages
- Dashboard

## 👨‍💻 Author

**Naveen Jayawardana**

Backend Developer | Full Stack Developer
