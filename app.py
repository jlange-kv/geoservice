"""Tiny geo service. Everything is in this one file on purpose — that's the mess
you're cleaning up. Do NOT rewrite the logic; move it into a real package."""

from fastapi import FastAPI
from pydantic import BaseModel
from shapely.geometry import shape, mapping

app = FastAPI()


class BufferRequest(BaseModel):
    geometry: dict   # a GeoJSON geometry
    distance: float  # buffer distance, in the units of the coordinates


def buffer_geometry(geometry: dict, distance: float) -> dict:
    """Buffer a GeoJSON geometry and return the result as GeoJSON."""
    geom = shape(geometry)
    return mapping(geom.buffer(distance))


@app.post("/buffer")
def buffer(req: BufferRequest) -> dict:
    return buffer_geometry(req.geometry, req.distance)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}
