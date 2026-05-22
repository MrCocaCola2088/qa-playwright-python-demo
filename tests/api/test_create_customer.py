from utils.api_client import APIClient
from fixtures.test_data import get_customer_payload

def test_create_customer():
    client = APIClient(token="fake_token")

    tenant_id = "tenant-a"
    payload = get_customer_payload()

    response = client.create_customer(tenant_id, payload)

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == payload["name"]
    assert data["tenant_id"] == tenant_id