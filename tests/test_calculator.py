from calculator import add, subtract


def test_add():
    assert add(3, 5) == 8


def test_subtract():
    assert subtract(5, 3) == 2
