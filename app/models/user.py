from app import app
from flask_sqlalchemy import SQLAlchemy
from uuid import uuid4
from ..config.connect import db
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

def get_uuid():
    return uuid4().hex

class User(db.Model):
    __tablename__= 'users'
    id = db.Column(db.String(11), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.Text, nullable=False)

    def create(user):
        hashed_password = bcrypt.generate_password_hash(user['password'])
        new_user = User(name=user['name'], email=user['email'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()

        return new_user