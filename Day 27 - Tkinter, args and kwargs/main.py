from tkinter import *

# Create a window
window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
# Adding padding/space around program. Can be added to individual components
window.config(padx=200, pady=200)

# Label (Component)
my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
# my_label.pack()
# Place is very specific
# my_label.place(x=100, y=150)

my_label.grid(column=0, row=0)

my_label.config(text="New Text")

# Button
def button_clicked():
    print("I got clicked")
    # Gets text entered in entry and saves it as variable
    new_text = input.get()
    my_label["text"] = new_text


# calls to action() when pressed
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

new_button = Button(text="You can click me too!", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input = Entry(width=30)
# Inserts default text in entry
input.insert(END, string="Some text to begin with.")
# input.pack()
input.grid(column=3, row=2)

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox
text.focus()
# Adds some text to begin with
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
# text.pack()

# Spinbox
def spinbox_used():
    # gets the current value in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()

# Scale
# Called with current scale value
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=10, command=scale_used)
# scale.pack()

# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on
checked_state = IntVar()
checkbutton = Checkbutton(
    text="Is On?", variable=checked_state, command=checkbutton_used
)
checked_state.get()
# checkbutton.pack()

# Radiobutton
def radiobutton_used():
    print(radio_state.get())


radio_state = IntVar()
radiobutton1 = Radiobutton(
    text="Option 1", value=1, variable=radio_state, command=radiobutton_used
)
radiobutton2 = Radiobutton(
    text="Option 2", value=2, variable=radio_state, command=radiobutton_used
)
radio_state.get()
# radiobutton1.pack()
# radiobutton2.pack()

# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
names = ["felipe", "Carlos", "Maria"]
for item in names:
    listbox.insert(names.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

# Menu Button

menu = Menubutton(direction="below", menu=names)
# menu.pack()

# import turtle

# felipe = turtle.Turtle
# felipe.write()


window.mainloop()
