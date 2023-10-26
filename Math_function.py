# Additon function
def add(a, b):
    return a + b

# Multiplication function
def multiply(a, b):
    return a * b

# Division function (including handling division by zero)
def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed")
    return a / b
