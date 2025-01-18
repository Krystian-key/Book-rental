# === VALID ===


def test_delete_form_authorized(client, valid_headers):
    form_id = 8
    response = client.delete(f"/form/delete?id={form_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() == True


# === INVALID ===


def test_delete_form_unauthorized(client, invalid_headers):
    form_id = 8
    response = client.delete(f"/form/delete?id={form_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_delete_form_no_auth(client):
    form_id = 8
    response = client.delete(f"/form/delete?id={form_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === RESTRICTED ===


def test_delete_form_restricted(client, valid_headers):
    form_id = 1
    response = client.delete(f"/form/delete?id={form_id}", headers=valid_headers)
    assert response.status_code == 409