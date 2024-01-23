import pytest
from fuel import convert, gauge

def test_convert_valid_fraction():
    assert convert("3/4") == 75

def test_convert_invalid_fraction_format():
    with pytest.raises(ValueError):
        convert("invalid_format")

def test_convert_x_greater_than_y():
    with pytest.raises(ValueError):
        convert("5/3")

def test_convert_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge_less_than_or_equal_1():
    assert gauge(1) == "E"

def test_gauge_greater_than_or_equal_99():
    assert gauge(99) == "F"

def test_gauge_between_1_and_99():
    assert gauge(50) == "50%"

# Add more test functions as needed

if __name__ == "__main__":
    pytest.main()
