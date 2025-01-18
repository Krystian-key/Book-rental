# === VALID ===


def test_add_lang(client, valid_headers):
    lang_add_data = {
        "lang": "Język"
    }
    response = client.post("/language/add", json=lang_add_data, headers=valid_headers)
    assert response.status_code == 201
    assert response.json()["lang"] == "Język"


# === INVALID ===


def test_add_lang_unauthorized(client, invalid_headers):
    lang_add_data = {
        "lang": "asda"
    }
    response = client.post("/language/add", json=lang_add_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_add_lang_no_auth(client):
    lang_add_data = {
        "lang": "asda"
    }
    response = client.post("/language/add", json=lang_add_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === NO DATA ===


def test_add_lang_no_data(client, valid_headers):
    response = client.post("/language/add", headers=valid_headers)
    assert response.status_code == 422


# === WRONG DATA ===


def test_add_lang_wrong_data(client, valid_headers):
    lang_add_data = {
        "lansdg": "asda"
    }
    response = client.post("/language/add", json=lang_add_data, headers=valid_headers)
    assert response.status_code == 422


# === LACKING DATA ===


def test_add_lang_lacking_data(client, valid_headers):
    lang_add_data = {
    }
    response = client.post("/language/add", json=lang_add_data, headers=valid_headers)
    assert response.status_code == 422


# === CONFLICT ===


def test_add_lang_conflict(client, valid_headers):
    lang_add_data = {
        "lang": "Język"
    }
    response = client.post("/language/add", json=lang_add_data, headers=valid_headers)
    assert response.status_code == 409