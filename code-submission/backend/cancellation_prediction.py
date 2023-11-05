import flight_engine
import weather_data
import cancellations
import dateutil
import datetime


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

    # Get weather predictions for origin and destination airports.
    origin_weather = weather_data.get_weather_data(
        coords_origin[0], coords_origin[1], departure_time
    )
    dest_weather = weather_data.get_weather_data(
        coords_destination[0], coords_destination[1], arrival_time
    )

    # Get historic cancellation percentages due to severe weather.
    departure_date = cancellations.dateCleanup(
        (
            dateutil.parser.parse(departure_time).date()
            - dateutil.relativedelta.relativedelta(years=5)
        ).strftime("%m/%d/%Y")
    )

    arrival_date = cancellations.dateCleanup(
        (
            dateutil.parser.parse(arrival_time).date()
            - dateutil.relativedelta.relativedelta(years=5)
        ).strftime("%m/%d/%Y")
    )

    history_percentage_origin = cancellations.getFlightCancelPer(
        departure_date, home_code
    )
    history_percentage_dest = cancellations.getFlightCancelPer(
        arrival_date, away_code
    )

    print(origin_weather)
    print(dest_weather)
    print(history_percentage_origin)
    print(history_percentage_dest)

    """
    Temperature ^2 * (0.15) + precipProb * (0.05) + humidity * (0.05) + windSpeed * (0.20) + shortForecast_weight * (0.25)
    """
    temp = origin_weather["temperature"]
    precipitation_prob = origin_weather["probabilityOfPrecipitation"]["value"]
    humidity = origin_weather["relativeHumidity"]["value"]
    wind_speed = int(origin_weather["windSpeed"][0])
    forecast = origin_weather["shortForecast"]

    """
    W_PoP * PoP + W_WS * WindSpeedScore + W_Temperature * TemperatureScore + W_RH * RelativeHumidity + W_Other * OtherConditionsScore) / (W_PoP + W_WS + W_Temperature + W_RH + W_Other
    """

    percentage = (
        temp * 0.1
        + precipitation_prob * 0.4
        + humidity * 0.1
        + wind_speed * 3
        + history_percentage_origin / 100
    ) / (0.1 + 0.4 + 0.1 + 0.3)
    return percentage


# print(
#     get_cancellation_percentage(
#         "7373",
#         "2023-11-05",
#     )
# )
