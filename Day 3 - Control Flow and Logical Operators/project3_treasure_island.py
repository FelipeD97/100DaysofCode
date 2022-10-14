print(
    """
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                               
"""
)


print("Welcome to Treasure Island\nYou're mission is to find the treasure.")

choice1 = input(
    'You\'re at a crossroad, where do you want to go? Type "left" or "right".'
).lower()

if choice1 == "left":

    choice2 = input(
        'You\'ve approached a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across'
    ).lower()

    if choice2 == "wait":

        choice3 = input(
            'You\'ve arrive at the island. Out of nowhere 3 mysterious doors appear. One red, one blue and one yellow. Which door would you like to enter to find the treasure? "Red", "Blue" or "Yellow"?'
        ).lower()

        if choice3 == "red":
            print(
                "Oh no! This door led to a fire. You've been burned alive! Game Over!"
            )
        elif choice3 == "blue":
            print(
                "Oh no! This door led to a cave of beasts. You've been eaten alive! Game Over!"
            )
        elif choice3 == "yellow":
            print("Yay! You've found the treasure! You Win!")
        else:
            print("You chose a door that did not exist. Game Over!!")
    else:
        print("Oh no! You were attacked by a shark when you tried to swim. Game Over!")

else:
    print("Oh no! You fell into a hole. Game Over!")
