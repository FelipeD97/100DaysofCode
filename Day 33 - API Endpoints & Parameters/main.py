import requests
from datetime import datetime

MY_LAT = 33.924129
MY_LONG = -84.379097

# response = requests.get("http://api.open-notify.org/iss-now.json")
# # if response.status_code == 404:
# #     raise Exception("That resource does not exist.")
# # elif response.status_code == 401:
# #     raise Exception("You are not authorized to access this data"
# response.raise_for_status()

# data = response.json()

# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {"lat": MY_LAT, "long": MY_LONG, "formatted": 0}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])


time_now = datetime.now()
print(time_now.hour)
