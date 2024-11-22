Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Basic Calculator Program
... 
... # Ask the user to input two numbers
... num1 = float(input("Enter the first number: "))
... num2 = float(input("Enter the second number: "))
... 
... # Ask the user to input a mathematical operation
... operation = input("Enter an operation (+, -, *, /): ")
... 
... # Perform the operation based on the user's input
... if operation == "+":
...     result = num1 + num2
...     print(f"{num1} + {num2} = {result}")
... elif operation == "-":
...     result = num1 - num2
...     print(f"{num1} - {num2} = {result}")
... elif operation == "*":
...     result = num1 * num2
...     print(f"{num1} * {num2} = {result}")
... elif operation == "/":
...     if num2 != 0:
...         result = num1 / num2
...         print(f"{num1} / {num2} = {result}")
...     else:
...         print("Error: Division by zero is not allowed.")
... else:
...     print("Invalid operation! Please enter one of +, -, *, or /.")
... 
SyntaxError: multiple statements found while compiling a single statement
>>> [DEBUG ON]
>>> [DEBUG OFF]
