import requests
from twilio.rest import Client
import os

ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
ACCOUNT_SID = os.environ.get("ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN")

params = {
    "lat": "44.057652",
    "lon": "17.197929",
    "appid": os.environ["OWM_API_KEY"],
    "cnt": 4
}

response = requests.get(url=ENDPOINT, params=params)
response.raise_for_status()

data = response.json()

rain = False

for entity in data["list"]:
    code = entity["weather"][0]["id"]
    if int(code) < 700:
        rain = True
        break

if rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It is going to rain today. Don't forget to bring an umbrella!☔",
        from_="some number here",
        to="some number here",
    )
    print(message.status)
