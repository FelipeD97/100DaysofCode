print("Welcome to the tip calculator")

bill = float(input("What is the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_people = float(input("How many people to split the bill? "))

tip_amount = bill * (tip / 100)
total_bill = bill + tip_amount

split_bill = total_bill / number_people
split_bill_rounded = round(split_bill, 2)
split_bill_rounded = "{:.2f}".format(split_bill)

print(f"Each person should pay: ${split_bill_rounded}")
