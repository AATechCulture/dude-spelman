import openmeteo_requests

import requests_cache
import pandas as pd
from retry_requests import retry
import cancellations

cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

airpot_long_lat_dict = cancellations.generateAirportLongLatDict()

def get_historical_weather_data(latitude, longitude, start_date, end_date):
    """
    Fetches historical weather data for a given geographical location and date range using the Open-Meteo API.

    Parameters:
        latitude (float): The latitude of the location.
        longitude (float): The longitude of the location.
        start_date (str): The start date for the data retrieval in 'YYYY-MM-DD' format.
        end_date (str): The end date for the data retrieval in 'YYYY-MM-DD' format.

    Returns:
        list: A list of response objects containing weather data.

    Raises:
        OpenMeteoRequestsError: If the API request fails or returns an error.
    """

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
    """
    Processes a list of weather data responses and existing airport codes to create a merged CSV file containing both weather data and flight cancellation data.

    Parameters:
        responses (list): A list of response objects containing weather data.
        airport_codes (list): A list of airport IATA codes corresponding to the weather data.

    Outputs:
        A CSV file named 'big_data.csv' containing the merged data.
        The file is saved to the current working directory.
    """


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

    flight_data = pd.read_csv("backend/dataset/Top25-Flight-Weather-Interrupt.csv", sep=",")
 
    print(master_data_frame)
    
    merged_data = pd.merge(flight_data,master_data_frame, on=["date","airport"], how='outer')
    merged_data.to_csv('big_data.csv', index=False)

responses = []
keys = []
for key in airpot_long_lat_dict.keys():
    responses.append(get_historical_weather_data(airpot_long_lat_dict[key][0], airpot_long_lat_dict[key][1], "2018-01-01", "2020-01-01"))
    keys.append(key)

create_csv_from_data_frame(responses, keys)

# trim the data set between to only include the years of 2018 and 2019
df = pd.read_csv('backend/dataset/big_data.csv')
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%y')

start_date = pd.to_datetime('1/1/18')
end_date = pd.to_datetime('12/31/19')

df_filtered = df[(pd.to_datetime(df['date']) >= start_date) & (pd.to_datetime(df['date']) <= end_date)]
df_filtered.to_csv('big_data.csv', index=False)
