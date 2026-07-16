# GEO-API-SERVICE

A geoservice with `/health` and `/buffer` endpoints.
Uses `uv` as a package manager.

```bash
uv sync
uv run uvicorn geoservice.app:app --port 8000
uv run pytest
```

The repo uses `pre-commit` for *pre-commit* hooks. Install
hooks using `uv run pre-commit install`.

a trivial commit
