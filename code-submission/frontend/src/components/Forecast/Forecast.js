import React, { useState } from "react";
import "./Forecast.css";

const Forecast = () => {
  const [departureCode, setDepartureCode] = useState("");
  const [arrivalCode, setArrivalCode] = useState("");
  const [weatherData, setWeatherData] = useState(null);
  const [selectedDepartureDate, setSelectedDepartureDate] = useState("");
  const [selectedArrivalDate, setSelectedArrivalDate] = useState("");

  const handleDepartureDateChange = (e) => {
    setSelectedDepartureDate(e.target.value);
  };

  const handleArrivalDateChange = (e) => {
    setSelectedArrivalDate(e.target.value);
  };

  return (
    <div className="forecast-container">
      <h1 className="title">Pre-Cancellation Metrics</h1>
      <h2 className="sub-title">Departure Airport Forecast</h2>
      <div className="departure-code">
        <h3>Enter Departure Airport Code:</h3>
        <input
          type="text"
          id="departureCode"
          value={departureCode}
          onChange={(e) => setDepartureCode(e.target.value)}
          placeholder="e.g. JFK"
        />
        <div>
          <label htmlFor="dateInput">Select a Date:</label>
          <input
            type="date"
            id="dateInput"
            value={selectedDepartureDate}
            onChange={handleDepartureDateChange}
          />
          <p>Selected Date: {selectedDepartureDate}</p>
        </div>
      </div>
      {/* For forecast info based on airport departure city weatherData?*/}
      <br />
      <h2>Arrival Airport Forecast</h2>

      <div className="arrival-code">
        <h3>Enter Arrival Airport Code:</h3>
        <input
          className="arrivalCode"
          type="text"
          id="arrivalCode"
          value={arrivalCode}
          onChange={(e) => setArrivalCode(e.target.value)}
          placeholder="e.g. LAX"
        />
        <div>
          <label htmlFor="dateInput">Select a Date:</label>
          <input
            type="date"
            id="dateInput"
            value={selectedArrivalDate}
            onChange={handleArrivalDateChange}
          />
          <p>Selected Date: {selectedArrivalDate}</p>
        </div>
      </div>
      {/* For forecast info based on airport arrival city weatherData?*/}
    </div>
  );
};

export default Forecast;
