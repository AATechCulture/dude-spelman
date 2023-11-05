import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry
import cancellations

# Setup the Open-Meteo API client with cache and retry on error
cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

airpot_long_lat_dict = cancellations.generateAirportLongLatDict()

def get_historical_weather_data(latitude, longitude, start_date, end_date):

    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "daily": ["weather_code", "temperature_2m_max", "precipitation_sum", "rain_sum", "snowfall_sum", "wind_speed_10m_max"]
    }

    responses = openmeteo.weather_api(url, params=params)
    
    return responses


def create_csv_from_data_frame(responses, airport_codes):
    
    master_data_frame = pd.DataFrame()
    for i, response in enumerate(responses):
        daily = response[0].Daily()

        daily_weather_code = daily.Variables(0).ValuesAsNumpy()
        daily_temperature_2m_max = daily.Variables(1).ValuesAsNumpy()
        daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy()
        daily_rain_sum = daily.Variables(3).ValuesAsNumpy()
        daily_snowfall_sum = daily.Variables(4).ValuesAsNumpy()
        daily_wind_speed_10m_max = daily.Variables(5).ValuesAsNumpy()

        daily_data = {"date": pd.date_range(
            start = pd.to_datetime(daily.Time(), unit = "s"),
            end = pd.to_datetime(daily.TimeEnd(), unit = "s"),
            freq = pd.Timedelta(seconds = daily.Interval()),
            inclusive = "left"
        )}

        daily_data["weather_code"] = daily_weather_code
        daily_data["airport"] = [airport_codes[i]]*len(daily_data["weather_code"])
        daily_data["temperature_2m_max"] = daily_temperature_2m_max
        daily_data["precipitation_sum"] = daily_precipitation_sum
        daily_data["rain_sum"] = daily_rain_sum
        daily_data["snowfall_sum"] = daily_snowfall_sum
        daily_data["wind_speed_10m_max"] = daily_wind_speed_10m_max


        dates = []
        for date in daily_data["date"]:
            formatted_date = date.strftime("%m/%d/%Y")
            dates.append(cancellations.dateCleanup(formatted_date))
            
        daily_data["date"] = daily_data["date"].astype(str)
        daily_data["date"] = dates

        daily_dataframe = pd.DataFrame(data = daily_data)
        master_data_frame = pd.concat([master_data_frame, daily_dataframe], ignore_index=True)

        # master_data_frame = master_data_frame.append(daily_dataframe, ignore_index=True)

    flight_data = pd.read_csv("backend/dataset/Top25-Flight-Weather-Interrupt.csv", sep=",")
    print(master_data_frame)
    merged_data =pd.merge(flight_data, master_data_frame, on=["date", "airport"])

    # for data in flight_data:


responses = []
keys = []
for key in airpot_long_lat_dict.keys():
    responses.append(get_historical_weather_data(airpot_long_lat_dict[key][0], airpot_long_lat_dict[key][1], "2023-10-17", "2023-10-31"))
    keys.append(key)

create_csv_from_data_frame(responses, keys)