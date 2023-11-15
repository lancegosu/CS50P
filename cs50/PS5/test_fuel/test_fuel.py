import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("3/4") == 75

def test_zerodivision():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_valueerror():
    with pytest.raises(ValueError):
        convert("a/1")
        convert("1/a")
        convert("2/1")

def test_gauge():
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"