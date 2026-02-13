from app.calculation import Calculation
from app.operation import add, div
import pytest

def test_calculation_create():
    calc = Calculation.create(2, 2, add)
    assert isinstance(calc, Calculation)

def test_calculation_perform():
    calc = Calculation(2, 3, add)
    assert calc.perform() == 5

def test_calculation_repr():
    calc = Calculation(2, 2, add)
    assert repr(calc) == "Calculation(2, 2, add)"

def test_calculation_divide_by_zero_pass_through():
    """Ensure the calculation wrapper allows the exception to bubble up."""
    calc = Calculation(10, 0, div)
    with pytest.raises(ValueError):
        calc.perform()