import sys
from decimal import Decimal, InvalidOperation
from app.calculator import Calculator
from app.calculation import CalculationFactory

def calculate_and_print(a, b, operation_name):
    """
    Helper to perform calculation using the Factory and print result.
    """
    try:
        # Use CalculationFactory (Assignment Requirement)
        calculation = CalculationFactory.create_calculation(a, b, operation_name)
        result = calculation.perform()
        Calculator.add_calculation(calculation)
        print(f"The result of {a} {operation_name} {b} is equal to {result}")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except ValueError as e:
        # Handles both invalid operations and invalid numeric inputs
        print(f"Error: {e}")

def main(): # pragma: no cover
    """
    Main REPL loop.
    """
    print("Welcome to the Calculator. Type 'exit' to quit.")
    print("Format: <operation> <number1> <number2>")
    print("Available operations: add, subtract, multiply, divide")

    while True:
        user_input = input(">>> ").strip().lower()
        if user_input == 'exit':
            print("Exiting...")
            break
        
        if user_input == 'history':
            history = Calculator.get_history()
            for item in history:
                print(item)
            continue
            
        if user_input == 'help':
            print("Usage: <operation> <a> <b>")
            print("Ops: add, subtract, multiply, divide")
            continue

        parts = user_input.split()
        if len(parts) != 3:
            print("Invalid format. Use: <operation> <a> <b>")
            continue

        operation, a_str, b_str = parts
        
        # EAFP: Attempt conversion
        try:
            a = float(a_str)
            b = float(b_str)
            calculate_and_print(a, b, operation)
        except ValueError:
            print(f"Invalid number input: {a_str} or {b_str} is not a valid number.")

if __name__ == "__main__": # pragma: no cover
    main()
