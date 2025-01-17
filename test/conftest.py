import sys
from pathlib import Path

# Dodaj katalog główny projektu do sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import pytest
from fastapi.testclient import TestClient
from main import app  # Import aplikacji FastAPI

WORKER_TOKEN = ""
INVALID_TOKEN = "asfe4t36235y4qer233tgr42gq35qgt"

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
    return {"Authorization": f"Bearer {INVALID_TOKEN}"}