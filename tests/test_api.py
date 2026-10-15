import pytest
from fastapi.testclient import TestClient
from app.main import create_app

@pytest.fixture
def client():
    # Each test gets its own application and memory store.
    with TestClient(create_app()) as test_client:
        yield test_client

def test_greeting_returns_json(client):
    response = client.get("/api/hello")
    assert response.status_code == 200
    assert isinstance(response.json()["message"], str)

def test_valid_post_returns_created_idea(client):
    # Send client.post("/api/ideas", json={"title": ..., "category": ...}).
    response = client.post(
        "/api/ideas", 
        json={"title": "Test Idea", "category": "Test Category"}
    )
    
    # Assert 201
    assert response.status_code == 201
    
    # Check response.json() id, title, and category.
    data = response.json()
    assert "id" in data
    assert data["title"] == "Test Idea"
    assert data["category"] == "Test Category"