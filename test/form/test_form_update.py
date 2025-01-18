# === VALID ===


def test_update_form_authorized(client, valid_headers):
    form_update_data = {
      "id": 1,
      "form": "Forma"
    }
    response = client.patch("/form/update", json=form_update_data, headers=valid_headers)
    assert response.status_code == 200
    assert response.json()["form"] == "Forma"


# === INVALID ===


def test_update_form_unauthorized(client, invalid_headers):
    form_update_data = {
        "id": 1,
        "form": "Forma"
    }
    response = client.patch("/form/update", json=form_update_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_update_form_no_auth(client):
    form_update_data = {
        "id": 1,
        "form": "Forma"
    }
    response = client.patch("/form/update", json=form_update_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu
