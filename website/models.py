from sqlalchemy import Column, Integer, String, Float, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from website import db

class Car(db.Model):
    __tablename__ = 'cars'
    
    id = Column(Integer, primary_key=True)
    brand = Column(String(100), nullable=False)
    model = Column(String(100), nullable=False)
    year = Column(Integer)
    price_per_day = Column(Float, nullable=False)
    location = Column(String(100), nullable=False)
    is_available = Column(Boolean, default=True)
    image_url = Column(String(255))
    season = Column(String(50))  # e.g., "Winter", "Summer", etc.

    bookings = relationship('Booking', backref='car', cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Car {self.brand} {self.model} (ID: {self.id})>'

class Booking(db.Model):
    __tablename__ = 'bookings'
    
    id = Column(Integer, primary_key=True)
    car_id = Column(Integer, ForeignKey('cars.id'), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    name = Column(String(100))  # Optional

    def __repr__(self):
        return f'<Booking for Car ID {self.car_id} from {self.start_date} to {self.end_date}>'
