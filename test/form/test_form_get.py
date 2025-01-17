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
    name = "Hard"
    response = client.get(f"/form/get-by-name?name={name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "form" in response.json()[0]
    assert name in response.json()[0]["form"]
