# === VALID ===


def test_add_person(client, valid_headers):
    person_add_data = {
      "name": "Imię",
      "surname": "Nazwisko",
      "birth_year": 1234,
      "death_year": 1238
    }
    response = client.post("/person/add", json=person_add_data, headers=valid_headers)
    assert response.status_code == 201
    assert response.json()["name"] == "Imię"


# === INVALID ===


def test_add_person_unauthorized(client, invalid_headers):
    person_add_data = {
        "name": "Imię",
        "surname": "Nazwisko",
        "birth_year": 1234,
        "death_year": 1238
    }
    response = client.post("/person/add", json=person_add_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_add_person_no_auth(client):
    person_add_data = {
        "name": "Imię",
        "surname": "Nazwisko",
        "birth_year": 1234,
        "death_year": 1238
    }
    response = client.post("/person/add", json=person_add_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === NO DATA ===


def test_add_person_no_data(client, valid_headers):
    response = client.post("/person/add", headers=valid_headers)
    assert response.status_code == 422


# === WRONG DATA ===


def test_add_person_wrong_data(client, valid_headers):
    person_add_data = {
        "namse": "Imię",
        "surname": "Nazwisko",
        "birvth_year": 1234,
        "death_year": 1238
    }
    response = client.post("/person/add", json=person_add_data, headers=valid_headers)
    assert response.status_code == 422


# === LACKING DATA ===


def test_add_person_lacking_data(client, valid_headers):
    person_add_data = {
        "surname": "Nazwisko",
        "birth_year": 1234,
        "death_year": 1238
    }
    response = client.post("/person/add", json=person_add_data, headers=valid_headers)
    assert response.status_code == 422


# === CONFLICT ===


def test_add_person_conflict(client, valid_headers):
    person_add_data = {
        "name": "Imię",
        "surname": "Nazwisko",
        "birth_year": 1234,
        "death_year": 1238
    }
    response = client.post("/person/add", json=person_add_data, headers=valid_headers)
    assert response.status_code == 409