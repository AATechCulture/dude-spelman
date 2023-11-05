import React from "react";
import Navbar from "../components/Navbar/Navbar";
import Hotel from "../components/Hotel/Hotel";
import AltFlights from "../components/AltFlights/AltFlights";
import Rideshare from "../components/Rideshare/Rideshare";

const PostCancellation = () => {
  return (
    <div>
      <Navbar />
      <AltFlights />
      <Hotel />
      <Rideshare />
    </div>
  );
};

export default PostCancellation;
