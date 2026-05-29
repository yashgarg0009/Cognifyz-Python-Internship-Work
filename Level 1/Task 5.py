# Task: Palindrome Checker
# Write a Python function that checks whether
# a given string is a palindrome. A palindrome
# is a word, phrase, or sequence that reads the
# same backward as forward (e.g., "madam" or "racecar").

word = input("Enter a word: ")

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")