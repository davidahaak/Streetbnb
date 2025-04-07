from . import db
from sqlalchemy.sql import func

class Car(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100))
	location = db.Column(db.String(100))
	description = db.Column(db.Text)
	image_url = db.Column(db.String(200))
