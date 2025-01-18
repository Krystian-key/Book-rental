# === VALID ===

def test_add_book(client, valid_headers):
    book_add_data = {
        "title": "Książka",
        "series": "Test Series",
        "lang_id": 1,
        "author_id": 1
    }
    response = client.post("/book/add", json=book_add_data, headers=valid_headers)
    assert response.status_code == 201
    assert response.json()["title"] == "Książka"

# === INVALID ===


def test_add_book_unauthorized(client, invalid_headers):
    book_add_data = {
        "title": "Test Book",
        "series": "Test Series",
        "lang_id": 1,
        "author_id": 3
    }
    response = client.post("/book/add", json=book_add_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_add_book_no_auth(client):
    book_add_data = {
        "title": "Test Book",
        "series": "Test Series",
        "lang_id": 1,
        "author_id": 4
    }
    response = client.post("/book/add", json=book_add_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === NO DATA ===


def test_add_book_no_data(client, valid_headers):
    response = client.post("/book/add", headers=valid_headers)
    assert response.status_code == 422


# === WRONG DATA ===


def test_add_book_wrong_data(client, valid_headers):
    book_add_data = {
        "titel": "Test Book",
        "serie": "Test Series",
        "lang_id": 1,
        "author_id": 5
    }
    response = client.post("/book/add", json=book_add_data, headers=valid_headers)
    assert response.status_code == 422


# === LACKING DATA ===


def test_add_book_lacking_data(client, valid_headers):
    book_add_data = {
        "title": "Test Book",
        "series": "Test Series",
        "lang_id": 6
    }
    response = client.post("/book/add", json=book_add_data, headers=valid_headers)
    assert response.status_code == 422


# === CONFLICT ===


def test_add_book_conflict(client, valid_headers):
    book_add_data = {
        "title": "Książka",
        "series": "Test Series",
        "lang_id": 1,
        "author_id": 1
    }
    response = client.post("/book/add", json=book_add_data, headers=valid_headers)
    assert response.status_code == 409