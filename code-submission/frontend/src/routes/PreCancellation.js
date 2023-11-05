import React, { useState, useEffect } from "react";
import Forecast from "../components/Forecast/Forecast";
import CancelRating from "../components/CancelRating/CancelRating";
import IROPS from "../components/IROPS/irops";
import Navbar from "../components/Navbar/Navbar";

const PreCancellation = () => {
  const [flightNumber, setFlightNumber] = useState("");
  const [flightDate, setFlightDate] = useState("");
  return (
    <div>
      <Navbar />
      <Forecast />
      <CancelRating
        flightNumber={flightNumber}
        setFlightNumber={setFlightNumber}
        flightDate={flightDate}
        setFlightDate={setFlightDate}
      />
      <IROPS />
    </div>
  );
};

export default PreCancellation;
