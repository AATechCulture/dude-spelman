import React, { useState, useEffect } from "react";
import "./CancelRating.css";
import axios from "axios";

const CancelRating = () => {
  const [flightNumber, setFlightNumber] = useState("");
  const [flightDate, setFlightDate] = useState("");
  const [percentage, setPercentage] = useState(null);

  // useEffect(() => {
  //   fetch("/predict-cancellation")
  //     .then((res) => res.json())
  //     .then((data) => {
  //       setPercentage(percentage);
  //       console.log(percentage);
  //     });
  // });

  return (
    <div>
      <h1>Flight Cancelation Rating</h1>
    </div>
  );
};

export default CancelRating;
