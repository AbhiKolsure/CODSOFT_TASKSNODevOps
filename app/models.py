"""Pydantic response models for the API."""

from pydantic import BaseModel, ConfigDict


class RootResponse(BaseModel):
    application: str
    version: str
    status: str
    message: str


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


class ApplicationInfo(BaseModel):
    name: str
    version: str
    environment: str
    description: str
    documentation: str


class ServiceStatus(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    status: str
    environment: str