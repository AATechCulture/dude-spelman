import json
from typing import Dict
import requests

api_url = "https://morehouse-flight-engine-20217cf44eba.herokuapp.com/"


def get_airport_info(airport_IATA: str) -> Dict:
    """TODO(elijahtruitt): Write docs.
    """

    request_url = api_url + f"airports?code={airport_IATA}"
    response = requests.get(request_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None  # Handle this outside the function.


def get_flights_on_date(date: str) -> Dict:
    """TODO(elijahtruitt): Write docs.
    """

    request_url = api_url + f"flights?date={date}"
    response = requests.get(request_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None  # Handle this outside the function.


print(get_flights_on_date("2024-11-05"))
