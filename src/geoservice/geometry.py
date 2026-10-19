from collections.abc import Sequence

import shapely
from shapely.geometry import mapping, shape


def buffer_geometry(geometry: dict, distance: float) -> dict:
    """Buffer a GeoJSON geometry and return the result as GeoJSON."""
    geom = shape(geometry)
    return mapping(geom.buffer(distance))


def calculate_area(
    shell: Sequence[Sequence[int | float]],
    holes: Sequence[Sequence[Sequence[int | float]]] | None,
) -> float:
    """Returns the area of a polygon with a certain shell and holes as calculated by
    shapely"""
    return shapely.Polygon(shell, holes).area
