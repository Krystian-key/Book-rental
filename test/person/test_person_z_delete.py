# === VALID ===


def test_delete_person_authorized(client, valid_headers):
    person_id = 8
    response = client.delete(f"/person/delete?id={person_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() == True


# === INVALID ===


def test_delete_person_unauthorized(client, invalid_headers):
    person_id = 8
    response = client.delete(f"/person/delete?id={person_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_delete_person_no_auth(client):
    person_id = 8
    response = client.delete(f"/person/delete?id={person_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === RESTRICTED ===


def test_delete_person_restricted(client, valid_headers):
    person_id = 1
    response = client.delete(f"/person/delete?id={person_id}", headers=valid_headers)
    assert response.status_code == 409