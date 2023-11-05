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
    <div className="rating-container">
      <h2 className="rating-header">The chance of your flight being cancelled is:</h2>
      <h1 className="rating">16%</h1>
      <p className="rating-explanation">The rating is the result of our flight cancellation algorithm which is influenced by airport weather conditons.</p>
      </div>
  );
};

export default CancelRating;
