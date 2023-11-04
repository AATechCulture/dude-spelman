import flight_engine
import weather_data


def get_cancellation_percentage(flight_number: str, flight_date: str) -> float:
    """Returns the chance a flight will be cancelled from severe weather.

    Uses various information sources (weather predictions from home and target
    airports, historical cancellation data, etc.) to make an accurate
    prediction on what chance there is that the plane may be cancelled due to
    a severe weather scenario.

    Input:
      flight_number (str): A string representation of an AA flight number.
      flight_date (str): A string representation of a flight's departure date
        with the format YYYY-MM-DD.

    Returns:
      A float representing the estimated percentage chance of the given flight
      to be cancelled due to severe weather complications.
    """

    # Get origin and destination airport information.
    flight_info = flight_engine.find_flight_info(flight_number, flight_date)
    home_code = flight_info["origin"]["code"]
    away_code = flight_info["destination"]["code"]

    airport_origin = flight_engine.get_airport_info(home_code)
    airport_dest = flight_engine.get_airport_info(away_code)

    coords_origin = (
        str(airport_origin["location"]["latitude"]),
        str(airport_origin["location"]["longitude"]),
    )
    coords_destination = (
        str(airport_dest["location"]["latitude"]),
        str(airport_dest["location"]["longitude"]),
    )
    departure_time = flight_info["departureTime"]
    arrival_time = flight_info["arrivalTime"]
    print(departure_time)
    print(coords_origin)

    # Get weather predictions for origin and destination airports.
    origin_weather = weather_data.get_weather_data(
        coords_origin[0], coords_origin[1], departure_time
    )
    dest_weather = weather_data.get_weather_data(
        coords_destination[0], coords_destination[1], arrival_time
    )


# get_cancellation_percentage(
#     "5268",
#     "2023-11-05",
# )
