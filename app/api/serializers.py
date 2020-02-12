from marshmallow import (
    Schema,
    ValidationError,
    fields,
    post_load,
    validates,
    validate,
    validates_schema,
)
from app.models import Customer
from app import db


class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_type = fields.Str(validate=validate.OneOf(["organization", "individual"]))
    customer_name = fields.Str(validate=validate.Length(min=1))
    payment_account = fields.Str(required=True, validate=validate.Length(min=5, max=20))

    email = fields.Str(
        required=False, validate=validate.Email(error="Not a valid email address")
    )
    phone = fields.Str(required=False)
    address = fields.Str(required=False)

    @validates_schema
    def validate_unique(self, data, **kwargs):
        customer_name = data.get("customer_name")
        payment_account = data.get("payment_account")
        customer_exist = Customer.query.filter(
            Customer.customer_name == customer_name
        ).first()
        payment_exist = Customer.query.filter(
            Customer.payment_account == payment_account
        ).first()

        errors = {}
        if customer_exist:
            errors["customer_name"] = ["Customer with such a name already exists"]
        if payment_exist:
            errors["payment_exist"] = [
                "Customer with such a payment account already exists"
            ]
        if errors:
            raise ValidationError(errors)

    @post_load
    def make_user(self, data, **kwargs):
        return Customer(**data)


customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
