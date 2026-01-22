# Task Management Backend API

A backend-focused REST API for managing users, projects, and tasks with JWT authentication and role-based access control.

## Tech Stack

- **FastAPI** – Web framework
- **SQLAlchemy** – ORM
- **SQLite** – Database
- **Passlib + bcrypt** – Password hashing
- **python-jose** – JWT tokens

## Features

- JWT-based authentication
- Role-based access control (Admin, Member)
- User registration and login
- Project and task management (planned)
- Task assignment, priorities, and due dates (planned)
- Activity logging (planned)
- Pagination and filtering (planned)

## Project Structure

```
app/
├── main.py           # FastAPI app entry point
├── database.py       # Database connection setup
├── models/
│   └── user.py       # User model
├── routes/
│   └── auth.py       # Auth endpoints (register/login)
└── utils/
    ├── auth.py       # JWT token creation
    └── security.py   # Password hashing
```

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/Aniketgawande1/task-management-backend-api.git
   cd task-management-backend-api
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install fastapi uvicorn sqlalchemy "passlib[bcrypt]" python-jose python-dotenv
   ```

4. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

5. **Open API docs**
   - Swagger UI: http://127.0.0.1:8000/docs
   - ReDoc: http://127.0.0.1:8000/redoc

## API Endpoints

### Auth

| Method | Endpoint         | Description       |
|--------|------------------|-------------------|
| POST   | `/auth/register` | Register new user |
| POST   | `/auth/login`    | Login and get JWT |

### Request Body (JSON)

```json
{
  "email": "user@example.com",
  "password": "yourpassword"
}
```

## Roadmap

- [x] Phase 1: Auth (register/login)
- [ ] Phase 2: Projects & Tasks CRUD
- [ ] Phase 3: Task assignment & priorities
- [ ] Phase 4: Activity logging
- [ ] Phase 5: Rate limiting & background jobs

## License

MIT
