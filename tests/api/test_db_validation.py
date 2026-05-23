from utils.api_client import APIClient
from utils.db_client import DBClient
@pytest.mark.skip(reason="Requires real DB")
def test_customer_persisted_in_db():
    api = APIClient(token="fake_token")
    db = DBClient()

    tenant_id = "tenant-a"

    # Step 1: create via API
    response = api.create_customer(tenant_id, {
        "name": "DB User",
        "email": "db@test.com"
    })

    customer_id = response.json()["id"]

    # Step 2: validate DB
    record = db.get_customer_by_id(customer_id)

    assert record is not None
    assert record[1] == "DB User"
    assert record[2] == tenant_id