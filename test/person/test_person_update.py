# === VALID ===


def test_update_person_authorized(client, valid_headers):
    response = client.get(f"/person/get-by-name?name=Imię")
    #assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]
    person_update_data = {
      "id": response.json()[0]["id"],
      "surname": "Nowenazwisko"
    }
    response = client.patch("/person/update", json=person_update_data, headers=valid_headers)
    assert response.status_code == 200
    assert response.json()["surname"] == "Nowenazwisko"


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
