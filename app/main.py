from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth
from app.models import user  # noqa: F401

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Managment Backend API")
app.include_router(auth.router)