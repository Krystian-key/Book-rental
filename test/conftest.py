import sys
from pathlib import Path

# Dodaj katalog główny projektu do sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pytest
from fastapi.testclient import TestClient
from main import app  # Import aplikacji FastAPI

WORKER_TOKEN = ""
USER_TOKEN = ""

def set_user_token(client):
    login_data = {
        "email": "john@example.com",
        "password": "hashed_password1"
    }
    response = client.post("/auth/login", json=login_data)
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()["access_token"] is not None
    global USER_TOKEN
    USER_TOKEN = response.json()["access_token"]


def set_worker_token(client):
    login_data = {
      "email": "jane@example.com",
      "password": "hashed_password2"
    }
    response = client.post("/auth/login", json=login_data)
    assert response.status_code == 200
    assert response.json() is not None
    assert response.json()["access_token"] is not None
    global WORKER_TOKEN
    WORKER_TOKEN = response.json()["access_token"]


@pytest.fixture(scope="module", autouse=True)
def setup_tests(client):
    set_user_token(client)
    set_worker_token(client)


@pytest.fixture(scope="module")
def client():
    """Fixture zwracający klienta testowego FastAPI."""
    with TestClient(app) as test_client:
        yield test_client

@pytest.fixture
def valid_headers():
    """Nagłówki autoryzacyjne dla użytkownika z uprawnieniami."""
    return {"Authorization": f"Bearer {WORKER_TOKEN}"}

@pytest.fixture
def invalid_headers():
    """Nagłówki autoryzacyjne dla użytkownika bez uprawnień."""
    return {"Authorization": f"Bearer {USER_TOKEN}"}