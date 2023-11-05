import React, { useState } from "react";
import "./CancelRating.css";

const CancelRating = () => {
  const [departureCode, setDepartureCode] = useState("");
  const [arrivalCode, setArrivalCode] = useState("");

  return (
    <div className="rating-container">
      <h2 className="rating-header">The chance of your flight being cancelled is:</h2>
      <h1 className="rating">16%</h1>
      <p className="rating-explanation">The rating is the result of our flight cancellation algorithm which is influenced by airport weather condiitons.</p>
      </div>
  );
};

export default CancelRating;
