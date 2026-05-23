def test_customer_contract():
    fake_response = {
    "id": "123",  # must be string
    "name": "John Doe",
    "email": "john@test.com",
    "tenant_id": "tenant-a"
}

    from utils.schemas import CustomerSchema

    validated = CustomerSchema(**fake_response)

    assert validated.name == "John Doe"