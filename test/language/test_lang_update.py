# === VALID ===


def test_update_lang_authorized(client, valid_headers):
    lang_update_data = {
      "id": 1,
      "lang": "Język"
    }
    response = client.patch("/language/update", json=lang_update_data, headers=valid_headers)
    assert response.status_code == 200
    assert response.json()["lang"] == "Język"


# === INVALID ===


def test_update_lang_unauthorized(client, invalid_headers):
    lang_update_data = {
        "id": 1,
        "lang": "Język"
    }
    response = client.patch("/language/update", json=lang_update_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_update_lang_no_auth(client):
    lang_update_data = {
        "id": 1,
        "lang": "Język"
    }
    response = client.patch("/language/update", json=lang_update_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu
