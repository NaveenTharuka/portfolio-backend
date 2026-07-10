from fastapi import APIRouter, Depends
from app.supabase.supabase import supabase
from app.models.project import Project,ProjectCreate,ProjectUpdate
from app.database import get_db
from sqlalchemy.orm import Session

from app.models.project import Project as ProjectOut

from app.db_models import Project

import app.services.project_services

projects_services = app.services.project_services

router = APIRouter()

@router.get("/projects/all",response_model=list[ProjectOut])
def get_all_projects(db : Session = Depends(get_db)):
    return projects_services.getAllProjects(db)