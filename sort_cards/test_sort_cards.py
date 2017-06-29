"""Test for the sorting cards code."""


import pytest
PARAMS_TABLE = [
    (list('39A5T824Q7J6K'), list('A23456789TJQK')),
    (list('Q286JK395A47T'), list('A23456789TJQK')),
    (list('54TQKJ69327A8'), list('A23456789TJQK')),
    (list('AJAJAJAJ'), list('AAAAJJJJ')),
    (['j'], ['j']),
    ([], [])
]


@pytest.mark.parametrize("data, result", PARAMS_TABLE)
def test_sort(data, result):
    """Test see if correct order of cards is yielded from different inputs."""
    from sort_cards import sort_cards
    assert sort_cards(data) == result
