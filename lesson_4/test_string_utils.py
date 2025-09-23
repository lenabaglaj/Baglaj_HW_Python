import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("  hello world", "hello world"),
    ("  python", "python"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   123abc", "123abc"),
    ("", ""),
    (" ", ""),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro", "s", True),
    ("hello world", "h", True),
    ("python", "y", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("123abc", "4", False),
    ("", "", True),
    (" ", "  ", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("skypro","s","kypro"),
    ("hello world", "e","hllo world"),
    ("python", "p","ython"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("123abc", "4","123abc"),
    ("Way", "way", "Way"),
    (" ", " ", ""),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected