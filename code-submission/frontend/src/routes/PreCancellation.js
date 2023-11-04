import React from "react";
import Forecast from "../components/Forecast/Forecast";
import CancelRating from "../components/CancelRating/CancelRating";
import IROPS from "../components/IROPS/irops";
import Hotel from "../components/Hotel/Hotel";

const PreCancellation = () => {
  return (
    <div>
      <Forecast />
      <CancelRating />
      <IROPS />
    </div>
  );
};

export default PreCancellation;
