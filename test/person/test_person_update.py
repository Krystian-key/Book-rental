# === VALID ===


def test_update_person_authorized(client, valid_headers):
    person_update_data = {
      "id": 8,
      "name": "Imię"
    }
    response = client.patch("/person/update", json=person_update_data, headers=valid_headers)
    assert response.status_code == 200
    assert response.json()["name"] == "Imię"


# === INVALID ===


def test_update_person_unauthorized(client, invalid_headers):
    person_update_data = {
        "id": 8,
        "name": "Imię"
    }
    response = client.patch("/person/update", json=person_update_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_update_person_no_auth(client):
    person_update_data = {
        "id": 8,
        "name": "Imię"
    }
    response = client.patch("/person/update", json=person_update_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu
