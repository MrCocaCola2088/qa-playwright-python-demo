from utils.api_client import APIClient
pytestmark = pytest.mark.integration
def test_create_customer_ui_and_verify_api(page):
    # Step 1: create via UI
    page.goto("https://example-crm.com/customers")

    page.click("text=New Customer")
    page.fill("#name", "Hybrid User")
    page.click("text=Save")

    # Step 2: get ID from UI (simulated)
    customer_id = "123"

    # Step 3: validate via API
    client = APIClient(token="fake_token")
    response = client.get_customer("tenant-a", customer_id)

    assert response.status_code == 200