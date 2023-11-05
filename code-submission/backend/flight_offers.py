from amadeus import ResponseError, Client

#pip3 install amadeus

amadeus = Client(
    client_id='0bI9rpxwYG37LhTmho985U14F1pBurIY',
    client_secret='QehM7zTGhLAwL6Ud'
)

# EXAMPLE variables
# originLocationCode = 'MAD'
# destinationLocationCode = 'BOS'
# departureDate = '2023-11-06'
# adults = '1'


def get_flight_offers(originLocationCode, destinationLocationCode, departureDate, adults):
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
    
        print(flight_offers.data)
        print(response_one_flight.data)

    except ResponseError as error:
        print(f"Invalid requesst for flights from {originLocationCode} to {destinationLocationCode} on {departureDate} with {adults} adults.")
        print(error)
        raise error
    
get_flight_offers('MAD', 'BOS', '2023-11-06', '1')