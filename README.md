# ocean_system

`ocean_system` is a small Python toolkit for early-stage voyage planning. Version 0.1 uses Open-Meteo's no-key APIs for geocoding, general weather, and marine weather, plus local great-circle calculations and a bundled starter port dataset.

## Features

- Unified HTTP client: `ocean.client.get(url, params)`
- Geocoding: place name to coordinates
- Marine weather forecasts by latitude/longitude
- General weather forecasts by latitude/longitude
- Great-circle distance, nautical miles, and initial bearing
- Simple voyage planning with ETA by vessel speed
- Bundled CSV port search
- CLI and demo script

## Install

```bash
pip install -r requirements.txt
```

## Examples

```python
from ocean.geocode import search
from ocean.marine import latest_conditions
from ocean.routing import plan

print(search("Singapore"))
print(latest_conditions(1.28, 103.84))
print(plan("Shanghai", "Singapore", speed=13))
```

Run the offline demo:

```bash
python examples/demo.py
```

Use the CLI:

```bash
python main.py ports Singapore
python main.py geocode Singapore
python main.py marine 1.28 103.84
python main.py route Shanghai Singapore --speed 13
```

## Development

```bash
pytest
```
