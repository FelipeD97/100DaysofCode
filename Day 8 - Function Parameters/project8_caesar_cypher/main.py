from art import logo

alphabet = [
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


def caesar(cipher_direction, start_text, shift_amount):
    end_text = ""

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"The {cipher_direction}d text is {end_text}")

print(logo)

is_active = True

while is_active:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26
    
    caesar(direction, text, shift)

    play_again = input("Would you like to restart the cipher program? Type 'yes' if you want to go again. Otherwise type 'no'.\n")

    if play_again == "no":
        is_active = False
    else:
        is_active



# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)

#         new_position = position + shift_amount

#         cipher_text += alphabet[new_position]
#     print(f"The encoded text is {cipher_text}")


# def decrypt(cipher_text, shift_amount):

#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)

#         new_position = position - shift_amount

#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")


# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)
# else:
#     print("Not an option.")
