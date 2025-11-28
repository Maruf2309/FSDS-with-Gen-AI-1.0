
import random

print("=== Welcome to the Number Guessing Game ===")

# Generate random number between 1 and 50
jackpot = random.randint(1, 50)
attempts = 0

while True:
    user_input = input("\nEnter your guess (1–50) or type 'exit' to quit: ")

    # Handle exit command
    if user_input.lower() == "exit":
        print("Game exited. Thanks for playing!")
        break  # stops the loop immediately

    # Skip invalid inputs
    if not user_input.isdigit():
        print("Invalid input! Please enter a number.")
        continue  # skip rest and ask again

    guess = int(user_input)
    attempts += 1

    # Compare guess with jackpot
    if guess < jackpot:
        print("Too low! Try a higher number.")
    elif guess > jackpot:
        print("Too high! Try a lower number.")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} attempts.")
        break  # end the game once correct

else:
    # This else runs only if while loop finishes normally (without break)
    pass  # Not used here, but included for example

print("\n=== Game Over ===")
