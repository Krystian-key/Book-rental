# === VALID ===


def test_add_form(client, valid_headers):
    form_add_data = {
        "form": "Formatestowa"
    }
    response = client.post("/form/add", json=form_add_data, headers=valid_headers)
    assert response.status_code == 201
    assert response.json()["form"] == "Formatestowa"


# === INVALID ===


def test_add_form_unauthorized(client, invalid_headers):
    form_add_data = {
        "form": "asda"
    }
    response = client.post("/form/add", json=form_add_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_add_form_no_auth(client):
    form_add_data = {
        "form": "asda"
    }
    response = client.post("/form/add", json=form_add_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === NO DATA ===


def test_add_form_no_data(client, valid_headers):
    response = client.post("/form/add", headers=valid_headers)
    assert response.status_code == 422


# === WRONG DATA ===


def test_add_form_wrong_data(client, valid_headers):
    form_add_data = {
        "from": "asda"
    }
    response = client.post("/form/add", json=form_add_data, headers=valid_headers)
    assert response.status_code == 422


# === LACKING DATA ===


def test_add_form_lacking_data(client, valid_headers):
    form_add_data = {
    }
    response = client.post("/form/add", json=form_add_data, headers=valid_headers)
    assert response.status_code == 422


# === CONFLICT ===


def test_add_form_conflict(client, valid_headers):
    form_add_data = {
        "form": "Formatestowa"
    }
    response = client.post("/form/add", json=form_add_data, headers=valid_headers)
    assert response.status_code == 409