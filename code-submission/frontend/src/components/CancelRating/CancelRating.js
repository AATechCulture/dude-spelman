import React, { useState, useEffect } from "react";
import "./CancelRating.css";

const CancelRating = ({
  
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
        console.log("percent", data);
      });
  });

  return (
    <div className="rating-container">
      <h2 className="rating-header">
        The chance of your flight being cancelled is:
      </h2>
      <h1 className="rating">{percentage.toFixed(2)}%</h1>
      <p className="rating-explanation">
        The rating is the result of our flight cancellation algorithm which is
        influenced by airport weather conditons.
      </p>
    </div>
  );
};

export default CancelRating;