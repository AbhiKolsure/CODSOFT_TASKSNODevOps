"""Application settings loaded from the environment."""

import os

APP_NAME = "DevOps Service Health API"
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENVIRONMENT = os.getenv("APP_ENVIRONMENT", "development")