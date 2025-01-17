from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

"""
def test_read_books():
    response = client.get("/book/get-all")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)  # Sprawdza, czy wynik jest listą
    assert len(data) > 0  # Upewnia się, że lista nie jest pusta
    # Sprawdź pierwszy element, jeśli dane mają ustaloną strukturę
    assert "title" in data[0]
    assert "author_id" in data[0]
"""

def test_get_all_books():
    response = client.get("/book/get-all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_book_by_id():
    # Zakładamy, że istnieje książka o ID 1
    book_id = 1
    response = client.get(f"/book/get-by-id?id={book_id}")
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()
    assert response.json()["id"] == book_id

