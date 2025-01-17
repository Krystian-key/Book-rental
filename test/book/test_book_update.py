"""
def test_update_book_authorized(client, valid_headers):
    book_update_data = {
        "id": 1,
        "title": "Updated Title",
        "series": "Updated Series",
        "lang_id": 2,
        "author_id": 1
    }
    response = client.patch("/book/update", json=book_update_data, headers=valid_headers)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Title"


def test_update_book_unauthorized(client, invalid_headers):
    book_update_data = {
        "id": 1,
        "title": "Unauthorized Update",
    }
    response = client.patch("/book/update", json=book_update_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


def test_update_book_no_auth(client):
    book_update_data = {
        "id": 1,
        "title": "No Auth Update",
    }
    response = client.patch("/book/update", json=book_update_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu
"""