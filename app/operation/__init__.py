"""
Arithmetic operations module.
"""

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def sub(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def mul(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def div(a: float, b: float) -> float:
    """
    Returns the division of two numbers.
    Demonstrates Look Before You Leap by checking for zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
    