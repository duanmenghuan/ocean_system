"""Voyage planning helpers based on great-circle distance."""

from __future__ import annotations

from math import asin, atan2, cos, degrees, radians, sin

from .distance import bearing, distance_nm
from .geocode import search


def plan(origin: str, destination: str, speed: float = 13) -> dict[str, float | str]:
    """Plan a simple great-circle voyage between two named locations.

    ``speed`` is expressed in knots, so the ETA is distance in nautical miles
    divided by speed.
    """

    if speed <= 0:
        raise ValueError("speed must be greater than zero")

    start = search(origin)
    end = search(destination)
    nm = distance_nm(start.latitude, start.longitude, end.latitude, end.longitude)
    return {
        "origin": start.name,
        "destination": end.name,
        "distance_nm": round(nm, 2),
        "eta_hours": round(nm / speed, 2),
        "bearing": round(bearing(start.latitude, start.longitude, end.latitude, end.longitude), 2),
    }


def interpolate_route(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
    points: int = 5,
) -> list[tuple[float, float]]:
    """Return evenly spaced great-circle waypoints including start and end."""

    if points < 2:
        raise ValueError("points must be at least 2")

    phi1, lambda1, phi2, lambda2 = map(radians, (lat1, lon1, lat2, lon2))
    delta = 2 * asin(
        min(
            1,
            (sin((phi2 - phi1) / 2) ** 2 + cos(phi1) * cos(phi2) * sin((lambda2 - lambda1) / 2) ** 2) ** 0.5,
        )
    )
    if delta == 0:
        return [(lat1, lon1)] * points

    waypoints = []
    for index in range(points):
        fraction = index / (points - 1)
        a = sin((1 - fraction) * delta) / sin(delta)
        b = sin(fraction * delta) / sin(delta)
        x = a * cos(phi1) * cos(lambda1) + b * cos(phi2) * cos(lambda2)
        y = a * cos(phi1) * sin(lambda1) + b * cos(phi2) * sin(lambda2)
        z = a * sin(phi1) + b * sin(phi2)
        phi = atan2(z, (x * x + y * y) ** 0.5)
        lamb = atan2(y, x)
        waypoints.append((round(degrees(phi), 6), round(degrees(lamb), 6)))
    return waypoints
