from fastapi import status
from fastapi.testclient import TestClient

from app.main import app
from app.database import get_db
from app.tests.database_utils import override_get_db

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)
CHARACTER_ID = 1
NOT_FOUND_CHARACETR_ID = 9999


def get_characters(url):
    return client.get(url)


def test_read_characters():
    response = get_characters("/character")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


def test_read_20_characters():
    response = get_characters("/character?limit=20")

    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 20


def test_read_characters_with_gender_filter():
    response = get_characters("/character/?limit=1&gender=Female")
    character = response.json()

    assert response.status_code == status.HTTP_200_OK
    assert len(character) == 1
    assert character[0]['gender'] == 'Female'


def test_create_comment_for_character():
    response = client.post(
        f"/character/{CHARACTER_ID}/comment",
        json={
            "message": "Testing a new comment for an character"
        }
    )

    assert response.status_code == status.HTTP_201_CREATED, response.text
    created_comment = response.json()
    assert created_comment["message"] == \
        "Testing a new comment for an character"
    assert "created_date" in created_comment

    comment_id = created_comment["id"]
    response = client.get(f"/comment/{comment_id}")
    assert response.status_code == 200, response.text
    returned_comment = response.json()
    assert returned_comment["id"] == comment_id
    assert returned_comment == created_comment


def test_create_comment_for_character_with_nonexistant_id():
    response = client.post(
        f"/character/{NOT_FOUND_CHARACETR_ID}/comment",
        json={
            "message": "Testing a new comment with non existant ID"
        }
    )

    assert response.status_code == status.HTTP_404_NOT_FOUND, response.text
    assert response.json() == {
        "detail": f"Character with id={NOT_FOUND_CHARACETR_ID} not Found"}
