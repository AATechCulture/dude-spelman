import React from "react";
import Navbar from "../components/Navbar/Navbar";
import Hotel from "../components/Hotel/Hotel";
import AltFlights from "../components/AltFlights/AltFlights";
import Rideshare from "../components/Rideshare/Rideshare";
import Footer from "../components/Footer/Footer";

const PostCancellation = () => {
  return (
    <div>
      <Navbar />
      <AltFlights />
      <Hotel />
      <Rideshare />
      <Footer />
    </div>
  );
};

export default PostCancellation;
