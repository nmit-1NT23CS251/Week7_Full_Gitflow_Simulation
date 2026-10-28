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
