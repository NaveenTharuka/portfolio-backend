from fastapi import APIRouter, Depends
from app.supabase.supabase import supabase
from app.models.project import Project,ProjectCreate,ProjectUpdate
from app.database import get_db
from sqlalchemy.orm import Session
from uuid import UUID
from app.services import project_services

router = APIRouter()

@router.get("/projects/all",response_model=list[Project])
def get_all_projects(db : Session = Depends(get_db)):
    return project_services.getAllProjects(db)

@router.delete("project/delete/{id}",response_model=ProjectOut)
def delete_project(id : UUID, db:Session = Depends(get_db)):
    return project_services.deleteProject(id, db)

@router.post("project/create")
def create_project(project:ProjectCreate, db:Session = Depends(get_db)):
    return project_services.addProject(project, db)