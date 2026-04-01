# We are going to write a program that generates a random number and asks the user to guess it.
#If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, the program prints “higher 
#number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number.
# Hint: Use the random module.

import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

guess = 0
guesses = 0

print("🎮 Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 100")

while guess != number:
    guess = int(input("Enter your guess: "))
    guesses += 1

    if guess > number:
        print("⬇️ Lower number please")
    elif guess < number:
        print("⬆️ Higher number please")
    else:
        print("🎉 Correct! You guessed the number!")
        print(f"You guessed it in {guesses} attempts.")
