def add(a, b):
    """Addition of two numbers"""
    return a + b

def subtract(a, b):
    """Subtraction of two numbers (a - b)"""
    return a - b

def multiply(a, b):
    """Multiplication of two numbers"""
    return a * b

def divide(a, b):
    """Division of two numbers (a / b)
    Raises ValueError if denominator is zero"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
