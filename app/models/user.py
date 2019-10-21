from datetime import datetime

from db.application import Base
from sqlalchemy import Column, DateTime, Integer, String, Text


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String)
    email = Column(Text, nullable=False)
    password_digest = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
