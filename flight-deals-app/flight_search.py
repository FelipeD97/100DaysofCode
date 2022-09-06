import requests

KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
KIWI_API_KEY = "8aDhIHgnBzWFwJeSHz2v81jKr9Esvc2N"


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



# flight_parameters = {
#     "date_from": "09/09/2022",
#     "date_to": "16/09/2022",
#     "fly_from": "SFO",
#     "fly_to": "LAX",
# }


# response = requests.get(
#     url=kiwi_endpoint, json=flight_parameters, headers=flight_header
# )
# print(response.text)
