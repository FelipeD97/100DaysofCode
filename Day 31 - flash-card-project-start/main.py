from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
flashcards = {}
timer = None


# -------------------------- READ FLASHCARDS -------------------------- #
try:
    data = pandas.read_csv("flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("flash-card-project-start/data/spanish_words.csv")
    flashcards = original_data.to_dict(orient="records")
else:
    flashcards = data.to_dict(orient="records")

# ---------------------- CREATE/FLIP FLASHCARDS ----------------------- #


def new_card():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    window.after_cancel(timer)
    current_card = random.choice(flashcards)
    canvas.itemconfig(card_picture, image=card_front)
    canvas.itemconfig(word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(language, text="Spanish", fill="black")
    flip_timer = window.after(30000, flip_card)
    countdown(30)


def flip_card():

    canvas.itemconfig(card_picture, image=card_back)
    canvas.itemconfig(word, text=current_card["English"], fill="white")
    canvas.itemconfig(language, text="English", fill="white")


# --------------------------- SAVE PROGRESS --------------------------- #


def words_to_learn():

    flashcards.remove(current_card)
    words_to_learn = pandas.DataFrame(flashcards)
    words_to_learn.to_csv(
        "flash-card-project-start/data/words_to_learn.csv", index=False
    )
    new_card()


# --------------------------- TIMER SETUP --------------------------- #


def countdown(count):
    global timer

    if count < 10:
        timer_text.config(text=f"0{count}")

    if count > 0:
        timer = window.after(1000, countdown, count - 1)
        print(count)
    timer_text.config(text=f"{count}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Language Flashcard Practice")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(30000, flip_card)
timer = window.after(1000, countdown)

timer_text = Label(text="00", bg=BACKGROUND_COLOR, font=("ariel", 36, "bold"))
timer_text.grid(row=0, column=0, columnspan=2)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_back = PhotoImage(file="flash-card-project-start/images/card_back.png")
card_picture = canvas.create_image(400, 263, image=card_front)
# timer_text = canvas.create_text(400, 50, text="30", font=("ariel", 36, "bold"))
language = canvas.create_text(400, 150, text="", font=("ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("ariel", 60, "bold"))
canvas.grid(row=1, column=0, columnspan=2)

# BUTTONS
right_image = PhotoImage(file="flash-card-project-start/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=words_to_learn)
right_button.grid(row=2, column=1)

wrong_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=new_card)
wrong_button.grid(row=2, column=0)

new_card()

window.mainloop()
