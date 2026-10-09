# DevOps Service Health API — CodSoft Task 1

## Project Overview

A small, modular FastAPI application that reports its own health and version, exposes useful application metadata, and returns example service statuses. It has no database or external API dependencies and is packaged for container execution.

## CodSoft Task 1

This project implements the **Dockerized Web Application** task with a working web application, a Dockerfile, dependency packaging, a Docker image, and browser-accessible endpoints. The image `codsoft-task1:latest` built successfully, and the container `codsoft-task1` started successfully.

## Technology Stack

- Python 3.12
- FastAPI and Pydantic
- Uvicorn ASGI server
- pytest and HTTPX test client
- Docker

## Project Structure

```text
app/                 Application package, settings, models, and routes
  routes/            Health, information, and service endpoints
tests/               API endpoint tests
Dockerfile           Python 3.12 container image definition
.dockerignore        Excludes local and unnecessary files from build context
requirements.txt     Runtime and test dependencies
pytest.ini           pytest discovery configuration
```

## Prerequisites

- Python 3.12 (or newer for local development)
- Docker Desktop or Docker Engine, running
- Git

## Local Setup

From the project root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

On macOS/Linux, activate with `source .venv/bin/activate`.

## Run Without Docker

```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Optional settings: `APP_VERSION` (defaults to `1.0.0`) and `APP_ENVIRONMENT` (defaults to `development`).

## Run Tests

```powershell
python -m pytest
```

## Docker Build

```powershell
docker build -t codsoft-task1:latest .
```

## Docker Run

```powershell
docker run --name codsoft-task1 -p 8000:8000 codsoft-task1:latest
```

The container runs as a non-root user. Without `-d`, `docker run` occupies the terminal while the container is running; press Ctrl+C to stop it. To run it in the background, add `-d` after `docker run`.

## Browser Verification

With the application running, open:

- http://localhost:8000 — application summary
- http://localhost:8000/health — health status
- http://localhost:8000/api/v1/info — application metadata
- http://localhost:8000/api/v1/services — example services
- http://localhost:8000/docs — Swagger UI
- http://localhost:8000/redoc — ReDoc

Verified responses: `/` returned HTTP 200, `/health` returned HTTP 200 with status `healthy`, and `/docs` returned HTTP 200.

## Docker Verification Commands

```powershell
docker images
docker ps
docker logs codsoft-task1
docker stop codsoft-task1
docker rm codsoft-task1
```

Automated test result: **6 passed**, with **2 deprecation warnings**.

## Troubleshooting

- **`docker` is not recognized:** install Docker Desktop/Engine and ensure its CLI is on `PATH`; reopen the terminal.
- **Docker daemon unavailable:** start Docker Desktop or the Docker service, then retry `docker info`.
- **Port 8000 is already in use:** stop the conflicting process or map another host port, for example `-p 8001:8000`, then use `http://localhost:8001`.
- **Python dependency/import errors:** activate the virtual environment and run `python -m pip install -r requirements.txt` from the project root.
- **PowerShell blocks activation:** use `python -m pip` directly with the virtual environment interpreter, `.\.venv\Scripts\python.exe -m pip install -r requirements.txt`.

## Task Completion Checklist

- [x] Application created
- [x] Dockerfile created
- [x] Dependencies packaged
- [x] Docker image `codsoft-task1:latest` built successfully
- [x] Docker container `codsoft-task1` started successfully
- [x] Application endpoints verified: `/` (HTTP 200), `/health` (HTTP 200, status `healthy`), and `/docs` (HTTP 200)
- [x] Tests passed (6 passed, 2 deprecation warnings)
- [x] README completed