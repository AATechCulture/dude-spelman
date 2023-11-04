import requests

"""
 STEPS:
 1. receive a list of data with longitude and latitude and time
 2. send back weather data
"""

# EXAMPLE variables
# longitude = "47.45" [string]
# latitude = "-122.31" [string]
# departue_times = "2023-11-04T13:00:00-05:00" [string]

def get_weather_data(longitude, latitude, departue_times):

    weather_data = requests.get(f"https://api.weather.gov/points/{longitude},{latitude}").json()
    seven_day_hourly_forecast = requests.get(weather_data['properties']["forecastHourly"]).json()

    for period in seven_day_hourly_forecast['properties']['periods']:
        if departue_times >= period['startTime'] and departue_times <= period['endTime']:
            return period