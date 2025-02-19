class FlightData:

    def __init__(
            self,
            price,
            origin_airport,
            destination_airport,
            out_date,
            return_date,
            stops
    ):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date
        self.stops = stops


def find_cheapest_flight(flights):
    if flights is None or not flights["data"]:
        print("No flight data available!")
        return FlightData(
            price="N/A",
            origin_airport="N/A",
            destination_airport="N/A",
            out_date="N/A",
            return_date="N/A",
            stops="N/A"
        )

    cheapest_flight_id_and_price = {
        "id": flights["data"][0]["id"],
        "price": float(flights["data"][0]["price"]["grandTotal"]),
        "number_stops": len(flights["data"][0]["itineraries"][0]["segments"]) - 1
    }

    for entry in flights["data"][1:]:
        current_flight_price = float(entry["price"]["grandTotal"])
        current_lowest_flight_price = cheapest_flight_id_and_price["price"]
        if current_flight_price < current_lowest_flight_price:
            cheapest_flight_id_and_price["id"] = entry["id"]
            cheapest_flight_id_and_price["price"] = current_flight_price
            cheapest_flight_id_and_price["number_stops"] = len(entry["itineraries"][0]["segments"]) - 1

    result_cheapest_flight = next(
        (flight for flight in flights["data"] if flight["id"] == cheapest_flight_id_and_price["id"]), None)

    cheapest_flight = FlightData(
        price=result_cheapest_flight["price"]["grandTotal"],
        origin_airport=result_cheapest_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"],
        destination_airport=result_cheapest_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"],
        out_date=result_cheapest_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0],
        return_date=result_cheapest_flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0],
        stops=len(result_cheapest_flight["itineraries"][0]["segments"]) - 1
    )

    return cheapest_flight
