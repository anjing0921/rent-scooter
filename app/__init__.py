from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()

def create_app(test_config=None):
    app = Flask(__name__)

    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")
    
    # Import models here for Alembic setup
    from app.models.rental import Rental
    from app.models.scooter import Scooter
    from app.models.customer import Customer

     # Register Blueprints here
    from .routes.scooter_routes import scooters_bp
    app.register_blueprint(scooters_bp)
    
    from .routes.customer_routes import customers_bp
    app.register_blueprint(customers_bp)

    from .routes.rental_routes import rentals_bp
    app.register_blueprint(rentals_bp)
    

    db.init_app(app)
    migrate.init_app(app, db)

    


    return app