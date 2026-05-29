# Task: Guessing Game
# Write a Python program that generates a
# random number between 1 and 100. The
# user should then try to guess the number.
# The program should provide hints such as
# "too high" or "too low" until the correct
# number is guessed.

import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number (1-100): "))

    if guess > number:
        print("Too High!")

    elif guess < number:
        print("Too Low!")

    else:
        print("Congratulations! You guessed the correct number.")
        break