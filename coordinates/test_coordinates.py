import pytest
PARAMS_TABLE_VALID = [
    ("-23, 25"),
    ("4, -3"),
    ("24.53525235, 23.45235"),
    ("04, -23.234235"),
    ("43.91343345, 143")
]
PARAMS_TABLE_INVALID = [
    ("23.234, - 23.4234"),
    ("2342.43536, 34.324236"),
    ("N23.43345, E32.6457"),
    ("99.234, 12.324"),
    ("6.325624, 43.34345.345"),
    ("0, 1,2"),
    ("0.342q0832, 1.2324"),
    ("23.245, 1e1")
]


@pytest.mark.parametrize("coords", PARAMS_TABLE_VALID)
def test_valid(coords):
    from coordinates import is_valid_coordinates
    assert is_valid_coordinates(coords) is True


@pytest.mark.parametrize("coords", PARAMS_TABLE_INVALID)
def test_invalid(coords):
    from coordinates import is_valid_coordinates
    assert is_valid_coordinates(coords) is False
