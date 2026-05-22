from utils.schemas import CustomerSchema
from utils.api_client import APIClient

def test_customer_contract():
    client = APIClient(token="fake_token")

    response = client.create_customer("tenant-a", {
        "name": "John",
        "email": "john@test.com"
    })

    data = response.json()

    # Validate schema
    customer = CustomerSchema(**data)

    assert customer.name == "John"