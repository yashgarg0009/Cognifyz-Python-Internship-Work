# Task: String Reversal
# Create a Python function that takes a string as input
# and returns the reverse of that string.
# For example, if the input is "hello",
# the function should return "olleh".

def reverse_string(text):
    return text[::-1]

user_input = input("Enter a string: ")
print("Reversed string:", reverse_string(user_input))