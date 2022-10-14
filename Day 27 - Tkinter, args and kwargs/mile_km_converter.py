from tkinter import *

window = Tk()
window.title("Mile to km Converter")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

# Miles input
mile_entry = Entry(width=10)
mile_entry.grid(column=1, row=0)

# Miles label
miles_label = Label(text="Miles", font=("Arial", 18, "bold"))
miles_label.grid(column=2, row=0)

# is equal to label
equal_label = Label(text="is equal to", font=("Arial", 18, "bold"))
equal_label.grid(column=0, row=1)

# Calculated km label
def mile_converter():
    miles = mile_entry.get()
    km = int(miles) * 1.609
    return km


total_km = Label(text="0", font=("Arial", 16, "bold"))
total_km.grid(column=1, row=1)

# Km label
km_label = Label(text="Km", font=("Arial", 18, "bold"))
km_label.grid(column=2, row=1)

# Calculate button
def button_clicked():
    converted_miles = mile_converter()
    total_km["text"] = str(converted_miles)


button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()
