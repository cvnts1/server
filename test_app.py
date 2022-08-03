from fastapi.testclient import TestClient
from app import covantis
from config import health_message

test_client = TestClient(covantis)

def test_health():
    response = test_client.get("/-/health")
    assert response.status_code == 200
    assert response.text == health_message

def test_echo():
    response = test_client.get("/api/echo?text=duck")
    assert response.status_code == 200
    assert response.text == health_message
