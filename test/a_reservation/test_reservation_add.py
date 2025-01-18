# === VALID ===


def test_add_reservation(client, valid_headers):
    reservation_add_data = {
        "user_id": 2,
        "copy_id": 3
    }
    response = client.post("/reservation/add", json=reservation_add_data, headers=valid_headers)
    assert response.status_code == 201
    assert response.json()["copy_id"] == 3


# === USER ===


def test_add_reservation_user(client, invalid_headers):
    reservation_add_data = {
        "user_id": 2,
        "copy_id": 4
    }
    response = client.post("/reservation/add", json=reservation_add_data, headers=invalid_headers)
    assert response.status_code == 201
    assert response.json()["copy_id"] == 4


# === NO AUTHORIZATION ===


def test_add_reservation_no_auth(client):
    reservation_add_data = {
        "user_id": 0,
        "copy_id": 1
    }
    response = client.post("/reservation/add", json=reservation_add_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === NO DATA ===


def test_add_reservation_no_data(client, valid_headers):
    response = client.post("/reservation/add", headers=valid_headers)
    assert response.status_code == 422


# === WRONG DATA ===


def test_add_reservation_wrong_data(client, valid_headers):
    reservation_add_data = {
        "urer_id": 0,
        "coy_id": 1
    }
    response = client.post("/reservation/add", json=reservation_add_data, headers=valid_headers)
    assert response.status_code == 422


# === LACKING DATA ===


def test_add_reservation_lacking_data(client, valid_headers):
    reservation_add_data = {
    }
    response = client.post("/reservation/add", json=reservation_add_data, headers=valid_headers)
    assert response.status_code == 422


# === CONFLICT ===


def test_add_reservation_conflict(client, valid_headers):
    reservation_add_data = {
        "user_id": 2,
        "copy_id": 3
    }
    response = client.post("/reservation/add", json=reservation_add_data, headers=valid_headers)
    assert response.status_code == 409