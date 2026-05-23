import requests

class APIClient:
    def __init__(self, token="fake-token"):
        self.base_url = "https://api.example-crm.com"
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_customer(self, tenant_id, payload):
        return requests.post(
            f"{self.base_url}/tenants/{tenant_id}/customers",
            json=payload,
            headers=self.headers
        )