import requests

CITIES_ENDPOINT = "https://api.sheety.co/********************************/flightDeals/prices"
USERS_ENDPOINT = "https://api.sheety.co/********************************/flightDeals/users"


class DataManager:

    def __init__(self, token: str):
        self.token = token
        self.destination_data = {}
        self.customer_data = {}

    def get_cities(self):
        response = requests.get(
            url=CITIES_ENDPOINT,
            headers={"Authorization": f"Bearer {self.token}"}
        )

        response.raise_for_status()
        cities = response.json()["prices"]
        return cities

    def edit_city_iata_code(self, object_id: int, iata_code: str):
        response = requests.put(
            url=f"{CITIES_ENDPOINT}/{object_id}",
            json={
                "price": {
                    "iataCode": iata_code,
                }
            },
            headers={"Authorization": f"Bearer {self.token}"}
        )

        response.raise_for_status()
        return response.json()

    def get_users_emails(self):
        response = requests.get(url=USERS_ENDPOINT)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
