# === VALID ===


def test_get_all_copies(client):
    response = client.get("/copy/get-all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_copy_by_id(client):
    copy_id = 1
    response = client.get(f"/copy/get-by-id?id={copy_id}")
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()
    assert response.json()["id"] == copy_id


def test_get_copy_by_edition_id(client):
    ed_id = 1
    response = client.get(f"/copy/get-by-edition-id?id={ed_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "ed_id" in response.json()[0]
    assert response.json()[0]["ed_id"] == ed_id


def test_get_copy_by_rented(client):
    rented = False
    response = client.get(f"/copy/get-by-rented?rented={rented}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "rented" in response.json()[0]
    assert response.json()[0]["rented"] == rented


# === EMPTY ===


def test_get_copy_by_id_none(client):
    copy_id = 0
    response = client.get(f"/copy/get-by-id?id={copy_id}")
    assert response.status_code == 200
    assert response.json() is None


def test_get_copy_by_edition_id_none(client):
    ed_id = 0
    response = client.get(f"/copy/get-by-edition-id?id={ed_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0