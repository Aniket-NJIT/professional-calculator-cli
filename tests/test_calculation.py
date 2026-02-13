"""
Tests for the Calculation class and CalculationFactory.
"""
import pytest
from app.calculation import Calculation, CalculationFactory
from app.operation import add, div

def test_calculation_perform():
    """Test that the perform method calls the operation correctly."""
    calc = Calculation(2, 3, add)
    assert calc.perform() == 5

def test_calculation_repr():
    """Test the string representation of a Calculation."""
    calc = Calculation(2, 2, add)
    assert repr(calc) == "Calculation(2, 2, add)"

def test_calculation_divide_by_zero_pass_through():
    """Ensure the calculation allows ZeroDivisionError to bubble up."""
    # Demonstrating that the Calculation object itself doesn't suppress errors
    calc = Calculation(10, 0, div)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()

def test_calculation_factory_create():
    """Test that the factory creates a Calculation object successfully."""
    calc = CalculationFactory.create_calculation(10, 5, 'add')
    assert isinstance(calc, Calculation)
    assert calc.perform() == 15

def test_calculation_factory_invalid_operation():
    """Test the factory handles unknown operation names (EAFP)."""
    with pytest.raises(ValueError, match="Unknown operation: power"):
        CalculationFactory.create_calculation(10, 5, 'power')