from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, Base
# Import models to ensure they are registered on Base.metadata before creating tables
from app.db_models import Project, Interest,Contact
import os

from app.routes import projects_routes, interest_routes, contact_routes

# Create all tables on startup
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="Portfolio Backend",
    description="Portfolio Backend",
    version="0.0.0"
)

app.include_router(projects_routes.router)
app.include_router(interest_routes.router)
app.include_router(contact_routes.router)


origins = [
    "http://localhost:3000",
    "http://localhost:3001"
]

frontend_url = os.getenv("FRONTEND_URL")
if frontend_url:
    origins.append(frontend_url)

# Clean and filter origins (remove None, duplicates, and trailing slashes)
cleaned_origins = []
for origin in origins:
    if origin:
        cleaned_origins.append(origin)
        stripped = origin.rstrip("/")
        if stripped not in cleaned_origins:
            cleaned_origins.append(stripped)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cleaned_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status":"healthy"}

