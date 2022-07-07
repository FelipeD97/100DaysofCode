import random
from hangman_stages import stages
from hangman_words import word_list


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
game_over = False
lives = len(stages) - 1

print(lives)
print(chosen_word)

for letter in chosen_word:
    display.append("_")

while not game_over:

    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
    print(f"{''.join(display)}")

    if guess not in chosen_word:
        lives -= 1
        print(f"Sorry! {guess} is not in this word.")

        if lives == 0:
            game_over = True
            print("Game Over!")

    if "_" not in display:
        game_over = True
        print("You Win!")

    print(stages[lives])
