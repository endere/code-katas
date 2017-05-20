"""Test for the mysterious function code."""


import pytest
PARAMS_TABLE = [
        (300, 2),
        (90783, 4),
        (123321, 0),
        (89282350306, 8),
        (3479283469, 5),
        (44444, 0),
        (123456789, 4),
        (222444666888000, 12),
        (111333555777999, 3)

]


@pytest.mark.parametrize("n, result", PARAMS_TABLE)
def test_trib(n, result):
    """Test to make sure the code outputs the correct number of holes in the result."""
    from mysterious import get_num
    assert get_num(n) == result
