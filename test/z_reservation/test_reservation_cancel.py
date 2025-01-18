# === VALID ===


def test_cancel_reservation_authorized(client, valid_headers):
    response = client.get("/reservation/get-my-reserved", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]

    reservation_id = response.json()[0]["id"]
    response = client.put(f"/reservation/cancel?id={reservation_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "status" in response.json()[0]
    assert response.json()[0]["status"] == "Cancelled"


# === USER ===


def test_cancel_reservation_user(client, invalid_headers):
    response = client.get("/reservation/get-my-reserved", headers=invalid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]

    reservation_id = response.json()[0]["id"]
    response = client.put(f"/reservation/cancel-my?id={reservation_id}", headers=invalid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "status" in response.json()[0]
    assert response.json()[0]["status"] == "Cancelled"


# === NO AUTHORIZATION ===


def test_cancel_reservation_no_auth(client):
    reservation_id = 1
    response = client.put(f"/reservation/cancel?id={reservation_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu