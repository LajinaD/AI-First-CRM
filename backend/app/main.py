from fastapi import FastAPI

from app.database import engine
from app.models import Base
from app.routers import interaction, chat, hcp
from app.routers import hcp

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI-First CRM API",
    version="1.0.0",
    description="Backend API for AI-First CRM HCP Module"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI-First CRM API 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

app.include_router(interaction.router)
app.include_router(hcp.router)
app.include_router(chat.router)