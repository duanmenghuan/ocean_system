"""Great-circle distance and bearing calculations."""

from __future__ import annotations

from math import atan2, cos, degrees, radians, sin, sqrt

from .config import EARTH_RADIUS_KM, KM_PER_NAUTICAL_MILE


def distance_km(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Return great-circle distance in kilometers using the haversine formula."""

    phi1, phi2 = radians(lat1), radians(lat2)
    delta_phi = radians(lat2 - lat1)
    delta_lambda = radians(lon2 - lon1)
    a = sin(delta_phi / 2) ** 2 + cos(phi1) * cos(phi2) * sin(delta_lambda / 2) ** 2
    return 2 * EARTH_RADIUS_KM * atan2(sqrt(a), sqrt(1 - a))


def distance_nm(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Return great-circle distance in nautical miles."""

    return distance_km(lat1, lon1, lat2, lon2) / KM_PER_NAUTICAL_MILE


def bearing(lat1: float, lon1: float, lat2: float, lon2: float) -> float:
    """Return initial bearing from point A to point B in degrees."""

    phi1, phi2 = radians(lat1), radians(lat2)
    delta_lambda = radians(lon2 - lon1)
    y = sin(delta_lambda) * cos(phi2)
    x = cos(phi1) * sin(phi2) - sin(phi1) * cos(phi2) * cos(delta_lambda)
    return (degrees(atan2(y, x)) + 360) % 360
