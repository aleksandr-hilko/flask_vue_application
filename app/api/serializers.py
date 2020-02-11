from marshmallow import Schema, fields, post_load, validates
from app.models import Customer, Person


class PersonSchema(Schema):
    id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    patronymic = fields.Str(required=False)
    email = fields.Str(required=False)
    phone = fields.Str(required=False)

    @post_load
    def make_person(self, data, **kwargs):
        return Person(**data)


class CustomerSchema(Schema):
    id = fields.Int(dump_only=True)
    customer_type = fields.Str()
    person = fields.Nested(PersonSchema, required=False)
    organization_name = fields.Str()
    payment_account = fields.Int(required=True)

    @validates("customer_type")
    def validate_customer_type(self, value):
        if value not in ["organization", "individual"]:
            raise ValidationError(
                "Customer should be either organization or individual."
            )


person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True)
