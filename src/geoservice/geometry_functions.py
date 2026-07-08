from shapely.geometry import mapping, shape


def buffer_geometry(geometry: dict, distance: float) -> dict:
    """Buffer a GeoJSON geometry and return the result as GeoJSON."""
    geom = shape(geometry)
    return mapping(geom.buffer(distance))
