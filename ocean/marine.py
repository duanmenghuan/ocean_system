"""Marine weather forecasts from Open-Meteo Marine Weather API."""

from __future__ import annotations

from typing import Any

from . import client
from .config import MARINE_URL

DEFAULT_HOURLY_VARIABLES = (
    "wave_height",
    "wave_direction",
    "wave_period",
    "sea_surface_temperature",
    "wind_wave_height",
    "wind_wave_direction",
    "wind_wave_period",
    "swell_wave_height",
    "swell_wave_direction",
    "swell_wave_period",
)


def forecast(
    latitude: float,
    longitude: float,
    hourly: tuple[str, ...] = DEFAULT_HOURLY_VARIABLES,
    forecast_days: int = 7,
) -> dict[str, Any]:
    """Return marine forecast data for the given coordinates."""

    return client.get(
        MARINE_URL,
        {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": ",".join(hourly),
            "forecast_days": forecast_days,
        },
    )


def latest_conditions(latitude: float, longitude: float) -> dict[str, Any]:
    """Return a compact dictionary containing the first forecast hour."""

    data = forecast(latitude, longitude, forecast_days=1)
    hourly = data.get("hourly", {})
    result: dict[str, Any] = {}
    for key, values in hourly.items():
        if isinstance(values, list) and values:
            result[key] = values[0]
    return result
