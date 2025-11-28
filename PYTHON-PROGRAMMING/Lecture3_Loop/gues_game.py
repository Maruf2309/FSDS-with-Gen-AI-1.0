
import random

# Step 1: Generate a random number between 1 and 100
jackpot = random.randint(1, 100)

# Step 2: Initialize attempt counter
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    try:
        # Step 2: Take input from user
        guess = int(input("Enter your guess: "))
        attempts += 1

        # Step 3, 4, 5, 6: Compare and give feedback
        if guess < jackpot:
            print("Wrong! Guess a higher number.")
        elif guess > jackpot:
            print("Wrong! Guess a lower number.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts.")
            break  # exit the loop when correct guess

    except ValueError:
        print("Invalid input! Please enter an integer number between 1 and 100.")
