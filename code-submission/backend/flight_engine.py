import json
from typing import Dict
import requests

__api_url = "https://morehouse-flight-engine-20217cf44eba.herokuapp.com/"


def get_airport_info(airport_IATA: str) -> Dict:
    """Get airport information from the given IATA.

    This function calls the AA Flight Engine to retrieve relevant data about
    any airport AA is in service with. These airports are referenced using
    their IATA codes (e.g. DFW), and the resulting information includes things
    like the airport's coordinates, and name.

    Input:
      airport_IATA (str): A three letter airport code (ATL, DFW, SFO).
    
    Returns:
      A JSON object with information about the requested airport.
    """

    request_url = __api_url + f"airports?code={airport_IATA}"
    response = requests.get(request_url)

    if response.status_code == 200:
        return response.json()
    else:
        return None  # Handle this outside the function.


def get_flights_on_date(date: str) -> Dict:
    """Returns all American Airlines flights on a specific date.

    This function constructs a dictionary of all AA flights departing on
    the given date, using the flight's number as the key to all relevant flight
    information.

    Input:
      date (str): A date with format YYYY-MM-DD.
    
    Returns:
      A dictionary of all AA flights that depart on the given date. We use a
      dictionary here to keep all future queries O(1), weighing the initial
      cost (O(n)) against multiple queries by functions utilizing this as a
      helper.
    """

    request_url = __api_url + f"flights?date={date}"
    response = requests.get(request_url)

    if response.status_code != 200:
        return None  # TODO(elijahtruitt): Maybe handle this better?

    # Transform into dict that can be refrenced easily.
    result = {}
    for flight in response.json():
        if flight["origin"]["code"] == "ATL":
            result[flight["flightNumber"]] = flight
    return result


def find_flight_info(flight_number: str, flight_date: str) -> Dict:
    """Provide flight info for any American Airlines flight.

    Given an AA flight number and the date of departure, this function returns
    relevant flight info including origin and destination airport info, times
    of departure and arrival, etc.

    Input:
      flight_number (str): A string representation of a flight number.
      flight_date (str): A string representation of a date (YYYY-MM-DD).
    
    Returns:
      A JSON object containing info on the requested flight.
    """

    flight_db = get_flights_on_date(flight_date)
    if flight_number not in flight_db:
        return None  # TODO(elijahtruitt): Maybe handle this better?

    flight_info = flight_db[flight_number]
    return flight_info


# print(get_flights_on_date("2015-11-05"))
# print(find_flight_info("1048", "2023-11-05"))
# print(find_flight_info("1048", "2023-11-05")) (old example)
