import requests
import pytest

@pytest.fixture
def login(base_url):
    payload = {
        "email": "customer@practicesoftwaretesting.com",
        "password": "welcome01"
    }
    response = requests.post(f"{base_url}/users/login", json=payload)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    return response.json().get("access_token")

def test_should_retrieve_invoices_with_valid_token(base_url, login):
    token = login
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{base_url}/invoices", headers=headers)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json().get("data", [])
    assert len(data) >= 15, f"Expected at least 15 invoices, but got {len(data)}"
 