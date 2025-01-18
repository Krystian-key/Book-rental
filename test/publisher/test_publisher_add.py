# === VALID ===


def test_add_publisher(client, valid_headers):
    publisher_add_data = {
      "name": "Wydawnictwotestowe",
      "localization": "awd",
      "foundation_year": 2025
    }
    response = client.post("/publisher/add", json=publisher_add_data, headers=valid_headers)
    assert response.status_code == 201
    assert response.json()["name"] == "Wydawnictwotestowe"


# === INVALID ===


def test_add_publisher_unauthorized(client, invalid_headers):
    publisher_add_data = {
        "name": "Wydawnictwotestowe",
        "localization": "Miasto",
        "foundation_year": 2025
    }
    response = client.post("/publisher/add", json=publisher_add_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_add_publisher_no_auth(client):
    publisher_add_data = {
        "name": "Wydawnictwotestowe",
        "localization": "Miasto",
        "foundation_year": 2025
    }
    response = client.post("/publisher/add", json=publisher_add_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === NO DATA ===


def test_add_publisher_no_data(client, valid_headers):
    response = client.post("/publisher/add", headers=valid_headers)
    assert response.status_code == 422


# === WRONG DATA ===


def test_add_publisher_wrong_data(client, valid_headers):
    publisher_add_data = {
        "nsame": "Wydawnictwotestowe",
        "localiazation": "Miasto",
        "founvdation_year": 2025
    }
    response = client.post("/publisher/add", json=publisher_add_data, headers=valid_headers)
    assert response.status_code == 422


# === LACKING DATA ===


def test_add_publisher_lacking_data(client, valid_headers):
    publisher_add_data = {
        "name": "Wydawnictwotestowe",
    }
    response = client.post("/publisher/add", json=publisher_add_data, headers=valid_headers)
    assert response.status_code == 422


# === CONFLICT ===


def test_add_publisher_conflict(client, valid_headers):
    publisher_add_data = {
        "name": "Wydawnictwotestowe",
        "localization": "awd",
        "foundation_year": 2025
    }
    response = client.post("/publisher/add", json=publisher_add_data, headers=valid_headers)
    assert response.status_code == 409