from app import db


class AddressMixin:
    email = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=True)


class UpdateModelMixin:
    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


class Employee(AddressMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50), nullable=True)
    profession = db.Column(db.String(50), nullable=False)
    is_manager = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Employee - {repr(self.person)}>"


class Customer(AddressMixin, UpdateModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50), unique=True, nullable=False)
    payment_account = db.Column(db.String(20), unique=True, nullable=False)

    projects = db.relationship("Project", backref="customer")

    def __repr__(self):
        return f"<Customer - {repr(self.customer_name)}>"


class Project(UpdateModelMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)
    has_contract = db.Column(db.Boolean, default=False, nullable=True)
    has_plan = db.Column(db.Boolean, default=False, nullable=True)
    price = db.Column(db.Integer, nullable=True)

    contract = db.Column(db.String(200), nullable=True)

    start_date = db.Column(db.DateTime, nullable=True)
    expiration_date = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f"<Project - {self.name}>"
