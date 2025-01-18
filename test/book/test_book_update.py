# === VALID ===


def test_update_book_authorized(client, valid_headers):
    response = client.get(f"/book/get-by-title?title=Książka")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "id" in response.json()[0]

    book_update_data = {
        "id": response.json()[0]["id"],
        "series": "Updated Series",
    }
    response = client.patch("/book/update", json=book_update_data, headers=valid_headers)
    assert response.status_code == 200
    assert response.json()["series"] == "Updated Series"


# === INVALID ===


def test_update_book_unauthorized(client, invalid_headers):
    book_update_data = {
        "id": 1,
        "title": "Unauthorized Update",
    }
    response = client.patch("/book/update", json=book_update_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_update_book_no_auth(client):
    book_update_data = {
        "id": 1,
        "title": "No Auth Update",
    }
    response = client.patch("/book/update", json=book_update_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu
