import React, { useState, useEffect } from "react";
import "./CancelRating.css";

const CancelRating = ({
  flightNumber,
  setFlightNumber,
  flightDate,
  setFlightDate,
}) => {
  const [percentage, setPercentage] = useState(null);

  useEffect(() => {
    fetch(
      "/predict-cancellation?" +
        new URLSearchParams({
          flight_number: 7373,
          flight_date: "2023-11-05",
        })
    )
      .then((res) => res.json())
      .then((data) => {
        setPercentage(data);
        console.log(data);
      });
  }, []);

  return (
    <div>
      <h1>Flight Cancelation Rating</h1>
    </div>
  );
};

export default CancelRating;