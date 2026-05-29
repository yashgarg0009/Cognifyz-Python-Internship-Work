# Task: Fibonacci Sequence
# Write a Python function that generates the
# Fibonacci sequence up to a given number of
# terms. The function should take an integer
# input from the user and display the
# Fibonacci sequence up to that number of
# terms.

n = int(input("Enter the number of terms: "))

a = 0
b = 1

print("Fibonacci Sequence:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c