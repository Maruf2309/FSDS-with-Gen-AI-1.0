
# Project: 
#1 Generate a randome number(1-100)
#2 Take an input from user - Guess the number
#3 Compare / match the number
#4 if the guess number > generated number then give a message to user guess a lower number
#5 if the guess number < generated number then give a message to user guess a higher number
#6 the guess number = generated number then give a message correct guess


import random  # in buit , so no need use !pip install

jackport = random.randint(1, 100)  # range  (randint is a fuction who take random number from a range)

# user input
guess_number = int(input("Enter your guess number: "))

# print(jackport)

while guess_number !=jackport: # Runs untill guess it matched

    if guess_number < jackport:
        print("Wrong! Guess Higher Number")

    else:
        print("Wrong! Guess lower Number")

    guess_number = int(input("Enter your guess number: "))
    counter +=1
else:
    print("correct guess")
    print("Your attempt is: ", counter)
   

# break hochhe, so uing loop

