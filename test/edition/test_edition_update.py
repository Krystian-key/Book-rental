# === VALID ===


def test_update_edition_authorized(client, valid_headers):
    edition_update_data = {
      "id": 1,
      "ed_title": "Tytuł Wydania"
    }
    response = client.patch("/edition/update", json=edition_update_data, headers=valid_headers)
    assert response.status_code == 200
    assert response.json()["ed_title"] == "Tytuł Wydania"


# === INVALID ===


def test_update_edition_unauthorized(client, invalid_headers):
    edition_update_data = {
        "id": 1,
        "ed_title": "Unauthorized Update",
    }
    response = client.patch("/edition/update", json=edition_update_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_update_edition_no_auth(client):
    edition_update_data = {
        "id": 1,
        "ed_title": "No Auth Update",
    }
    response = client.patch("/edition/update", json=edition_update_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu
