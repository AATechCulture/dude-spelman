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
    var myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");
    var raw = JSON.stringify({
      flight_number: 1234,
      flight_date: "2023-11-05",
    });

    var requestOptions = {
      method: "GET",
      headers: myHeaders,
      body: raw,
      redirect: "follow",
    };

    fetch("http://localhost:8000/predict-cancellation", requestOptions)
      .then((response) => response.text())
      .then((result) => console.log(result))
      .catch((error) => console.log("error", error));
  };

  console.log("percentage", percentage);
  return (
    <div className="rating-container">
      <h2 className="rating-header">
        The chance of your flight being cancelled is:
      </h2>
      <h1 className="rating">16%</h1>
      <p className="rating-explanation">
        The rating is the result of our flight cancellation algorithm which is
        influenced by airport weather conditons.
      </p>
    </div>
  );
};

export default CancelRating;
