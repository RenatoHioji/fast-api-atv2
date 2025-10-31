import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

# ------------------ TESTE GET /posts ------------------
@patch("app.external_api.fetch_all")
def test_get_all_success(mock_fetch_all, client):
    mock_fetch_all.return_value = [
        {"id": 1, "title": "Fake title", "body": "Fake body", "userId": 1}
    ]
    response = client.get("/posts")
    assert response.status_code == 200
    assert response.json() == [{"id": 1, "title": "Fake title", "body": "Fake body", "userId": 1}]

@patch("app.external_api.fetch_all")
def test_get_all_failure(mock_fetch_all, client):
    mock_fetch_all.side_effect = Exception("Erro de rede")
    response = client.get("/posts")
    assert response.status_code == 500

# ------------------ TESTE GET /posts/{id} ------------------
@patch("app.external_api.fetch_by_id")
def test_get_by_id_success(mock_fetch_by_id, client):
    mock_fetch_by_id.return_value = {"id": 1, "title": "Hello", "body": "World", "userId": 1}
    response = client.get("/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1

@patch("app.external_api.fetch_by_id")
def test_get_by_id_not_found(mock_fetch_by_id, client):
    mock_fetch_by_id.return_value = None
    response = client.get("/posts/9999")
    assert response.status_code == 404

# ------------------ TESTE POST /posts ------------------
@patch("app.external_api.create")
def test_create_success(mock_create, client):
    mock_create.return_value = {"id": 101, "title": "New", "body": "Post", "userId": 1}
    data = {"title": "New", "body": "Post", "userId": 1}
    response = client.post("/posts", json=data)
    assert response.status_code == 201
    assert response.json()["id"] == 101

@patch("app.external_api.create")
def test_create_failure(mock_create, client):
    mock_create.return_value = None
    data = {"title": "Bad", "body": "Request", "userId": 1}
    response = client.post("/posts", json=data)
    assert response.status_code == 502
