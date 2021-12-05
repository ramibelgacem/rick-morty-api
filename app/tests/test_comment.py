from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.database import get_db
from app.tests.database_utils import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
EPISODE_ID = 1

new_user_response = client.post(
    "/user/",
    json={
        "email": "fakeusercomment@email.com",
        "password": "fakepassword"
    }
)
created_user = new_user_response.json()

new_comment_response = client.post(
    f"/episode/{EPISODE_ID}/comment",
    json={
        "message": "Testing a new comment",
        "user_id": created_user['id']
    }
)
new_comment = new_comment_response.json()


def test_update_comment():
    response = client.put(
        f"/comment/{new_comment['id']}",
        json={
            "message": "Updating a comment"
        }
    )

    assert response.status_code == status.HTTP_202_ACCEPTED, response.text
    updated_comment = response.json()
    assert updated_comment["message"] == "Updating a comment"


def test_delete_comment():
    assert new_comment_response.status_code == \
        status.HTTP_201_CREATED, new_comment_response.text

    response = client.delete(f"/comment/{new_comment['id']}")
    assert response.status_code == status.HTTP_200_OK, response.text
