from app.api import bp
from app import db
from app.api.serializers import customer_schema
from flask import request
from marshmallow import ValidationError
from app.models import Customer
from sqlalchemy import or_


@bp.route("/customers", methods=["POST"])
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
    return result


@bp.route("/customers", methods=["GET"])
def get_customers():
    customers = Customer.query.all()
    customers = customer_schema.dump(customers, many=True)
    return {"customers": customers}


@bp.route("/customers/<int:pk>", methods=["GET"])
def get_customer(pk):
    customer = Customer.query.get_or_404(pk)
    customer = customer_schema.dump(customer)
    return {"customer": customer}


@bp.route("/customers/<int:pk>", methods=["PUT"])
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
    return result
