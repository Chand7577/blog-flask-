from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


# user table


class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(155),unique=True)
    username=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    date_created=db.Column(db.DateTime(), default=func.now())