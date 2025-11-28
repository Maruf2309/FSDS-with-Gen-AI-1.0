
# 🎯 Smart Number Guessing Game (with hints)

import random

print("=== 🎮 Welcome to the Smart Number Guessing Game ===")
print("I'm thinking of a number between 1 and 100. Try to guess it!")

# Step 1: Generate a random number
jackpot = random.randint(1, 100)
attempts = 0
hint_counter = 0

# Step 2: Run until correct guess or exit
while True:
    user_input = input("\nEnter your guess (1–100) or type 'exit' to quit: ")

    # Exit condition
    if user_input.lower() == "exit":
        print("Game exited. Better luck next time!")
        break

    # Skip invalid input (not an integer)
    if not user_input.isdigit():
        print("❌ Invalid input! Please enter a valid number.")
        continue

    # Convert to integer
    guess = int(user_input)
    attempts += 1
    hint_counter += 1

    # Step 3: Compare guess with jackpot
    if guess < jackpot:
        print("📉 Too low! Try a higher number.")
    elif guess > jackpot:
        print("📈 Too high! Try a lower number.")
    else:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
        break  # Stop the loop when guessed correctly

    # Step 4: Give hint every 3 wrong guesses
    if hint_counter == 3:
        lower_hint = max(1, jackpot - random.randint(5, 15))
        upper_hint = min(100, jackpot + random.randint(5, 15))
        print(f"💡 Hint: The number is between {lower_hint} and {upper_hint}.")
        hint_counter = 0  # reset after giving hint

else:
    # This would only execute if the loop ends naturally (not via 'break')
    pass

print("\n=== 🏁 Game Over ===")
