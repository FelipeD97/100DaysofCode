# import smtplib

# my_email = "felipedunbar37@gmail.com"
# password = "kjtlbaavdawkxrul"

# with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="felipe37d@yahoo.com",
#         msg="Subject:Hello\n\nThis is the body of my email",
#     )

# import datetime as dt

# today = dt.datetime.now()
# year = today.year
# month = today.month
# day_of_week = today.weekday()
# # print(month)

# date_of_birth = dt.datetime(year=1997, month=1, day=4)
# print(date_of_birth)

import smtplib
import datetime as dt
from random import choice

with open("Day 32/quotes.txt", "r") as file:
    quotes = file.readlines()
    quote = choice(quotes)

date = dt.datetime.now()
day_of_week = date.weekday()

my_email = "felipedunbar37@gmail.com"
password = "kjtlbaavdawkxrul"

if day_of_week == 6:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="felipe37d@yahoo.com",
            msg=f"Subject:Motivational Sunday\n\n{quote}",
        )
