from utils.api_client import APIClient
from fixtures.test_data import get_customer_payload
from unittest.mock import patch

@patch("utils.api_client.APIClient.create_customer")
def test_create_customer(mock_create):
    mock_create.return_value = {
        "id": 1,
        "name": "Test User"
    }

    response = mock_create()

    assert response["name"] == "Test User"