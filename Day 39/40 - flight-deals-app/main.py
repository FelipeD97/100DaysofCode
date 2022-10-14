# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_manager import UserManager
from datetime import datetime, timedelta


data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager()
user_manager = UserManager()

ORIGIN_CITY_IATA = "ATL"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.search_flights(
        ORIGIN_CITY_IATA, destination["iataCode"], tomorrow, six_month_from_today
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        notification_manager.send_text(
            message=f"Low price alert! Only ${flight.price} to fly from {flight.cityFrom} to {flight.cityTo}"
        )
user_manager.create_user()
