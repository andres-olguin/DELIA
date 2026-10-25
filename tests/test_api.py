import pytest
from fastapi.testclient import TestClient

from app.main import app

LOG = {"agent_name": "bot", "model_used": "gpt", "prompt": "p", "response": "r",
       "tokens_used": 10, "latency_ms": 12.5}

@pytest.fixture
def client():
    return TestClient(app)

def test_root(client):
    r = client.get("/")
    assert r.status_code == 200 and r.json()["status"] == "online"

def test_create_audit_log(client):
    r = client.post("/audit/", json=LOG)
    body = r.json()
    assert r.status_code == 200
    assert body["id"] and body["timestamp"] and body["status"] == "SUCCESS"

def test_create_audit_log_validates(client):
    assert client.post("/audit/", json={"agent_name": "bot"}).status_code == 422

def test_list_audit_logs_paginates(client):
    for _ in range(3):
        client.post("/audit/", json=LOG)
    r = client.get("/audit/", params={"skip": 1, "limit": 2})
    assert r.status_code == 200 and len(r.json()) == 2
