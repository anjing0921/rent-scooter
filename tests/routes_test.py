from app.models.rental import Rental
from app.models.customer import Customer
from app.models.scooter import Scooter


SCOOTER_CHARGE_PERCENT = 52.3
SCOOTER_MODEL = "SHADOW SCREAM"
SCOOTER_ID = 1


CUSTOMER_NAME = "ANNA"
CUSTOMER_ID = 1
CUSTOMER_EMAIL = "ANNA@GMAIL.COM"
CUSTOMER_PHONE = "123-123-1234"

def test_get_all_customers_with_no_records(client):
    # Act
    response = client.get("/customers")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_customers_one_saved_customer(client, one_customer):
    # Act
    response = client.get("/customers")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0]["name"] == CUSTOMER_NAME
    assert response_body[0]["id"] == CUSTOMER_ID
    assert response_body[0]["phone"] == CUSTOMER_PHONE
    assert response_body[0]["email"] == CUSTOMER_EMAIL

def test_get_scooter(client, one_scooter):
    # Act
    response = client.get("/scooters/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["model"] == SCOOTER_MODEL
    assert response_body["id"] == SCOOTER_ID
    assert response_body["change_percent"] == SCOOTER_CHARGE_PERCENT

