"""Health and application information endpoints."""

from fastapi import APIRouter

from app.config import APP_NAME, APP_VERSION, APP_ENVIRONMENT
from app.models import ApplicationInfo, HealthResponse

router = APIRouter()


@router.get("/health", response_model=HealthResponse, tags=["health"])
async def health_check() -> HealthResponse:
    """Report whether the API process is responding."""
    return HealthResponse(status="healthy", service=APP_NAME, version=APP_VERSION)


@router.get("/info", response_model=ApplicationInfo, tags=["information"])
async def application_info() -> ApplicationInfo:
    """Return useful metadata about this application."""
    return ApplicationInfo(
        name=APP_NAME,
        version=APP_VERSION,
        environment=APP_ENVIRONMENT,
        description="A lightweight API demonstrating Dockerized service health reporting.",
        documentation="/docs",
    )