# === VALID ===


def test_get_all_languages(client):
    response = client.get("/language/get-all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_language_by_id(client):
    lang_id = 1
    response = client.get(f"/language/get-by-id?id={lang_id}")
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()
    assert response.json()["id"] == lang_id


def test_get_language_by_name(client):
    name = "ish"
    response = client.get(f"/language/get-by-name?name={name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "lang" in response.json()[0]
    assert name in response.json()[0]["lang"]


# === EMPTY ===


def test_get_language_by_id_none(client):
    lang_id = 0
    response = client.get(f"/language/get-by-id?id={lang_id}")
    assert response.status_code == 200
    assert response.json() is None


def test_get_language_by_name_none(client):
    name = "afseeafsfes"
    response = client.get(f"/language/get-by-name?name={name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0