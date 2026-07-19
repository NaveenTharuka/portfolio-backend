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
    image = Column(String, nullable=True)
    github = Column(String, nullable=True)
    demo_url = Column(String, nullable=True)
    tags = Column(JSON, nullable=True)  # Store as JSON arra
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)

class Interest(Base):
    __tablename__="interests"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = Column(String, nullable=False)
    description = Column(Text, nullable=False)

class Contact(Base):
    __tablename__="contacts"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    title = Column(String, nullable=False)
    message = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    read = Column(Boolean, default=False)