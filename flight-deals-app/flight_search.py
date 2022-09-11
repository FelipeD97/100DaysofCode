import requests
from pprint import pprint
from flight_data import FlightData
from dotenv import load_dotenv
import os

load_dotenv()

KIWI_ENDPOINT = os.environ["KIWI_ENDPOINT"]
KIWI_API_KEY = os.environ["KIWI_API_KEY"]


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def get_destination_code(self, city_name):

        flight_header = {"apikey": KIWI_API_KEY}
        query = {"term": city_name, "location_types": "city"}

        response = requests.get(
            url=f"{KIWI_ENDPOINT}/locations/query", params=query, headers=flight_header
        )
        data = response.json()["locations"]
        code = data[0]["code"]

        return code

    def search_flights(self, fromCityCode, toCityCode, fromTime, toTime):

        params = {
            "fly_from": fromCityCode,
            "fly_to": toCityCode,
            "dateFrom": fromTime.strftime("%d/%m/%Y"),
            "dateTo": toTime.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "usd",
        }

        headers = {"apikey": KIWI_API_KEY}

        response = requests.get(
            url=f"{KIWI_ENDPOINT}/search", params=params, headers=headers
        )
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights for {toCityCode}")
            return None
        # pprint(f"{city}: {data[0]['price']}")
        flight_data = FlightData(
            cityFrom=data["route"][0]["cityFrom"],
            cityTo=data["route"][0]["cityTo"],
            nightsInDest=data["nightsInDest"],
            price=data["price"],
        )
        print(f"{flight_data.cityTo}: ${flight_data.price}")
        return flight_data
