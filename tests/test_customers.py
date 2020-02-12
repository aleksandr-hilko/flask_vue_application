import pytest
from app.models import Customer
from .common import fake


def generate_customer_data():
    customer_data = {
        "customer_name": fake.name(),
        "payment_account": str(fake.ipv4()),
        "email": fake.email(),
        "phone": fake.phone_number(),
    }
    return customer_data


@pytest.fixture
def customer(create_db):
    data = generate_customer_data()
    customer = Customer(**data)
    create_db.session.add(customer)
    create_db.session.commit()
    customer = Customer.query.filter(
        Customer.customer_name == customer.customer_name
    ).first()
    return customer


def test_get_customers(client, customer):
    response = client.get("/api/customers")
    assert response.status_code == 200
    resp_json = response.json
    assert len(resp_json) == 1
    assert customer.customer_name == resp_json[0]["customer_name"]
    assert customer.payment_account == resp_json[0]["payment_account"]
    assert customer.email == resp_json[0]["email"]
    assert customer.phone == resp_json[0]["phone"]


def test_get_customer(client, customer):
    response = client.get(f"/api/customers/{customer.id}")
    assert response.status_code == 200
    resp_json = response.json
    assert customer.customer_name == resp_json["customer_name"]
    assert customer.payment_account == resp_json["payment_account"]
    assert customer.email == resp_json["email"]
    assert customer.phone == resp_json["phone"]


def test_create_customer(client, create_db):
    data = generate_customer_data()
    resp = client.post("/api/customers", json=data)
    assert resp.status_code == 200
    resp_json = resp.json
    assert resp_json["customer_name"] == data["customer_name"]
    assert resp_json["payment_account"] == data["payment_account"]
    assert resp_json["email"] == data["email"]
    assert resp_json["phone"] == data["phone"]


def test_update_customer(client, customer):
    data = generate_customer_data()
    resp = client.put(f"/api/customers/{customer.id}", json=data)
    assert resp.status_code == 200
    resp = client.get(f"/api/customers/{customer.id}")
    resp_json = resp.json
    assert resp_json["customer_name"] == data["customer_name"]
    assert resp_json["payment_account"] == data["payment_account"]
    assert resp_json["email"] == data["email"]
    assert resp_json["phone"] == data["phone"]


def test_delete_customer(client, customer):
    resp = client.delete(f"/api/customers/{customer.id}")
    assert resp.status_code == 204
    resp = client.get(f"/api/customers/{customer.id}")
    assert resp.status_code == 404
