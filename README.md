# Streetbnb

Streetbnb is a simple web application that serves as a seasonal car rental platform. The goal of this project is to make it easy for users to browse and book cars for seasonal stays in popular destinations like Aspen, Cape Cod, and Palm Beach. Unlike traditional daily rental services, Streetbnb is designed for people staying for longer periods who want something more flexible and straightforward.

## About the Project

This project was built for the CPSC-4345 Database Systems course. It showcases how relational databases can be used alongside web development tools to create a functional application.

The focus was on keeping things clean and easy to use, without overcomplicating the design. Users can search for available cars, view listings, and book a car directly through the website.

## Main Features

- Search cars by location
- View available cars (availability is automatically handled)
- Book a car with a simple form — no login or account required
- Clean and responsive design using Bootstrap
- Car images stored locally (no external hosting)

## Tools and Technologies

- Python (Flask framework)
- MySQL (with SQLAlchemy ORM)
- HTML, Bootstrap, Jinja2 for the frontend
- Local static files for images and CSS

## How to Run

### Prerequisites

- Python 3.x installed
- MySQL server running
- Install the required Python libraries

### Setup

1. Clone the repository:


git clone https://github.com/yourusername/streetbnb.git
cd streetbnb


2. Install dependencies:


pip install -r requirements.txt


3. Update the database URI in `__init__.py` to match your MySQL credentials:

python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/dbname'


4. Create the database tables:

python
python
>>> from website import db, create_app
>>> app = create_app()
>>> with app.app_context():
    db.create_all()


5. Run the app:

python main.py


Once it's running, you can visit `http://127.0.0.1:5000/` in your browser.

## Notes and Future Ideas

Right now, the app is simple and focuses on core functionality. In the future, it could be expanded with:

- User accounts and admin panel for adding/editing cars
- Filtering by season or availability dates
- Ability for users to manage their bookings

## Credits

This project was developed by David Haak and Balqees Mohammad as part of our work for the Database Systems course.

---

Thanks for checking out our project!
