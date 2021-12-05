from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.database import get_db
from app.tests.database_utils import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


new_user_response = client.post(
    "/user/",
    json={
        "email": "fakeuser@email.com",
        "password": "fakepassword"
    }
)
created_user = new_user_response.json()


def test_create_user():
    assert new_user_response.status_code == \
        status.HTTP_200_OK, new_user_response.text


def test_read_user():
    read_user_response = client.get(f"/user/{created_user['id']}")
    assert read_user_response.status_code == \
        status.HTTP_200_OK, read_user_response.text

    read_user = read_user_response.json()
    assert created_user['id'] == read_user['id']


def test_update_user():
    update_user_response = client.put(
        f"/user/{created_user['id']}",
        json={
            "email": "newfakeuser@email.com"
        }
    )
    assert update_user_response.status_code == \
        status.HTTP_202_ACCEPTED, update_user_response.text

    updated_user = update_user_response.json()
    assert updated_user['email'] == "newfakeuser@email.com"


def test_delete_user():
    client.delete(f"/user/{created_user['id']}")
    read_user_response = client.get(f"/user/{created_user['id']}")
    assert read_user_response.status_code == \
        status.HTTP_404_NOT_FOUND, read_user_response.text
