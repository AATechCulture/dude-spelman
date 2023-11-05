import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)


def get_historical_weather_data(latitude, longitude, start_date, end_date):

    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "start_date": "2023-10-30",
        "end_date": "2023-10-31",
        "hourly": ["temperature_2m", "relative_humidity_2m", "precipitation", "rain", "snowfall", "weather_code" "wind_speed_10m"]
    }

    responses = openmeteo.weather_api(url, params=params)
    
    return responses