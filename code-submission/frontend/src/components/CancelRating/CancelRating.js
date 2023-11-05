import React, { useState, useEffect } from "react";
import "./CancelRating.css";

const CancelRating = ({
  
}) => {
  const [percentage, setPercentage] = useState(null);

  // Define variables for flight number and flight date
  const flightNumber = 7373;
  const flightDate = '2023-11-05';

  useEffect(() => {
    // Use the flightNumber and flightDate variables in the API call
    fetch("/predict-cancellation?" + new URLSearchParams({
      flight_number: flightNumber,
      flight_date: flightDate
    }))
      .then((res) => res.json())
      .then((data) => {
        setPercentage(data.percentage); // Assuming 'percentage' is received in the API response
        console.log(data.percentage);
      })
      .catch((error) => {
        console.error('Error fetching percentage:', error);
      });
  }, [flightNumber, flightDate]); // Incl
  return (
    <div>
      <h1>Cancellation Percentage</h1>
      {percentage !== null ? (
        <p>The cancellation percentage is: {percentage}</p>
      ) : (
        <p>Loading percentage...</p>
      )}
    </div>
  );
};

export default CancelRating;