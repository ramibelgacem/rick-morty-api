from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_epsiodes():
    response = client.get("/episode")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 40
