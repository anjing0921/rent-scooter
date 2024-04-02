from app import db
from app.models.customer import Customer
from app.models.rental import Rental
from app.models.scooter import Scooter
from flask import Blueprint, jsonify, make_response, request, abort
from app.routes.routes_helper_functions import *

customers_bp = Blueprint("customers_bp", __name__, url_prefix="/customers")

#============================== customers_bp.route =============================
#============================================================================

# POST /customers
@customers_bp.route("", methods=["POST"])
def create_customer():
    request_body = request.get_json()
    try:
        new_customer = Customer.from_dict(request_body)
    except KeyError as key_error:
        abort(make_response({"details":f"Request body must include {key_error.args[0]}."}, 400))
    
    db.session.add(new_customer)
    db.session.commit()

    return make_response(jsonify(f"Customer {new_customer.name} successfully created"), 201)

#GET /customers
@customers_bp.route("", methods=["GET"])
def read_all_customers():

    customers = Customer.query.all()

    customers_response = []
    for customer in customers:
        customers_response.append(customer.to_dict())
        
    return jsonify(customers_response)


# GET /customers/<customer_id>
@customers_bp.route("/<customer_id>", methods=["GET"])
def read_one_customer(customer_id):
    
    customer = validate_model(Customer,customer_id)

    return customer.to_dict()

# PUT /customers/<customer_id>
@customers_bp.route("/<customer_id>", methods=["PUT"])
def update_customer(customer_id):
    
    customer = validate_model(Customer, customer_id)

    try:
        request_body = request.get_json()
        customer.name = request_body["name"]
        customer.email = request_body["email"]
        customer.phone = request_body["phone"]
    except:
        abort(make_response(jsonify("Bad Request"), 400))

    db.session.commit()

    return make_response(f"Customer #{customer.id} successfully updated")


# DELETE /customers/<customer_id>
@customers_bp.route("/<customer_id>", methods=["DELETE"])
def delete_customer(customer_id):
    
    customer  = validate_model(Customer,customer_id)

    db.session.delete(customer)
    db.session.commit()

    return make_response(f"Customer #{customer.id} successfully deleted")

# `GET /customers/<customer_id>/rentals`
#List the customers who currently have the scooter checked out
# @customers_bp.route("/<customer_id>/rentals", methods=["GET"])
# def get_rentals_by_customer_id(customer_id):

#     customer = validate_model(Customer, customer_id)
#     Scooter_query = Rental.query.filter_by(customer_id=customer.id).join(Scooter)
#     request_body = request.get_json()
#     new_rental = Rental(
#         is_returned = request_body["is_returned"],
#         customer = customer
#     )

#     db.session.add(new_rental)
#     db.session.commit()

#     return make_response(jsonify(f"Rental {new_rental.id} by {new_rental.customer.name} successfully created"), 201)

# `GET /customers/<id>/rentals`
#List the customers who previous have the scooter checked out
@customers_bp.route("/<id>/history", methods=["GET"])
def read_a_customers_all_rental_history(id):
    customer = validate_model(Customer, id)
    customer_rental = Rental.query.filter_by(customer_id=customer.id,check_out_status = False).join(Video).all()

    customer_history_res =[]
    for video in customer_rental:
        customer_history_res.append(video.video.to_dict())
    return jsonify(customer_history_res), 200