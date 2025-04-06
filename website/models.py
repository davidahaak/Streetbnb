from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func



class Car(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	location = db.Column(db.String(100))
	description = db.Column(db.Text)
	image_url = db.Column(db.String(200))
