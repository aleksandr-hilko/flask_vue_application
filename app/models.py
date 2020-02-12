from app import db


class AddressMixin:
    email = db.Column(db.String(120), nullable=True)
    phone = db.Column(db.String(120), nullable=True)
    address = db.Column(db.String(120), nullable=True)


class Employee(AddressMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50), nullable=True)
    profession = db.Column(db.String(50), nullable=False)
    is_manager = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Employee - {repr(self.person)}>"


class Customer(AddressMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(50), unique=True, nullable=False)
    payment_account = db.Column(db.String(20), unique=True, nullable=False)

    projects = db.relationship("Project", backref="customer")

    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        return f"<Customer - {repr(self.customer_name)}>"


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)

    start_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Project - {self.name}>"
