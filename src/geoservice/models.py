from pydantic import BaseModel


class BufferRequest(BaseModel):
    geometry: dict  # a GeoJSON geometry
    distance: float  # buffer distance, in the units of the coordinates
