# === VALID ===


def test_get_all_persons(client):
    response = client.get("/person/get-all")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_person_by_id(client):
    copy_id = 1
    response = client.get(f"/person/get-by-id?id={copy_id}")
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()
    assert response.json()["id"] == copy_id


def test_get_person_by_name(client):
    name = "George"
    response = client.get(f"/person/get-by-name?name={name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "name" in response.json()[0]
    assert name in response.json()[0]["name"]


def test_get_person_by_surname(client):
    surname = "Orwell"
    response = client.get(f"/person/get-by-surname?surname={surname}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "surname" in response.json()[0]
    assert surname in response.json()[0]["surname"]


def test_get_person_by_birth_year(client):
    year = 1896
    response = client.get(f"/person/get-by-birth-year?birth={year}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "birth_year" in response.json()[0]
    assert response.json()[0]["birth_year"] == year


def test_get_person_by_death_year(client):
    year = 1740
    response = client.get(f"/person/get-by-death-year?death={year}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "death_year" in response.json()[0]
    assert response.json()[0]["death_year"] == year


# === EMPTY ===


def test_get_person_by_id_none(client):
    copy_id = 0
    response = client.get(f"/person/get-by-id?id={copy_id}")
    assert response.status_code == 200
    assert response.json() is None


def test_get_person_by_name_none(client):
    name = "reyhrt"
    response = client.get(f"/person/get-by-name?name={name}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_person_by_surname_none(client):
    surname = "erhttre"
    response = client.get(f"/person/get-by-surname?surname={surname}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_person_by_birth_year_none(client):
    year = 0
    response = client.get(f"/person/get-by-birth-year?birth={year}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_person_by_death_year_none(client):
    year = 0
    response = client.get(f"/person/get-by-death-year?death={year}")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0
