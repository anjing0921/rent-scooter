from app import db
from app.models.rental import Rental
from app.models.customer import Customer
from app.models.scooter import Scooter
from flask import Blueprint, jsonify, make_response, request, abort
from app.routes.routes_helper_functions import *

scooters_bp = Blueprint("scooters_bp", __name__, url_prefix="/scooters")

#============================== videos_bp.route =============================
#============================================================================
def get_not_available_scooters():
        scooter_charge_percent_low_query = Scooter.query.filter(Scooter.charge_percent <= 15)
        scooter_in_ues_query = Scooter.query.filter(Scooter.charge_percent > 15).join(Rental).filter(Rental.is_returned == False)
        scooter_not_available_id_list = []
    
        for scooter in scooter_charge_percent_low_query:
            scooter_not_available_id_list.append(scooter.id)
        print(f"low charge = {scooter_not_available_id_list}")
        for scooter in scooter_in_ues_query:
            scooter_not_available_id_list.append(scooter.id)
        print(scooter_not_available_id_list)
        return scooter_not_available_id_list

#GET /scooters/available
#Retrieve a list of all scooters, with a filter query for limiting the list based on availability
@scooters_bp.route("/available", methods=["GET"])
def get_available_scooters():
    scooters_not_available_query = get_not_available_scooters()
    scooters_all_query = Scooter.query.all()
    response_body = []
    for scooter in scooters_all_query:
        if scooter.id not in scooters_not_available_query:
            response_body.append(scooter.to_dict())
    print(response_body)
    return jsonify(response_body)

# POST /scooters
@scooters_bp.route("", methods=["POST"])
def create_scooter():
    request_body = request.get_json()
    
    try:
        new_scooter = Scooter.from_dict(request_body)
    except KeyError as key_error:
        abort(make_response({"details":f"Request body must include {key_error.args[0]}."}, 400))
    
    db.session.add(new_scooter)
    db.session.commit()
    
    return make_response(jsonify(f"Scooter {new_scooter.id} successfully created"), 201)

#GET /scooters
@scooters_bp.route("", methods=["GET"])
def read_all_scooters():
    
    scooters = Scooter.query.all()

    scooters_response = []
    for scooter in scooters:
        scooters_response.append(scooter.to_dict())
        
    return jsonify(scooters_response)

# GET /scooters/<scooter_id>
@scooters_bp.route("/<scooter_id>", methods=["GET"])
def read_one_scooter(scooter_id):
    scooter = validate_model(Scooter,scooter_id)
    return scooter.to_dict()

# PUT /scooters/<scooter_id>
@scooters_bp.route("/<scooter_id>", methods=["PUT"])
def update_customer(scooter_id):
    scooter = validate_model(Scooter, scooter_id)

    try:
        request_body = request.get_json()
        scooter.model = request_body["model"]
        scooter.charge_percent= request_body["charge_percent"]
        
    except:
        abort(make_response(jsonify("Bad Request"), 400))

    db.session.commit()

    return make_response(f"scooter #{scooter.id} successfully updated")

# DELETE /customers/<scooter_id>
@scooters_bp.route("/<scooter_id>", methods=["DELETE"])
def delete_scooter(scooter_id):
    
    scooter  = validate_model(Customer,scooter_id)

    db.session.delete(scooter)
    db.session.commit()

    return make_response(f"Scooter #{scooter.id} successfully deleted")