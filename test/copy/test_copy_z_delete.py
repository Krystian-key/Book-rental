# === VALID ===


def test_delete_copy_authorized(client, valid_headers):
    response = client.get("/copy/get-all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]

    copy_id = response.json()[len(response.json())-1]["id"]
    response = client.delete(f"/copy/delete?id={copy_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() == True


# === INVALID ===


def test_delete_copy_unauthorized(client, invalid_headers):
    copy_id = 8
    response = client.delete(f"/copy/delete?id={copy_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_delete_copy_no_auth(client):
    copy_id = 8
    response = client.delete(f"/copy/delete?id={copy_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === RESTRICTED ===


def test_delete_copy_restricted(client, valid_headers):
    copy_id = 1
    response = client.delete(f"/copy/delete?id={copy_id}", headers=valid_headers)
    assert response.status_code == 409