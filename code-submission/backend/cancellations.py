import airportsdata
import pandas as pd

airports = airportsdata.load("IATA")
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


def dateCleanup(incomingDate: str):
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


# print(getDataTotData(dateCleanup("1/02/2020"),"ATL"))
# print(getDataTotData("1/9/10", "ATL"))
