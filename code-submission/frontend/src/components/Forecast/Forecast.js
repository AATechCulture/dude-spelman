import React, { useState } from "react";

const Forecast = () => {
  const [departureCode, setDepartureCode] = useState("");
  const [arrivalCode, setArrivalCode] = useState("");
  return (
    <div>
      <h1 className="departure-code" type="text" value={departureCode}>
        Enter Departure Airport Code:
      </h1>
      <input />
      <br />
      <h1 className="arrival-code" type="text" value={arrivalCode}>
        Enter Arrival Airport Code:
      </h1>
      <input />
    </div>
  );
};

export default Forecast;
