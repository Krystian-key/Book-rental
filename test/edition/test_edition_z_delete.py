# === VALID ===


def test_delete_edition_authorized(client, valid_headers):
    response = client.get(f"/edition/get-by-isbn?isbn=11111111111")
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()

    edition_id = response.json()["id"]
    response = client.delete(f"/edition/delete?id={edition_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() == True


# === INVALID ===


def test_delete_edition_unauthorized(client, invalid_headers):
    edition_id = 8
    response = client.delete(f"/edition/delete?id={edition_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_delete_edition_no_auth(client):
    edition_id = 8
    response = client.delete(f"/edition/delete?id={edition_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === RESTRICTED ===


def test_delete_edition_restricted(client, valid_headers):
    edition_id = 1
    response = client.delete(f"/edition/delete?id={edition_id}", headers=valid_headers)
    assert response.status_code == 409