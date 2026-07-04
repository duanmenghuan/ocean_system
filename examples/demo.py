"""Demo script for the ocean package."""

from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from ocean.distance import distance_nm
from ocean.ports import get


if __name__ == "__main__":
    shanghai = get("Shanghai")
    singapore = get("Singapore")
    nm = distance_nm(shanghai.latitude, shanghai.longitude, singapore.latitude, singapore.longitude)
    print(f"{shanghai.name} -> {singapore.name}: {nm:.0f} nautical miles")
