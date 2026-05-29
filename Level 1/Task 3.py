# Task: Email Validator
# Develop a Python function that validates
# whether a given string is a valid email
# address. Implement checks for the format,
# including the presence of an "@" symbol and
# a domain name.

email = input("Enter an email address: ")

if "@" in email and "." in email:
    print("Valid Email Address")
else:
    print("Invalid Email Address")