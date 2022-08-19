from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
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

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letters = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)
    new_password = "".join(password_list)
    password_entry.insert(END, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please don't leave any fields blank!"
        )
    else:
        try:
            with open("password-manager-start/data.json", mode="r") as file:
                # Reading the old data
                data = json.load(file)
        except FileNotFoundError:
            with open("password-manager-start/data.json", mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("password-manager-start/data.json", mode="w") as file:
                # Saving updated data
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD DATA ------------------------------- #


def search():
    website = website_entry.get()
    try:
        with open("password-manager-start/data.json", mode="r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(
            title="Error", message="No current list of passwords. Please add password."
        )
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(
                title=website, message=f"email: {email} \npassword: {password}"
            )
        else:
            messagebox.showerror(
                title="Error",
                message=f"{website} does not exist in password manager. Please enter a valid website.",
            )


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_image = PhotoImage(file="password-manager-start/logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:", font=("Courier", 16))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", font=("Courier", 16))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", font=("Courier", 16))
password_label.grid(row=3, column=0)

# Entrys
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

email_entry = Entry(width=35)
email_entry.insert(END, "felipe.a.dunbar@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=12, command=search)
search_button.grid(row=1, column=2)

window.mainloop()
