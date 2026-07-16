"""Tiny geo service that buffers a geometry."""

from fastapi import FastAPI

from geoservice.geometry import buffer_geometry
from geoservice.models import BufferRequest

app = FastAPI()


@app.post("/buffer")
def buffer(req: BufferRequest) -> dict:
    "Returns buffered geometry."
    return buffer_geometry(req.geometry, req.distance)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


# Format error
a = [1,2]

# Lint error
if 1==True:
    print("Hello")
