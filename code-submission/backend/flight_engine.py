import json
from typing import Dict
import requests

__api_url = "https://morehouse-flight-engine-20217cf44eba.herokuapp.com/"


def get_airport_info(airport_IATA: str) -> Dict:
    """TODO(elijahtruitt): Write docs."""

    request_url = __api_url + f"airports?code={airport_IATA}"
    response = requests.get(request_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None  # Handle this outside the function.


def get_flights_on_date(date: str) -> Dict:
    """TODO(elijahtruitt): Write docs."""

    request_url = __api_url + f"flights?date={date}"
    response = requests.get(request_url)

    if response.status_code != 200:
        return None  # TODO(elijahtruitt): Maybe handle this better?

    # Transform into dict that can be refrenced easily.
    result = {}
    for flight in response.json():
        result[flight["flightNumber"]] = flight
    return result


def find_flight_info(flight_number: str, flight_date: str):
    """TODO(elijahtruitt): Write docs."""

    flight_db = get_flights_on_date(flight_date)
    if flight_number not in flight_db:
        return None  # TODO(elijahtruitt): Maybe handle this better?

    flight_info = flight_db[flight_number]
    return flight_info


# print(get_flights_on_date("2023-11-05"))
# find_flight_info("5268", "2023-11-05")
