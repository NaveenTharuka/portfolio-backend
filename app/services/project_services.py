from app.database import get_db
from sqlalchemy.orm import Session

def getAllProjects(db:Session):
    try:
        return db.query(Project).all()
        
    except Exception as e:
        return {"error":str(e)}