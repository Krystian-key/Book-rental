# === VALID ===


def test_delete_lang_authorized(client, valid_headers):
    lang_id = 8
    response = client.delete(f"/language/delete?id={lang_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() == True


# === INVALID ===


def test_delete_lang_unauthorized(client, invalid_headers):
    lang_id = 8
    response = client.delete(f"/language/delete?id={lang_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_delete_lang_no_auth(client):
    lang_id = 8
    response = client.delete(f"/language/delete?id={lang_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === RESTRICTED ===


def test_delete_lang_restricted(client, valid_headers):
    lang_id = 1
    response = client.delete(f"/language/delete?id={lang_id}", headers=valid_headers)
    assert response.status_code == 409