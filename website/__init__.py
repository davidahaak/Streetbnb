from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'abcdefghijklmnop'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:18427DaH#@localhost:3306/streetbnb_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Optional but recommended

    db.init_app(app)

    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .models import Car  

    with app.app_context():
        db.create_all()

    return app
