import React, { useState, useEffect } from "react";
import "./CancelRating.css";

const CancelRating = () => {
  const [flightNumber, setFlightNumber] = useState("");
  const [flightDate, setFlightDate] = useState("");
  const [percentage, setPercentage] = useState(null);

  useEffect(() => {
    fetch("/hello")
      .then((res) => res.json())
      .then((data) => {
        setPercentage(percentage);
        console.log(percentage);
      });
  }, []);

  return (
    <div>
      <h1>Flight Cancelation Rating</h1>
    </div>
  );
};

export default CancelRating;
