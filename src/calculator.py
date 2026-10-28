"""Simple calculator used to demonstrate a Gitflow development lifecycle."""


def add(a: float, b: float) -> float:
    """Return the sum of two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference between two numbers."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide two numbers, rejecting zero as the denominator."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def square(a):
    return a * a


def safe_divide(a, b):
    """Safely divide two numbers and handle division by zero."""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b
