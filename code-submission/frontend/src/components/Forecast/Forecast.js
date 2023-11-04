import React, { useState } from "react";
import "./Forecast.css";

const Forecast = () => {
  const [departureCode, setDepartureCode] = useState("");
  const [arrivalCode, setArrivalCode] = useState("");

  return (
    <div>
      <div className="departure-code">
        <h1 type="text" value={departureCode}>
          Enter Departure Airport Code:
        </h1>
        <input />
      </div>
      {/* For forecast info based on airport departure city */}
      <br />
      <div className="arrival-code">
        <h1 type="text" value={arrivalCode}>
          Enter Arrival Airport Code:
        </h1>
        <input />
      </div>
      {/* For forecast info based on airport arrival city */}
    </div>
  );
};

export default Forecast;
