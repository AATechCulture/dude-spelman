import flight_engine


def get_cancellation_percentage(flight_number: str, flight_date: str) -> float:
    """Returns the chance a flight will be cancelled from severe weather.

    Uses various information sources (weather predictions from home and target
    airports, historical cancellation data, etc.) to make an accurate
    prediction on what chance there is that the plane may be cancelled due to
    a severe weather scenario.
    """

    # Get origin and destination airport information.
    flight_info = flight_engine.find_flight_info(flight_number, flight_date)
    home_code = flight_info["origin"]["code"]
    away_code = flight_info["destination"]["code"]

    origin_coords = flight_engine.get_airport_info(home_code)
    dest_coords = flight_engine.get_airport_info(away_code)

    # Get weather predictions for origin and destination airports.


# get_cancellation_percentage("3282", "2024-11-04")
