import React, { useState } from "react";
import "./Forecast.css";

const Forecast = () => {
  const [departureCode, setDepartureCode] = useState("");
  const [arrivalCode, setArrivalCode] = useState("");

  return (
    <div>
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
      </div>
      {/* For forecast info based on airport departure city */}
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
      </div>
      {/* For forecast info based on airport arrival city */}
    </div>
  );
};

export default Forecast;
