# === VALID ===


def test_update_publisher_authorized(client, valid_headers):
    response = client.get(f"/publisher/get-by-name?name=Wydawnictwotestowe")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]
    publisher_update_data = {
      "id": response.json()[0]["id"],
      "localization": "Miasto"
    }
    response = client.patch("/publisher/update", json=publisher_update_data, headers=valid_headers)
    assert response.status_code == 200
    assert response.json()["localization"] == "Miasto"


# === INVALID ===


def test_update_publisher_unauthorized(client, invalid_headers):
    publisher_update_data = {
        "id": 8,
        "name": "Wydawnictwo"
    }
    response = client.patch("/publisher/update", json=publisher_update_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_update_publisher_no_auth(client):
    publisher_update_data = {
        "id": 8,
        "name": "Wydawnictwo"
    }
    response = client.patch("/publisher/update", json=publisher_update_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu
