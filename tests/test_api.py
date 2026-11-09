"""Protect against accidentally re-enabling unauthenticated audit or raw egress."""
import pytest
from fastapi.testclient import TestClient

from app.main import app

LOG = {"agent_name": "bot", "model_used": "test-model", "prompt": "SYNTHETIC_SENTINEL",
       "response": "fake", "tokens_used": 10, "latency_ms": 12.5}


@pytest.fixture
def client():
    return TestClient(app)


def test_root_reports_lab_only(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "laboratory"
    assert r.json()["production_ready"] is False


def test_unauthenticated_audit_write_is_disabled(client):
    assert client.post("/audit/", json=LOG).status_code == 503


def test_unauthenticated_audit_read_is_disabled(client):
    assert client.get("/audit/").status_code == 503


def test_proxy_is_disabled_with_valid_payload(client):
    payload = {"model": "test-only", "messages": [{"role": "user", "content": "SYNTHETIC_PII"}]}
    resp = client.post("/proxy/v1/chat", json=payload,
                       headers={"Authorization": "Bearer FAKE_TEST_TOKEN"})
    assert resp.status_code == 503
    assert "disabled" in resp.json()["detail"].lower()


def test_proxy_never_calls_provider(client, monkeypatch):
    import httpx
    async def forbidden_post(*args, **kwargs):
        raise AssertionError("Forbidden: network request attempted")
    monkeypatch.setattr(httpx.AsyncClient, "post", forbidden_post)
    payload = {"model": "test-only", "messages": [{"role": "user", "content": "fake@sample.invalid"}]}
    assert client.post("/proxy/v1/chat", json=payload).status_code == 503


def test_forward_helper_is_also_disabled():
    import asyncio
    from fastapi import HTTPException
    from models.chat import ChatRequest, ChatMessage
    from services.proxy import forward_request

    request = ChatRequest(model="test", messages=[ChatMessage(role="user", content="fake")])
    with pytest.raises(HTTPException) as exc:
        asyncio.run(forward_request(request, api_key="FAKE"))
    assert exc.value.status_code == 503
