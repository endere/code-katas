"""Test the forbes code."""
from forbes import find_billionaires
import json
with open('data.json') as data_file:
    data = json.load(data_file)

with open('edited_data.json') as edited_data_file:
    edited_data = json.load(edited_data_file)
#json reader found at https://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-using-python


def test_forbes():
    """Test if function returns manually found results from json."""
    assert find_billionaires(data) == (['Phil Knight', 24400000000, 'Nike'], ['Mark Zuckerberg', 44600000000, 'Facebook'])


def test_forbes_with_data_changed_so_there_are_invalid_ages_and_non_billionaires():
    """Test if function returns manually found results from json once jason (including original winners) has been edited."""
    assert find_billionaires(edited_data) == (['Carlos Slim Helu', 50000000000, 'telecom'], ['Sergey Brin', 34400000000, 'Google'])
