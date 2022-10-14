############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
suits = ["Hearts", "Clubs", "Spades", "Diamonds"]

computer_cards = []
user_cards = []


def deal_card(list_of_cards):
    card = list_of_cards[random.randint(0, len(cards) - 1)]

    return card


def calculate_score(dealt_cards):

    for card in dealt_cards:
        if card == 11 and sum(dealt_cards) > 21:
            dealt_cards.remove(card)
            dealt_cards.append(1)

    score = sum(dealt_cards)

    if score == 21:
        score = 0

    return score


is_active = True

computer_cards.append(deal_card(cards))
computer_cards.append(deal_card(cards))
user_cards.append(deal_card(cards))
user_cards.append(deal_card(cards))

print(computer_cards, user_cards)

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

if computer_score == 0 or computer_score > 21:
    is_active = False
elif user_score == 0 or user_score > 21:
    is_active = False

if input("Draw another card? Type 'y' for yes & 'n' for no: ") == "y":
    user_cards.append(deal_card(cards))

print(calculate_score(computer_cards))
print(computer_cards)
print(calculate_score(user_cards))
print(user_cards)


# Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

# Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

# Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

# Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

# Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
