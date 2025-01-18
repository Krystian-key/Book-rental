# === VALID ===


def test_return_rental_authorized(client, valid_headers):
    response = client.get("/rental/get-my-rented", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]

    rental_id = response.json()[0]["id"]
    response = client.put(f"/rental/return?id={rental_id}", headers=valid_headers)
    assert response.status_code == 200
    assert "return_date" in response.json()
    assert response.json()["return_date"] is not None


# === USER ===


def test_return_rental_user(client, invalid_headers):
    response = client.get("/rental/get-my-rented", headers=invalid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]

    rental_id = response.json()[0]["id"]
    response = client.put(f"/rental/return-my?id={rental_id}", headers=invalid_headers)
    assert response.status_code == 200
    assert "return_date" in response.json()
    assert response.json()["return_date"] is not None


# === NO AUTHORIZATION ===


def test_return_rental_no_auth(client):
    rental_id = 1
    response = client.put(f"/rental/return?id={rental_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu