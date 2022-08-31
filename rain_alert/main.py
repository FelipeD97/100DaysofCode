import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall?"
api_key = "701f61902e80d23ead3b68287a9f0a1b"

account_sid = "AC2a0f33734f055850b5c78c41ad28af23"
auth_token = "45d2cc80eca47395c3849a3a549d7372"

weather_parameters = {
    "lat": 26.549,
    "lon": 83.979,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)
will_rain = False

for hour_data in weather_data["hourly"][:12]:
    condition_data = hour_data["weather"][0]["id"]
    if condition_data < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain today. Bring an umbrella. ☔️",
        from_="+12399778103",
        to="+12144058076",
    )
