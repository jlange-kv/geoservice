"""Tiny geo service that buffers a geometry."""

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
