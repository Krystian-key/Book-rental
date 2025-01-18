# === VALID ===


def test_delete_publisher_authorized(client, valid_headers):
    name = "Wydawnictwotestowe"
    response = client.get(f"/publisher/get-by-name?name={name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]
    publisher_id = response.json()[0]["id"]
    print(f"Publisher ID: {publisher_id}")
    response = client.delete(f"/publisher/delete?id={publisher_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() == True


# === INVALID ===


def test_delete_publisher_unauthorized(client, invalid_headers):
    publisher_id = 8
    response = client.delete(f"/publisher/delete?id={publisher_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_delete_publisher_no_auth(client):
    publisher_id = 8
    response = client.delete(f"/publisher/delete?id={publisher_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === RESTRICTED ===


def test_delete_publisher_restricted(client, valid_headers):
    publisher_id = 1
    response = client.delete(f"/publisher/delete?id={publisher_id}", headers=valid_headers)
    assert response.status_code == 409