"""Test the API contract, including validation and state isolation."""

import pytest
from fastapi.testclient import TestClient

from app.main import app, items


@pytest.fixture(autouse=True)
def reset_items():
    """Keep every test independent."""
    items.clear()
    yield
    items.clear()


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_item(client):
    response = client.post("/items", json={"name": "Notebook"})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": "Notebook"}


@pytest.mark.parametrize("name", ["a", "a" * 100, "नोटबुक", " "])
def test_valid_name_boundaries_and_unicode(client, name):
    response = client.post("/items", json={"name": name})
    assert response.status_code == 201
    assert response.json() == {"id": 1, "name": name}


@pytest.mark.parametrize(
    "payload",
    [
        {},
        {"name": ""},
        {"name": "x" * 101},
        {"name": None},
        {"name": 123},
        {"name": True},
        {"name": []},
        {"name": {}},
    ],
)
def test_invalid_names(client, payload):
    response = client.post("/items", json=payload)
    assert response.status_code == 422
    assert response.json()["detail"][0]["loc"] == ["body", "name"]
    assert items == []


def test_malformed_json(client):
    response = client.post(
        "/items", content='{"name":', headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422
    assert response.json()["detail"][0]["type"] == "json_invalid"
    assert items == []


def test_repeated_requests(client):
    for identifier, name in enumerate(["One", "Two", "One"], start=1):
        response = client.post("/items", json={"name": name})
        assert response.status_code == 201
        assert response.json() == {"id": identifier, "name": name}
    assert len(items) == 3


def test_invalid_request_does_not_consume_identifier(client):
    assert client.post("/items", json={"name": ""}).status_code == 422
    assert client.post("/items", json={"name": "Valid"}).json()["id"] == 1


def test_openapi_contract(client):
    response = client.get("/openapi.json")
    assert response.status_code == 200
    schema = response.json()
    assert "200" in schema["paths"]["/health"]["get"]["responses"]
    assert {"201", "422"} <= schema["paths"]["/items"]["post"]["responses"].keys()
    fields = schema["components"]["schemas"]["ItemIn"]
    assert fields["required"] == ["name"]
    assert fields["properties"]["name"]["minLength"] == 1
    assert fields["properties"]["name"]["maxLength"] == 100


@pytest.mark.parametrize("path", ["/docs", "/redoc"])
def test_interactive_docs(client, path):
    assert client.get(path).status_code == 200
