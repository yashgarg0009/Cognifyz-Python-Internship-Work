# Task: Calculator Program
# Create a Python program that acts as a basic
# calculator. It should prompt the user to
# enter two numbers and an operator (+, -, *, /, %),
# and then display the result of the operation.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, %): ")

if operator == "+":
    print("Result =", num1 + num2)

elif operator == "-":
    print("Result =", num1 - num2)

elif operator == "*":
    print("Result =", num1 * num2)

elif operator == "/":
    if num2 != 0:
        print("Result =", num1 / num2)
    else:
        print("Cannot divide by zero")

elif operator == "%":
    print("Result =", num1 % num2)

else:
    print("Invalid operator")