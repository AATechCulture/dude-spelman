import React, { useState, useEffect } from "react";
import "./CancelRating.css";
import axios from "axios";

const CancelRating = ({
  flightNumber,
  setFlightNumber,
  flightDate,
  setFlightDate,
}) => {
  const [percentage, setPercentage] = useState(null);

  const handleCalculatePercentage = () => {
    axios
      .get(`http://localhost:5000/predict-cancellation`, {
        params: {
          flight_number: flightNumber,
          flight_date: flightDate,
        },
      })
      .then((response) => {
        setPercentage(response.data);
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
<<<<<<< HEAD
    <div className="rating-container">
      <h2 className="rating-header">The chance of your flight being cancelled is:</h2>
      <h1 className="rating">16%</h1>
      <p className="rating-explanation">The rating is the result of our flight cancellation algorithm which is influenced by airport weather conditons.</p>
      </div>
=======
    <div>
      <button onClick={handleCalculatePercentage}>
        Calculate Cancellation Percentage
      </button>
      <h4>Cancellation Percentage:</h4>
      <p>{percentage}%</p>
    </div>
>>>>>>> 546710d (moving variables)
  );
};

export default CancelRating;
