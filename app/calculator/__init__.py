"""
Calculator module.
Manages the history of calculations and provides a facade for the application.
"""
from typing import List
from app.calculation import Calculation

class Calculator:
    """
    Manages the history of calculations.
    """
    history: List[Calculation] = []

    @staticmethod
    def add_calculation(calculation: Calculation):
        """Adds a calculation to history."""
        Calculator.history.append(calculation)

    @staticmethod
    def get_history() -> List[Calculation]:
        """Retrieves the full history."""
        return Calculator.history

    @staticmethod
    def clear_history():
        """Clears the history."""
        Calculator.history.clear()

    @staticmethod
    def get_latest() -> Calculation:
        """Gets the latest calculation. Returns None if empty."""
        if Calculator.history:
            return Calculator.history[-1]
        return None
        