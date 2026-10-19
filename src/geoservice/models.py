from collections.abc import Sequence

from pydantic import BaseModel, ConfigDict


class BufferRequest(BaseModel):
    geometry: dict  # a GeoJSON geometry
    distance: float  # buffer distance, in the units of the coordinates


class PolygonRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    shell: Sequence[Sequence[float]]
    holes: Sequence[Sequence[Sequence[float]]] | None = None
