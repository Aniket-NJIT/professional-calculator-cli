import pytest
from app.operation import add, sub, mul, div

@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (-1, 1, 0),
    (0, 0, 0)
])
def test_add(a, b, expected):
    assert add(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (2, 5, -3)
])
def test_sub(a, b, expected):
    assert sub(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 3, 9),
    (3, 0, 0)
])
def test_mul(a, b, expected):
    assert mul(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    (5, 2, 2.5)
])
def test_div(a, b, expected):
    assert div(a, b) == expected

def test_div_by_zero():
    with pytest.raises(ValueError):
        div(10, 0)