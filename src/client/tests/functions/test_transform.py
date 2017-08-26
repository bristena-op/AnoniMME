import pytest

from functions.transform import string_to_number, number_to_string


@pytest.mark.parametrize(("test_input", "expected"), [
    ("AAAAAA", 71748523475265),
    ("BU1SO5", 58614814430530),
    ("%$!", 2171941),
    ("", 0),
])
def test_string_to_number(test_input, expected):
    assert string_to_number(test_input) == expected


@pytest.mark.parametrize(("test_input", "expected"), [
    (71748523475265, "AAAAAA"),
    (0, ""),
])
def test_number_to_string(test_input, expected):
    assert number_to_string(test_input) == expected



@pytest.mark.parametrize("test_input", [
    "AAAAA",
    "SASGDG43534643DGDFGdf",
    ""
])
def test_full_conversion(test_input):

    assert number_to_string(string_to_number(test_input)) == test_input

