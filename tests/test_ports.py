import pytest

from ocean.exceptions import PortNotFoundError
from ocean.ports import get, search


def test_search_port_by_name():
    matches = search("Singapore")
    assert matches[0].unlocode == "SGSIN"


def test_get_port_by_unlocode():
    port = get("CNSHA")
    assert port.name == "Shanghai"


def test_get_missing_port_raises():
    with pytest.raises(PortNotFoundError):
        get("Not A Port")
