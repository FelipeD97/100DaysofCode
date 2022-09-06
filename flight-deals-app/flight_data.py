import requests

KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
KIWI_API_KEY = "8aDhIHgnBzWFwJeSHz2v81jKr9Esvc2N"

params = {
    "fly_from": "LGA",
    "fly_to": "MIA",
    "dateFrom": "06/09/2022",
    "dateTo": "10/09/2022",
}
headers = {"apikey": KIWI_API_KEY}

response = requests.get(url=f"{KIWI_ENDPOINT}/search", params=params, headers=headers)
data = response.json()[0]
print(data)


class FlightData:
    # This class is responsible for structuring the flight data.

    pass
