"""Test proper parenthetics function."""


import pytest
from parenthetics import parenthetics

PARAMS_TABLE = [
    ('()()()', 0),
    ('', 0),
    ('(()', 1),
    ('))', -1),
    ('((()))', 0),
    (')))(((', -1),
    ('iasjdfngiasnfgi(nas)rg', 0),
    ('iasjd(fngiasnfgi(nas)rg', 1),
    ('ia)sjd(fngiasnfgi(nas)rg', -1),
]


@pytest.mark.parametrize("data, result", PARAMS_TABLE)
def test_parenthetics(data, result):
    """Assert the parenthetics function outputs the proper number."""
    assert parenthetics(data) == result
