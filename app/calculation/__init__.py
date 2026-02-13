"""
Calculation module.
This module defines the Calculation class and the CalculationFactory.
"""
from typing import Callable
from app.operation import add, sub, mul, div

class Calculation: # pylint: disable=too-few-public-methods
    """
    Represents a single calculation entity.
    """
    def __init__(self, a: float, b: float, operation: Callable[[float, float], float]):
        self.a = a
        self.b = b
        self.operation = operation

    def perform(self) -> float:
        """Executes the stored operation."""
        return self.operation(self.a, self.b)

    def __repr__(self):
        """String representation for debugging/history."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"

class CalculationFactory:
    """
    Factory class to create Calculation instances based on operation names.
    """
    @staticmethod
    def create_calculation(a: float, b: float, op_name: str) -> Calculation:
        """
        Creates a calculation based on the operation name string.
        Demonstrates EAFP by attempting to access the dictionary.
        """
        operations = {
            'add': add,
            'subtract': sub,
            'multiply': mul,
            'divide': div
        }
        
        try:
            operation_func = operations[op_name]
            return Calculation(a, b, operation_func)
        except KeyError as exc:
            # Fixes W0707: Explicitly re-raising with 'from exc'
            raise ValueError(f"Unknown operation: {op_name}") from exc
