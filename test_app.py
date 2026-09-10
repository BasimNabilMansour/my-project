from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Task Manager API is running!"


def test_get_tasks():
    client = app.test_client()

    response = client.get("/tasks")

    assert response.status_code == 200
    assert len(response.json) == 3