"""Test suite for string pyramid kata."""
import string_pyramid
import pytest
PARAMS_TABLE_ABOVE = [
    ('abc', '''\
aaaaa
abbba
abcba
abbba
aaaaa'''),
    ('abcd', '''\
aaaaaaa
abbbbba
abcccba
abcdcba
abcccba
abbbbba
aaaaaaa'''),
    ('*#', '***\n*#*\n***')
]

PARAMS_TABLE_SIDE = [
    ('abc', '  c  \n bbb \naaaaa'),
    ('abcd', '   d   \n  ccc  \n bbbbb \naaaaaaa'),
    ('*#', ' # \n***')
]

PARAMS_TABLE_VISIBLE = [
    ('abcd', 49),
    ('abc', 25),
    ('*#', 9)
]
PARAMS_TABLE_ALL = [
    ('abcd', 84),
    ('abc', 35),
    ('*#', 10)
]


@pytest.mark.parametrize("input, result", PARAMS_TABLE_ABOVE)
def test_watch_from_above(input, result):
    """Test if function gives correct top down view."""
    assert string_pyramid.watch_pyramid_from_above(input) == result


@pytest.mark.parametrize("input, result", PARAMS_TABLE_SIDE)
def test_watch_from_side(input, result):
    """Test if function gives correct side view."""
    assert string_pyramid.watch_pyramid_from_the_side(input) == result


@pytest.mark.parametrize("input, result", PARAMS_TABLE_ALL)
def test_count_all(input, result):
    """Test if function gives correct number of total stones."""
    assert string_pyramid.count_all_characters_of_the_pyramid(input) == result


@pytest.mark.parametrize("input, result", PARAMS_TABLE_VISIBLE)
def test_count_visible(input, result):
    """Test if function gives correct number of visible stones."""
    assert string_pyramid.count_visible_characters_of_the_pyramid(input) == result
