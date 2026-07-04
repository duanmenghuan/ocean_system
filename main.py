"""Command line interface for ocean_system."""

from __future__ import annotations

import argparse
import json

from ocean.geocode import search as geocode_search
from ocean.marine import latest_conditions
from ocean.ports import search as port_search
from ocean.routing import plan


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Ocean system CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    geocode_parser = subparsers.add_parser("geocode", help="Find coordinates for a place")
    geocode_parser.add_argument("name")

    marine_parser = subparsers.add_parser("marine", help="Fetch latest marine conditions")
    marine_parser.add_argument("latitude", type=float)
    marine_parser.add_argument("longitude", type=float)

    route_parser = subparsers.add_parser("route", help="Plan a simple voyage")
    route_parser.add_argument("origin")
    route_parser.add_argument("destination")
    route_parser.add_argument("--speed", type=float, default=13)

    ports_parser = subparsers.add_parser("ports", help="Search bundled port data")
    ports_parser.add_argument("query")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    if args.command == "geocode":
        result = geocode_search(args.name).__dict__
    elif args.command == "marine":
        result = latest_conditions(args.latitude, args.longitude)
    elif args.command == "route":
        result = plan(args.origin, args.destination, args.speed)
    else:
        result = [port.__dict__ for port in port_search(args.query)]
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
