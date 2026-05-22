import requests

BASE_URL = "https://api.example-crm.com"

class APIClient:
    def __init__(self, token):
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_customer(self, tenant_id, payload):
        return requests.post(
            f"{BASE_URL}/tenants/{tenant_id}/customers",
            json=payload,
            headers=self.headers
        )

    def get_customer(self, tenant_id, customer_id):
        return requests.get(
            f"{BASE_URL}/tenants/{tenant_id}/customers/{customer_id}",
            headers=self.headers
        )