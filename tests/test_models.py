"""Tests for atlas-foundry-144 model availability and API."""

import pytest
from fastapi.testclient import TestClient
from src.index import app

client = TestClient(app)


def test_root_endpoint():
    """GET / returns welcome message."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "atlas-foundry-144" in data["message"]
    assert data["status"] == "online"


def test_models_endpoint():
    """GET /lists available free models."""
    response = client.get("/models")
    assert response.status_code == 200
    data = response.json()
    assert "count" in data
    assert data["count"] == 3
    model_ids = list(data["models"].keys())
    assert "deepseek-v4.1-flash" in model_ids
    assert "kimi-k3" in model_ids
    assert "glm-5.3-flash" in model_ids


def test_health_endpoint():
    """GET /health returns healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_model_info_endpoint():
    """GET /v1/{model_id} returns model info."""
    response = client.get("/v1/deepseek-v4.1-flash")
    assert response.status_code == 200
    data = response.json()
    assert data["model"] == "DeepSeek V4.1 Flash"
    assert data["provider"] == "deepseek"
    assert data["free"] is True


def test_chat_endpoint():
    """POST /v1/{model_id}/chat returns chat confirmation."""
    response = client.post("/v1/deepseek-v4.1-flash/chat")
    assert response.status_code == 200
    data = response.json()
    assert data["free"] is True
    assert "DeepSeek V4.1 Flash" in data["message"]


def test_unknown_model_returns_404():
    """GET /v1/unknown returns 404."""
    response = client.get("/v1/unknown-model")
    assert response.status_code == 404


def test_chat_unknown_model_returns_404():
    """POST /v1/unknown-model/chat returns 404."""
    response = client.post("/v1/unknown-model/chat")
    assert response.status_code == 404
