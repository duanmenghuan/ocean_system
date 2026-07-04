from ocean.distance import bearing, distance_km, distance_nm
from ocean.routing import interpolate_route


def test_distance_between_shanghai_and_singapore_is_reasonable():
    km = distance_km(31.2304, 121.4737, 1.2897, 103.8501)
    nm = distance_nm(31.2304, 121.4737, 1.2897, 103.8501)

    assert 3750 < km < 3900
    assert 2020 < nm < 2110


def test_bearing_range():
    value = bearing(31.2304, 121.4737, 1.2897, 103.8501)
    assert 190 < value < 230


def test_interpolate_route_includes_endpoints():
    points = interpolate_route(0, 0, 10, 10, points=3)
    assert points[0] == (0.0, 0.0)
    assert points[-1] == (10.0, 10.0)
    assert len(points) == 3
