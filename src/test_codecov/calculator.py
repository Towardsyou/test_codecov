"""Calculator helpers with simple, testable behavior."""


def add(left: float, right: float) -> float:
    """Return the sum of two numbers."""
    return left + right


def divide(dividend: float, divisor: float) -> float:
    """Return dividend divided by divisor."""
    if divisor == 0:
        raise ValueError("divisor cannot be zero")

    return dividend / divisor


def is_even(number: int) -> bool:
    """Return whether an integer is even."""
    return number % 2 == 0


def is_odd(number: int) -> bool:
    """Return whether an integer is odd."""
    return not is_even(number)

def multiply(left: float, right: float) -> float:
    """Return the product of two numbers."""
    return left * right
