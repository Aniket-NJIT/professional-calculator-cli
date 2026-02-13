from app.calculator import Calculator
from app.calculation import Calculation
from app.operation import add

def test_add_calculation():
    Calculator.clear_history()
    calc = Calculation(1, 1, add)
    Calculator.add_calculation(calc)
    assert len(Calculator.history) == 1

def test_get_history():
    Calculator.clear_history()
    calc = Calculation(1, 1, add)
    Calculator.add_calculation(calc)
    assert Calculator.get_history() == [calc]

def test_get_latest():
    Calculator.clear_history()
    calc1 = Calculation(1, 1, add)
    calc2 = Calculation(2, 2, add)
    Calculator.add_calculation(calc1)
    Calculator.add_calculation(calc2)
    assert Calculator.get_latest() == calc2

def test_get_latest_empty():
    Calculator.clear_history()
    assert Calculator.get_latest() is None

def test_clear_history():
    Calculator.clear_history()
    calc = Calculation(1, 1, add)
    Calculator.add_calculation(calc)
    Calculator.clear_history()
    assert len(Calculator.history) == 0