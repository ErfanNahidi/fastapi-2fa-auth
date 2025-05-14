from sqlalchemy import Column , String , DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from .database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True , default=uuid.uuid4)
    username = Column(String, unique=True , nullable=False)
    password_hash = Column(String, nullable=False)
    opt_secret = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    last_login = Column(DateTime, nullable=True)