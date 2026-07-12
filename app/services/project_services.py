from app.database import get_db
from sqlalchemy.orm import Session
from app.db_models import Project
from app.models.project import ProjectCreate
from fastapi import HTTPException

from uuid import UUID

def getAllProjects(db:Session):
    try:
        return db.query(Project).all()
        
    except Exception as e:
        return {"error":str(e)}

def addProject(project:ProjectCreate, db:Session):
    db_project = Project(
        title = project.title,
        description = project.description,
        category = project.category,
        tech = project.tech,
        image = project.image,
        github = project.github,
        tags = project.tags
    )

    try:
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project
    except Exception as e:
        return {"error":str(e)}


def deleteProject(id:UUID, db:Session):
    db_project = db.query(Project).filter(Project.id == id).first()

    if not db_project:
        raise HTTPException(status_code=404,detail="Project not Found")
    
    try:
        db.delete(db_project)
        db.commit()
        return {"message": "Project Deleted Successfully"}
    except Exception as e:
        return {"error":str(e)}