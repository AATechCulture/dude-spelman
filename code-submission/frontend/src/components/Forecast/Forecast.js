import React, { useState, useEffect } from "react";
import flights from "../../assets/flights.png"
import "./Forecast.css";

const Forecast = () => {
  const [flightCode, setFlightCode] = useState("");
  const [selectedDepartureDate, setSelectedDepartureDate] = useState("");
  const [flightData, setFlightData] = useState({});
  const [weatherData, setWeatherData] = useState([]);

  useEffect(() => {
    fetch(
      "/bonito-flakes?" +
        new URLSearchParams({
          flight_number: 7373,
          flight_date: "2023-11-05",
        })
    )
      .then((response) => response.json())
      .then((data) => {
        setFlightData(data);
        console.log("airport data", data);
      })
      .catch((error) => console.error("Error:", error));

    fetch(
      "/get-weather?" +
        new URLSearchParams({
          flight_number: 7373,
          flight_date: "2023-11-05",
        })
    )
      .then((response) => response.json())
      .then((data) => {
        setWeatherData(data);
        console.log("weather data", data);
      })
      .catch((error) => console.error("Error:", error));
  }, []);

  return (
    <div className="forecast-container">
      <h1 className="title">Pre-Cancellation Metrics</h1>
      <div className="flight-code">
      <h3>Flight Code:</h3>
      <input
        type="text"
        id="departureCode"
        value={flightCode}
        onChange={(e) => setFlightCode(e.target.value)}
      />
      <div className="date-picker">
        <label htmlFor="dateInput">Select a Date:</label>
        <input type="date" id="dateInput" value={selectedDepartureDate} />
      </div>
      <div className="submit">
          {" "}
          <input className="submit-btn" type="submit" value="Submit"></input>
        </div>
      </div>
      <h2 className="sub-title">Departure Airport Forecast</h2>
      <div className="departure-code"></div>
      {/* For forecast info based on airport departure city weatherData?*/}
      <br />
      <h2>Arrival Airport Forecast</h2>

      <div className="arrival-code">
        <br />
      </div>
      {/* For forecast info based on airport arrival city weatherData?*/}
    </div>
  );
};

export default Forecast;
