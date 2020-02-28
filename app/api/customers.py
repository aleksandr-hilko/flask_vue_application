from app.api import bp
from app import db
from app.api.serializers import customer_schema
from flask import request, jsonify
from marshmallow import ValidationError
from app.models import Customer
from app.helpers import check_token


@bp.route("/customers", methods=["POST"])
@check_token
def create_customer():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    try:
        customer = customer_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400
    db.session.add(customer)
    db.session.commit()
    result = customer_schema.dump(
        Customer.query.filter(Customer.customer_name == customer.customer_name).first()
    )
    return jsonify(result), 201


@bp.route("/customers", methods=["GET"])
@check_token
def get_customers():
    customers = Customer.query.all()
    customers = customer_schema.dump(customers, many=True)
    return jsonify(customers)


@bp.route("/customers/<int:pk>", methods=["GET"])
@check_token
def get_customer(pk):
    customer = Customer.query.get_or_404(pk)
    customer = customer_schema.dump(customer)
    return jsonify(customer)


@bp.route("/customers/<int:pk>", methods=["PUT"])
@check_token
def update_customer(pk):
    customer = Customer.query.get_or_404(pk)
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400
    errors = customer_schema.validate(json_data, partial=True)
    if errors:
        return errors, 400
    customer.update(**json_data)
    db.session.commit()
    result = customer_schema.dump(customer)
    return jsonify(result), 201


@bp.route("/customers/<int:pk>", methods=["DELETE"])
@check_token
def delete_customer(pk):
    customer = Customer.query.get_or_404(pk)
    db.session.delete(customer)
    db.session.commit()
    return "", 204
