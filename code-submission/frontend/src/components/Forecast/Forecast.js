import React, { useState } from "react";
import "./Forecast.css";

const Forecast = () => {
  const [departureCode, setDepartureCode] = useState("");
  const [arrivalCode, setArrivalCode] = useState("");

  return (
    <div className="forecast-container">
      <div className="departure-code">
        <h1>Enter Departure Airport Code:</h1>
        <input
          type="text"
          value={departureCode}
          onChange={(e) => setDepartureCode(e.target.value)}
        />
      </div>
      {/* For forecast info based on airport departure city */}
      <br />
      <div className="arrival-code">
        <h1>Enter Arrival Airport Code:</h1>
        <input
          type="text"
          value={arrivalCode}
          onChange={(e) => setArrivalCode(e.target.value)}
        />
      </div>
      {/* For forecast info based on airport arrival city */}
    </div>
  );
};

export default Forecast;
