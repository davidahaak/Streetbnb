from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models import Car, Booking  # Added Booking model
from . import db

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template('home.html')

@views.route('/cars', methods=['GET', 'POST'])
def list_cars():
    if request.method == 'POST':
        search_location = request.form.get('location').strip().lower()
        cars = Car.query.filter(Car.location.ilike(f"%{search_location}%")).all()
        
        if not cars:
            flash(f'No listings available for "{search_location.title()}". Showing all cars instead.')
            return redirect(url_for('views.list_cars'))
        
        return render_template('car_list.html', cars=cars)

    # GET request fallback
    cars = Car.query.filter_by(is_available=True).all()
    return render_template('car_list.html', cars=cars)

@views.route('/book/<int:car_id>', methods=['GET', 'POST'])
def book_car(car_id):
    car = Car.query.get_or_404(car_id)

    if request.method == 'POST':
        name = request.form.get('name')
        start_date = request.form.get('start_date')
        end_date = request.form.get('end_date')

        booking = Booking(
            car_id=car.id,
            start_date=start_date,
            end_date=end_date,
            name=name
        )

        db.session.add(booking)
        db.session.commit()

        flash('✅ Booking successful!')
        return redirect(url_for('views.list_cars'))

    return render_template('book_car.html', car=car)
