from calculator import add, subtract, multiply


def test_add():
    assert add(3, 5) == 8


def test_subtract():
    assert subtract(5, 3) == 2


def test_subtract():
    assert multiply(3, 5) == 15
