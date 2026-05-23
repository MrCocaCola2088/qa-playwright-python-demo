import responses
from utils.api_client import APIClient

@responses.activate
def test_customer_not_accessible_from_other_tenant():
    responses.add(
        responses.POST,
        "https://api.example-crm.com/tenants/tenant-a/customers",
        json={"id": "123", "tenant_id": "tenant-a"},
        status=201
    )

    client = APIClient(token="fake-token")
    res = client.create_customer("tenant-a", {"name": "John"})
    
    assert res.status_code == 201