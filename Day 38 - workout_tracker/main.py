import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

GOOGLE_API_KEY = "8cf56c56b85ce29f4a9482e9ad42e01d"

GENDER = "male"
WEIGHT_KG = 73.93
HEIGHT_CM = 182.88
AGE = 25

sheety_endpoint = os.environ["SHEET_ENDPOINT"]
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercise you did: ")
exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}
exercise_headers = {"x-app-key": API_KEY, "x-app-id": APP_ID}

response = requests.post(
    url=exercise_endpoint, json=exercise_params, headers=exercise_headers
)
result = response.json()

date = datetime.now().strftime("%m/%d/%Y")
time = datetime.now().strftime("%I:%M")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheet_headers = {"Authorization": f"Basic {os.environ['TOKEN']}"}
sheety_response = requests.post(
    url=sheety_endpoint, json=sheet_inputs, headers=sheet_headers
)

# sheety_response = requests.delete(
#     url=f"{sheety_endpoint}/2", json=sheet_inputs, headers=sheet_headers
# )
print(sheety_response.text)
