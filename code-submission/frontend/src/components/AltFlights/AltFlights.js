import "./AltFlights.css";
import React, { useState, useEffect } from "react";
import axios from "axios"
import flights from "../../assets/flights.png"
import { Link } from "react-router-dom";

const AltFlights = () => {

  const [flightData, setFlightData] = useState(null);

  useEffect(() => {
    const fetchFlightInfo = async () => {
      try {
        const response = await axios.post('http://localhost:8000/flight_info', {
          originLocationCode: 'MAD',
          destinationLocationCode: 'BOS',
          departureDate: '2023-11-06',
          adults: '1'
        });
        setFlightData(response.data);
      } catch (error) {
        console.error('Error fetching flight info:', error);
      }
    };

    fetchFlightInfo();
  }, []);


  return (
    <div className="alt-flights-container">
      <h1>Flight Information</h1>
=
      {flightData ? (
        <div>
          <h2>Flight Offers</h2>
          <ul>
            {flightData[0].data.map((offer, index) => (
              <li key={index}>
                <h3>Offer {index + 1}</h3>
                <p>Airline: {offer.offerItems[0].services[0].segments[0].flightSegment.carrierCode}</p>
                <p>Departure: {offer.offerItems[0].services[0].segments[0].flightSegment.departure.iataCode}</p>
                <p>Arrival: {offer.offerItems[0].services[0].segments[0].flightSegment.arrival.iataCode}</p>
                {/* Add more details as needed */}
              </li>
            ))}
          </ul>
        </div>
      ) : (
        <Link to="https://www.aa.com/homePage.do" target="_blank"><img className="flight-image" src={flights} alt="logo"/></Link>

      )}
    </div>
    
  );
};

export default AltFlights;
