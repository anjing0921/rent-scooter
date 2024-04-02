from app import db
from app.models.rental import Rental
from app.models.customer import Customer
from app.models.scooter import Scooter
from flask import Blueprint, jsonify, make_response, request, abort
from app.routes.scooter_routes import get_not_available_scooters
from app.routes.routes_helper_functions import *

rentals_bp = Blueprint("rentals_bp", __name__, url_prefix="/rentals")

#============================== rentals_bp.route =============================
#============================================================================
# `POST /rentals/check-out`
# Rent an available scooter
# A customer should only be able to rent a scooter if it is not already currently being rented by another customer.
# A customer should only be able to rent a scooter if they are not currently renting another scooter.
#A customer should only be able to rent a scooter if it is >15% charged.
@rentals_bp.route("/check-out", methods=["POST"])
def create_rental():
    
    scooter_available_id_list = []
    scooters_not_available_query = get_not_available_scooters()
    scooters_all_query = Scooter.query.all()
    for scooter in scooters_all_query:
        if scooter.id not in scooters_not_available_query:
            scooter_available_id_list.append(scooter.id)
   
    print(f"scooter_available_id_list = {scooter_available_id_list}")
    customer_in_use_query = Customer.query.join(Rental).filter(Rental.is_returned == False)
    customer_in_use_id_list = []
    
    for customer in customer_in_use_query:
        customer_in_use_id_list.append(customer.id)

    print(customer_in_use_id_list)
    request_body = request.get_json()
    if request_body["scooter_id"] not in scooter_available_id_list :
        abort(make_response({"message":f"Scooter is not available."}, 400))

    if request_body["customer_id"] in customer_in_use_id_list :
        abort(make_response({"message":f"Please return your rental first."}, 400))
    
    customer = validate_model(Customer, request_body["customer_id"])
    scooter = validate_model(Scooter, request_body["scooter_id"])
    try:
        new_rental = Rental.from_dict(request_body)
    except:
        abort(make_response({"message":f"Missing data"}, 400))

    db.session.add(new_rental)
    db.session.add(customer)
    db.session.commit()

    rental_response = new_rental.to_dict()
   
    return jsonify(rental_response), 200

# `POST /rentals/check-in`
# Return a rented scooter
# Once a scooter is returned, it is available to rent by another customer.
@rentals_bp.route("/check-in", methods=["POST"])
def check_in_rental():
    request_body = request.get_json()
    try:
        rental = Rental.from_dict(request_body)
    except:
        abort(make_response({"message":f"Missing data"}, 400))
    customer = validate_model(Customer, request_body["customer_id"])
    scooter = validate_model(Scooter, request_body["scooter_id"])

    rental = db.session.query(Rental).filter_by(scooter_id=scooter.id, customer_id=customer.id).first() 
   
    rental.is_returned = True  

    db.session.add(rental)
    db.session.commit()

    rental_response = rental.to_dict()

    return jsonify(rental_response), 200