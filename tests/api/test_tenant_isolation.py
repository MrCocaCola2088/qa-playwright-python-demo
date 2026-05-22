from utils.api_client import APIClient

def test_customer_not_accessible_from_other_tenant():
    client = APIClient(token="fake_token")

    tenant_a = "tenant-a"
    tenant_b = "tenant-b"

    # Create customer in tenant A
    create_res = client.create_customer(tenant_a, {
        "name": "Tenant A User"
    })

    customer_id = create_res.json()["id"]

    # Try accessing from tenant B
    response = client.get_customer(tenant_b, customer_id)

    assert response.status_code in [403, 404]