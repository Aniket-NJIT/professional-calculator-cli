from typing import Callable
from app.operation import add, sub, mul, div

class Calculation:
    """
    Represents a single calculation entity.
    """
    def __init__(self, a: float, b: float, operation: Callable[[float, float], float]):
        self.a = a
        self.b = b
        self.operation = operation

    @staticmethod
    def create(a: float, b: float, operation: Callable[[float, float], float]):
        """Factory method to create a Calculation object."""
        return Calculation(a, b, operation)

    def perform(self) -> float:
        """Executes the stored operation."""
        return self.operation(self.a, self.b)

    def __repr__(self):
        """String representation for debugging."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"