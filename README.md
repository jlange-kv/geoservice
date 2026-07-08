# GEO-API-SERVICE

A geoservice with `/health` and `/buffer` endpoints.
Uses `uv` as a package manager.

```bash
uv sync
uv run uvicorn geoservice.app:app --port 8000
uv run pytest
```