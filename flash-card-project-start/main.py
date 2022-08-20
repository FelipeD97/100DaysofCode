from tkinter import *


BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Language Flashcard Practice")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="flash-card-project-start/images/card_front.png")
card_picture = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400, 150, text="Language", font=("ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# BUTTONS
right_image = PhotoImage(file="flash-card-project-start/images/right.png")
right_button = Button(image=right_image, highlightthickness=0)
right_button.grid(row=1, column=1)
wrong_image = PhotoImage(file="flash-card-project-start/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0)
wrong_button.grid(row=1, column=0)

window.mainloop()
