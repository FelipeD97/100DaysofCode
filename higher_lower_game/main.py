import random
from os import name, system

from game_data import populations_2020
from logos import title, vs


# Create a function to randomly select a key,value pair from population data
def random_country(populations):
    country_info = random.choice(populations)
    return country_info


# Create a function that checks user guess against answer
def check_answer(guess, pop_a, pop_b):
    if pop_a > pop_b:
        return guess == "A"
    else:
        return guess == "B"

# Create a function to clear the console
def clear():

    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

score = 0
is_active = True
country2 = random.choice(populations_2020)

while is_active:
    country1 = country2
    country2 = random_country(populations_2020)
    
    if country1 == country2:
        country2 = random_country(populations_2020)

    print(title)
    print(f"Compare A: {country1['Name']}")
    print(vs)
    print(f"Against B: {country2['Name']}\n")

    guess = input("Which country has the highest population? Type 'A' or 'B': ").upper()
    is_correct = check_answer(guess, country1["Population"], country2["Population"])

    if is_correct:
        score += 1
        print(f"You're right!\nCurrent score: {score}\n")
        clear()
    else:
        clear()
        print(title)
        print(f"Sorry that's wrong.\nFinal score: {score}\n")
        is_active = False
