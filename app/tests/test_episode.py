from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.database import get_db
from app.tests.database_utils import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
EPISODE_ID = 1


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
    comment = response.json()
    assert comment["message"] == "Testing a new comment for an episode"
    assert "created_date" in comment

    response = get_episodes()
    episodes = response.json()
    first_episode = episodes[0]
    last_comment = first_episode["comments"][-1]
    assert last_comment == comment
