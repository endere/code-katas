"""Test for the roman numeral code."""


import pytest


PARAMS_TABLE = [
    ('XXI', 21),
    ("IV", 4),
    ("MMXVII", 2017),
    ("MCMXC", 1990),
    ("DXCIII", 593),
    ("CCXXXIV", 234),
    ("M", 1000)

]


@pytest.mark.parametrize("n, result", PARAMS_TABLE)
def test_roman(n, result):
    """Test to ensure correct numerical output from roman numeral code."""
    from roman import solution
    assert solution(n) == result
