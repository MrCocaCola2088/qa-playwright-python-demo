from utils.api_client import APIClient
from unittest.mock import patch

@patch("utils.api_client.requests.post")
def test_create_customer(mock_post):
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {
        "id": "123",
        "name": "Test User"
    }

    client = APIClient()
    response = client.create_customer("tenant-a", {"name": "Test User"})

    assert response.status_code == 201
    assert response.json()["name"] == "Test User"