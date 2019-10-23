from datetime import datetime
from app.wsgi import database as db


class BaseModel(db.Model):
    created_at = db.Column(db.DateTime(), nullable=False)
    updated_at = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    # @db.declared_attr
    # def __tablename__(cls):
    #     return f"{ cls.__name__.lower() }s"
