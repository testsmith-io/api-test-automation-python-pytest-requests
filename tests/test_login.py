import requests

def test_should_return_access_token_on_successful_login(base_url):
    payload = {
        "email": "customer@practicesoftwaretesting.com",
        "password": "welcome01"
    }
    response = requests.post(f"{base_url}/users/login", json=payload)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    response_body = response.json()
    assert "access_token" in response_body, "Response does not contain 'access_token'"
