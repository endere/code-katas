"""Test for the hungry foxes code."""


import pytest
PARAMS_TABLE = [
        ("CCC[CCC]FCC[CCCCC]CFFFF[CCC]FFFF", "...[CCC]F..[CCCCC].FFFF[CCC]FFFF"),
        ("...[CCC]...[CCCFC].....[CCC]....", "...[CCC]...[...F.].....[CCC]...."),
        ("CCC[CCC]FCC[CCCFC]CFFFF[CCC]FFFF", "...[CCC]F..[...F.].FFFF[CCC]FFFF"),
        ("CCC[CCC]CCC[CCCFC]CCCCC[CCC]CCCC", "CCC[CCC]CCC[...F.]CCCCC[CCC]CCCC"),
        ("CCCFFFF", "...FFFF"),
        ("[C]", "[C]"),
        ("CCC[FFFC", "CCC[FFF.")

]


@pytest.mark.parametrize("farm, result", PARAMS_TABLE)
def test_trib(farm, result):
    """Test to see which chickens survive night, based on rules supplied in kata (written in foxes.py)."""
    from foxes import hungry_foxes
    assert hungry_foxes(farm) == result
