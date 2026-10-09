from fastapi.testclient import TestClient

from app.config import APP_NAME, APP_VERSION
from app.main import app

client = TestClient(app)


def test_root_returns_application_details() -> None:
    response = client.get("/")
    assert response.status_code == 200
    body = response.json()
    assert body["application"] == APP_NAME
    assert body["version"] == APP_VERSION
    assert body["status"] == "running"
    assert body["message"]


def test_health_returns_healthy_status() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": APP_NAME, "version": APP_VERSION}


def test_versioned_health_endpoint_works() -> None:
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_info_returns_application_metadata() -> None:
    response = client.get("/api/v1/info")
    assert response.status_code == 200
    body = response.json()
    assert body["name"] == APP_NAME
    assert body["version"] == APP_VERSION
    assert body["environment"]
    assert body["documentation"] == "/docs"


def test_swagger_and_redoc_are_available() -> None:
    assert client.get("/docs").status_code == 200
    assert client.get("/redoc").status_code == 200