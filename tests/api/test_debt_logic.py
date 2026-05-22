def test_debt_record_calculation():
    # simulate request
    payload = {
        "amount": 1000,
        "interest": 0.1
    }

    # fake response simulation
    response_data = {
        "total": 1100
    }

    assert response_data["total"] == payload["amount"] * (1 + payload["interest"])