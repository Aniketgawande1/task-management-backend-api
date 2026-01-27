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

---

## How This Project Works

### Application Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT (Browser/App)                      │
└─────────────────────────────┬───────────────────────────────────┘
                              │ HTTP Request
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FastAPI Server (main.py)                     │
│                    Running on localhost:8000                     │
└─────────────────────────────┬───────────────────────────────────┘
                              │ Routes to
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Routes (routes/auth.py)                     │
│                   /auth/register  /auth/login                    │
└─────────────────────────────┬───────────────────────────────────┘
                              │ Uses
                              ▼
┌──────────────┬──────────────┴──────────────┬───────────────────┐
│   Models     │         Utils               │    Database       │
│  (user.py)   │  (security.py, auth.py)     │  (database.py)    │
└──────────────┴─────────────────────────────┴───────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      SQLite Database (task.db)                   │
└─────────────────────────────────────────────────────────────────┘
```

### File-by-File Explanation

| File | Purpose |
|------|---------|
| `main.py` | Entry point - creates FastAPI app, initializes DB tables, registers routes |
| `database.py` | Database connection - SQLite setup, session factory, Base class |
| `models/user.py` | User model - defines users table structure |
| `models/task.py` | Task model - defines tasks table structure |
| `routes/auth.py` | Auth endpoints - register and login APIs |
| `utils/security.py` | Password handling - hash and verify passwords |
| `utils/auth.py` | JWT tokens - create access tokens |

### Authentication Flow

#### Registration
```
1. POST /auth/register { "email": "...", "password": "..." }
2. Check if email exists → Error 400 if yes
3. Hash password using passlib
4. Save user to database
5. Return { "message": "User created" }
```

#### Login
```
1. POST /auth/login { "email": "...", "password": "..." }
2. Find user by email → Error 401 if not found
3. Verify password → Error 401 if wrong
4. Create JWT token with user_id and role
5. Return { "access_token": "...", "token_type": "bearer" }
```

### Database Structure

```
┌─────────────────────────────────────────┐
│              users table                │
├─────────────────────────────────────────┤
│ id │ email │ password_hash │ role │ ... │
└─────────────────────────────────────────┘
         │
         │ user_id (Foreign Key)
         ▼
┌─────────────────────────────────────────┐
│              tasks table                │
├─────────────────────────────────────────┤
│ id │ title │ completed │ user_id │ ...  │
└─────────────────────────────────────────┘
```

---

## Roadmap

- [x] Phase 1: Auth (register/login)
- [ ] Phase 2: Projects & Tasks CRUD
- [ ] Phase 3: Task assignment & priorities
- [ ] Phase 4: Activity logging
- [ ] Phase 5: Rate limiting & background jobs

## License

MIT
