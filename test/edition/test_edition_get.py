# === VALID ===


def test_get_all_editions(client):
    response = client.get("/edition/get-all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_edition_by_id(client):
    ed_id = 1
    response = client.get(f"/edition/get-by-id?id={ed_id}")
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()
    assert response.json()["id"] == ed_id


def test_get_edition_by_book_id(client):
    book_id = 1
    response = client.get(f"/edition/get-by-book-id?id={book_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "book_id" in response.json()[0]
    assert response.json()[0]["book_id"] == book_id


def test_get_edition_by_ed_num(client):
    ed_num = 3
    response = client.get(f"/edition/get-by-edition-number?num={ed_num}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "ed_num" in response.json()[0]
    assert response.json()[0]["ed_num"] == ed_num


def test_get_edition_by_ed_year(client):
    ed_year = 1980
    response = client.get(f"/edition/get-by-edition-year?year={ed_year}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "ed_year" in response.json()[0]
    assert response.json()[0]["ed_year"] == ed_year


def test_get_edition_by_isbn(client):
    isbn = 9781234567001
    response = client.get(f"/edition/get-by-isbn?isbn={isbn}")
    assert response.status_code == 200
    assert response.json() is not None
    assert "isbn" in response.json()
    assert response.json()["isbn"] == isbn


def test_get_edition_by_ukd(client):
    ukd = '82-101'
    response = client.get(f"/edition/get-by-ukd?ukd={ukd}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "ukd" in response.json()[0]
    assert response.json()[0]["ukd"] == ukd


def test_get_edition_by_ed_title(client):
    title = "Harry Potter"
    response = client.get(f"/edition/get-by-edition-title?title={title}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "ed_title" in response.json()[0]
    assert title in response.json()[0]["ed_title"]


def test_get_edition_by_ed_series(client):
    series = "Potter"
    response = client.get(f"/edition/get-by-edition-series?series={series}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "ed_series" in response.json()[0]
    assert series in response.json()[0]["ed_series"]


def test_get_edition_by_illustrator_id(client):
    ill_id = 2
    response = client.get(f"/edition/get-by-illustrator-id?id={ill_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "illustrator_id" in response.json()[0]
    assert response.json()[0]["illustrator_id"] == ill_id


def test_get_edition_by_translator_id(client):
    tran_id = 6
    response = client.get(f"/edition/get-by-translator-id?id={tran_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "translator_id" in response.json()[0]
    assert response.json()[0]["translator_id"] == tran_id


def test_get_edition_by_ed_lang_id(client):
    ed_lang_id = 1
    response = client.get(f"/edition/get-by-edition-language-id?id={ed_lang_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "ed_lang_id" in response.json()[0]
    assert response.json()[0]["ed_lang_id"] == ed_lang_id


def test_get_edition_by_publisher_id(client):
    publisher_id = 1
    response = client.get(f"/edition/get-by-publisher-id?id={publisher_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "publisher_id" in response.json()[0]
    assert response.json()[0]["publisher_id"] == publisher_id


def test_get_edition_by_form_id(client):
    form_id = 1
    response = client.get(f"/edition/get-by-form-id?id={form_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "form_id" in response.json()[0]
    assert response.json()[0]["form_id"] == form_id


# === EMPTY ===


def test_get_edition_by_id_none(client):
    ed_id = 0
    response = client.get(f"/edition/get-by-id?id={ed_id}")
    assert response.status_code == 200
    assert response.json() is None


def test_get_edition_by_book_id_none(client):
    book_id = 0
    response = client.get(f"/edition/get-by-book-id?id={book_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_edition_by_ed_num_none(client):
    ed_num = 0
    response = client.get(f"/edition/get-by-edition-number?num={ed_num}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_edition_by_ed_year_none(client):
    ed_year = 0
    response = client.get(f"/edition/get-by-edition-year?year={ed_year}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_edition_by_isbn_none(client):
    isbn = 0
    response = client.get(f"/edition/get-by-isbn?isbn={isbn}")
    assert response.status_code == 200
    assert response.json() is None


def test_get_edition_by_ukd_none(client):
    ukd = 'vgjfdjft'
    response = client.get(f"/edition/get-by-ukd?ukd={ukd}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_edition_by_ed_title_none(client):
    title = "rthstrhst"
    response = client.get(f"/edition/get-by-edition-title?title={title}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_edition_by_ed_series_none(client):
    series = "srthrhtrt"
    response = client.get(f"/edition/get-by-edition-series?series={series}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_edition_by_illustrator_id_none(client):
    ill_id = 0
    response = client.get(f"/edition/get-by-illustrator-id?id={ill_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_edition_by_translator_id_none(client):
    tran_id = 0
    response = client.get(f"/edition/get-by-translator-id?id={tran_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_edition_by_ed_lang_id_none(client):
    ed_lang_id = 0
    response = client.get(f"/edition/get-by-edition-language-id?id={ed_lang_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_edition_by_publisher_id_none(client):
    publisher_id = 0
    response = client.get(f"/edition/get-by-publisher-id?id={publisher_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_edition_by_form_id_none(client):
    form_id = 0
    response = client.get(f"/edition/get-by-form-id?id={form_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0