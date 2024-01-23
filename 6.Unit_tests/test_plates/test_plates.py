import pytest
from plates import is_valid


def test_invalid_length():
    assert is_valid("F") == False
    assert is_valid("DRE1365") == False
    assert is_valid("AR") == True
    assert is_valid("YT1234") == True
    assert is_valid("er53") == True


def test_non_alphanumeric():
    assert is_valid("DT@23") == False
    assert is_valid("XY_:67") == False
    assert is_valid("ui,44") == False



def test_invalid_first_two_chars():
    assert is_valid("6TYUPO") == False
    assert is_valid("45873") == False


def test_invalid_sequence():
    assert is_valid("AB123CD") == False
    assert is_valid("XU6TA") == False


def test_invalid_starting_zero():
    assert is_valid("AP0124") == False
    assert is_valid("XY0") == False
