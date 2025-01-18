# === VALID ===


def test_delete_lang_authorized(client, valid_headers):
    name = "Język"
    response = client.get(f"/language/get-by-name?name={name}")
    #assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]
    lang_id = response.json()[0]["id"]
    print(f"lang_id: {lang_id}")
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