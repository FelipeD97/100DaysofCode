import requests
from datetime import datetime
import smtplib
import time


MY_EMAIL = "felipedunbar37@gmail.com"
PASSWORD = "kjtlbaavdawkxrul"

MY_LAT = 33.906323  # Your latitude
MY_LONG = -84.368829  # Your longitude


def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if (MY_LAT - 5) <= iss_latitude <= (MY_LAT + 5) and (
        MY_LONG - 5
    ) <= iss_longitude <= (MY_LAT - 5):
        return True


# Your position is within +5 or -5 degrees of the ISS position.


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now < sunrise and time_now > sunset:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if iss_overhead and is_dark:
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="felipe37d@yahoo.com",
                msg=f"Subject:Look Up👆🏾\n\n The ISS is above you in the sky.",
            )
