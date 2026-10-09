from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_services_returns_example_services() -> None:
    response = client.get("/api/v1/services")
    assert response.status_code == 200
    services = response.json()
    assert len(services) >= 1
    for service in services:
        assert service["name"]
        assert service["status"] in {"healthy", "degraded", "unavailable"}
        assert service["environment"]