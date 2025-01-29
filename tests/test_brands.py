import requests

def test_should_retrieve_at_least_two_brands(base_url):
    response = requests.get(f"{base_url}/brands")
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
    data = response.json()
    assert len(data) >= 2, f"Expected at least 2 brands, but got {len(data)}"