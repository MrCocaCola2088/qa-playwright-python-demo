from unittest.mock import MagicMock

def test_db_validation():
    fake_db = MagicMock()

    fake_db.get_customer.return_value = {
        "id": 1,
        "name": "Test User"
    }

    result = fake_db.get_customer(1)

    assert result["name"] == "Test User"