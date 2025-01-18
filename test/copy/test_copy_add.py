# === VALID ===


def test_add_copy(client, valid_headers):
    ed_id = 1
    copy_add_data = {
        "ed_id": ed_id
    }
    response = client.post("/copy/add", json=copy_add_data, headers=valid_headers)
    assert response.status_code == 201
    assert response.json()["ed_id"] == ed_id


# === INVALID ===


def test_add_copy_unauthorized(client, invalid_headers):
    copy_add_data = {
        "ed_id": 1
    }
    response = client.post("/copy/add", json=copy_add_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_add_copy_no_auth(client):
    copy_add_data = {
        "ed_id": 1
    }
    response = client.post("/copy/add", json=copy_add_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === NO DATA ===


def test_add_copy_no_data(client, valid_headers):
    response = client.post("/copy/add", headers=valid_headers)
    assert response.status_code == 422


# === WRONG DATA ===


def test_add_copy_wrong_data(client, valid_headers):
    copy_add_data = {
        "de_id": 1
    }
    response = client.post("/copy/add", json=copy_add_data, headers=valid_headers)
    assert response.status_code == 422


# === LACKING DATA ===


def test_add_copy_lacking_data(client, valid_headers):
    copy_add_data = {
    }
    response = client.post("/copy/add", json=copy_add_data, headers=valid_headers)
    assert response.status_code == 422