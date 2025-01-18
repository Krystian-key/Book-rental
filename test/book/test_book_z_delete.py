# === VALID ===


def test_delete_book_authorized(client, valid_headers):
    response = client.get(f"/book/get-by-title?title=Książka")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]
    book_id = response.json()[0]["id"]
    response = client.delete(f"/book/delete?id={book_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() == True


# === INVALID ===


def test_delete_book_unauthorized(client, invalid_headers):
    book_id = 8
    response = client.delete(f"/book/delete?id={book_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_delete_book_no_auth(client):
    book_id = 8
    response = client.delete(f"/book/delete?id={book_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === RESTRICTED ===


def test_delete_book_restricted(client, valid_headers):
    book_id = 1
    response = client.delete(f"/book/delete?id={book_id}", headers=valid_headers)
    assert response.status_code == 409