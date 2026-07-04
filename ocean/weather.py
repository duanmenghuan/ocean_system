"""General weather forecasts from Open-Meteo Weather API."""

from __future__ import annotations

from typing import Any

from . import client
from .config import WEATHER_URL


def forecast(latitude: float, longitude: float, forecast_days: int = 7) -> dict[str, Any]:
    """Return general weather forecast data for the given coordinates."""

    return client.get(
        WEATHER_URL,
        {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": "temperature_2m,wind_speed_10m,wind_direction_10m,precipitation",
            "forecast_days": forecast_days,
        },
    )
