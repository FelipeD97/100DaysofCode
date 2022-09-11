from pprint import pprint
from dotenv import load_dotenv
import os
import requests

load_dotenv()

sheet_endpoint = os.environ["SHEET_ENDPOINT"]

# pprint(requests.get(sheet_endpoint))


class DataManager:
    # * This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.destination_data = {}

    # ?
    def get_destination_data(self):
        response = requests.get(sheet_endpoint)
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id  from sheet_data to update the Google Sheet with the IATA codes. (Do this using code). HINT: Remember to check the checkbox to allow PUT requests in Sheety.
    def update_destination_codes(self):

        for city in self.destination_data:
            new_data = {"price": {"iataCode": city["iataCode"]}}
            response = requests.put(url=f"{sheet_endpoint}/{city['id']}", json=new_data)
            # print(response.text)
