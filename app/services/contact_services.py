from app.models.contact import Contact, ContactOut ,ContactUpdate, ContactCreate
from app.db_models import Contact
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from uuid import UUID

def createContact(contact:ContactCreate, db: Session):
    db_contact = Contact(
        name = contact.name,
        email = contact.email,
        title = contact.title,
        message = contact.message
    )
    try:
        db.add(db_contact)
        db.commit()
        db.refresh(db_contact)
        return db_contact
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def getContacts(db: Session):
    try:
        contacts = db.query(Contact).all()
        return contacts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
def deleteContact(id:UUID, db: Session):
    db_contact = db.query(Contact).filter(Contact.id == id).first()

    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    try:
        db.delete(db_contact)
        db.commit()
        return {"message": "Contact Deleted Successfully"}, status.HTTP_200_OK
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def markAsRead(id:UUID, db:Session):
    db_contact = db.query(Contact).filter(Contact.id == id).first()

    if not db_contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    try:
        db_contact.read = True
        db.commit()
        db.refresh(db_contact)
        return db_contact
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))