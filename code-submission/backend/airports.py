import airportsdata
import pandas as pd

airports = airportsdata.load("IATA")
# print(airports['SEA'])
# print(airports['ATL'])
# atlData = pd.read_csv('code-submission/backend/dataset/ATL_2010_23.csv')


def getFlightsCancelNum(departDate: str, airportCode: str):
    """
    Desc: Retrieves the # of Canceled Flights on a given date from an airport solely due to Extreme Weather
    Input:
        departDate - String in "Month/Date/Year" Format. Ex: "10/25/2023"
        airportCode - String in the IATA Format for airport identification. Ex: "JFK"
    Output:
        Int
    """
    airlineData = pd.read_csv(
        f"code-submission/backend/dataset/{airportCode}_2010_23.csv", sep=","
    )
    return airlineData[airlineData["Date"] == departDate]["Canceled_Flights"]


def getFlightCancelPer(departDate: str, airportCode: str):
    """ """
    airlineData = pd.read_csv(
        f"code-submission/backend/dataset/{airportCode}_2010_23.csv", sep=","
    )
    return airlineData[airlineData["Date"] == departDate]["Canceled_Percentage"]


def getDataTotData(departDate: str, airportCode: str):
    """ """
    airlineData = pd.read_csv(
        f"code-submission/backend/dataset/{airportCode}_2010_23.csv", sep=","
    )
    return airlineData[airlineData["Date"] == departDate]


getFlightsCancelNum("1/9/10", "ATL")
