"""Custom exceptions for the ocean package."""


class OceanError(Exception):
    """Base exception for ocean package errors."""


class OceanHTTPError(OceanError):
    """Raised when an HTTP request fails."""


class GeocodingError(OceanError):
    """Raised when a location cannot be geocoded."""


class PortNotFoundError(OceanError):
    """Raised when a port cannot be found."""
