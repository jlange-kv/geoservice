"""These tests already assert the useful things. Your job is to make them run
under the new package structure (import geoservice, not this flat module) — not
to rewrite them."""

from http import HTTPStatus

from fastapi.testclient import TestClient

from geoservice.app import app

client = TestClient(app)


def test_buffer_returns_a_polygon():
    resp = client.post(
        "/buffer",
        json={
            "geometry": {"type": "Point", "coordinates": [10.75, 59.91]},
            "distance": 1,
        },
    )
    assert resp.status_code == HTTPStatus.OK
    assert resp.json()["type"] == "Polygon"


def test_health_responds():
    resp = client.get("/health")
    assert resp.status_code == HTTPStatus.OK
    assert resp.json() == {"status": "ok"}
