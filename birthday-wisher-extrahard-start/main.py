##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import smtplib
import datetime as dt
from random import choice
import pandas

MY_EMAIL = "felipedunbar37@gmail.com"
PASSWORD = "kjtlbaavdawkxrul"

data = pandas.read_csv("birthday-wisher-extrahard-start/birthdays.csv")

birthdays_dict = {
    (data_row["month"], data_row["day"]): data_row
    for (index, data_row) in data.iterrows()
}

today = dt.datetime.now()
today_tuple = (today.month, today.day)

for birthday, data in birthdays_dict.items():
    if birthday == today_tuple:
        letters = []

        with open(
            "birthday-wisher-extrahard-start/letter_templates/letter_1.txt"
        ) as data_1:
            letter1 = data_1.read()
            letters.append(letter1)
        with open(
            "birthday-wisher-extrahard-start/letter_templates/letter_2.txt"
        ) as data_2:
            letter2 = data_2.read()
            letters.append(letter2)
        with open(
            "birthday-wisher-extrahard-start/letter_templates/letter_3.txt"
        ) as data_3:
            letter3 = data_3.read()
            letters.append(letter3)

        letter = choice(letters)
        email = letter.replace("[NAME]", data["name"])

        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=data["email"],
                msg=f"Subject:Happy Birthday\n\n{email}",
            )
