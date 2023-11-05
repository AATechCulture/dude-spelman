import React from "react";
import { Link } from "react-router-dom";
import Uber from "../../assets/Uber.jpg"
const Rideshare = () => {
  return (
    <div className="rideshare-info">
    <h1>Uber to your Hotel</h1>
    <p>Earn AAvantage miles when you ride with Uber</p>
    <div className="rideshare-info-card">
      <div className="rideshare-logo">
        <Link to="https://www.uber.com/" target="_blank">
          <img src={Uber} alt="Uber Logo" />
        </Link>
      </div>
    </div>
  </div>
  );
  
};

export default Rideshare;
