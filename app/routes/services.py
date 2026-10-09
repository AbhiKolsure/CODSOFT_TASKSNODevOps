"""Example service status endpoint."""

from fastapi import APIRouter

from app.config import APP_ENVIRONMENT
from app.models import ServiceStatus

router = APIRouter()

_SERVICES = (
    ServiceStatus(name="api-gateway", status="healthy", environment=APP_ENVIRONMENT),
    ServiceStatus(name="worker", status="healthy", environment=APP_ENVIRONMENT),
    ServiceStatus(name="notification-service", status="degraded", environment=APP_ENVIRONMENT),
)


@router.get("/services", response_model=list[ServiceStatus], tags=["services"])
async def list_services() -> list[ServiceStatus]:
    """Return predefined example service statuses."""
    return list(_SERVICES)