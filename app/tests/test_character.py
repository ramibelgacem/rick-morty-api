from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_characters():
    response = client.get("/character")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 660
