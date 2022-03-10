import requests

API_URL = "http://127.0.0.1:8000"


def test_get_index():
    response = requests.get(
        url=f"{API_URL}/"
    )

    assert response.status_code == 200
    data = response.json()

    assert "status" in data
    assert data["status"] == 1


def test_get_temperature():
    response = requests.get(
        url=f"{API_URL}/temperature",
        params={
            "lat": 0,
            "lon": 0
        }
    )

    assert response.status_code == 200, response.content

    response = requests.get(
        url=f"{API_URL}/temperature",
        params={
            "lat": 0,
        }
    )

    assert response.status_code == 422

    response = requests.get(
        url=f"{API_URL}/temperature",
        params={
            "lon": 0,
        }
    )

    assert response.status_code == 422
