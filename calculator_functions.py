def add(a, b):
    return a + b
    # твій код — поверни суму

def subtract(a, b):
    return a - b
    # твій код — поверни різницю

def multiply(a, b):
    return a * b
    # твій код — поверни добуток

def divide(a, b):
    return a // b
    # твій код — поверни частку

print(add(10, 5))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(10, 5))

def calculate(a, b, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    else:
        return "Невідома операція"

print(calculate(5, 6, "multiply"))
print(calculate(4, 2, "subtract"))
print(calculate(6, 7))
