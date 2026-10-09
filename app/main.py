"""FastAPI application entry point."""

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.config import APP_NAME, APP_VERSION
from app.models import RootResponse
from app.routes import health, services

app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="A small, container-ready service health API for CodSoft DevOps Internship Task 1.",
)


@app.exception_handler(Exception)
async def unexpected_error_handler(request: Request, exc: Exception) -> JSONResponse:
    """Return a consistent JSON response for unexpected server errors."""
    return JSONResponse(status_code=500, content={"detail": "An unexpected server error occurred."})


@app.get("/", response_model=RootResponse, tags=["general"])
async def root() -> RootResponse:
    """Welcome endpoint describing the running application."""
    return RootResponse(
        application=APP_NAME,
        version=APP_VERSION,
        status="running",
        message="Welcome to the DevOps Service Health API.",
    )


app.include_router(health.router)
app.include_router(health.router, prefix="/api/v1")
app.include_router(services.router, prefix="/api/v1")