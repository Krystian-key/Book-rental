# === VALID ===


def test_add_rental(client, valid_headers):
    rental_add_data = {
        "user_id": 2,
        "copy_id": 1
    }
    response = client.post("/rental/add", json=rental_add_data, headers=valid_headers)
    assert response.status_code == 201
    assert response.json()["copy_id"] == 1


# === USER ===


def test_add_rental_user(client, invalid_headers):
    rental_add_data = {
        "user_id": 2,
        "copy_id": 2
    }
    response = client.post("/rental/add", json=rental_add_data, headers=invalid_headers)
    assert response.status_code == 201
    assert response.json()["copy_id"] == 2


# === NO AUTHORIZATION ===


def test_add_rental_no_auth(client):
    rental_add_data = {
        "user_id": 0,
        "copy_id": 1
    }
    response = client.post("/rental/add", json=rental_add_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === NO DATA ===


def test_add_rental_no_data(client, valid_headers):
    response = client.post("/rental/add", headers=valid_headers)
    assert response.status_code == 422


# === WRONG DATA ===


def test_add_rental_wrong_data(client, valid_headers):
    rental_add_data = {
        "reer_id": 0,
        "coy_id": 1
    }
    response = client.post("/rental/add", json=rental_add_data, headers=valid_headers)
    assert response.status_code == 422


# === LACKING DATA ===


def test_add_rental_lacking_data(client, valid_headers):
    rental_add_data = {
    }
    response = client.post("/rental/add", json=rental_add_data, headers=valid_headers)
    assert response.status_code == 422


# === CONFLICT ===


def test_add_rental_conflict(client, valid_headers):
    rental_add_data = {
        "user_id": 2,
        "copy_id": 1
    }
    response = client.post("/rental/add", json=rental_add_data, headers=valid_headers)
    assert response.status_code == 409