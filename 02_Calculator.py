"""
Simple CLI Calculator with History
Author: Aniket M. Warghat
Description: A modular calculator that performs basic arithmetic operations 
and maintains a log of session calculations.
"""

# --- Arithmetic Functions ---

def add(x, y):
    """Returns the sum of two numbers."""
    return x + y

def subtract(x, y):
    """Returns the difference of two numbers."""
    return x - y

def multiply(x, y):
    """Returns the product of two numbers."""
    return x * y

def divide(x, y):
    """
    Returns the quotient of two numbers.
    Includes a safety check for division by zero.
    """
    if y == 0:
        return "Error: Division by zero is undefined."
    else:
        return x / y

# --- Main Program ---

history = []  # List to store calculation strings for session logging

while True:
    print("\n" + "-"*13 + " Simple Calculator " + "-"*13)
    print("1. Add | 2. Subtract | 3. Multiply | 4. Divide | 5. History | 6. Exit")

    op = input("Enter Option (1-6): ")

    try:
        op = int(op)

        # Operations 1-4: Basic Math
        if 1 <= op <= 4:
            num1 = float(input("Enter Num1: "))
            num2 = float(input("Enter Num2: "))

            if op == 1:
                result = add(num1, num2)
                output = f"{num1} + {num2} = {result}"
            elif op == 2:
                result = subtract(num1, num2)
                output = f"{num1} - {num2} = {result}"
            elif op == 3:
                result = multiply(num1, num2)
                output = f"{num1} * {num2} = {result}"
            elif op == 4:
                result = divide(num1, num2)
                output = f"{num1} / {num2} = {result}"

            print(f"Result: {result}")
            
            # Only log to history if it wasn't a division error string
            if isinstance(result, (int, float)):
                history.append(output)

        # Operation 5: Display Logged History
        elif op == 5:
            if not history:
                print("No calculations yet!")
            else:
                print("\n------ Calculation History ------")
                for index, item in enumerate(history, 1):
                    print(f"{index}. {item}")

        # Operation 6: Terminate Program
        elif op == 6:
            print("Exiting Program... Goodbye!")
            break 

        else:
            print(f"'{op}' is not a valid menu option.")

    except ValueError:
        # Catches cases where input is not a number
        print(f"Input Error: Please enter a valid numerical value.")