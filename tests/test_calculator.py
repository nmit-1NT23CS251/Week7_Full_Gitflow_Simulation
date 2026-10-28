"""Tests run locally and in GitHub Actions."""
import pytest
from src.calculator import add, subtract, multiply, divide


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(9, 4) == 5


def test_multiply():
    assert multiply(6, 7) == 42


def test_divide():
    assert divide(12, 4) == 3


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(7, 0)
