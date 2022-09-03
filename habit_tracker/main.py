from email import header
from heapq import heappush
import requests
from datetime import datetime as dt

USERNAME = "fdunbar"
TOKEN = "fbdt44ef4q296jfg"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Coding Tracker",
    "unit": "min",
    "type": "int",
    "color": "momiji",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

add_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
today = dt.today()
formatted_today = today.strftime("%Y%m%d")

pixel_data = {
    "date": formatted_today,
    "quantity": input("How many minutes did you code? "),
}

response = requests.post(url=add_pixel_endpoint, json=pixel_data, headers=headers)

update_endpoint = f"{add_pixel_endpoint}/{formatted_today}"

new_pixel_data = {"quantity": "240"}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

delete_endpoint = f"{add_pixel_endpoint}/{formatted_today}"

# response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
