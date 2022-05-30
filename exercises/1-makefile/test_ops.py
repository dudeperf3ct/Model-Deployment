import pytest
from ops import add, divide, multiply

def test_add():
    assert 2 == add(1, 1)

def test_multiply():
    assert 0 == multiply(1, 0)
    assert -1 == multiply(1, -1)

def test_divide():
    assert 0 == divide(0, 1)

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)