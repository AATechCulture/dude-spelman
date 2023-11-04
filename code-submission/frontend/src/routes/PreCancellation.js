import React from "react";
import Forecast from "../components/Forecast/Forecast";
import CancelRating from "../components/CancelRating/CancelRating";
import IROPS from "../components/IROPS/irops";
import Navbar from "../components/Navbar/Navbar";

const PreCancellation = () => {
  return (
    <div>
      <Navbar />
      <Forecast />
      <CancelRating />
      <IROPS />
    </div>
  );
};

export default PreCancellation;
