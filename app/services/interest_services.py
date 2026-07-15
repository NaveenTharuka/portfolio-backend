from app.database import get_db
from sqlalchemy.orm import Session
from fastapi import HTTPException
from uuid import UUID

from app.db_models import Interest
from app.models.interest import InterestCreate, InterestOut

def getAllInterests(db:Session):
    try:
        return db.query(Interest).all()
    except Exception as e:
        return {"error" : str(e)}

def addInterest(interest:InterestCreate, db: Session):
    db_interest = Interest(
        title = interest.title,
        desc = interest.desc
    )

    try:
        db.add(db_interest)
        db.commit()
        db.refresh(db_interest)
        return db_interest
    except Exception as e:
        return {"error":str(e)}


def deleteInterest(id:UUID, db: Session):
    db_interest = db.query(Interest).filter(Interest.id == id).first()

    if not db_interest:
        raise HTTPException(status_code=404, detail="Interest not found")

    try:
        db.delete(db_interest)
        db.commit()
        return {"message": "Interest Deleted Successfully"}
    except Exception as e:
        return {"error" : str(e)}