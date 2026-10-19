"""These tests already assert the useful things. Your job is to make them run
under the new package structure (import geoservice, not this flat module) — not
to rewrite them."""

from http import HTTPStatus

import pytest
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


VALID_SHELL = ((0, 0), (0, 10), (10, 10), (10, 0))
VALID_HOLES = (((0, 0), (0, 1), (1, 1), (1, 0)), ((8, 8), (8, 9), (9, 9), (9, 8)))

GOOD_CASES = (
    (({"shell": VALID_SHELL}, 100.0), "shell"),
    (({"shell": VALID_SHELL, "holes": (VALID_HOLES[0],)}, 99.0), "shell w hole"),
    (({"shell": VALID_SHELL, "holes": VALID_HOLES}, 98.0), "shell w holes"),
)

INVALID_SHELL = ((0, 0), (0, 1))
BAD_CASES = (
    (({"shell": INVALID_SHELL}, HTTPStatus.UNPROCESSABLE_CONTENT), "invalid polygon"),
    (({"holes": VALID_SHELL}, HTTPStatus.UNPROCESSABLE_CONTENT), "missing key"),
    (
        ({"shell": VALID_SHELL, "hol": VALID_HOLES}, HTTPStatus.UNPROCESSABLE_CONTENT),
        "invalid key",
    ),
    (({"shell": "invalid"}, HTTPStatus.UNPROCESSABLE_CONTENT), "invalid data type"),
)


@pytest.mark.parametrize(
    "request_data,expected",
    [case[0] for case in GOOD_CASES],
    ids=[case[1] for case in GOOD_CASES],
)
def test_area_valid_request(request_data, expected):
    resp = client.post("/area", json=request_data)
    assert resp.status_code == HTTPStatus.OK
    assert resp.json()["area"] == expected


@pytest.mark.parametrize(
    "request_data,expected",
    [case[0] for case in BAD_CASES],
    ids=[case[1] for case in BAD_CASES],
)
def test_area_422_response(request_data, expected):
    resp = client.post("/area", json=request_data)
    assert resp.status_code == expected
