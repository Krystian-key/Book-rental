# === VALID ===


def test_get_all_publishers(client):
    response = client.get("/publisher/get-all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_publisher_by_id(client):
    publ_id = 1
    response = client.get(f"/publisher/get-by-id?id={publ_id}")
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()
    assert response.json()["id"] == publ_id


def test_get_publisher_by_name(client):
    name = "Publ"
    response = client.get(f"/publisher/get-by-name?name={name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "name" in response.json()[0]
    assert name in response.json()[0]["name"]


def test_get_publisher_by_city(client):
    city = "New"
    response = client.get(f"/publisher/get-by-city?city={city}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "localization" in response.json()[0]
    assert city in response.json()[0]["localization"]


def test_get_publisher_by_foundation_year(client):
    year = 1846
    response = client.get(f"/publisher/get-by-foundation-year?year={year}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "foundation_year" in response.json()[0]
    assert response.json()[0]["foundation_year"] == year


# === EMPTY ===


def test_get_publisher_by_id_none(client):
    publ_id = 0
    response = client.get(f"/publisher/get-by-id?id={publ_id}")
    assert response.status_code == 200
    assert response.json() is None


def test_get_publisher_by_name_none(client):
    name = "fhdhgfhds"
    response = client.get(f"/publisher/get-by-name?name={name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_publisher_by_city_none(client):
    city = "frygjy"
    response = client.get(f"/publisher/get-by-city?city={city}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_publisher_by_foundation_year_none(client):
    year = 0
    response = client.get(f"/publisher/get-by-foundation-year?year={year}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0
