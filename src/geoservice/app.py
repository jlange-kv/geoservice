"""Tiny geo service that buffers a geometry."""

from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from geoservice.geometry import buffer_geometry, calculate_area
from geoservice.models import BufferRequest, PolygonRequest

app = FastAPI()


@app.post("/buffer")
def buffer(req: BufferRequest) -> dict:
    "Returns buffered geometry."
    return buffer_geometry(req.geometry, req.distance)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/area")
def area(req: PolygonRequest) -> dict:
    """Returns area of a polygon.

    Request can only contain keys shell and holes.
    Shell is required, holes optional.
    """
    try:
        return {"area": calculate_area(req.shell, req.holes)}
    except ValueError as e:
        raise HTTPException(
            status_code=HTTPStatus.UNPROCESSABLE_CONTENT, detail=f"{e}"
        ) from e
