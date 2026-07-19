from fastapi import APIRouter, Depends ,status
from app.models.contact import ContactOut ,ContactCreate
from app.services.contact_services import createContact, getContacts, deleteContact, markAsRead
from app.database import get_db
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List

router = APIRouter()

@router.post("/contact/create", response_model=ContactOut)
def create_contact(contact:ContactCreate, db: Session = Depends(get_db)):
    return createContact(contact, db)


@router.delete("/contact/delete/{id}")
def delete_contact(id:UUID, db:Session = Depends(get_db)):
    return deleteContact(id, db)

@router.put("/contact/mark_as_read/{id}", response_model=ContactOut)
def mark_as_read(id:UUID, read:bool ,db:Session = Depends(get_db)):
    return markAsRead(id, read, db)

@router.get("/contact/all", response_model=List[ContactOut])
def get_contacts(db:Session = Depends(get_db)):
    return getContacts(db)