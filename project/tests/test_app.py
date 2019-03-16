import pytest
from app import app
from molten import testing


@pytest.fixture(scope="session")
def client():
    return testing.TestClient(app)


def test_ping(client):
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json()["message"] == "Pong!"
