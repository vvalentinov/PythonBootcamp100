import requests


class FlightSearch:

    def __init__(self, api_key: str, api_secret: str):
        self.api_key = api_key
        self.api_secret = api_secret
        self.token = self.generate_token()

    def generate_token(self):
        response = requests.post(
            url="https://test.api.amadeus.com/v1/security/oauth2/token",
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            json={
                "grant_type": "client_credentials",
                "client_id": self.api_key,
                "client_secret": self.api_secret
            })

        response.raise_for_status()

        token = response.json()["access_token"]
        token_expiration = response.json()["expires_in"]

        print(f"Your new generated token is {token}")
        print(f"Your token expires in {token_expiration} seconds")
        return token

    def get_city_iata_code(self, city_name: str):
        response = requests.get(
            url="https://test.api.amadeus.com/v1/reference-data/locations/cities",
            params={"keyword": city_name},
            headers={"Authorization": f"Bearer {self.token}"})

        response.raise_for_status()

        city_iata_code = response.json()["data"][0]["iataCode"]
        return city_iata_code

    def search_for_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        response = requests.get(
            url="https://test.api.amadeus.com/v2/shopping/flight-offers",
            headers={"Authorization": f"Bearer {self.token}"},
            params={
                "originLocationCode": origin_city_code,
                "destinationLocationCode": destination_city_code,
                "departureDate": from_time.strftime("%Y-%m-%d"),
                "returnDate": to_time.strftime("%Y-%m-%d"),
                "adults": 1,
                "nonStop": "true",
                "currencyCode": "GBP",
                "max": "10",
            }
        )

        response.raise_for_status()
        flights_data = response.json()
        return flights_data
