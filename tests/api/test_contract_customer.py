def test_customer_contract():
    fake_response = {
        "id": 1,
        "name": "John Doe"
    }

    from utils.schemas import CustomerSchema

    validated = CustomerSchema(**fake_response)

    assert validated.name == "John Doe"