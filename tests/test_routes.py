import pytest
from main import app as flask_app
import uuid

@pytest.fixture
def client():
    flask_app.config["TESTING"] = True
    return flask_app.test_client()


def test_create_and_delete_message(client):
    payload = {"message": "madam"}
    response = client.post("/api/v1/messages", json=payload)
    assert response.status_code == 201
    response_data = response.get_json()

    message_id = response_data.get("message_id")
    assert response_data["is_palindrome"] is True
    assert message_id is not None

    delete_response = client.delete(f"/api/v1/messages/{message_id}")
    assert delete_response.status_code == 200
    assert "Message deleted successfully" in delete_response.get_json()["message"]


def test_create_invalid_payload(client):
    response = client.post("/api/v1/messages", json={})
    assert response.status_code == 400
    assert "error" in response.get_json()


def test_read_non_existent_message(client):
    random_id = str(uuid.uuid4())
    response = client.get(f"/api/v1/messages/{random_id}")
    assert response.status_code == 404
    assert "error" in response.get_json()

