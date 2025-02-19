import requests

BASE_ENDPOINT = "https://api.sheety.co/********************************/flightDeals/prices"


class DataManager:

    def __init__(self, token: str):
        self.token = token

    def get_cities(self):
        response = requests.get(
            url=BASE_ENDPOINT,
            headers={"Authorization": f"Bearer {self.token}"})

        response.raise_for_status()
        cities = response.json()["prices"]
        return cities

    def edit_city_iata_code(self, object_id: int, iata_code: str):
        response = requests.put(
            url=f"{BASE_ENDPOINT}/{object_id}",
            json={
                "price": {
                    "iataCode": iata_code,
                }
            },
            headers={"Authorization": f"Bearer {self.token}"})

        response.raise_for_status()
        return response.json()
