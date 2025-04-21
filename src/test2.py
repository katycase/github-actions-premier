from test import add, subtract, multiply, divide
import pytest


def test_add():
        assert add(2, 3) == 5
    
def test_subtract():
        assert(subtract(5, 3), 2)

def test_multiply():
        assert(multiply(4, 5), 20)


def test_divide():
        assert(divide(10, 2), 5)


def test_divide0():
        with pytest.raises(ValueError):
                divide(10, 0)

 