import pytest
from app import create_app
from app.models.rental import Rental
from app.models.customer import Customer
from app.models.scooter import Scooter
from app import db
from flask.signals import request_finished

SCOOTER_CHARGE_PERCENT = 52.3
SCOOTER_MODEL = "SHADOW SCREAM"


CUSTOMER_NAME = "ANNA"
CUSTOMER_EMAIL = "ANNA@GMAIL.COM"
CUSTOMER_PHONE = "123-123-1234"

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        db.session.remove()

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def one_scooter(app):
    new_scooter = Scooter(
        charge_percent=SCOOTER_CHARGE_PERCENT, 
        model=SCOOTER_MODEL
        )
    db.session.add(new_scooter)
    db.session.commit()

@pytest.fixture
def one_customer(app):
    new_customer = Customer(
        name=CUSTOMER_NAME,
        email=CUSTOMER_EMAIL,
        phone=CUSTOMER_PHONE
    )
    db.session.add(new_customer)
    db.session.commit()
