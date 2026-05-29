# Task: Password Strength Checker
# Create a Python function that evaluates
# the strength of a password entered by the
# user. Implement checks for factors such as
# length, presence of uppercase and
# lowercase letters, digits, and special
# characters.

password = input("Enter a password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    else:
        has_special = True

if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong Password")
else:
    print("Weak Password")