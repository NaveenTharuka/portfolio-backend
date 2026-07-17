from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional, List
from datetime import datetime

# Base Project model (for responses)
class Project(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    title: str
    description: str
    category: str
    image: Optional[str] = None  
    github: Optional[str] = None  
    demo_url:Optional[str] = None
    tags: List[str] 
    created_at: Optional[datetime] = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)

# For creating new projects (input model)
class ProjectCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    description: str = Field(..., min_length=1, max_length=1000)
    category: str = Field(..., min_length=1, max_length=50)
    image: Optional[str] = None
    github: Optional[str] = None
    demo_url:Optional[str] = None
    tags: List[str] = Field(default_factory=list)

# For updating existing projects (partial updates)
class ProjectUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1, max_length=1000)
    category: Optional[str] = Field(None, min_length=1, max_length=50)
    image: Optional[str] = None
    github: Optional[str] = None
    demo_url:Optional[str] = None
    tags: Optional[List[str]] = None