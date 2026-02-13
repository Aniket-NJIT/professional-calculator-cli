# Professional Python Calculator

![Build Status](https://github.com/Aniket-NJIT/professional-calculator-cli/actions/workflows/main.yml/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Code Quality](https://img.shields.io/badge/pylint-10%2F10-brightgreen)

A modular, professional-grade command-line calculator application built in Python. This project demonstrates clean architecture, design patterns, and strict software engineering best practices, including 100% test coverage and continuous integration (CI/CD).

## Features

- **REPL Interface**: Interactive command-line interface (Read-Eval-Print Loop) for continuous calculation.
- **Modular Architecture**: distinct separation of concerns between Operations, Calculation logic, History management, and Commands.
- **Robust Error Handling**: Implements both **LBYL** (Look Before You Leap) and **EAFP** (Easier to Ask Forgiveness than Permission) strategies.
- **History Management**: Tracks, stores, and retrieves calculation history.
- **Dynamic Command Loading**: Extensible Command Pattern for handling user inputs.
- **Professional Quality**: 
  - **100% Test Coverage** with `pytest`.
  - **10/10 Code Quality** score with `pylint`.
  - **CI/CD Pipeline** using GitHub Actions.

## Installation & Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Aniket-NJIT/professional-calculator-cli.git
   cd professional-calculator-cli
   ```

2. **Create a Virtual Environment**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4. **How to use:**
    ```bash
    python main.py
    ```

5. **Supported Commands**
    - Arithmetic: add, subtract, multiply, divide
    - System:
        - history: View all past calculations.
        - exit: Quit the application.
        - help: View available commands.

6. **Example Session**
    ```bash
    >>> add 10 5
    The result of 10 add 5 is equal to 15.0
    >>> divide 50 0
    Error: Cannot divide by zero
    >>> multiply 2.5 4
    The result of 2.5 multiply 4 is equal to 10.0
    >>> history
    Calculation(10.0, 5.0, add)
    Calculation(2.5, 4.0, multiply)
    ```

7. **Design Patterns & Architecture**
    This project strictly adheres to the DRY (Don't Repeat Yourself) principle and utilizes several key design patterns:

    1. Command Pattern (app/commands)
    Decouples the object that invokes the operation (the REPL) from the one that knows how to perform it. This makes adding new commands (like power or root) easy without modifying the main loop.

    2. Facade Pattern (app/calculator)
    The Calculator class acts as a facade, providing a simplified interface to the complex subsystem of calculation history and operations.

    3. Factory Method (app/calculation)
    The Calculation.create() method encapsulates the logic of instantiating new calculation objects, ensuring consistent object creation.

    4. Strategy Pattern (Implied)
    The operations (add, sub, mul, div) act as interchangeable strategies that can be passed into the Calculation engine.

8. **Testing & Quality**
    This project enforces strict quality gates. The build will fail if test coverage drops below 100% or if code quality issues are introduced.
    To run the full test suite and check coverage:
    ```bash
    python -m pytest
    ```
