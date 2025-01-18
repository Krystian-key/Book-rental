# === VALID ===


def test_get_all_rentals(client, valid_headers):
    response = client.get("/rental/get-all", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

"""
def test_get_rental_by_id(client, valid_headers):
    rental_id = 1
    response = client.get(f"/rental/get-by-id?id={rental_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() is not None
    assert "id" in response.json()
    assert response.json()["id"] == rental_id
"""

def test_get_rental_by_user_id(client, valid_headers):
    user_id = 2
    response = client.get(f"/rental/get-by-user-id?id={user_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "user_id" in response.json()[0]
    assert response.json()[0]["user_id"] == user_id

"""
def test_get_rental_by_user_id_rented(client, valid_headers):
    user_id = 2
    response = client.get(f"/rental/get-rented-by-user-id?id={user_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "user_id" in response.json()[0]
    assert response.json()[0]["user_id"] == user_id
    assert response.json()[0]["return_date"] is None


def test_get_rental_by_user_id_returned(client, valid_headers):
    user_id = 2
    response = client.get(f"/rental/get-returned-by-user-id?id={user_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "user_id" in response.json()[0]
    assert response.json()[0]["user_id"] == user_id
    assert response.json()[0]["return_date"] is not None
"""

def test_get_rental_by_copy_id(client, valid_headers):
    copy_id = 1
    response = client.get(f"/rental/get-by-copy-id?id={copy_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "copy_id" in response.json()[0]
    assert response.json()[0]["copy_id"] == copy_id


def test_get_rental_my(client, valid_headers):
    user_id = 2
    response = client.get(f"/rental/get-my", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "user_id" in response.json()[0]
    assert response.json()[0]["user_id"] == user_id

"""
def test_get_rental_my_rented(client, valid_headers):
    user_id = 2
    response = client.get(f"/rental/get-my-rented", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "user_id" in response.json()[0]
    assert response.json()[0]["user_id"] == user_id
    assert response.json()[0]["return_date"] is None


def test_get_rental_my_returned(client, valid_headers):
    user_id = 2
    response = client.get(f"/rental/get-my-returned", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert "user_id" in response.json()[0]
    assert response.json()[0]["user_id"] == user_id
    assert response.json()[0]["return_date"] is not None
"""

# === INVALID ===


def test_get_all_rentals_unauthorized(client, invalid_headers):
    response = client.get("/rental/get-all", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


def test_get_rental_by_id_unauthorized(client, invalid_headers):
    rental_id = 1
    response = client.get(f"/rental/get-by-id?id={rental_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


def test_get_rental_by_user_id_unauthorized(client, invalid_headers):
    user_id = 2
    response = client.get(f"/rental/get-by-user-id?id={user_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


def test_get_rental_by_user_id_rented_unauthorized(client, invalid_headers):
    user_id = 2
    response = client.get(f"/rental/get-rented-by-user-id?id={user_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


def test_get_rental_by_user_id_returned_unauthorized(client, invalid_headers):
    user_id = 2
    response = client.get(f"/rental/get-returned-by-user-id?id={user_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


def test_get_rental_by_copy_id_unauthorized(client, invalid_headers):
    copy_id = 1
    response = client.get(f"/rental/get-by-copy-id?id={copy_id}", headers=invalid_headers)
    assert response.status_code == 403  # Forbidden: użytkownik bez wymaganej roli


# === NO AUTHORIZATION ===


def test_get_all_rentals_no_auth(client):
    response = client.get("/rental/get-all")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_rental_by_id_no_auth(client):
    rental_id = 1
    response = client.get(f"/rental/get-by-id?id={rental_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_rental_by_user_id_no_auth(client):
    user_id = 2
    response = client.get(f"/rental/get-by-user-id?id={user_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_rental_by_user_id_rented_no_auth(client):
    user_id = 2
    response = client.get(f"/rental/get-rented-by-user-id?id={user_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_rental_by_user_id_returned_no_auth(client):
    user_id = 2
    response = client.get(f"/rental/get-returned-by-user-id?id={user_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_rental_by_copy_id_no_auth(client):
    copy_id = 1
    response = client.get(f"/rental/get-by-copy-id?id={copy_id}")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_rental_my_no_auth(client):
    user_id = 2
    response = client.get(f"/rental/get-my")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_rental_my_rented_no_auth(client):
    user_id = 2
    response = client.get(f"/rental/get-my-rented")
    assert response.status_code == 401  # Unauthorized: brak tokenu


def test_get_rental_my_returned_no_auth(client):
    user_id = 2
    response = client.get(f"/rental/get-my-returned")
    assert response.status_code == 401  # Unauthorized: brak tokenu


# === EMPTY ===


def test_get_rental_by_id_none(client, valid_headers):
    rental_id = 0
    response = client.get(f"/rental/get-by-id?id={rental_id}", headers=valid_headers)
    assert response.status_code == 200
    assert response.json() is None


def test_get_rental_by_user_id_none(client, valid_headers):
    user_id = 0
    response = client.get(f"/rental/get-by-user-id?id={user_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_rental_by_user_id_rented_none(client, valid_headers):
    user_id = 0
    response = client.get(f"/rental/get-rented-by-user-id?id={user_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_rental_by_user_id_returned_none(client, valid_headers):
    user_id = 0
    response = client.get(f"/rental/get-returned-by-user-id?id={user_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0


def test_get_rental_by_copy_id_none(client, valid_headers):
    copy_id = 0
    response = client.get(f"/rental/get-by-copy-id?id={copy_id}", headers=valid_headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) == 0