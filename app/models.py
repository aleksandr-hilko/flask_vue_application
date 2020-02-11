from app import db
import enum


class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    patronymic = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    phone = db.Column(db.String(120), unique=True, nullable=True)

    employee = db.relationship("Employee", uselist=False, backref="person")
    customer = db.relationship("Customer", uselist=False, backref="person")

    def __repr__(self):
        return f"<Person {self.first_name} {self.last_name} {self.patronymic}>"


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=False)
    profession = db.Column(db.String(50), nullable=False)
    is_manager = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Employee - {repr(self.person)}>"


class CustomerTypeEnum(enum.Enum):
    organization = "organization"
    individual = "individual"


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_type = db.Column(
        db.Enum(CustomerTypeEnum), default=CustomerTypeEnum.individual, nullable=False
    )
    owner_id = db.Column(db.Integer, db.ForeignKey("person.id"), nullable=True)
    organization_name = db.Column(db.String(50), unique=True, nullable=True)
    payment_account = db.Column(db.Integer, unique=True, nullable=False)

    projects = db.relationship("Project", backref="customer")

    def __repr__(self):
        return self.organization_name or f"<Customer - {repr(self.person)}>"


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"), nullable=False)

    start_date = db.Column(db.DateTime, nullable=False)
    expiration_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<Project - {self.name}>"
