import requests

# EXAMPLE variables
# longitude = "47.45" [string]
# latitude = "-122.31" [string]
# departue_times = "2023-11-04T13:00:00-05:00" [string]

def get_weather_data(longitude, latitude, departure_time):
    """
    Fetches weather data for a specific location and time.

    This function takes geographical coordinates (longitude and latitude) and a departure time,
    then makes a request to the National Weather Service API to retrieve the hourly weather forecast.

    Parameters:
    - longitude (str): The longitude of the location
    - latitude (str): The latitude of the location
    - departure_time (str): The ISO 8601 formatted date and time

    Returns:
    weather data for the specified time period. If no matching time period is found in the forecast data, None is returned.
    """

    weather_data = requests.get(f"https://api.weather.gov/points/{longitude},{latitude}").json()
    seven_day_hourly_forecast = requests.get(weather_data['properties']["forecastHourly"]).json()

    for period in seven_day_hourly_forecast['properties']['periods']:
        if departure_time >= period['startTime'] and departure_time <= period['endTime']:
            return period 
    return None

# print(get_weather_data("47.45", "-122.31", "2023-11-04T15:00:00-05:00"))