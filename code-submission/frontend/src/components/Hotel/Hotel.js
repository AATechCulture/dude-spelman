import React from "react";
import "./Hotel.css";
import Hyatt from "../../assets/Hyatt_Logo.jpeg";
import IHG from "../../assets/IHG_Logo.png";
import Marriot from "../../assets/Marriot_Logo.png";
import { Link } from "react-router-dom";

const Hotel = () => {
  return (
    <div className="hotel-info">
      <h1>Book Your Hotels Here</h1>
      <p>Earn AAvantage miles when you stay at these Hotels</p>
      <div className="hotel-info-card">
        <div className="Hyatt-logo">
          <Link to="https://www.hyatt.com/" target="_blank">
            <img src={Hyatt} alt="Hyatt Logo" />
          </Link>
        </div>
        <div className="IHG-logo">
          <Link
            to="https://www.ihg.com/hotels/gb/en/reservation"
            target="_blank"
          >
            <img src={IHG} alt="IHG Logo" />
          </Link>
        </div>
        <div className="Marriot-logo">
          <Link to="https://www.marriott.com/default.mi" target="_blank">
            <img src={Marriot} alt="Marriot Logo" />
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Hotel;