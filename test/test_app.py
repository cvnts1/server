""" Testing module """
from fastapi.testclient import TestClient
from app import server
from config import health_message

test_client = TestClient(server)

def test_health():
    """ Test health endpoint """
    response = test_client.get("/-/health")
    assert response.status_code == 200
    assert response.json()["message"] == health_message

def test_echo():
    """ Test echo endpoint """
    response = test_client.get("/api/echo?text=duck")
    assert response.status_code == 200
    assert response.json()["key"] == "duck"
