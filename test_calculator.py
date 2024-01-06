import pytest
import tkinter as tk
from calculator import Calculator

@pytest.fixture
def calculator_app():
    root = tk.Tk()
    calc = Calculator(root)
    return calc, root

def test_addition(calculator_app):
    calculator, _ = calculator_app
    calculator.calculate(2)
    calculator.calculate('+')
    calculator.calculate(3)
    assert calculator.result.get("1.0", tk.END).strip() == "5"

def test_subtraction(calculator_app):
    calculator, _ = calculator_app
    calculator.calculate(7)
    calculator.calculate('-')
    calculator.calculate(3)
    assert calculator.result.get("1.0", tk.END).strip() == "4"

def test_multiplication(calculator_app):
    calculator, _ = calculator_app
    calculator.calculate(4)
    calculator.calculate('*')
    calculator.calculate(3)
    assert calculator.result.get("1.0", tk.END).strip() == "12"

def test_division(calculator_app):
    calculator, _ = calculator_app
    calculator.calculate(8)
    calculator.calculate('/')
    calculator.calculate(2)
    assert calculator.result.get("1.0", tk.END).strip() == "4"

def test_clear(calculator_app):
    calculator, _ = calculator_app
    calculator.calculate(5)
    calculator.calculate('+')
    calculator.calculate(3)
    calculator.clear()
    assert calculator.result.get("1.0", tk.END).strip() == ""

def test_error_handling(calculator_app):
    calculator, _ = calculator_app
    calculator.calculate(5)
    calculator.calculate('/')
    calculator.calculate(0)
    assert calculator.result.get("1.0", tk.END).strip() == "Error"

# Add more test cases as needed
