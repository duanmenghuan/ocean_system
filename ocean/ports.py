"""Port lookup utilities backed by the bundled CSV dataset."""

from __future__ import annotations

import csv
from functools import lru_cache
from pathlib import Path

from .exceptions import PortNotFoundError
from .models import Port

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "ports.csv"


@lru_cache(maxsize=1)
def load_ports() -> tuple[Port, ...]:
    """Load bundled port records."""

    with DATA_FILE.open(newline="", encoding="utf-8") as file_obj:
        return tuple(
            Port(
                unlocode=row["unlocode"],
                name=row["name"],
                country=row["country"],
                latitude=float(row["latitude"]),
                longitude=float(row["longitude"]),
            )
            for row in csv.DictReader(file_obj)
        )


def search(query: str) -> list[Port]:
    """Return ports whose name, country, or UN/LOCODE contains *query*."""

    normalized = query.strip().lower()
    if not normalized:
        return list(load_ports())

    return [
        port
        for port in load_ports()
        if normalized in port.name.lower()
        or normalized in port.country.lower()
        or (port.unlocode and normalized in port.unlocode.lower())
    ]


def get(query: str) -> Port:
    """Return the best matching port or raise :class:`PortNotFoundError`."""

    matches = search(query)
    if not matches:
        raise PortNotFoundError(f"No port found for {query!r}")
    return matches[0]
