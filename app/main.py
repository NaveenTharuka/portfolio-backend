from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
# Import models to ensure they are registered on Base.metadata before creating tables
from app.db_models import Project, Interest
import os

from app.routes import projects_routes, interest_routes

# Create all tables on startup
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Portfolio Backend",
    description="Portfolio Backend",
    version="0.0.0"
)

app.include_router(projects_routes.router)
app.include_router(interest_routes.router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        os.getenv("FRONTEND_URL")
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status":"healthy"}

