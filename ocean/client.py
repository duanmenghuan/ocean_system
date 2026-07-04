"""Small HTTP client wrapper used by all data-source modules."""

from __future__ import annotations

import json
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from .config import DEFAULT_TIMEOUT
from .exceptions import OceanHTTPError


def get(url: str, params: dict[str, Any] | None = None, timeout: int = DEFAULT_TIMEOUT) -> dict[str, Any]:
    """Fetch JSON from *url* using query *params*.

    A single wrapper keeps API access centralized so future providers can be
    swapped in with minimal changes to geocoding, weather, and marine modules.
    """

    query = urlencode(params or {})
    full_url = f"{url}?{query}" if query else url
    request = Request(full_url, headers={"User-Agent": "ocean-system/0.1"})

    try:
        with urlopen(request, timeout=timeout) as response:
            charset = response.headers.get_content_charset() or "utf-8"
            return json.loads(response.read().decode(charset))
    except (HTTPError, URLError, TimeoutError) as exc:
        raise OceanHTTPError(f"HTTP request failed for {url}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise OceanHTTPError(f"Response from {url} was not valid JSON") from exc
