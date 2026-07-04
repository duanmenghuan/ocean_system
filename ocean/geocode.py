"""Geocoding helpers backed by the Open-Meteo Geocoding API."""

from __future__ import annotations

from . import client
from .config import GEOCODING_URL
from .exceptions import GeocodingError
from .models import Location


def search(name: str, count: int = 1, language: str = "en") -> Location:
    """Return the best matching location for *name*."""

    if not name.strip():
        raise GeocodingError("Location name must not be empty")

    payload = client.get(
        GEOCODING_URL,
        {"name": name, "count": count, "language": language, "format": "json"},
    )
    results = payload.get("results") or []
    if not results:
        raise GeocodingError(f"No geocoding result found for {name!r}")

    item = results[0]
    return Location(
        name=item["name"],
        latitude=float(item["latitude"]),
        longitude=float(item["longitude"]),
        country=item.get("country"),
        timezone=item.get("timezone"),
    )
