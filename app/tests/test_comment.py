from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.database import get_db
from app.tests.database_utils import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
COMMENT_ID = 16
EPISODE_ID = 1


def test_update_comment():
    response = client.put(
        f"/comment/{COMMENT_ID}",
        json={
            "message": "Updating a comment"
        }
    )

    assert response.status_code == status.HTTP_202_ACCEPTED, response.text
    created_comment = response.json()
    assert created_comment["message"] == "Updating a comment"


def test_delete_comment():
    response = client.post(
        f"/episode/{EPISODE_ID}/comment",
        json={
            "message": "This comment will be deleted"
        }
    )
    assert response.status_code == status.HTTP_201_CREATED, response.text
    created_comment = response.json()

    response = client.delete(f"/comment/{created_comment['id']}")
    assert response.status_code == status.HTTP_200_OK, response.text
