# === VALID ===

def test_get_all_forms(client):
    response = client.get("/form/get-all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_form_by_id(client):
    form_id = 1
    response = client.get(f"/form/get-by-id?id={form_id}")
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()
    assert response.json()["id"] == form_id


def test_get_form_by_name(client):
    name = "Audio"
    response = client.get(f"/form/get-by-name?name={name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "form" in response.json()[0]
    assert name in response.json()[0]["form"]


# === EMPTY ===


def test_get_form_by_id_none(client):
    form_id = 0
    response = client.get(f"/form/get-by-id?id={form_id}")
    assert response.status_code == 200
    assert response.json() is None


def test_get_form_by_name_none(client):
    name = "asfaesafe"
    response = client.get(f"/form/get-by-name?name={name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0
