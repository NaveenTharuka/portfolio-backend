from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional, List
from datetime import datetime

class Contact(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    name:str
    email:str
    title:str
    message:str
    created_at:datetime = Field(default_factory=datetime.now)
    read:bool=False

class ContactCreate(BaseModel):
    name:str
    email:str
    title:str
    message:str

class ContactUpdate(BaseModel):
    read:bool

class ContactOut(Contact):
    pass