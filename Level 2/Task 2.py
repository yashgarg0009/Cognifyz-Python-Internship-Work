# Task: Number Guesser
# Create a number guessing game where the
# program generates a random number
# between a specified range, and the user tries
# to guess it. Provide feedback to the user if
# their guess is too high or too low.

import random

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

number = random.randint(start, end)

while True:
    guess = int(input("Enter your guess: "))

    if guess > number:
        print("Too High!")

    elif guess < number:
        print("Too Low!")

    else:
        print("Congratulations! You guessed the correct number.")
        break