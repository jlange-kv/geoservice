"""Tiny geo service. Everything is in this one file on purpose — that's the mess
you're cleaning up. Do NOT rewrite the logic; move it into a real package."""

from fastapi import FastAPI

from geoservice.geometry_functions import buffer_geometry
from geoservice.models import BufferRequest

app = FastAPI()


@app.post("/buffer")
def buffer(req: BufferRequest) -> dict:
    return buffer_geometry(req.geometry, req.distance)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
