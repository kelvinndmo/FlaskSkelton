#your database models go here
from app import db
from sqlalchemy.dialects.postgresql import JSON


class User(db.Model):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(20), unique=True, nullable =False)
  email = db.Column(db.String(120), unique=True, nullable =False)
  image_file = db.Column(db.String(120), nullable =False, default='default.jpg')
  password = db.Column(db.String(60), nullable =False)