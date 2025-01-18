# === VALID ===


def test_get_all_books(client):
    response = client.get("/book/get-all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_book_by_id(client):
    book_id = 1
    response = client.get(f"/book/get-by-id?id={book_id}")
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()
    assert response.json()["id"] == book_id


def test_get_book_by_title(client):
    title = "Harry Potter"
    response = client.get(f"/book/get-by-title?title={title}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "title" in response.json()[0]
    assert title in response.json()[0]["title"]


def test_get_book_by_series(client):
    series = "Potter"
    response = client.get(f"/book/get-by-series?series={series}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "series" in response.json()[0]
    assert series in response.json()[0]["series"]


def test_get_book_by_author_id(client):
    author_id = 1
    response = client.get(f"/book/get-by-author-id?id={author_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "author_id" in response.json()[0]
    assert response.json()[0]["author_id"] == author_id


def test_get_book_by_language_id(client):
    lang_id = 1
    response = client.get(f"/book/get-by-language-id?id={lang_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "lang_id" in response.json()[0]
    assert response.json()[0]["lang_id"] == lang_id


# === EMPTY ===


def test_get_book_by_id_none(client):
    book_id = 0
    response = client.get(f"/book/get-by-id?id={book_id}")
    assert response.status_code == 200
    assert response.json() is None


def test_get_book_by_title_none(client):
    title = "asdfefe"
    response = client.get(f"/book/get-by-title?title={title}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_book_by_series_none(client):
    series = "asefesfs"
    response = client.get(f"/book/get-by-series?series={series}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_book_by_author_id_none(client):
    author_id = 0
    response = client.get(f"/book/get-by-author-id?id={author_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_book_by_language_id_none(client):
    lang_id = 0
    response = client.get(f"/book/get-by-language-id?id={lang_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0