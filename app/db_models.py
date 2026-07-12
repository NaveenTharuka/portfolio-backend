from sqlalchemy import Column, String, Boolean, Text, DateTime, Float, JSON
from sqlalchemy.dialects.postgresql import UUID
import uuid
import datetime
from app.database import Base

class Project(Base):
    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String, nullable=False)
    tech = Column(JSON, nullable=False)  # Store as JSON array
    image = Column(String, nullable=True)
    github = Column(String, nullable=True)
    tags = Column(JSON, nullable=True)  # Store as JSON array
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)

class Interest(Base):
    __tablename__="interests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    desc = Column(Text, nullable=False)
