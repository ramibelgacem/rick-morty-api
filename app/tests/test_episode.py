from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.database import get_db
from app.tests.database_utils import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
EPISODE_ID = 1
NOT_FOUND_EPISODE_ID = 999


def get_episodes():
    return client.get("/episode")


def test_read_epsiodes():
    response = get_episodes()

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 40


def test_create_comment_for_episode():
    response = client.post(
        f"/episode/{EPISODE_ID}/comment",
        json={
            "message": "Testing a new comment for an episode"
        }
    )

    assert response.status_code == status.HTTP_201_CREATED, response.text
    created_comment = response.json()
    assert created_comment["message"] == "Testing a new comment for an episode"
    assert "created_date" in created_comment

    comment_id = created_comment["id"]
    response = client.get(f"/comment/{comment_id}")
    assert response.status_code == 200, response.text
    returned_comment = response.json()
    assert returned_comment["id"] == comment_id
    assert returned_comment == created_comment


def test_create_comment_for_episode_with_nonexistant_id():
    response = client.post(
        f"/episode/{NOT_FOUND_EPISODE_ID}/comment",
        json={
            "message": "Testing a new comment with non existant ID"
        }
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text
    assert response.json() == {
        "detail": f"Episode with id={NOT_FOUND_EPISODE_ID} not Found"}
