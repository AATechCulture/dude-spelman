import airportsdata
import pandas as pd


airports = airportsdata.load("IATA")
# Top 25 Busiest Airports in the USA via IATA Airport Code
top25AirCodes = [
    "ATL",
    "DFW",
    "DEN",
    "ORD",
    "LAX",
    "JFK",
    "LAS",
    "MCO",
    "MIA",
    "CLT",
    "SEA",
    "PHX",
    "EWR",
    "SFO",
    "IAH",
    "BOS",
    "FLL",
    "MSP",
    "LGA",
    "DTW",
    "PHL",
    "SLC",
    "DCA",
    "SAN",
    "BWI",
]


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
        f"https://raw.githubusercontent.com/AATechCulture/dude-spelman/main/code-submission/backend/dataset/{airportCode}_2010_23.csv",
        sep=",",
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
        f"https://raw.githubusercontent.com/AATechCulture/dude-spelman/main/code-submission/backend/dataset/{airportCode}_2010_23.csv"
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
        f"https://raw.githubusercontent.com/AATechCulture/dude-spelman/main/code-submission/backend/dataset/{airportCode}_2010_23.csv",
        sep=",",
    )
    return airlineData[airlineData["Date"] == dateCleanup(departDate)]


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
    Desc: Generates a Dictionary with Airline Codes as Keys & Airport Long/Lats as Dictionary Values stored in a tuple.
    Ex. {}"ATL": (33.63,84.42)}
    Output:
        Dictionary filled with Airline Codes & Airport Long/Lats
    """
    airportDict = {}
    for airportCode in top25AirCodes:
        airportDict[airportCode] = (
            round(airports[airportCode]["lat"], 2),
            round(airports[airportCode]["lon"], 2),
        )
    return airportDict