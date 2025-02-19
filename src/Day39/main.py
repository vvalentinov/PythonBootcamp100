from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager
from dotenv import load_dotenv
import os
import datetime as dt

load_dotenv()

sheety_api_token = os.getenv("SHEETY_API_TOKEN")
flight_search_api_key = os.getenv("FLIGHT_SEARCH_API_KEY")
flight_search_api_secret = os.getenv("FLIGHT_SEARCH_API_SECRET")
twilio_sid = os.getenv("TWILIO_SID")
twilio_token = os.getenv("TWILIO_TOKEN")

data_manager = DataManager(sheety_api_token)
flight_search = FlightSearch(flight_search_api_key, flight_search_api_secret)
notification_manager = NotificationManager(twilio_sid, twilio_token)

now = dt.datetime.now()
tomorrow = now + dt.timedelta(days=1)
six_month_from_now = now + dt.timedelta(days=(6 * 30))

cities = data_manager.get_cities()

for city_entry in cities:
    sheet_city_id = city_entry["id"]
    sheet_city_name = city_entry["city"]
    sheet_city_iata_code = city_entry["iataCode"]
    sheet_city_lowest_price = city_entry["lowestPrice"]

    if sheet_city_iata_code == "":
        city_iata_code = flight_search.get_city_iata_code(sheet_city_name)
        data_manager.edit_city_iata_code(object_id=sheet_city_id, iata_code=city_iata_code)

    flights = flight_search.search_for_flights(
        origin_city_code="LON",
        destination_city_code=sheet_city_iata_code,
        from_time=tomorrow,
        to_time=six_month_from_now
    )

    cheapest_flight = find_cheapest_flight(flights)
    if cheapest_flight.price != "N/A":
        print(f"{sheet_city_name}: £{cheapest_flight.price}")
        notification_manager.send_sms(
            message_body=f"Low price alert! Only £{cheapest_flight.price} to fly "
                         f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                         f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}.",
            from_number="Some Number Here...",
            to_number="Some Number Here..."
        )
