import airportsdata
import pandas as pd
import requests
import weather_data
import flight_engine
from datetime import datetime, timedelta
import dateutil


airports = airportsdata.load("IATA")
top25AirCodes = ["ATL","DFW","DEN","ORD","LAX","JFK","LAS","MCO","MIA","CLT","SEA","PHX","EWR","SFO","IAH","BOS","FLL","MSP","LGA","DTW","PHL","SLC","DCA","SAN","BWI"]
#parameters = {'access_key'='45cf71b762b4a38a7395848c6b6f5147'}
#api_result = requests.get('https://api.aviationstack.com/v1/flights', parameters)
#api_response = api_result.json()

# print(airports['SEA'])
# print(airports['ATL'])
# atlData = pd.read_csv('code-submission/backend/dataset/ATL_2010_23.csv')


def getFlightCancelNum(departDate: str, airportCode: str):
    """
    Desc: Retrieves the # of Canceled Flights on a given date from an airport solely due to Extreme Weather
    Input:
        departDate - String in "Month/Date/Year" Format. Ex: "10/25/2023"
        airportCode - String in the IATA Format for airport identification. Ex: "JFK"
    Output:
        Integer of the Canceled Flights on a given date
    """
    airlineData = pd.read_csv(
        f"code-submission/backend/dataset/{airportCode}_2010_23.csv", sep=","
    )
    
    return airlineData[airlineData["Date"] == dateCleanup(departDate)][
        "Canceled_Flights"
    ]


def getFlightCancelPer(departDate: str, airportCode: str):
    """
    Desc: Retrieves the % of Canceled Flights on a given date from an airport solely due to Extreme Weather
    Input:
        departDate - String in "Month/Date/Year" Format. Ex: "10/25/2023"
        airportCode - String in the IATA Format for airport identification. Ex: "JFK"
    Output:
        Float of the % of Canceled Flights on a given date
    """
    airlineData = pd.read_csv(
        f"code-submission/backend/dataset/{airportCode}_2010_23.csv", sep=","
    )
    return airlineData[airlineData["Date"] == dateCleanup(departDate)][
        "Canceled_Percentage"
    ]


def getDataTotData(departDate: str, airportCode: str):
    """
    Desc: Retrieves the Total Data of Flights on from an airport solely due to Extreme Weather
    Input:
        departDate - String in "Month/Date/Year" Format. Ex: "10/25/2023"
        airportCode - String in the IATA Format for airport identification. Ex: "JFK"
    """
    airlineData = pd.read_csv(
        f"code-submission/backend/dataset/{airportCode}_2010_23.csv", sep=","
    )
    return airlineData[airlineData["Date"] == dateCleanup(departDate)]

#def runningDelayTotal(depart)

def dateCleanup(incomingDate: str):
    """
    Desc: Standardizies MM/DD/YY format of inputs for use in CSV files based on input for FAA Dataset. 
    Deals with excess 0s and the starting '20' in years
    Input:
        incomingDate - String in "Month/Date/Year" Format with incorrect format. Ex: "01/05/2023"
    Output:
        Corrected version of date. Ex: "1/5/23"
    """
    dateSplit = incomingDate.split("/")
    # print(dateSplit)
    if dateSplit[0][0] == "0":
        dateSplit[0] = dateSplit[0][1:]
    if dateSplit[1][0] == "0":
        dateSplit[1] = dateSplit[1][1:]
    if len(dateSplit[2]) == 4:
        dateSplit[2] = dateSplit[2][2:]
    result = ""
    for value in dateSplit:
        result += value + "/"
    return result[0:-1]

def generateAirportLongLatDict():
    """
    Desc: Generates a Dictionary with Airline Codes as Keys & Airline Long/Lats as Dictionary Values stored in a tuple.
    Ex. "ATL": (33.63,84.42)
    """
    airportDict = {}
    for airportCode in top25AirCodes:
        #tempData = round(airports[airportCode]["lat"],2)
        #print(tempData)
        airportDict[airportCode] = (round(airports[airportCode]["lat"],2),round(airports[airportCode]["lon"],2))
    return airportDict

def getWeatherBetweenDates(start_date:datetime, end_date:datetime,lat:str,long:str):
    """
    (TODO: IGNORE, OUT OF DATE VERSION OF INITIAL HISTORICAL_WEATHER_DATA.PY IMPLEMENTATION)
    """
    #print("HI")
    current_date = start_date
    while current_date.date() <= end_date.date():
        #yield current_date
        #formatted_date = current_date.strftime("%m/%d/%Y")
        iso_time = current_date.strftime("%Y-%m-%dT%H:%M:%S%z")
        #print(iso_time)
        origin_weather = weather_data.get_weather_data(
            #"47.45", "-122.31", "2023-11-06T13:00:00-05:00"
            #lat,long, "2023-11-04T13:00:00-05:00"
            #iso_time
        )
        #dateutil.parser.parse(current_date).date()
        #print(origin_weather)
        temp = origin_weather["temperature"]
        precipitation_prob = origin_weather["probabilityOfPrecipitation"]["value"]
        humidity = origin_weather["relativeHumidity"]["value"]
        wind_speed = int(origin_weather["windSpeed"][0])
        forecast = origin_weather["shortForecast"]

        #print(temp)
        current_date+=timedelta(days=1)

def parseWeatherData():
    """
    (TODO: IGNORE, OUT OF DATE VERSION OF INITIAL HISTORICAL_WEATHER_DATA.PY IMPLEMENTATION)
    """
    airportDict = generateAirportLongLatDict()
    print(airportDict)
    for airCode in airportDict.keys():
        #print(datetime(2020,10,1)+timedelta(hours=12))
        #print(airportDict[airCode][0])
        #print(airportDict[airCode][1])
        getWeatherBetweenDates(
            datetime(2020,10,1)+timedelta(hours=12),
            datetime(2020,10,5)+timedelta(hours=12),
            airportDict[airCode][0],
            airportDict[airCode][1]
        )
    """temp = origin_weather["temperature"]
    precipitation_prob = origin_weather["probabilityOfPrecipitation"]["value"]
    humidity = origin_weather["relativeHumidity"]["value"]
    wind_speed = int(origin_weather["windSpeed"][0])
    forecast = origin_weather["shortForecast"]
    """


#parseWeatherData()
# print(getDataTotData(dateCleanup("1/02/2020"),"ATL"))
# print(getDataTotData("1/9/10", "ATL"))
