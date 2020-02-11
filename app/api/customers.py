from app.api import bp
from app import db
from app.api.serializers import customer_schema, person_schema
from flask import request
from marshmallow import ValidationError
from app.models import Customer


@bp.route("/customers", methods=["POST"])
def create_customer():
    json_data = request.get_json()
    if not json_data:
        return {"message": "No input data provided"}, 400

    person_data = json_data["person"]
    try:
        person = person_schema.load(person_data)
    except ValidationError as err:
        return err.messages, 400
    db.session.add(person)

    try:
        data = customer_schema.load(json_data)
    except ValidationError as err:
        return err.messages, 400

    customer = Customer(
        customer_type=data.get("customer_type"),
        person=person,
        organization_name=data.get("organization_name"),
        payment_account=data.get("payment_account"),
    )

    db.session.add(customer)
    db.session.commit()
    result = customer_schema.dump(Customer.query.get(customer.id))
    return {"customer": result}
