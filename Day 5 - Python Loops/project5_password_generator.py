import random

print("Welcome to the PyPassword Generator")

number_of_letters = int(input("How many letters would you like in your password? "))
number_of_symbols = int(input("How many symbols? "))
number_of_numbers = int(input("How many numbers? "))

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
symbols = ["!", "@", "#", "$", "%", "&", "*", "(", ")", "/", "?", "{"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

password = []

random.shuffle(letters)
random.shuffle(symbols)
random.shuffle(numbers)


for x in range(0, number_of_letters):
    password.append(letters[x])

for x in range(0, number_of_symbols):
    password.append(symbols[x])

for x in range(0, number_of_numbers):
    password.append(numbers[x])

random.shuffle(password)

new_password = ""

for x in password:
    new_password += x

print(f"Your password is: {new_password}")
