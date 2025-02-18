import requests
import datetime as dt
import os

DOMAIN = "https://trackapi.nutritionix.com"
EXERCISE_ENDPOINT = f"{DOMAIN}/v2/natural/exercise"
SHEETY_WORKSHEET_ENDPOINT = os.environ.get("SHEETY_WORKSHEET_ENDPOINT")

SHEETY_TOKEN = os.environ.get("SHEETY_TOKEN")
NUTRITIONIX_APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
NUTRITIONIX_APP_KEY = os.environ.get("NUTRITIONIX_APP_KEY")

query = input("Tell me which exercises you did: ")

response = requests.post(
    url=EXERCISE_ENDPOINT,
    json={"query": query},
    headers={
        "Content-Type": "application/json",
        "x-app-id": NUTRITIONIX_APP_ID,
        "x-app-key": NUTRITIONIX_APP_KEY
    })

response.raise_for_status()

exercises = response.json()["exercises"]

for exercise in exercises:
    body = {
        "workout": {
            "date": dt.date.today().strftime("%Y-%m-%d"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    response = requests.post(
        url=SHEETY_WORKSHEET_ENDPOINT,
        json=body,
        headers={"Authorization": f"Bearer {SHEETY_TOKEN}"}
    )

    response.raise_for_status()
