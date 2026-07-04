from ocean import geocode, marine, weather
from ocean.models import Location


def test_geocode_search_maps_open_meteo_response(monkeypatch):
    def fake_get(url, params):
        return {"results": [{"name": "Singapore", "latitude": 1.289, "longitude": 103.851, "country": "Singapore"}]}

    monkeypatch.setattr(geocode.client, "get", fake_get)
    result = geocode.search("Singapore")

    assert result == Location(name="Singapore", latitude=1.289, longitude=103.851, country="Singapore", timezone=None)


def test_marine_latest_conditions_uses_first_hour(monkeypatch):
    def fake_forecast(latitude, longitude, forecast_days=1):
        return {"hourly": {"time": ["2026-07-04T00:00"], "wave_height": [1.2], "wave_direction": [90]}}

    monkeypatch.setattr(marine, "forecast", fake_forecast)
    assert marine.latest_conditions(1.28, 103.84) == {
        "time": "2026-07-04T00:00",
        "wave_height": 1.2,
        "wave_direction": 90,
    }


def test_weather_forecast_calls_client(monkeypatch):
    calls = {}

    def fake_get(url, params):
        calls["params"] = params
        return {"hourly": {}}

    monkeypatch.setattr(weather.client, "get", fake_get)
    assert weather.forecast(1, 2, forecast_days=3) == {"hourly": {}}
    assert calls["params"]["forecast_days"] == 3
