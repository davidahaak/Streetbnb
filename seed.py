from website import create_app, db
from website.models import Car

app = create_app()

with app.app_context():
    cars = [

        Car(
            brand="Subaru",
            model="Outback",
            year=2022,
            price_per_day=65.0,
            location="Denver",
            is_available=True,
            image_url="images/cars/subaru_outback.jpg",
            season="Winter"
        ),

        Car(
            brand="Toyota",
            model="Camry",
            year=2021,
            price_per_day=45.0,
            location="Phoenix",
            is_available=True,
            image_url="images/cars/toyota_camry.png",
            season="Summer"
        ),

        Car(
            brand="Jeep",
            model="Wrangler",
            year=2023,
            price_per_day=80.0,
            location="Salt Lake City",
            is_available=True,
            image_url="images/cars/jeep_wrangler.AVIF",
            season="Winter"
        ),

        Car(
            brand="Audi",
            model="Q5",
            year=2021,
            price_per_day=95.0,
            location="Aspen",
            is_available=True,
            image_url="images/cars/audi_q5.jpg",
            season="Winter"
        ),

        Car(
            brand="Jeep",
            model="Grand Cherokee",
            year=2022,
            price_per_day=85.0,
            location="Aspen",
            is_available=True,
            image_url="images/cars/jeep_grand_cherokee.AVIF",
            season="Winter"
        ),

        Car(
            brand="BMW",
            model="4 Series Convertible",
            year=2020,
            price_per_day=120.0,
            location="Palm Beach",
            is_available=True,
            image_url="images/cars/bmw_4series_convertible.AVIF",
            season="Summer"
        ),

        Car(
            brand="Ford",
            model="Mustang Convertible",
            year=2021,
            price_per_day=110.0,
            location="Palm Beach",
            is_available=True,
            image_url="images/cars/ford_mustang_convertible.AVIF",
            season="Summer"
        ),

        Car(
            brand="Toyota",
            model="RAV4",
            year=2022,
            price_per_day=70.0,
            location="Cape Cod",
            is_available=True,
            image_url="images/cars/toyota_rav4.AVIF",
            season="Fall"
        ),

        Car(
            brand="Honda",
            model="CR-V",
            year=2021,
            price_per_day=68.0,
            location="Cape Cod",
            is_available=True,
            image_url="images/cars/honda_crv.jpg",
            season="Fall"
        ),

        Car(
            brand="Tesla",
            model="Model 3",
            year=2023,
            price_per_day=130.0,
            location="Seattle",
            is_available=True,
            image_url="images/cars/tesla_model3.jpg",
            season="Spring"
        )

    ]

    db.session.add_all(cars)
    db.session.commit()
