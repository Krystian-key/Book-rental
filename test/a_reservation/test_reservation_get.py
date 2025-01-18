# === VALID ===


def test_get_all_reservations(client, valid_headers):
    response = client.get("/reservation/get-all", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_reservation_by_id(client, valid_headers):
    reservation_id = 1
    response = client.get(f"/reservation/get-by-id?id={reservation_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()
    assert response.json()["id"] == reservation_id


def test_get_reservation_by_user_id(client, valid_headers):
    user_id = 2
    response = client.get(f"/reservation/get-by-user-id?id={user_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "user_id" in response.json()[0]
    assert response.json()[0]["user_id"] == user_id


def test_get_reservation_by_user_id_reserved(client, valid_headers):
    user_id = 2
    response = client.get(f"/reservation/get-reserved-by-user-id?id={user_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "user_id" in response.json()[0]
    assert response.json()[0]["user_id"] == user_id
    assert response.json()[0]["status"] == "Reserved" or response.json()[0]["status"] == "Awaiting"


def test_get_reservation_by_copy_id(client, valid_headers):
    copy_id = 3
    response = client.get(f"/reservation/get-by-copy-id?id={copy_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "copy_id" in response.json()[0]
    assert response.json()[0]["copy_id"] == copy_id


def test_get_reservation_my(client, valid_headers):
    user_id = 2
    response = client.get(f"/reservation/get-my", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "user_id" in response.json()[0]
    assert response.json()[0]["user_id"] == user_id


def test_get_reservation_my_reserved(client, valid_headers):
    user_id = 2
    response = client.get(f"/reservation/get-my-reserved", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "user_id" in response.json()[0]
    assert response.json()[0]["user_id"] == user_id
    assert response.json()[0]["status"] == "Reserved" or response.json()[0]["status"] == "Awaiting"


# === INVALID ===


def test_get_all_reservations_unauthorized(client, invalid_headers):
    response = client.get("/reservation/get-all", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


def test_get_reservation_by_id_unauthorized(client, invalid_headers):
    reservation_id = 1
    response = client.get(f"/reservation/get-by-id?id={reservation_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


def test_get_reservation_by_user_id_unauthorized(client, invalid_headers):
    user_id = 2
    response = client.get(f"/reservation/get-by-user-id?id={user_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


def test_get_reservation_by_user_id_reserved_unauthorized(client, invalid_headers):
    user_id = 2
    response = client.get(f"/reservation/get-reserved-by-user-id?id={user_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


def test_get_reservation_by_copy_id_unauthorized(client, invalid_headers):
    copy_id = 3
    response = client.get(f"/reservation/get-by-copy-id?id={copy_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_get_all_reservations_no_auth(client):
    response = client.get("/reservation/get-all")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_reservation_by_id_no_auth(client):
    reservation_id = 1
    response = client.get(f"/reservation/get-by-id?id={reservation_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_reservation_by_user_id_no_auth(client):
    user_id = 2
    response = client.get(f"/reservation/get-by-user-id?id={user_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_reservation_by_user_id_reserved_no_auth(client):
    user_id = 2
    response = client.get(f"/reservation/get-reserved-by-user-id?id={user_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_reservation_by_copy_id_no_auth(client):
    copy_id = 3
    response = client.get(f"/reservation/get-by-copy-id?id={copy_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_reservation_my_no_auth(client):
    user_id = 2
    response = client.get(f"/reservation/get-my")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_reservation_my_reserved_no_auth(client):
    user_id = 2
    response = client.get(f"/reservation/get-my-reserved")
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === EMPTY ===


def test_get_reservation_by_id_none(client, valid_headers):
    reservation_id = 0
    response = client.get(f"/reservation/get-by-id?id={reservation_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() is None


def test_get_reservation_by_user_id_none(client, valid_headers):
    user_id = 0
    response = client.get(f"/reservation/get-by-user-id?id={user_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_reservation_by_user_id_reserved_none(client, valid_headers):
    user_id = 0
    response = client.get(f"/reservation/get-reserved-by-user-id?id={user_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_reservation_by_copy_id_none(client, valid_headers):
    copy_id = 0
    response = client.get(f"/reservation/get-by-copy-id?id={copy_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0