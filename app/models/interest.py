from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional, List
from datetime import datetime

class Interest(BaseModel):
    id:UUID = Field(default_factory=uuid4)
    title : str
    desc : str

class InterestCreate(BaseModel):
    title: str
    desc: str

class InterestOut(Interest):
    pass
    
