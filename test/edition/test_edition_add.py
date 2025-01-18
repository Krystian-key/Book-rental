# === VALID ===


def test_add_edition(client, valid_headers):
    edition_add_data = {
      "book_id": 3,
      "ed_title": "Tytuł wydania",
      "ed_series": "Seria",
      "illustrator_id": 2,
      "translator_id": 3,
      "ed_lang_id": 2,
      "publisher_id": 4,
      "ed_num": 2,
      "ed_year": 2025,
      "form_id": 3,
      "isbn": 11111111111,
      "ukd": "1235"
    }
    response = client.post("/edition/add", json=edition_add_data, headers=valid_headers)
    assert response.status_code == 201
    assert response.json()["ed_title"] == "Tytuł wydania"


# === INVALID ===


def test_add_edition_unauthorized(client, invalid_headers):
    edition_add_data = {
      "book_id": 1,
      "ed_title": "Tytuł Wydania",
      "ed_series": "Seria Wydania",
      "illustrator_id": 2,
      "translator_id": 3,
      "ed_lang_id": 4,
      "publisher_id": 5,
      "ed_num": 1,
      "ed_year": 2025,
      "form_id": 1,
      "isbn": 2643245645,
      "ukd": "1235"
    }
    response = client.post("/edition/add", json=edition_add_data, headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_add_edition_no_auth(client):
    edition_add_data = {
      "book_id": 1,
      "ed_title": "Tytuł Wydania",
      "ed_series": "Seria Wydania",
      "illustrator_id": 2,
      "translator_id": 3,
      "ed_lang_id": 4,
      "publisher_id": 5,
      "ed_num": 1,
      "ed_year": 2025,
      "form_id": 1,
      "isbn": 2643245645,
      "ukd": "1235"
    }
    response = client.post("/edition/add", json=edition_add_data)
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === NO DATA ===


def test_add_edition_no_data(client, valid_headers):
    response = client.post("/edition/add", headers=valid_headers)
    assert response.status_code == 422


# === WRONG DATA ===


def test_add_edition_wrong_data(client, valid_headers):
    edition_add_data = {
      "bkoo": 1,
      "ed_title": "Tytuł Wydania",
      "serie": "Seria Wydania",
      "illustrator_id": 2,
      "translator_id": 3,
      "ed_lang_id": 4,
      "publisher_id": 5,
      "ed_num": 1,
      "ed_year": 2025,
      "form_id": 1,
      "isbn": 2643245645,
      "ukd": "1235"
    }
    response = client.post("/edition/add", json=edition_add_data, headers=valid_headers)
    assert response.status_code == 422


# === LACKING DATA ===


def test_add_edition_lacking_data(client, valid_headers):
    edition_add_data = {
      "book_id": 1,
      "ed_series": "Seria Wydania",
      "illustrator_id": 2,
      "translator_id": 3,
      "form_id": 1,
      "isbn": 2643245645,
      "ukd": "1235"
    }
    response = client.post("/edition/add", json=edition_add_data, headers=valid_headers)
    assert response.status_code == 422


# === CONFLICT ===


def test_add_edition_conflict(client, valid_headers):
    edition_add_data = {
        "book_id": 3,
        "ed_title": "Tytuł wydania",
        "ed_series": "Seria",
        "illustrator_id": 2,
        "translator_id": 3,
        "ed_lang_id": 2,
        "publisher_id": 4,
        "ed_num": 2,
        "ed_year": 2025,
        "form_id": 3,
        "isbn": 11111111111,
        "ukd": "1235"
    }
    response = client.post("/edition/add", json=edition_add_data, headers=valid_headers)
    assert response.status_code == 409