from fastapi import APIRouter, Depends
from app.supabase.supabase import supabase
from app.models.interest import InterestCreate, InterestOut
from app.database import get_db
from sqlalchemy.orm import Session
from uuid import UUID
from app.services import interest_services

router = APIRouter()

@router.get("/interests/all",response_model=list[InterestOut])
def get_all_interests(db : Session = Depends(get_db)):
    return interest_services.getAllInterests(db)

@router.delete("/interest/delete/{id}")
def delete_interest(id : UUID, db:Session = Depends(get_db)):
    return interest_services.deleteInterest(id, db)

@router.post("/interest/create",response_model=InterestOut)
def create_interest(interest:InterestCreate, db:Session = Depends(get_db)):
    return interest_services.addInterest(interest, db)