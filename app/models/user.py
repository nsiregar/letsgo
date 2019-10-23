from app.wsgi import database as db
from db.model import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    id = db.Column(db.Integer(), primary_key=True)
    first_name = db.Column(db.String(), nullable=False)
