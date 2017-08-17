import pytest
from twisted import compute_sum
PARAMS_TABLE = [
    (1, 1),
    (2, 3),
    (3, 6),
    (4, 10),
    (10, 46),
    (11, 48),
    (12, 51)
]


@pytest.mark.parametrize("number, result", PARAMS_TABLE)
def test_twisted(number, result):
    assert compute_sum(number) == result