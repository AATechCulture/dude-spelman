from amadeus import ResponseError, Client

amadeus = Client(
    client_id='0bI9rpxwYG37LhTmho985U14F1pBurIY',
    client_secret='QehM7zTGhLAwL6Ud'
)

def get_flight_info(originLocationCode, destinationLocationCode, departureDate, adults):
    """
    Retrieves flight offers and pricing information for flights from a specified origin to a destination on a given date for a certain number of adults. 

    Parameters:
    - originLocationCode (str): The IATA code for the origin airport.
    - destinationLocationCode (str): The IATA code for the destination airport.
    - departureDate (str): The departure date for the flight search in 'YYYY-MM-DD' format.
    - adults (int): The number of adult passengers.

    Returns:
    - list: A list containing two elements:
        - The first element is the raw response from the flight offers search API call.
        - The second element is the pricing information for the first flight offer.

    Raises:
    - ResponseError: An error response from the Amadeus API with details about what went wrong with the request.
    """

    try:
        flight_offers = amadeus.shopping.flight_offers_search.get(
            originLocationCode=originLocationCode,
            destinationLocationCode=destinationLocationCode,
            departureDate=departureDate,
            adults=adults
        )
        
        flight_prices = amadeus.shopping.flight_offers_search.get(
            originLocationCode=originLocationCode, 
            destinationLocationCode=destinationLocationCode,
            departureDate=departureDate, 
            adults=adults).data
        
        response_one_flight = amadeus.shopping.flight_offers.pricing.post(flight_prices[0])

        return [flight_offers, flight_prices]

    except ResponseError as error:
        print(f"Invalid requesst for flights from {originLocationCode} to {destinationLocationCode} on {departureDate} with {adults} adults.")
        print(error)
        raise error