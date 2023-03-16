# Define function for addition
def add(num1, num2):
    return num1 + num2

# Define function for subtraction
def subtract(num1, num2):
    return num1 - num2

# Define function for multiplication
def multiply(num1, num2):
    return num1 * num2

# Define function for division
def divide(num1, num2):
    return num1 / num2

# Get user input for numbers and operation
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

# Perform calculation based on user input
if operation == '+':
    print(num1, "+", num2, "=", add(num1, num2))
elif operation == '-':
    print(num1, "-", num2, "=", subtract(num1, num2))
elif operation == '*':
    print(num1, "*", num2, "=", multiply(num1, num2))
elif operation == '/':
    print(num1, "/", num2, "=", divide(num1, num2))
else:
    print("Invalid operation")
