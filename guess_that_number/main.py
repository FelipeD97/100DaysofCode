# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from logo import logo


def pick_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    turns = 0
    if difficulty == "easy":
        turns = 10
        return turns
    elif difficulty == "hard":
        turns = 5
        return turns


def get_guess():
    make_guess = int(input("Make a guess: "))

    return make_guess


print(logo)
print("Welcome to Guess That Number!\nI'm thinking of a number between 1 and 100.")
number = random.randint(1, 100)

available_turns = pick_difficulty()
is_active = True

while is_active:

    if available_turns == 0:
        print("You've run out of guesses. You lose.")
        is_active = False

    print(f"You have {available_turns} attempts remaining to guess the number.")
    guess = get_guess()

    if guess > number:
        print("Too high\nGuess Again.")
        available_turns -= 1
    elif guess < number:
        print("Too low.\nGuess Again.")
        available_turns -= 1
    else:
        print(f"That's it! My number was {number}.")
        is_active = False
