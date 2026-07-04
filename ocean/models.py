"""Data models used by the ocean package."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    """A named geographic position."""

    name: str
    latitude: float
    longitude: float
    country: str | None = None
    timezone: str | None = None


@dataclass(frozen=True)
class Port:
    """A port entry with approximate coordinates."""

    name: str
    country: str
    latitude: float
    longitude: float
    unlocode: str | None = None
