from datetime import datetime

from db.application import Base
from sqlalchemy import Column, DateTime, Integer, String, Text


class Community(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)
    created_at = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.utcnow)
